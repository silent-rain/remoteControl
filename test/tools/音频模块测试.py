from threading import *
import time
import pyaudio  # sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
import wave

from lib import settings

"""
音频模块
pyaudio:
依赖库
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
"""

# 定义数据流块
CHUNK = 1024


class PlayMusic(Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.wf = wave.open(filename, 'rb')  # (sys.argv[1], 'rb')
        self.play_audio = pyaudio.PyAudio()  # 创建一个播放器

        # 打开数据流
        self.stream = self.play_audio.open(format=self.play_audio.get_format_from_width(self.wf.getsampwidth()),
                                           channels=self.wf.getnchannels(),
                                           rate=self.wf.getframerate(),
                                           output=True)
        # 读取数据
        self.data = self.wf.readframes(CHUNK)

        self.flag = True

    def run(self) -> None:
        while len(self.data) > 5:
            if not self.flag:
                return None
            # 播放
            self.stream.write(self.data)
            self.data = self.wf.readframes(CHUNK)

    def stop(self) -> None:
        """
        停止播放
        :return:
        """
        self.flag = False


if __name__ == "__main__":
    tr = PlayMusic(settings.SOUND_ONLINE)
    # tr.setDaemon(True)
    tr.start()
    time.sleep(1)
    tr.stop()

    tr = PlayMusic(settings.SOUND_ONLINE)
    # tr.setDaemon(True)
    tr.start()

    # tr.stop()
    # tr.join()
