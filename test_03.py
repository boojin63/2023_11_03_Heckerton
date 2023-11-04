import serial
import cv2
import pygame

pygame.mixer.init()
pygame.init()

# 상수로 파일 경로 정의
SERIAL_PORT = '/dev/cu.usbmodem142201'
VIDEO_FILE = '/Users/boojin/PycharmProjects/pythonProject/videos/test_04.mov'
SOUND_FILE = '/Users/boojin/PycharmProjects/pythonProject/videos/sound_test.wav'

try:
    ser = serial.Serial(SERIAL_PORT, 9600)

    while True:
        data = ser.readline().strip()
        waterlevel = int(data)

        if waterlevel >= 90:
            print(f"데이터가 {waterlevel}% 이상입니다")

            video = cv2.VideoCapture(VIDEO_FILE)
            while video.isOpened():
                ret, frame = video.read()
                if not ret:
                    break
                cv2.imshow("Water Level Alert", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            video.release()
            cv2.destroyAllWindows()

            sound = pygame.mixer.Sound(SOUND_FILE)
            sound.play()

            pygame.time.delay(int(sound.get_length() * 1000))

except serial.SerialException as e:
    print(f"시리얼 포트 오류: {e}")

finally:
    pygame.mixer.quit()