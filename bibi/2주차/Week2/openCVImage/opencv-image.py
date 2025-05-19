#기본 이미지 출력 코드입니다

import cv2
image = cv2.imread("../Image/testimage.jpg", cv2.IMREAD_ANYCOLOR)
#cv2.imread(fileName, flags) -> flags : 이미지 불러올때 적용할초기상태
#ANYCLOLOR : 가능한 3채널 색상이미지로 사용 ? -> 나중에 알아보기
cv2.imshow("Image Test", image)
cv2.waitKey(0) #키입력 대기함수 사용하지 않을 경우 바로 윈도우가 종료됨 -> 키 입력시 윈도우를 종료하는 메서드


# 추가
# height, width = image.shape #width vs width channel
# print(height, width)
cv2.destroyAllWindows()