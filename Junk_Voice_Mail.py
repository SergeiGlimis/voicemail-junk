import speech_recognition as sr

Spam_Keywords = (".org",".com","We","Register","we need","dollars",
                 "help us")
# i will also decipher in a later version of the call is from a known contact or not.
Non_Spam_Keywords = ("love you","i'll","see you","hey man","sup man",
                     "it's me","later","home")

VM_Audio_File = sr.AudioFile("harvard.wav")

r = sr.Recognizer()

with VM_Audio_File as source:
    audio = r.record(source)

value = r.recognize_google(audio)
print (value)


def Decipher_Junk_VoiceMail():
    
    pass
