
## Overview

This program can be used to decipher if wav files or text are spam voicemails or are not spam voicemails.
You must download a dependency and make sure the files you are running it on will work.

## Setup and Dependencies

First you need to make sure the wav files aren’t corrupted or broken, if they are the program wil throw
an error, also make sure they are in the same folder as the program. There is only one dependency, this
is a modlue called simply Speech Recognition so you must install Speech Recognition to get the recognition
module.

    Pip3 install SpeechRecognition 

## Usage Details

when the program is run you can use the function DecSpam() for classifying one string. To get the string
of the wav use VoiceWav() to get the text. You can use DecMult() to decipher multiple strings at once
separated by a *.

If you want to use it for voicemails in wav format you must first use VoiceWav() with
the file you wish to get the text transcript for, as an argument in string form. Make sure to have
the .wav at the end. You can return this to a varible and then you can use DecSpam() with that varible
as the argument. This will return TRUE of FALSE, TRUE means it is spam, FALSE means it is not a spam
message. if you wish to get more info on either why or how it is working you can turn on DEBUGGING by
changing DEBUGGING from FALSE to TRUE.

    DEBUGGING = FALSE

/ 

    DEBUGGING = TRUE

This will print everything it is doing and all the things that
make the program classify the message in the way that it does. 
