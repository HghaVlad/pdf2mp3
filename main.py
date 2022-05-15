from pdfminer.high_level import extract_text
from gtts import gTTS
import os.path

def imporpdf():
    path = input("Please enter the full path: ")
    if os.path.isfile(path) and path.endswith('.pdf'):
        print("Importing done")
        text = extract_text(path).replace("\n",'')
        print("Please enter where paste mp3 file\nYou can enter 'pass' to set file path:\n"+str(path.replace(".pdf",'.mp3')))
        outputfile(text,path)
    elif path == 'Cancle':
        pass
    else:
        print("Please enter right path pdf file")
        print("You can print 'Cancle' to stop program")
        imporpdf()
def outputfile(text,inpath):
    outpath = input()
    if outpath == 'Cancle':
        pass
    elif outpath == 'pass':
        outpath = inpath.replace(".pdf",".mp3")
        getlanguage(text,outpath)
    else:
        getlanguage(text,outpath)

def getlanguage(text,outpath):
    lang = input("Please enter the language\n For example 'ru' or 'en': ")
    if len(lang) == 2:
        print("Language selecting completed")
        converting(text,outpath,lang)
    else:
        print("Pring right language")
        getlanguage(text,outpath)

def converting(text,path,lang):
    print("STARTING CONVERTING")
    tts = gTTS(text, lang=lang)
    print("STARTING RECORDING")
    tts.save(path)
    print(text)
    print("Job completed")

if __name__ == "__main__":
	imporpdf()