from gtts import gTTS
tts = gTTS('Привет. Я сексуальная блондинка. Пойдёшь вечером ко мне в гости?', lang='ru')
tts.save('hello.mp3')
