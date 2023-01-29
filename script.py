import speech_recognition as sr
import argparse

def speech_to_text(filename, language):
    # initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the speech and store in audio_text
    with sr.AudioFile(filename) as source:
        audio_text = r.record(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        result = r.recognize_google(audio_text, language=language)
        print("Text: " + result)

        # Save the result to a text file
        with open("result.txt", "w") as f:
            f.write(result)

    except:
        print("Sorry, I did not get that")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="The name of the audio file to process")
    parser.add_argument("-l", "--language", type=str, default="fr-FR", help="The language of the audio file (fr-FR, en-US, or ar-AE)")
    args = parser.parse_args()
    speech_to_text(args.filename, args.language)
