import cv2
import mediapipe as mp
import time

# initializes a video capture object
cap = cv2.VideoCapture(0)
# define mpHands
mpHands = mp.solutions.hands
# create an object called hands
hands = mpHands.Hands(False, 2, 1, 0.5,0.5)
# tool to draw in mediapipe
mpDraw = mp.solutions.drawing_utils

# to get the fps
pTime = 0
cTime = 0
while True:
    # This function reads a frame from the video capture object (cap) and returns two values:
    # success: A boolean indicating whether the frame was successfully captured.
    # img: The captured video frame as an image.
    success, img = cap.read()

    # convert the image's colors to RGB bec the hands object can use only RGB images
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # get the results
    results = hands.process(imgRGB)
    # shows the x, y, z
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # get each landmark id
            # x, y, z decimal number -> x,y in pixels
            for id, lm in enumerate(handLms.landmark):
                # get the shape of the img
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id ,cx, cy)
                # example of giving order to a landmark
                if id == 0:
                   cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
            # draw the hands points             draw conections
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 /(cTime-pTime)
    pTime = cTime

    # print that in the img output, time --> str
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (0, 255, 0), 3)


    cv2.imshow("image", img)
    cv2.waitKey(1)