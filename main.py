import pygame
import pygame.midi
from pygame.locals import *

pygame.midi.init()

print("\n \n \n ")
print"AVAILABLE MIDI DEVICES"
for x in range(0, pygame.midi.get_count()):
    device = ' - '.join(map(str, pygame.midi.get_device_info(x)))
    output  = ' | '.join((str(x), device))
    print(output)
print("\n")

inputDeviceID = raw_input("INPUT DEVICE ID: ")
outputDeviceID = raw_input("OUTPUT DEVICE ID: ")

inputDevice = pygame.midi.Input(int(inputDeviceID))

print("Reading input stream: ")

while True: 
     print(inputDevice.read(100))

