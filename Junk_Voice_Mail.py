import speech_recognition as sr
from difflib import SequenceMatcher

Spam_Keywords = (".org",".com","we","register","we need","dollars",
                 "help us","irs","this is","interested","donate","donation")
# i will also decipher in a later version of the call is from a known contact or not.
Non_Spam_Keywords = ("love you","i'll","see you","hey man","sup man","what's up",
                     "it's me","later","home"," i ", "honey","mom","dad")

Example_Spam = ["hello this is june with infocus we are looking for people to help us fund our service"
                ,"hi there, this is bob with idso we need you to register with us to help us get trump elected"
                ,"Hi i'm hanna and im with bic we're looking for people who are interested in pens",
                "this is the IRS you have been audited Call us at",
                "Hello I'm calling with doornob inc. we are looking for people to register for our service"]

Example_Non_Spam = ["Hey man it's john, thought i'd call and see how your doing, I'll see you on monday bye",
                    "hey honey it's jim couldn't remember which icecream you wanted me to buy get back to me as soon as you can love you bye",
                    "Hey sam it's kim i'm gonna need you you to work late on friday, get back to me let me know if that works for you bye",
                    "hey dad it's me just wanted to let you know im coming out for fathers dad, get back to me as soon as you can i love you bye."]


DEBUGGING = True
def debug_print(text):
    # this allows you to turn off the printing of things that aren't needed undless it's by the developer 
    global DEBUGGING
    if DEBUGGING:
        print(text)

def Decipher_Spam(File):
    #takes an arguent which is the file 
    debug_print("Starting to decipher.") # uses the debug print
    VM_Audio_File = sr.AudioFile(str(File)) # uses the file that was an argument and makes it a file recognizable to speech recognition.
    debug_print("parsing audio into speech recognition module")
    r = sr.Recognizer() #makes the recognition function easier to call

    with VM_Audio_File as source: # uses that file we gave to speechRecognition 
        audio = r.record(source) # play the audio file under the hood and recognise the speech, this text will be put to "audio".
    debug_print("recognize audio")
    value = r.recognize_google(audio).lower() # names it value now and makes it lower cased to avoid inconsistancies.
    debug_print(value)
    value2 = str(value).split() # split the text from the file by word.
    debug_print("spliting ")
# this next section checks to see if more spam keywords or non-spam keywords are in it. And then 
    spam = 0
    non_spam = 0
    for word in value2:
        if word in Spam_Keywords:
            debug_print(word)
            spam = spam+1

        elif word in Non_Spam_Keywords:
            non_spam = non_spam +1

    if spam > non_spam:
        debug_print("spam was more then not spam keywords")
        for ran in Example_Spam:
            Matcher = SequenceMatcher(ran, value).ratio()
            debug_print("matcher number" + str(Matcher))
            if Matcher > 0.3:
                
                debug_print(Matcher)
        
                debug_print("this was SPAM!")
        
                return True
        
        
    elif non_spam > spam:
        debug_print("nonspam was more then spam keywords")
        for ran in Example_Non_Spam:
            Matcher = SequenceMatcher(ran, value).ratio()
            debug_print("matcher number"+str(Matcher))
            if Matcher > 0.3:
                
                debug_print(Matcher)
                debug_print("this was not a spam message")
                return False
        
        
    else:
        debug_print("was unable to decipher")
        return None
        

print(Decipher_Spam('test_leo.wav')) # print the output either True or False.
