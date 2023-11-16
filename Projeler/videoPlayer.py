import cv2
import os
from pathlib import Path


video_ismi = input("video ismi giriniz: ")
video_yolu = input("video yolu giriniz: ")

def videoyu_bul(isim,yol):
    bulunan_videolar = list()
    for path, subdirs, files in os.walk(yol):
        for i in files:
            if(isim==i):
                bulunan_videolar.append(os.path.join(path,i))
    return bulunan_videolar[0]


os.chdir(Path(videoyu_bul(video_ismi,video_yolu)).parent)

son_video_yolu = videoyu_bul(video_ismi, video_yolu)

def videoyuOynat(yol):
    video = cv2.VideoCapture(yol)
    while True:
        yakalanan, kare = video.read()
        if not yakalanan:
            print("video bitti")
            break
        cv2.imshow("Video",kare)
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()
    
videoyuOynat(son_video_yolu)