import cv2
import numpy as np
import time

capture_video = cv2.VideoCapture(0) 	# Input Video using Webcam 0


time.sleep(1)
count = 0
background = 0

for i in range(60):						# Giving time for camera to open and take a snap of view to use as a background
	return_val, background = capture_video.read()
	if return_val == False :
		continue

background = np.flip(background, axis = 1) # flipping the frame to its mirror image


while (capture_video.isOpened()):
	return_val, img = capture_video.read()
	if not return_val :
		break
	count = count + 1
	img = np.flip(img, axis = 1)

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)		# Converting image to HSV


	lower_red = np.array([100, 40, 40])	
	upper_red = np.array([100, 255, 255])
	mask1 = cv2.inRange(hsv, lower_red, upper_red)	# setting the upper and lower ranges for mask1

	lower_red = np.array([155, 40, 40])
	upper_red = np.array([180, 255, 255])
	mask2 = cv2.inRange(hsv, lower_red, upper_red)	# setting the upper and lower ranges for mask1

	mask1 = mask1 + mask2		# Now all mask data is in mask 1

	# Refining the mask corresponding to the detected red color
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3),
										np.uint8), iterations = 2)
	mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations = 1)
	mask2 = cv2.bitwise_not(mask1)

	# Final Output
	res1 = cv2.bitwise_and(background, background, mask = mask1)
	res2 = cv2.bitwise_and(img, img, mask = mask2)
	final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

	cv2.imshow("INVISIBLE MAN", final_output)
	k = cv2.waitKey(10)
	if k == 27:
		break
