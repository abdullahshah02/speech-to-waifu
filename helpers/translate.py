import deepl
from settings import DEEPL_API_KEY


def translate(text: str, target_lang: str = "JA") -> str:
    """
    Translate text using the DeepL API.

    Documentation: https://github.com/DeepLcom/deepl-python

    Args:
        api_key (str): The API key to use.
        text (str): The text to translate.
        target_lang (str): The language to translate the text to.

    Returns:
        The translated text.
    """
    auth_key = DEEPL_API_KEY
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(text, target_lang=target_lang)
    return result.text
