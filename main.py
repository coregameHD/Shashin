#!/usr/bin/env python3

'''
Project: Shashin
Description: Interactive Photo Booth on Raspberry Pi 3
Tools: Python3, PIL, Pillow, OpenCV2

Github: https://github.com/coregameHD/Shashin
'''

import capture
import frontend

def run():
    capture.ShashinVideoCapture()
    frontend.ShashinImageEditor()

run()
