import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(duration, filename="recorded_audio.wav"):
    fs = 44100  # Sampling frequency (frames per second)
    channels = 2  # Number of audio channels (stereo)

    print(f"Recording for {duration} seconds...")

    # Start recording
    recorded_audio = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()  # Wait for recording to finish

    # Save recorded audio to a WAV file
    write(filename, fs, recorded_audio)

    print(f"Saved audio to {filename}")

if __name__ == "__main__":
    recording_duration = 5  # Specify recording duration in seconds
    record_audio(recording_duration)