import cv2
import mediapipe as mp
import pyautogui
import time
import pickle
import warnings
import tkinter as tk
from tkinter import filedialog
import os

warnings.filterwarnings("ignore", category=UserWarning)


root = tk.Tk()
root.withdraw()
root.iconbitmap("icon.ico")
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = filedialog.askopenfilename(
    title="Select your trained model file",
    initialdir=current_dir,
    filetypes=[("Pickle Files", "*.pkl"), ("All Files", "*.*")]
)


if not file_path:
    print("No model file selected. Exiting.")
    exit()


with open(file_path, "rb") as f:
    model = pickle.load(f)

print(f"Model loaded successfully: {file_path}")

# with open("E:\Learning\Python\GestureRecognition\gesture_model.pkl", "rb") as f:
#     model = pickle.load(f)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
prev_label = None
last_trigger_time = 0

while True:
    success, frame = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.extend([lm.x, lm.y, lm.z])


            label = str(model.predict([landmarks])[0])


            if time.time() - last_trigger_time > 1:
                if label == 'good' and prev_label != 'good':
                    pyautogui.press('left')
                    print("previous page")
                    prev_label = 'good'
                    last_trigger_time = time.time()
                elif label == 'ok' and prev_label != 'ok':
                    pyautogui.press('right')
                    print("next page")
                    prev_label = 'ok'
                    last_trigger_time = time.time()
    else:
        prev_label = None

    cv2.imshow("Hand Gesture PPT Controller", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()