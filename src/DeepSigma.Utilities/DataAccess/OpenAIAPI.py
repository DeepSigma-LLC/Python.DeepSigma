import openai
from openai import *


class CustomOpenAI:
    apikey = None

    def __init__(self, api_key: str, use_azure: bool = False, azure_endpoint: str = None, azure_api_version: str = None):
        self.apikey: str = api_key
        if use_azure:
            self.client = self.__get_azure_client(azure_endpoint, azure_api_version)
        else:
            self.client = OpenAI(api_key=self.apikey)

    def __get_azure_client(self, url_endpoint: str, api_version: str) -> openai.AzureOpenAI:
        client = openai.AzureOpenAI(api_version=api_version,
                                    azure_endpoint=url_endpoint,
                                    api_key=self.apikey)
        return client

    def chat_completion(self, prompt: str, model: str) -> str:
        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content

    def get_embedding(self, text: str, model: str) -> list[float]:
        """
        Generate embedding.
        :param text:
        :param model:
        :return:
        """
        response = self.client.embeddings.create(
            input=text,
            model=model
        )

        embedding: list[float] = response.data[0].embedding
        return embedding

    def speech_to_text(self, file_path: str, model: str) -> str:
        audio_file = open(file_path, "rb")
        response = self.client.audio.transcriptions.create(
            model=model,
            file=audio_file
        )
        return response.text

    def text_to_speech(self, text: str, model: str, voice: str = "alloy") -> str:
        response = self.client.audio.speech.create(
            model=model,
            voice=voice,
            input=text
        )
        return response.text