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

4. [DeepL API Key](https://www.deepl.com/pro-api?cta=header-pro-api/).

5. Install `ffmpeg` and add it to the PATH.
    - [Windows](https://ffmpeg.org/download.html)
    - [Ubuntu](https://linuxize.com/post/how-to-install-ffmpeg-on-ubuntu-20-04/)

## Setting Up 

Once you have all the pre-requisites, run the following commands to start the project:
- Create a copy of the `.env.example` file and rename it to `.env`.
- Replace the `DEEPL_API_KEY` with your api key.
- Run the following commands in the terminal:
    - `pip install -r requirements.txt`
    - `python main.py`

## Useful Links
- [Voice Vox Documentation](https://voicevox.github.io/voicevox_engine/api/)
- [DeepL API Documentation](https://www.deepl.com/docs-api/introduction/)
- [Whisper Documentation](https://github.com/openai/whisper)
- If you have issues installing PyAudio on Ubuntu, refer to [this post](https://stackoverflow.com/questions/73268630/error-could-not-build-wheels-for-pyaudio-which-is-required-to-install-pyprojec)
- Refer to [this post](https://stackoverflow.com/questions/73845566/openai-whisper-filenotfounderror-winerror-2-the-system-cannot-find-the-file) if you get the following error when trying to transcribe text using whisper:
`FileNotFoundError: [WinError 2] The system cannot find the file specified`
