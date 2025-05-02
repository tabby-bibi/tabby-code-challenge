from warnings import catch_warnings

import numpy as np
import cv2

capture = cv2.VideoCapture(0)
#Video Capture - 비디오 출력 클래스를 통해 내장 및 외장 카메라의 정보를 받아옴
#index : 카메라의 장치 번호 , 노트북 카메라(내장)의 경우 0번
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#카메라 속성 설정 메서드 : 카메라의 속성(propid)과 값(value)를 설정할 수 있다

while cv2.waitKey(33) < 0: # waitKey : 키 입력 대기함수 , 지정된 시간동안 키 입력있을때까지 프로그램 지연시킨다
    ret, frame = capture.read() #프레임 읽기메서드 : 카메라의 상대 및 프레임을 받아온다
    #ret : 카메라의 상태가저장, 정상 작동할 경우 True를 반환, 작동하지 않을 경우 False를 반환
    #frame : 현재 시점의 프레임이 저장된다.
    cv2.imshow("VedioFrame", frame)


capture.release() #카메라 장치에서 받아온 메모리 해제
cv2.destroyAllWindows() #모든 윈도우 창 제거 함수
#특정 윈도우마 제거할 경우 cv2.destroyWindow(winname)으로 제거할 수 있다.

