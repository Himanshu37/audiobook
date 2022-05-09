import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('file.pdf', 'rb'))

import pyttsx3
speaker = pyttsx3.init()


# Initialize the speaker
speaker = pyttsx3.init()
rate = speaker.getProperty('rate')   
print(rate)
speaker.setProperty('rate', 125)

voices = speaker.getProperty('voices')
print(voices)
#changing index, changes voices, 0 for male
speaker.setProperty('voice', voices[0].id)
#changing index, changes voices, 1 for female
speaker.setProperty('voice', voices[1].id)

volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)

for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()


engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()


speaker.stop()

