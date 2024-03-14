{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "67150454-0d56-4319-9b01-79ddaa0f6767",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import mediapipe as mp\n",
    "import pyautogui\n",
    "\n",
    "\n",
    "kartik = cv2.VideoCapture(0)\n",
    "face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)\n",
    "screen_w, screen_h = pyautogui.size()\n",
    "while True:\n",
    "    _, frame = kartik.read()\n",
    "    frame = cv2.flip(frame, 1)\n",
    "    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)\n",
    "    output = face_mesh.process(rgb_frame)\n",
    "    landmark_points = output.multi_face_landmarks \n",
    "    frame_h, frame_w, _ = frame.shape\n",
    "    if landmark_points:\n",
    "        landmarks = landmark_points[0].landmark\n",
    "        for id, landmark in enumerate(landmarks[474:478]): \n",
    "            x = int(landmark.x * frame_w)\n",
    "            y = int(landmark.y * frame_h)\n",
    "            cv2.circle(frame, (x, y), 3, (0, 255, 0))\n",
    "            if id == 1:\n",
    "                screen_x = screen_w * landmark.x\n",
    "                screen_y = screen_h * landmark.y\n",
    "                pyautogui.moveTo(screen_x, screen_y)\n",
    "        left = [landmarks[145], landmarks[159]]\n",
    "        for landmark in left:\n",
    "            x = int(landmark.x * frame_w)\n",
    "            y = int(landmark.y * frame_h)\n",
    "            cv2.circle(frame, (x, y), 3, (0, 255, 255))\n",
    "        if (left[0].y - left[1].y) < 0.004:\n",
    "            pyautogui.click()\n",
    "            pyautogui.sleep(1)\n",
    "    cv2.imshow('Eye Controlled Mouse', frame)\n",
    "    cv2.waitKey(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fb26627b-2115-4f8c-9841-07b6b34f23d2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7cb07140-ed4e-41b6-b9ff-40109ded3720",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
