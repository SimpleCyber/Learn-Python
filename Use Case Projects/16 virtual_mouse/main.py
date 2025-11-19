import cv2
import mediapipe as mp
import pyautogui
import numpy as np


index_x , index_y =0 ,0
# Initialize video capture, hand detector, and drawing utilities
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
drawing_utils = mp.solutions.drawing_utils

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Offsets and smoothing
index_offset_x, index_offset_y = 10, 10  # Adjust these values as needed
thumb_offset_x, thumb_offset_y = 15, 15  # Adjust these values as needed
smoothing_factor = 5
prev_x, prev_y = 0, 0

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Hand detection
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        hand = hands[0]
        drawing_utils.draw_landmarks(frame, hand)

        landmarks = hand.landmark
        frame_width, frame_height, _ = frame.shape

        for id, landmark in enumerate(landmarks):
            x, y = int(landmark.x * frame_width), int(landmark.y * frame_height)

            # Apply smoothing
            x = prev_x + (x - prev_x) / smoothing_factor
            y = prev_y + (y - prev_y) / smoothing_factor

            # Convert x and y to integers for OpenCV drawing functions
            x = int(x)
            y = int(y)

            if id == 8:  # Index Finger Tip
                cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
                index_x = np.interp(x, [0, frame_width], [0, screen_width])
                index_y = np.interp(y, [0, frame_height], [0, screen_height])
                pyautogui.moveTo(index_x - index_offset_x, index_y - index_offset_y)

            if id == 4:  # Thumb Tip
                cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)
                thumb_x = np.interp(x, [0, frame_width], [0, screen_width])
                thumb_y = np.interp(y, [0, frame_height], [0, screen_height])
                distance = np.linalg.norm([index_x - thumb_x, index_y - thumb_y])

                # Dynamic click detection based on distance
                if distance < 20:  # Threshold for click detection
                    pyautogui.click()
                    pyautogui.sleep(1)

            prev_x, prev_y = x, y

    cv2.imshow('Virtual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
