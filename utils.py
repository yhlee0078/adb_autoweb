import os
import glob
import time
#import cv2
#import numpy as np


from config import CORD_CLOSE_APP, CORD_CLOSE_APP_VERT
# TODO: integrate scell implementation with RF_NUM
from config import RF_NUM

import logging
import coloredlogs
import pprint as pp

logger = logging.getLogger(__name__)
coloredlogs.install(level=logging.INFO)

def cmd(cmd, interval=1):
    os.system("adb shell " + cmd)
    time.sleep(interval)


def check_adb():
    os.system("adb devices")
    time.sleep(2)


def close_all_app():
    cmd("input keyevent KEYCODE_APP_SWITCH", interval=1)
    cmd("input tap %d %d" % CORD_CLOSE_APP, interval=1)
    #cmd("input keyevent KEYCODE_DPAD_DOWN", interval=3)
    #cmd("input keyevent KEYCODE_ENTER", interval=3)
    #cmd("input keyevent KEYCODE_HOME")

def close_all_app_vert():
    cmd("input keyevent KEYCODE_APP_SWITCH", interval=1)
    cmd("input tap %d %d" % CORD_CLOSE_APP_VERT, interval=1)
    #cmd("input keyevent KEYCODE_DPAD_DOWN", interval=3)
    #cmd("input keyevent KEYCODE_ENTER", interval=3)
    #cmd("input keyevent KEYCODE_HOME")

def get_links(fname):
    with open(fname, 'r') as f:
        links = f.read().splitlines()
    links = list(map(lambda x: x.split(','), links))
    return links
    #ssh.close()
