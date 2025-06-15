import pyttsx3

if __name__ == "__main__":
    print('Welcome to the Robo speech synthesizer! Created by "Jaydeep"')
    while True:
        x = input("Enter what you want to be pronounced: ")
        if x=="exit":
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()