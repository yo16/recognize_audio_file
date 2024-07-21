from dotenv import load_dotenv
import os
import subprocess
import speech_recognition as sr

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


    # 音声認識
    # Initialize the recognizer
    r = sr.Recognizer()

    # Transcribe the audio file
    with sr.AudioFile(wav_audio_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="ja-JP")

    return text

if __name__=="__main__":
    text = getText("./data/_10452999.m4a")
    print(text)
