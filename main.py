import winsound
from settings import Speaker
from helpers.record import record_audio
from helpers.transcribe import transcribe
from helpers.translate import translate
from helpers.voicevox import synthesize

print("========VOICEVOX TRANSLATOR========")

speaker_id = Speaker.MOCHIKO_NORMAL.value
params = {
    "volumeScale": 5.0,
    "intonationalScale": 1.0,
    "prePhonemeLength": 1.0,
    "postPhonemeLength": 1.0,
}

while True:
    (file_name, success) = record_audio()

    if not success:
        print("Exiting...")
        break
    print()

    print("Transcribing...")
    transcription = transcribe(file_name)
    print("Finished Transcribing.")
    print("Result:", transcription)
    print()

    print("Translating...")
    translation = translate(transcription)
    print("Finished Translating.")
    print("Result:", translation)
    print()

    print("Synthesizing...")
    synthesized_audio_file = synthesize("output.wav", translation, speaker_id, **params)
    print("Finished Synthesizing.")
    print()

    winsound.PlaySound("output.wav", winsound.SND_FILENAME)
