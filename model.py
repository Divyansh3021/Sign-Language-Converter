import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model
import time
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',125)
voices = engine.getProperty('voice')
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HAZEL_11.0")

class hand_detection:

    def __init__(self, string):
        self.string = string

    def gesture_detect(self):
        mpHands = mp.solutions.hands
        hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        mpDraw = mp.solutions.drawing_utils

        prev_classname = ""

        # Load the gesture recognizer model
        model = load_model("Gesture Recognition\mp_hand_gesture")

        # Load class names
        f = open('Gesture Recognition\gesture.names', 'r')
        classNames = f.read().split('\n')
        f.close()
        print(classNames)
        cap = cv2.VideoCapture(0)
        while True:
            # Read each frame from the webcam
            _, frame = cap.read()
            x, y, c = frame.shape
            # Flip the frame vertically
            frame = cv2.flip(frame, 1)
            framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Get hand landmark prediction
            result = hands.process(framergb)
            className = ''
            # post process the result
            if result.multi_hand_landmarks:
                landmarks = []
                for handslms in result.multi_hand_landmarks:
                    for lm in handslms.landmark:
                        # print(id, lm)
                        lmx = int(lm.x * x)
                        lmy = int(lm.y * y)
                        landmarks.append([lmx, lmy])
                    # Drawing landmarks on frames
                    mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
                    # Predict gesture
                    prediction = model.predict([landmarks])
                    # print(prediction)
                    classID = np.argmax(prediction)

                    # prev_classname = className
                    className = classNames[classID]
            # show the prediction on the frame
            # cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
            #             1, (0,0,255), 2, cv2.LINE_AA)

            # Show the final output
            cv2.imshow("Output", frame)
            print("Prev_classname is: ", prev_classname)
            print("Current Classname is: ", className)

            if prev_classname != className:
                self.string = self.string + className + " "

            prev_classname = className
            # cv2.putText(frame, self.string, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 
            #             1, (0,0,255), 2, cv2.LINE_AA)

            print("Current string is: " +self.string)

            if cv2.waitKey(1) == ord('q'):
                break
            time.sleep(0.1)
            

        # release the webcam and destroy all active windows
        cap.release()

        cv2.destroyAllWindows()

        self.speak()

    def speak(self):
        engine.say(self.string)
        engine.runAndWait()

import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize



print(op_str)
class string_to_symbol:

    def __init__(self, string):
        self.string = string
        stop_words = set(stopwords.words('english'))

    def removing_stop_words(self):
        words = self.string.split()

        op_str = ""
        for word in words:
            if not word in stop_words:
                op_str += word + " "
        
        return op_str 

# hand_object = hand_detection("")
# hand_object.gesture_detect()