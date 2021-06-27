# Creating a VideoCapture object
# This will be used for image acquisition later in the code.

cap = cv2.VideoCapture("video.mp4")
time.sleep(3)     

background=0

for i in range(30):                     # So much time given to prevent descrepencies due to the camera just starting up.
  ret,background = cap.read()
background = np.flip(background,axis=1) # Laterally invert the image / flip the image.

ret, img = cap.read()                   # Capturing the live frame
img = np.flip(imgaxis=1)                # Laterally invert the image / flip the image

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
mask1 = cv2.inRange(hsv, lower_red, upper_red) # Masking a range of red colors

lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsv,lower_red,upper_red)

mask1 = mask1+mask2                           # Generating the final mask to detect red color

mask1 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
mask1 = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8)) # Segmenting out the detected red colored cloth


mask2 = cv2.bitwise_not(mask1)                # Creating an inverted mask to segment out the cloth from the frame

res1 = cv2.bitwise_and(img,img,mask=mask2)    # Segmenting the cloth out of the frame using bitwise and with the inverted mask

res2 = cv2.bitwise_and(background, background, mask = mask1) # Vreating image showing static background frame pixels only for the masked region

# Generating the final output
final_output = cv2.addWeighted(res1,1,res2,1,0)
imshow("magic",final_output)
cv2.waitKey(1)
