# coding:utf-8
import subprocess
import wave
import pyaudio


def play_audio(wav_name):
    wf = wave.open(wav_name, "r")
    # ストリーム開始
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(1024)
    while(data != ''):
        stream.write(data)
        data = wf.readframes(1024)
    stream.close()      # ストリーム終了
    p.terminate()

cmd = ["sinsy","-x","/usr/local/dic/","-m","/home/kumagai/Downloads/hts_voice_nitech_jp_song070_f001-0.90/nitech_jp_song070_f001.htsvoice","-o","out.wav","test_score2.xml"]
returncode = subprocess.call(tuple(cmd))

play_audio("out.wav")
