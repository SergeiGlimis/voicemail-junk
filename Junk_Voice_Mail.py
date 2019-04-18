import speech_recognition as sr
from difflib import SequenceMatcher

Spam_Keywords = (".org",".com","we","register","we need","dollars",
                 "help us","irs","this is","interested","donate",
                 "donation","information","insurance","social security",
                 "sweepstakes","help us","cash","money","price","won","winning"
                 ,"successful","Marketing","business","retire","income","incrute"
                 ,"online","give us","elect","trump","want","donations","don't wait call")

# i will also decipher in a later version of the call is from a known contact or not.
Non_Spam_Keywords = ("love you","i'll","see you","hey man","sup man","what's up",
                     "it's me","later","home"," i ", "honey","mom","dad","dude",
                     "bro","love","last week","i'll see you","wanted to see"
                     "shopping","supermarket","kids","thanks","we'll see you",
                     "hey dude","appointment","office","remember","bring","wait",
                     "my","me","outside","walking","driving","love you","okay",
                     "yesterday","tomorrow","can we")


DEBUGGING = True
def debug_print(text):
    # this allows you to turn off the printing of things that aren't needed undless it's by the developer 
    global DEBUGGING
    if DEBUGGING:
        print(text)



def VoiceWav(File):
    #takes an arguent which is the file 
    debug_print("Starting to decipher.") # uses the debug print
    VM_Audio_File = sr.AudioFile(str(File)) # uses the file that was an argument and makes it a file recognizable to speech recognition.
    debug_print("parsing audio into speech recognition module")
    r = sr.Recognizer() #makes the recognition function easier to call

    with VM_Audio_File as source: # uses that file we gave to speechRecognition 
        audio = r.record(source) # play the audio file under the hood and recognise the speech, this text will be put to "audio".
    debug_print("recognize audio")
    value = r.recognize_google(audio).lower()
    return value



    
def DecSpam(value):
 # names it value now and makes it lower cased to avoid inconsistancies.
    debug_print(value)
    value2 = str(value).split() # split the text from the file by word.
    debug_print("spliting ")
# this next section checks to see if more spam keywords or non-spam keywords are in it. And then 
    spam = 0
    non_spam = 0
    for word in value2: # for every word in the message do something
        if word in Spam_Keywords: # if one of those words is in the spam word list do something
            debug_print(word)
            spam = spam+1

        elif word in Non_Spam_Keywords: # if it's in the non spam list do something
            debug_print(word)
            non_spam = non_spam +1

    if spam > non_spam:
        debug_print("spam was more then not spam keywords")
        debug_print("this was SPAM!")
        return True
        
        
    elif non_spam > spam:
        debug_print("nonspam was more then spam keywords")
        debug_print("this was not a spam message")
        return False
        
        
    else:
        debug_print("was unable to decipher")
        return None
        

if __name__=="__main__":
    
    v1 = VoiceWav("test_1.wav")
    v2 = VoiceWav("test_2.wav")
    v3 = VoiceWav("test_3.wav")
    v4 = VoiceWav("test_4.wav")

    DecSpam(v1)
    DecSpam(v2)
    DecSpam(v3)
    DecSpam(v4)

    
