import cv2
import numpy as np
import mediapipe as mp

img_size = 128
minValue = 70
source = cv2.VideoCapture(0)
count = 0
string = " "
prev = " "
prev_val = 0
# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

while source.isOpened():
    ret, img = source.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect hands using Mediapipe
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        # Extracting hand landmarks and drawing bounding box
        bbox_min, bbox_max = np.min(hand_landmarks.landmark, axis=0), np.max(hand_landmarks.landmark, axis=0)
        bbox_min, bbox_max = tuple(np.multiply(bbox_min, [img.shape[1], img.shape[0]]).astype(int)), \
                             tuple(np.multiply(bbox_max, [img.shape[1], img.shape[0]]).astype(int))
        cv2.rectangle(img, bbox_min, bbox_max, (255, 0, 0), 2)

        # Crop and preprocess the hand region
        crop_img = img[bbox_min[1]:bbox_max[1], bbox_min[0]:bbox_max[0]]
        crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

        count = count + 1
        if count % 100 == 0:
            prev_val = count

        cv2.putText(img, str(prev_val // 100), (300, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)

        blur = cv2.GaussianBlur(crop_img, (5, 5), 2)
        th3 = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        ret, res = cv2.threshold(th3, minValue, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        resized = cv2.resize(res, (img_size, img_size))

        normalized = resized / 255.0
        reshaped = np.reshape(normalized, (1, img_size, img_size, 1))

        result = model.predict(reshaped)
        label = np.argmax(result, axis=1)[0]

        if count == 300:
            count = 99
            prev = labels_dict[label]
            if label == 0:
                string = string + " "
            else:
                string = string + prev

        cv2.putText(img, prev, (24, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv2.putText(img, string, (275, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 200, 200), 2)

    cv2.imshow('LIVE', img)

    key = cv2.waitKey(1)
    if key == 27:  # press Esc. to exit
        break

print(string)
cv2.destroyAllWindows()
source.release()
cv2.destroyAllWindows()