# -*- coding: utf-8 -*-
import pyaudio  # sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
import wave

from PyQt5.QtCore import QThread

from lib import settings

"""
音频模块
pyaudio:
依赖库
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
"""

# 定义数据流块
CHUNK = 1024


class PlayMusic(QThread):
    def __init__(self):
        super().__init__()

        # 创建一个播放器
        self.play_audio = pyaudio.PyAudio()

        # 打开数据流
        self.stream = None

        # 控制开关
        self.flag = True

        # 数据
        self.data = b''

        # 读取文件对象
        self.wf = None

        # 运行中
        self.flag_run = False

    def open(self, filename: str) -> None:
        """
        读取音频
        :param filename:
        :return:
        """
        # 控制开关
        self.flag = True

        self.wf = wave.open(filename, 'rb')  # (sys.argv[1], 'rb')
        # 打开数据流
        self.stream = self.play_audio.open(format=self.play_audio.get_format_from_width(self.wf.getsampwidth()),
                                           channels=self.wf.getnchannels(),
                                           rate=self.wf.getframerate(),
                                           output=True)

        # 读取数据
        self.data = self.wf.readframes(CHUNK)

    def run(self) -> None:
        while len(self.data) > 2:
            if not self.flag:
                return None
            self.flag_run = True
            # 播放
            self.stream.write(self.data)
            self.data = self.wf.readframes(CHUNK)
        self.flag = False  # 读取完成,关闭

    def stop(self) -> None:
        """
        停止播放
        :return:
        """
        self.flag = False
        self.flag_run = False


if __name__ == "__main__":
    tr = PlayMusic()
    # tr.setDaemon(True)
    tr.open(settings.SOUND_ONLINE)
    tr.start()
    # time.sleep(1)
    tr.stop()

    tr = PlayMusic()
    tr.open(settings.SOUND_ONLINE)
    # tr.setDaemon(True)
    tr.start()

    # tr.stop()
    # tr.join()
