# Imports for my Virtual Mouse
import cv2
import mediapipe as mp
import pyautogui   #This import is for conneting our finger landmark with arrow motion

#Soo Here Cv2 used to capture Image/Video
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()  #Its Using for Detect Object our Hand
drawing_utils = mp.solutions.drawing_utils  #Its Using for drawing points on hands
screen_width, screen_height = pyautogui.size() #This for getting whole screen width,height for our cursor
index_y = 0
while True:
#Landmarks is detecting in hand_detector var
#Getting Frame with cv2 and output landmarks in hands so next adding condintion
    _, frame = cap.read()
    frame = cv2.flip(frame, 1) #This fill flip camera video in same direction 0 means x axis 1 means Y axis
    frame_height, frame_width, _= frame.shape #From shape we get height and with of frame for Screensize arrow motion
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand) #Calling utils to draw landmarks and display
            landmarks = hand.landmark #Now to point finger landmark as no 8 we will set a loop for every frame
            for id, landmark in enumerate(landmarks): #Need to now x,y mark of finger
                x = int(landmark.x*frame_width)  #X is horizontal axis
                y = int(landmark.y*frame_height) #Y is Vertical axiis
                #By adding int() braces we get decimal numbersx

                # print(x,y) #Point finger landmark as no 8 to detect and draw a circle on it
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    #Now we have to connect out landmark piont with arrow so we'r using pyautogui
                    index_x = screen_width/frame_width*x #This for getting actual frame of your window
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y) #To move Cursor use moveTo

                #For Cursor Event x
                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    #Now we have to connect out landmark piont with arrow so we'r using pyautogui
                    thumb_x = screen_width/frame_width*x #This for getting actual frame of your window
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    #Condition for shortest and no distance between two points
                    if abs(index_y - thumb_y) < 25:
                        pyautogui.click(button='right')
                        pyautogui.sleep(1)
                        print('right')

                #For Cursor Event x
                if id == 12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    #Now we have to connect out landmark piont with arrow so we'r using pyautogui
                    thumb_x = screen_width/frame_width*x #This for getting actual frame of your window
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    #Condition for shortest and no distance between two points
                    if abs(index_y - thumb_y) < 15:
                        pyautogui.click(button='left')
                        pyautogui.sleep(1)
                        print('left')

                #For Scroll Event X
                if id == 20:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    #Now we have to connect out landmark piont with arrow so we'r using pyautogui
                    thumb_x = screen_width/frame_width*x #This for getting actual frame of your window
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    #Condition for shortest and no distance between two points
                    if abs(index_y - thumb_y) < 55:
                        pyautogui.hscroll(100)
                        pyautogui.sleep(1)
                        print('scrollup')

                #For Event Y
                if id == 16:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    #Now we have to connect out landmark piont with arrow so we'r using pyautogui
                    thumb_x = screen_width/frame_width*x #This for getting actual frame of your window
                    thumb_y = screen_height/    frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    #Condition for shortest and no distance between two points
                    if abs(index_y - thumb_y) <50:
                        pyautogui.hscroll(-100)
                        pyautogui.sleep(1)
                        print('scrolldown')

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)

# cap.release()