# recognize_audio_file
音声ファイルを文字興しする

# 環境準備
- [FFmpeg](https://www.ffmpeg.org/)を端末にインストールしておく
    - windowsの場合、コンパイル済のexeを入手し、program filesなどへコピーしておけばよい
- `.env`ファイルに、`FFMPEG_PATH=path/to/ffmpeg.exe`の形で書いておく
    - `ffmpeg.exe`以外のexeも、同じフォルダにあるものとして利用される可能性あり

# 概要
- `.m4a`形式（MEPG-4）を`.wav`形式へ変換し、それを[SpeechRecognition · PyPI](https://pypi.org/project/SpeechRecognition/)を使って文字列へ変換している。

# 実行に際してメモ
- `speech_recognition`で利用している、`recognize_google`は、googleの[Speech-to-Text AI](https://cloud.google.com/speech-to-text?_gl=1*1co8hjh*_up*MQ..&gclid=Cj0KCQjwwO20BhCJARIsAAnTIVR2VbEiFKUwlcEL4sV3-a1hCv-qW26louZ2G-9fQGnp1Kt23xl5OZgaAqPjEALw_wcB&gclsrc=aw.ds&hl=ja)を使っている模様。
    - １か月で60分間の音声認識が無料
    - おそらく１か月で60分の制限を超えた時点で、利用できなくなると思われる（ipアドレスか何かでカウントされている）
    - 内部的には、[googleapis/google-api-python-client: 🐍 The official Python client library for Google's discovery based APIs.](https://github.com/googleapis/google-api-python-client)を使用しているようだが、詳細は調べ切れていない

# そのほか
- Speech to textを使うだけなのであれば、`speech_recognition`ではなく、`google-api-python-client`を使えばよかった。
