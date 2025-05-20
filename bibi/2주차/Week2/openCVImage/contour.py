import cv2
import numpy as np

# 이미지 불러오기
src = cv2.imread("../Image/thumbs_up_down.jpg")

# HSV 색공간으로 변환
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 피부색 범위 정의 (다양한 조명에 따라 값 조정 가능)
lower_skin = np.array([0, 30, 60])
upper_skin = np.array([20, 150, 255])

# 마스크 생성
mask = cv2.inRange(hsv, lower_skin, upper_skin)

# 잡음 제거
mask = cv2.medianBlur(mask, 5)

# 윤곽선 검출
contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

# 윤곽선 그리기
for i in range(len(contours)):
    cv2.drawContours(src, [contours[i]], -1, (0, 255, 0), 2)
    cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# 결과 보기
cv2.imshow("Mask", mask)
cv2.imshow("Contours", src)
cv2.waitKey(0)
cv2.destroyAllWindows()