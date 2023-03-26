import whisper


def transcribe(audio_file: str) -> str:
    """
    This function transcribes an audio file using the Whisper library.

    Documentation: https://github.com/openai/whisper

    Args:
        audio_file (str): The path of the audio file to transcribe.

    Returns:
        The transcription of the audio file.
    """
    assert audio_file != "", "ERROR: The audio file to transcribe is not defined."

    base_model = whisper.load_model("tiny")
    result = base_model.transcribe(audio_file, fp16=False)
    return result["text"]
