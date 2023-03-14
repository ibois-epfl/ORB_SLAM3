import cv2
import os
import time
import numpy as np

# Read the video from specified path
cap = cv2.VideoCapture("/home/ibois/Downloads/long_beam_record.mov")
fps = 30

exportPath = "./dataset/ExportedFrames/01"
# create a folder to store the frames
if not os.path.exists(exportPath):
    os.makedirs(exportPath)

if(cap.isOpened()== False):
    print("Error opening video stream or file")

frameCounter = 763

# Read until video is completed
while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Display the resulting frame
        cv2.imshow('Frame', frame)
        cv2.imwrite(exportPath + "%06d.png" % frameCounter, frame)
        frameCounter += 1

        # Press Q on keyboard to  exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

intervalBetweenFrames = int(1000000000 / fps)
startTime = time.time() * 1e9
with open(os.path.join(exportPath, 'times.txt'), 'w') as file:
    for i in range(frameCounter):
        file.write(format(startTime + intervalBetweenFrames * i, '.0f') + "\n")