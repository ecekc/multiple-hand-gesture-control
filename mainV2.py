import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw

    if hands:
        for hand in hands:
            lmList = hand["lmList"]  # List of 21 Landmarks points
            fingers = detector.fingersUp(hand)
            handType = hand["type"]  # "Right" veya "Left"

            # Hesaplanacak metin konumu için başlangıç noktası
            if handType == "Left":
                baseX = 10
            elif handType == "Right":
                baseX = img.shape[1] - 150

            # Parmak durumlarını metin olarak görüntüleme
            for i, finger in enumerate(fingers):
                text = "Up" if finger else "Down"
                cv2.putText(img, f"{handType} Hand - Finger {i+1}: {text}", (baseX, 30 + i * 20), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)

            # Parmak durumlarını metin olarak görüntüleme
            for i, finger in enumerate(fingers):
                text = "Up" if finger else "Down"
                cv2.putText(img, f"{handType} Hand - Finger {i+1}: {text}", (baseX, 30 + i * 20), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)

            

    cv2.imshow("Resim", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
