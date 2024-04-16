import speech_recognition as sr

def recognize_speech(timeout=1.5):  
    """
    This function uses the speech_recognition library to recognize speech input from the user
    with a specified timeout for silence detection.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=timeout)
            natural_command = recognizer.recognize_google(audio)
            print("You said: " + natural_command)
            return natural_command
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return None
        except sr.UnknownValueError:
            print("Sorry, I could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None
