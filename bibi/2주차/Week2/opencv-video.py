# 동영상 출력 - *.avi, *mp4, *.gif(다른 이미지 확장자와 다르게 프레임 존재하므로 영상처리)
# 기존 저장 되어 있는  동영상을 출력
import cv2

capture = cv2.VideoCapture("Video/test.mp4")
# 동영상의 파일 경로를 지정하여 파일을 가져온다
while cv2.waitKey(33) < 0:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

capture.release()
cv2.destroyAllWindows()

    #CAP_PROPS_POS_FRAMES : 동영상의 현재 프레임 수
    #CAP_PROP_FRAME_COUNT : 동영상의 총 프레임 수
    # -> IF문을 통해 현제 프레임 수와 종 프레임수를 비교해서 같은경우(제일마지막프레임의 경우)
    # CAPTURE.SET을 통해 동영상의 현재 프레임을 초기화한다
    # 또는 CPATURE.OPEN을 통해 동영상 파일을 다시불러올수도 있다!

