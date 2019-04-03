import os
import speech_recognition as sr
import sys
import webbrowser


def talk(words):
    print(words)
    os.system('say ' + words)


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Говорите')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        result = r.recognize_google(audio, language='ru-RU').lower()
        print(f'Вы сказали {result}')
    except sr.UnknownValueError:
        talk('Я вас не поняла')
        result = command()
    return result


def make(commands):
    if 'открой сайт' in commands:
        talk('Уже открываю')
        url = commands[12:]
        print(url)
        webbrowser.open(f'http://{url}')
    elif 'выключись' in commands:
        talk('Завершаюсь. Хорошего дня')
        sys.exit()


def main():
    while True:
        make(command())


if __name__ == '__main__':
    main()
