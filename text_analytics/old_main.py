from text_analytics import TextAnalytics
from translate import Translate
import numpy as np
import secret
import csv

input_file = "../data/input.csv"
input_file = r"D:\Code\TechMahindraMS\data\input.csv"
output_file = "../data/output.csv"
output_file = r"D:\Code\TechMahindraMS\data\output.csv"

txt_analytics = TextAnalytics(secret.analytics_endpoint,
                              secret.analytics_key)
translate = Translate(secret.tran_doc_endpoint, secret.tran_key, secret.region,
                      secret.api_version)

raw_data = []

with open(input_file, "r") as ip_file:
    csv_reader = csv.reader(ip_file)
    raw_data = list(csv_reader)

data = []
for d in raw_data[1:]:  # skip header
    if not txt_analytics.is_english(d[1]):
        translated = translate.translate(d[0])
        d.append(translated)
    else:
        d.append(d[1])
    data.append(d)

data = np.array(data)
queries = data[:, 2].tolist()

redacted = txt_analytics.pii_recognition(queries)
redacted = np.array(redacted).reshape(data.shape[0], 1)
data = np.hstack((data, redacted))

with open(output_file, "w") as file:
    file.write("id,raw_verbatim,translated,scrubbed\n")
    for i, d in enumerate(data):
        file.write(f"{','.join(d)}\n")
