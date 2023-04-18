import os
import openai


class GPT_Model:
    def __init__(self):
        self._set_key()
        self._set_organization()

    def _query(self, prompt_text, max_tokens, temperature, context=None):
        message_log = [{"role": "user", "content": prompt_text}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=message_log,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content

    def _set_key(self):
        openai.api_key = os.environ.get("OPENAI_API_KEY")

    def _get_key(self):
        return openai.api_key

    def _set_organization(self):
        openai.organization = os.environ.get("ORGANIZATION_ID")

    def _get_organization(self):
        return openai.organization
