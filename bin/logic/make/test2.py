# -*- coding: utf-8 -*-
import os
import sys
from os.path import dirname, abspath

BASE_PATH = abspath(dirname(dirname(dirname(dirname(__file__)))))
print("asssssss")
print(BASE_PATH)
sys.path.append(BASE_PATH)
current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
print("222", dirname(__file__))
