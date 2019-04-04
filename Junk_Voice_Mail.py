import speech_recognition as sr

Spam_Keywords = (".org",".com","We","Register","we need","dollars",
                 "help us")
# i will also decipher in a later version of the call is from a known contact or not.
Non_Spam_Keywords = ("love you","i'll","see you","hey man","sup man",
                     "it's me","later","home")

Example_Spam = ["","","","",""]

Example_Non_Spam = ["","","",""]




def Decipher_If_Junk_VoiceMail(File):
    VM_Audio_File = sr.AudioFile(str(File))

    r = sr.Recognizer()

    with VM_Audio_File as source:
        audio = r.record(source)

    value = r.recognize_google(audio)
    print (value)

    spam = 0
    non_spam = 0
    for word in value:
        if word in Spam_Keywords:
            spam = spam +1

        elif word in Non_Spam_Keywords:
            non_spam = non_spam +1

    if spam > non_spam:
        return True
        print("this was SPAM!")
        
    elif non_spam > spam:
        return False
        print("this was not a spam message")
        
    else:
        print("was unable to decipher")
        return None
        


