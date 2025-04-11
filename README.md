# 📽️Hand Gesture Controlled PPT Page Turner

This Python program allows you to control PowerPoint slides using hand gestures captured by a webcam. With a trained hand gesture recognition model, you can perform actions like moving to the **next** or **previous** slide using specific gestures.

## 📸 Demo

![](E:\Learning\Python\PageTurn\page_turn.gif)



## 🚀 Features

- Real-time hand gesture detection using **MediaPipe**
- Gesture classification using a **custom-trained model**
- Automatically simulates **keyboard input** (`left` and `right` arrow keys) for slide control
- Easy model selection via a file dialog
- Supports gesture labels like `'good'` and `'ok'`



## 🧪 How to Use

1. **Train a gesture model**

   Please check [gesture_recognition](https://github.com/chloexj/gesture_recognition). If you don't want to train your own model, there's a link to download the one I trained.

2. **Install dependencies**

   ```bash
   pip install opencv-python mediapipe pyautogui scikit-learn
   ```

3. **Run the program**

   ```bash
   python page_turn.py

3. **Select your model** when the file dialog appears.

4. **Show gestures to the camera**:

   - `good` 👍 → previous page

   - `ok` 👌 → next page

5. **Exit**: Press `ESC` to quit the program.