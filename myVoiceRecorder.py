import sounddevice as sd
import wavio as wv

freq = 44100
duration = int(input("Please enter the duration of record(as a second):"))


def record_voice(freq, duration):

    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

    sd.wait()

    wv.write("record.wav", recording, freq, sampwidth=2)


try:
    record_voice(freq, duration)
except ValueError:
    print("Please enter second!! ")
