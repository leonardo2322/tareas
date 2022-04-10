
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('puedes hablar...')
    audio = r.listen(source)
    
    try: 
        texts = r.recognize_google(audio)
        print('que dices {}'.format(texts))
    except:
        print('i am sorry i can not understand!')
        