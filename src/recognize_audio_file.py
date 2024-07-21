from dotenv import load_dotenv
import os
import io
import subprocess

import speech_recognition as sr
from google.cloud import speech_v1p1beta1 as speech

## ffmpegをパスに追加
load_dotenv()
ffmpeg_path = os.getenv("FFMPEG_PATH")


# .m4aファイルを文字興しする
def getText(m4a_file_path):
    # .m4aファイルを、.wavファイルへ変換
    tmp_dir = "./tmp"
    os.makedirs(tmp_dir, exist_ok=True)
    m4a_filename_without_extension = os.path.splitext(os.path.basename(m4a_file_path))[0]
    wav_audio_path = f"{tmp_dir}/{m4a_filename_without_extension}.wav"

    # ffmpeg.exeを直接コマンドで実行する
    # この代わりに実行するモジュールがあったが、pathの関係か、うまく動かないのでこの形になった
    command = [ffmpeg_path, "-i", m4a_file_path, wav_audio_path, "-y"]
    subprocess.run(command, check=True)


    # wavファイルから文字興しする
    text = wav2text_speech_recognition(wav_audio_path)
    #text = wav2text_google_speech_to_text(wav_audio_path)
    return text


def wav2text_speech_recognition(wav_audio_path):
    # 音声認識
    # Initialize the recognizer
    r = sr.Recognizer()

    # Transcribe the audio file
    with sr.AudioFile(wav_audio_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="ja-JP")

    return text


# いちおう書いてみたSpeech to text版
# 認証周りを一切やらずに書いただけなので、当然エラーになり、そこまでしかできていない状態
def wav2text_google_speech_to_text(wav_audio_path):
    client = speech.SpeechClient()

    with io.open(wav_audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ja-JP",
    )

    response = client.recognize(config=config, audio=audio)
    text = ""
    for result in response.results:
        text += result.alternatives[0].transcript

    return text


if __name__=="__main__":
    text = getText("./data/_10453009.m4a")
    print(text)
