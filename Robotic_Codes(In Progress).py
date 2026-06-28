# code has yet to be tested will be tested
# Robot movement will be reworked at a later time 
from gpiozero import Robot, Motor
from time import sleep
from playsound3 import playsound
import random
import os

robot = Robot(left = Motor(27, 22), right = Motor (23, 24))
my_audio_folder = 'Once recording session has processed please - I need to put the directory here'


def play_random_audio(levels):
    folder = os.path.join(my_audio_folder, levels)
    clips = os.listdir(folder)
    chosen = random.choice(clips)
    playsound(os.path.join(folder, chosen))


def check_scores(avg_score):
    if avg_score < 100:
        play_random_audio('levels100')
        robot.forward(0.5)
        sleep(5)
        robot.left(1)
        robot.stop()
    elif avg_score < 200:
        play_random_audio('level200')
        robot.forward(1)
        sleep(1)
        robot.right(1)
        robot.left(1)
        sleep(5)
        robot.stop()
    elif avg_score < 300:
        play_random_audio('levels300')
        robot.forward(-1)
        sleep(1)
        robot.forward(1)
        robot.stop()
    elif avg_score < 400:
        play_random_audio('levels400')
        robot.forward(-2)
        sleep(5)
        robot.forward(1)
        robot.stop()
    else:
        print('Let me just add this as a place holder ')
   

    
if __name__ == '__main__':
    my_audio_folder = 'path goes here'

        



