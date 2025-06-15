import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibarary
import requests
import re

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "1efd926d0f2a42cbb271913fa1ad9267"
# https://newsapi.org/v2/top-headlines?country=us&apiKey=1efd926d0f2a42cbb271913fa1ad9267
# api = 1efd926d0f2a42cbb271913fa1ad9267

# New api = pub_1835352e5d134b16be82120135f4bd6a

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")  
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open stack overflow" in c.lower():
        speak("Opening Stack Overflow")
        webbrowser.open("https://stackoverflow.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open instagram" in c.lower():
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif "open github" in c.lower():
        speak("Opening GitHub")
        webbrowser.open("https://github.com")
    elif "open snapchat" in c.lower():
        speak("Opening Snapchat")
        webbrowser.open("https://www.snapchat.com")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles',[])
            if not articles:
                speak("Sorry, I couldn't find any news articles.")
            else:
                for i, article in enumerate(articles[:5]):  # Limit to 5 headlines
                    title = article.get('title', 'No title')
                    print(f"News {i+1}: {title}")
                    speak(f"News {i+1}: {title}")
        elif r.status_code == 401:
             speak("Sorry, I couldn't fetch the news right now.")

#  Weather section
    elif "weather" in c.lower():
        # Extract city name from the command
        match = re.search(r"weather in ([a-zA-Z ]+)", c.lower())
        if match:
            city = match.group(1).strip()
            api_key = "13f2758c7de51fc00a34e006cb57db12"  # Replace with your OpenWeatherMap API key
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                weather_report = f"The weather in {city.title()} is {desc} with a temperature of {temp} degrees Celsius."
                print(weather_report)
                speak(weather_report)
            else:
                speak(f"Sorry, I couldn't find the weather for {city}.")
        else:
            speak("Please specify the city, for example: 'weather in Mumbai'.")
  #wheather section end

 

                
  # Enddd->     
    else:
        # Improved: Answer questions using Google Search via SerpAPI with better extraction and debug info
        import requests
        import urllib.parse
        import json
        serpapi_key = "YOUR_SERPAPI_KEY"  # Replace with your SerpAPI key
        query = urllib.parse.quote(c)
        url = f"https://serpapi.com/search.json?q={query}&api_key={serpapi_key}&engine=google"
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                data = resp.json()
                print("[DEBUG] SerpAPI response:\n", json.dumps(data, indent=2))  # Print full response for debugging
                answer = None
                # Try to get a direct answer box, knowledge graph, or snippet
                if 'answer_box' in data:
                    ab = data['answer_box']
                    answer = ab.get('answer') or ab.get('snippet') or ab.get('highlighted_words')
                    if isinstance(answer, list):
                        answer = ', '.join(answer)
                if not answer and 'knowledge_graph' in data:
                    kg = data['knowledge_graph']
                    answer = kg.get('description') or kg.get('title')
                if not answer and 'organic_results' in data and len(data['organic_results']) > 0:
                    answer = data['organic_results'][0].get('snippet')
                if not answer and 'related_questions' in data and len(data['related_questions']) > 0:
                    answer = data['related_questions'][0].get('snippet')
                if answer:
                    print(f"Jarvis: {answer}")
                    speak(str(answer))
                else:
                    speak("Sorry, I couldn't find a direct answer to that on Google.")
            else:
                speak("Sorry, I couldn't fetch information from Google.")
        except Exception as e:
            print(f"Google search error: {e}")
            speak("Sorry, I couldn't process your request.")

if __name__ == "__main__":
    speak("Intializing Jarvis...... ")

    while True:
        r = sr.Recognizer()
        print("Recoganizing....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=4)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yupp, I am here")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

            
        except Exception as e:
            print("error; {0}".format(e))