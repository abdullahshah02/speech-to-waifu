import requests
from settings import VOICEVOX_PORT


def synthesize(output_file_name: str, text: str, speaker_id: str, **kwargs) -> str:
    """
    This file synthesizes a voice from text using the VoiceVox Core library.

    Documentation: https://voicevox.github.io/voicevox_engine/api/

    Args:
        output_file_name (str): The path of the output file.
        text (str): The text to synthesize.
        speaker_id (str): The speaker ID to use.
        **kwargs: Additional arguments to pass to the synthesis endpoint.

    Returns:
        The path of the output file.
    """
    audio_query_response = requests.post(
        f"http://localhost:{VOICEVOX_PORT}/audio_query?speaker={speaker_id}&text={text}"
    )

    payload = {**audio_query_response.json(), **kwargs}
    sythesized_audio = requests.post(
        f"http://localhost:{VOICEVOX_PORT}/synthesis?speaker={speaker_id}", json=payload
    )

    with open(output_file_name, "wb") as f:
        f.write(sythesized_audio.content)

    return output_file_name


def access_voicevox_api(method: str, endpoint: str, **kwargs) -> str:
    """
    This file accesses the VoiceVox Core API.

    Args:
        method (str): The method to use.
        endpoint (str): The endpoint to access.
        **kwargs: Additional arguments to pass to the endpoint.

    Returns:
        The response from the endpoint.
    """
    assert method in ["POST", "GET"], "ERROR: The method is not defined."
    assert endpoint != "", "ERROR: The endpoint is not defined."

    response = {}

    if method == "POST":
        response = requests.post(
            f"http://localhost:{VOICEVOX_PORT}/{endpoint}", json=kwargs
        )
    elif method == "GET":
        response = requests.get(
            f"http://localhost:{VOICEVOX_PORT}/{endpoint}", params=kwargs
        )

    return response
