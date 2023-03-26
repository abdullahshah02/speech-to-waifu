import pyaudio
import wave
import keyboard


def record_audio(
    key: str = "shift", output_file_name: str = "./output.wav"
) -> tuple[str, bool]:
    """
    This function records audio from the microphone and saves it to a file.
    It will record audio as long as the "key" is pressed.

    Args:
        key (str): The key to press to start recording.
        output_file_name (str): The name of the file to save the audio to.

    Returns:
        str: The path of the file the audio was saved to.
        bool: Whether or not the recording was successful.
    """
    assert key != "", "ERROR: The key to press to start recording is not defined."

    p = pyaudio.PyAudio()
    recordedFrames = []

    chunk = 1024
    format = pyaudio.paInt16
    channels = 2
    rate = 44100

    stream = p.open(
        format=format,
        channels=channels,
        rate=rate,
        frames_per_buffer=chunk,
        input=True,
    )

    print(f"Hold the '{key}' key to start recording. (Esc to quit)")
    while True:
        if keyboard.is_pressed(key):
            print("Recording...")
            try:
                while True:
                    data = stream.read(chunk)
                    recordedFrames.append(data)
                    if keyboard.is_pressed(key) is False:
                        break
            except:
                print("ERROR: An error occured during recording.")

            print("Finished Recording.")
            break
        elif keyboard.is_pressed("escape"):
            return (None, False)

    # Stop recording
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save audio to file
    wf = wave.open(output_file_name, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b"".join(recordedFrames))
    wf.close()

    return (output_file_name, True)
