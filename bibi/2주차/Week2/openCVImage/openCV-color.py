import cv2
import numpy as np

# HSV 검은색 범위 지정
lower_black = np.array([0, 0, 0])
upper_black = np.array([180, 255, 50])  # 명도 낮은 검은색

# 노트북 카메라 캡처
capturedVideo = cv2.VideoCapture(0)

while True:
    success, video = capturedVideo.read()
    if not success:
        break

    # BGR -> HSV 변환
    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    # 마스크 생성
    mask = cv2.inRange(img, lower_black, upper_black)

    # 윤곽선 검출
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # 일정 면적 이상만
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Mask Test", mask)
    cv2.imshow("Detected", video)

    # ESC 키 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

capturedVideo.release()
cv2.destroyAllWindows()
