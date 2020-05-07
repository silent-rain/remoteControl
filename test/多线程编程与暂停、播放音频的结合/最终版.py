from threading import *
import time
# from playsound import playsound  # pip install playsound
import pyaudio  # sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
import wave

from lib import settings

"""
pyaudio:
依赖库
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
"""

# 定义数据流块
CHUNK = 1024


class MyMusic(Thread):
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

        self.__flag = Event()  # 用于暂停线程的标识
        self.__flag.set()
        self.ifdo = True

    def run(self) -> None:
        while self.ifdo:
            while len(self.data) > 5:
                self.__flag.wait()
                print('I am running...')
                # time.sleep(2)

                # 播放
                self.stream.write(self.data)
                self.data = self.wf.readframes(CHUNK)
            self.wf = wave.open(self.filename, 'rb')
            self.data = self.wf.readframes(CHUNK)
        # self.data = ''

    def pause(self) -> None:
        """
        暂停播放
        :return:
        """
        self.__flag.clear()  # 设置为False, 让线程阻塞

    def resume(self) -> None:
        """
        继续播放
        :return:
        """
        self.__flag.set()  # 设置为True, 让线程停止阻塞

    def stop(self) -> None:
        """
        停止播放
        :return:
        """
        self.ifdo = False


if __name__ == "__main__":
    tr = MyMusic(settings.SOUND_ONLINE)
    # tr.setDaemon(True)
    tr.start()
    print('\nI will pause it...')
    time.sleep(2)
    # tr.pause()
    print("i will resume it...")
    time.sleep(2)
    tr.resume()
    print("i will stop it...")
    time.sleep(2)
    # tr.stop()
    # time.sleep(1)
    # tr.stop()
    # tr.join()
