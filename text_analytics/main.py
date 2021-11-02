from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import numpy as np
import requests
import secret
import uuid
import csv

raw_data = []
input_file = r"D:\Code\TechMahindraMS\data\input.csv"
output_file = r"D:\Code\TechMahindraMS\data\output.csv"

with open(input_file, "r") as ip_file:
    csv_reader = csv.reader(ip_file)
    raw_data = list(csv_reader)

ta_cred = AzureKeyCredential(secret.analytics_key)


def is_english(query):
    client = TextAnalyticsClient(secret.analytics_endpoint, ta_cred)
    try:
        response = client.detect_language([query], country_hint="us")
        response = response[0]
        if response.primary_language.name != "English":
            return False
        else:
            return True
    except Exception as err:
        print("Encountered exception. {}".format(err))
        return True


def translate(query):
    params = {"api-version": secret.api_version, "to": "en"}
    headers = {"Ocp-Apim-Subscription-Key": secret.tran_key,
               "Ocp-Apim-Subscription-Region": secret.region,
               "Content-type": "application/json",
               "X-ClientTraceId": str(uuid.uuid4())
              }
    body = [{'text': query}]
    request = requests.post(secret.tran_doc_endpoint, params=params,
                            headers=headers, json=body)
    response = request.json()[0]
    return response["translations"][0]["text"]


def pii_recognition(queries): 
    client = TextAnalyticsClient(secret.analytics_endpoint, ta_cred)
    response = client.recognize_pii_entities(queries, language="en")
    result = [r for r in response if not r.is_error]
    redacted = [r.redacted_text for r in result]
    return redacted


data = []
for d in raw_data[1:]:  # skip header
    if not is_english(d[1]):
        translated = translate(d[0])
        d.append(translated)
    else:
        d.append(d[1])
    data.append(d)

data = np.array(data)
queries = data[:, 2].tolist()

redacted = pii_recognition(queries)


redacted = np.array(redacted).reshape(data.shape[0], 1)
data = np.hstack((data, redacted)).tolist()

with open(output_file, "w") as file:
    file.write("id,raw_verbatim,translated,scrubbed\n")
    for i, d in enumerate(data):
        file.write(f"{','.join(d)}\n")
