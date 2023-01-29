# Speech to Text Conversion using Google API
This script uses the speech_recognition library to convert audio files to text using the Google Speech Recognition API. The script takes an audio file and a language as input and outputs the transcribed text to the console and to a text file.

### Requirements
- Python 3.x
- speech_recognition library (install using pip install speech_recognition) 

```sh
python script.py audio_file.wav -l fr-FR
```
Where **audio_file.wav** is the name of the audio file to process and **fr-FR** is the language of the audio (can be **fr-FR**, **en-US**, or **ar-AE**). The default language is French if the -l option is not specified.

The transcribed text will be displayed on the console and saved in a text file named **result.txt**.

### Note
The Google Speech Recognition API is not free and may have usage limits. Please refer to the Google Cloud Platform pricing page for more information.

