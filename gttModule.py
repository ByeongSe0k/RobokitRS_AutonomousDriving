import speech_recognition as sr
from gtts import gTTS
import os
import playsound
import time as t

#음성변환
def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename='voice.mp3'
    tts.save(filename) # 파일을 만들고
    playsound.playsound(filename) # 해당 음성파일을 실행(즉, 음성을 말함)
    os.remove(filename) # <---- 이부분이 없으면 퍼미션 에러 발생(아마도 파일을 연 상태에서 추가적인 파일생성 부분에서 에러가 발생하는 것으로 보임)

#음성인식
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("지금 말씀하세요!")
        t.sleep(1)
        audio = r.listen(source)
        said = " "

        try:
            said = r.recognize_google(audio, language="ko-KR")
            print("speak : ", said)

        except Exception as e:
            print("Exception: ")
    
    return said

speak("2초 후에 '지금 말씀하세요: '가 나오면 음성이 인식됩니다.")

text=get_audio()
speak(text)

speak("2초 후에 '지금 말씀하세요: '가 나오면 음성이 인식됩니다.")
text=get_audio()
speak(text)

if "전진" in text:
    speak("앞으로 이동합니다.")
    print("앞으로 이동")
    forward(5)
    t.sleep(1)