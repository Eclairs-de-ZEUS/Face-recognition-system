import pyaudio
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

def speech_to_file(filename: str, record_sec: int) -> None:
    audio = pyaudio.PyAudio()

    # start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    # recording
    print ("Recording...")
    frames = []
    for i in range(0, int(RATE / CHUNK * record_sec)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("Recording finished")

    # stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save in wav file
    waveFile = wave.open(filename, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
