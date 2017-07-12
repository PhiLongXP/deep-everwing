import deep_capture
from PIL import Image

import time

dc = deep_capture.create_display_capture()
dc.init()
dc.start()

time.sleep(0.1) # Wait for DC start

GAME_RECT = [160, 157, 321, 570]
# 3 frame per seconds
for i in range(100):
    time.sleep(0.3)
    frame = dc.capture(GAME_RECT)
    frame = frame[...,[2,1,0,3]] #BGRA -> RGBA
    im = Image.fromarray(frame)
    im.save("captures/%d.png"%time.time())
dc.stop()
