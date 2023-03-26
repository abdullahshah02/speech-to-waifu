# Speech to Waifu

Speech to Waifu is an exciting project that takes voice recognition and deep learning to a whole new level.
Speak your thoughts and have an anime waifu will repeat your words back to you!

## Pre-requisites:

1. Python 3.9.9
    - [Windows](https://www.python.org/downloads/release/python-399/)
    - [Ubuntu](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/)

2. Docker
    - [Windows](https://www.docker.com/products/docker-desktop/)
    - [Ubuntu](https://docs.docker.com/desktop/install/linux-install/)

3. [Voicevox Image](https://hub.docker.com/r/voicevox/voicevox_engine)

4. [DeepL API Key](https://www.deepl.com/pro-api?cta=header-pro-api/). Once you have this, add it to the `.env` file as `DEEPL_API_KEY`.

## Setting up 

Once you have all the pre-requisites, run the following commands to start the project:
- `python3.9 -m pip install -r requirements.txt`
- `python3.9 main.py`

## Useful Links
- If you have issues installing PyAudio on Ubuntu, refer to [this post](https://stackoverflow.com/questions/73268630/error-could-not-build-wheels-for-pyaudio-which-is-required-to-install-pyprojec)
- [Voice Vox Documentation](https://voicevox.github.io/voicevox_engine/api/)
- [DeepL API Documentation](https://www.deepl.com/docs-api/introduction/)
- [Whisper Documentation](https://github.com/openai/whisper)