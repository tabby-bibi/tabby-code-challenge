# openCV - 이미지 윤곽선 검출
import cv2

src = cv2.imread("../Image/thumbs_up_down.jpg")

gray = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
#이미지의 색공간 변경함수  : 이미지의 색상 공간을 변경하는데 사용
ret, binary = cv2.threshold(gray, 127, 255, )



#이미지 이진화
binary = cv2.bitwise_not(binary)
#
# while True:
#     cv2.imshow("binary", src)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#윤곽선, 계층 구조 : cv2.findContours

for i in range(len(contours)):
    cv2.drawContours(src, [contours[i]], i, (0, 255, 0), 2)
    cv2.putText(src, str(i), tuple(contours[i][0][0]), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0) , 1)
    print(i, hierarchy[0][i])
    cv2.imshow("Contours", src)
    cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == 27:
        break



cv2.destroyAllWindows()

