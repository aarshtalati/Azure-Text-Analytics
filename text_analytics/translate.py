import requests
import uuid
import secret


class Translate():
    """ This class translates text to English.
    """
    def __init__(self, endpoint: str, key: str, region: str, ver: str) -> None:
        self.path = "translate" if endpoint.endswith("/") else "/translate"
        self.url = secret.tran_txt_endpoint + self.path
        self.params = {
            "api-version": ver,
            "to": "en"
        }
        self.headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': region,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }

    def translate(self, query: str) -> str:
        """ Translates text to English.

        Args:
            query (str): The text to translate.

        Returns:
            str: Translated string returned from Azure Cognitive services.
        """
        body = [{'text': query}]
        request = requests.post(self.url, params=self.params,
                                headers=self.headers, json=body)
        response = request.json()[0]
        return response["translations"][0]["text"]
