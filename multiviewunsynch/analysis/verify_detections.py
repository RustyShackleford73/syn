# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import numpy as np
import cv2
from time import sleep
'''
This script verifies drone detections of a given video by playing the video with the detections in background
'''

# Read a video and its corresponding detection
detection_path = 'test/kpts_cam0.dat'
video_path = '/mnt/usb/bodypose3d/media/cam0_test.mp4'
joint_id = 0
# Create a mask for detections in the same size of the video
detection = np.loadtxt(detection_path, usecols=(0, 2*joint_id+1,2*joint_id+2)).T.astype(int)
# detection = np.loadtxt(detection_path[1:],usecols=(0,1,2)).T.astype(int)
cap = cv2.VideoCapture(video_path)
cap.set(cv2.CAP_PROP_POS_FRAMES,10)
frame_0 = cap.read()[1]
traj = np.zeros_like(frame_0)
for i in range(detection.shape[1]):
    traj[detection[2,i],detection[1,i],0] = 1

# Plot all detections in each frame
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # frame = cv2.flip(frame,0)
        sleep(0.1)
        frame[traj[:,:,0]==1]=np.array([255,0,0])     # Color of the traj can be specified
        # frame = cv2.resize(frame,(1400,570))
        cv2.imshow('Check Dectections, Press \'q\' to end',frame)

    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


print('Finish!')