# -*- coding: utf-8 -*-
import pyaudio
import numpy as np


def monitor_audio():
    chunk = 512
    format_ = pyaudio.paInt16
    channels = 1
    rate = 48000
    p = pyaudio.PyAudio()
    stream = p.open(format=format_,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)


if __name__ == '__main__':
    monitor()
