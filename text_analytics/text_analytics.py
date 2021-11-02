from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


class TextAnalytics:
    """ This class reads data from csv file, translates text to English,
        removes personally identifiable information (PII) and performs
        sentiment analysis. MSDN Ref: "Quickstart: Use the Text Analytics
        client library and REST API"
    """

    def __init__(self, endpoint: str, key: str) -> None:
        # text analytics end point & key
        self.ta_ep: str = endpoint
        self.ta_key: str = key
        self.client: TextAnalyticsClient = None

    def authenticate_client(self) -> None:
        """ Initializes an instance of text analytics client.
        """
        ta_cred = AzureKeyCredential(self.ta_key)
        self.client = TextAnalyticsClient(self.ta_ep, ta_cred)

    def is_english(self, query: str) -> bool:
        """ Returns a boolean result indicating if the query string is in
            English.

        Args:
            query (str): A string to check if it is in English.

        Returns:
            bool: Returns if a given string is in English
        """
        # TODO: find a reliable way to check if the connection is active, to
        # avoid azure.core.exceptions.ServiceRequestError: Failed to establish
        # a new connection: [Errno 11001] getaddrinfo failed
        # self.authenticate_client()
        try:
            response = self.client.detect_language([query], country_hint="us")
            response = response[0]
            if response.primary_language.name != "English":
                return False
            else:
                return True
        except Exception as err:
            print("Encountered exception. {}".format(err))
            return True

    def pii_recognition(self, queries: list[str]) -> list[str]:
        """ Redacts personally identifiable information (PII).

        Args:
            queries (list[str]): The list of string to redact.

        Returns:
            list[str]: List of redacted strings returned from Azure.
        """
        # TODO: find a reliable way to check if the connection is active, to
        # avoid azure.core.exceptions.ServiceRequestError: Failed to establish
        # a new connection: [Errno 11001] getaddrinfo failed
        # self.authenticate_client()
        response = self.client.recognize_pii_entities(queries, language="en")
        result = [r for r in response if not r.is_error]
        redacted = [r.redacted_text for r in result]
        # TODO: accept a threshold parameter. Only send redacted text if above
        # that certain threshold
        return redacted
