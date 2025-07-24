# 🎚️ Gesture-Based Volume Controller

Control your system’s audio volume using hand gestures in real-time through your webcam!  
Built using Python, OpenCV, MediaPipe, and Pycaw, this project turns your fingers into a virtual volume knob 🔊.

---

## 📽️ Demo
[Watch Video on LinkedIn](https://www.linkedin.com/posts/ramlah-munir_...)

---

## 🚀 Features
- 📷 Real-time hand detection with MediaPipe
- 🖐️ Finger distance tracking (thumb & index)
- 🎛️ Volume control based on gesture distance
- 📊 Visual feedback with animated bars
- 🧠 Smooth interpolation for precise control
- 🕒 FPS display for performance

---

## 💻 Tech Stack
| Component | Purpose |
|----------|---------|
| Python   | Programming Language |
| OpenCV   | Image processing & rendering |
| MediaPipe | Hand landmark detection |
| Pycaw    | Audio endpoint interface (Windows) |

---

## 🛠️ Installation

```bash
git clone https://github.com/Ramlah7/gesture-volume-controller.git
cd gesture-volume-controller
pip install -r requirements.txt
python main.py
