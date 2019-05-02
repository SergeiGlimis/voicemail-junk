
## Overview

This program can be used to decipher if wav files or text are spam voicemails or are not spam voicemails.
You must download a dependency and make sure the files you are running it on will work.

## Setup and Dependencies

First you need to make sure the wav files aren’t corrupted or broken. If they are the program wil throw
an error, also make sure they are in the same folder as the program. There is only one dependency, this
is a module simply called Speech Recognition, so you must install Speech Recognition to get the recognition
features to work. The program must be connected to the internet to function without any errors.

    Pip3 install SpeechRecognition 

## Usage

from the program you can use the function DecSpam() for classifying one string. To get the string
of a wav file use VoiceWav() to get the text. You can use DecMult() to decipher multiple strings at once
separated by a *.

## Usage Details

If you want to use it for voicemails in .wav format you must first use VoiceWav() with
the file you wish to get the text transcript for, as an argument in string form. Make sure to have
the .wav at the end. You can return this to a varible and then you can use DecSpam() with that varible
as the argument. This will return TRUE, FALSE or NONE. TRUE means it is spam, FALSE means it is not a spam
message and NONE means it was unable to decipher it. if you wish to get more info on either why or how it
is working you can turn on DEBUGGING by changing DEBUGGING from FALSE to TRUE.

    DEBUGGING = FALSE

/ 

    DEBUGGING = TRUE

This will print everything it is doing and all the things that make the program classify the message in the
way that it does. If you wish to use this on multiple Strings use the DecMult() with the voicemails in text form in 
a string. between each voicemail in the strong put a * symbol. this tells the program that you wish to decipher each
one seperately. This will return a list of booleans in order. the first in the string will be the first and so on.

    example:
        [True,False,True,True,None,True]

## Trouble Shooting

first of all if something is giving you trouble dont shoot it!!
there are a few reasons the program may throw an error or not work as intended.

 OFFINE: if there is no internet access then the Speech recognition module can't reach it's server and function,
 this will throw an error.

 NONE: This progrma is not perfect yet so it sometimes will not be able to decipher some voicemails. If this is
 the case the program will return NONE.

 RECOGNIZE: if you decide to change the recognition engine from google to something else it may not be acurate and
 may give an error if that service requires an API key or ID.
 
