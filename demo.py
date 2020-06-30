import speech_recognition as sr
import webbrowser as web#to open the query in web browser
r1=sr.Recognizer()#1st instance
r2=sr.Recognizer()#2nd instance
r3=sr.Recognizer()#3rd instance

with sr.Microphone() as source:#input is from microphone
    print('[search edureka:search youtube]')
    print('speak now...')
    audio=r3.listen(source)#taking input

if 'Google' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='https://www.google.com/search?q='
    with sr.Microphone() as source:#input is from microphone
        print('search your query')
        audio=r2.listen(source)#taking input

    try:
        get=r2.recognize_google(audio)
        print(get)
        web.get().open_new(url+get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))

if 'video' in r1.recognize_google(audio):
    r2=sr.Recognizer()
    url='https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:#input is from microphone
        print('search for a vedio')
        audio=r1.listen(source)#taking input

    try:
        get=r1.recognize_google(audio)
        print(get)
        web.get().open_new(url+get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))