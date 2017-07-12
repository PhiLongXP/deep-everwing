import easy_classify
import cv2
import glob
import time

import matplotlib.pyplot as plt

ec = easy_classify.EasyClassify('data')

training = False

if training:
    ec.train(reset=False, tensorboard=True)
else:
    ec.load()

game_imgs = glob.glob("data/game/*.png")
home_imgs = glob.glob("data/home/*.png")
over_imgs = glob.glob("data/over/*.png")

for img in over_imgs[:3] + home_imgs[:3] + over_imgs[:3]:
    img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    t1 = time.time()
    print(ec.classify(img))
    t2 = time.time() - t1
    print('Time: %.5f'%t2)

    # plt.imshow(img)
    # plt.show()
