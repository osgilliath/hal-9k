## hal-9k
A simple chatbot in the terminal, a close and (not so) evil version of hal 9000, from 2001: a space odyssey. This bot can engage in conversations, retrieve weather information, and search Wikipedia.

_"The 9000 series is the most reliable computer ever made."_
---

**cool stuff**
_ask him:_ who are you

## features
- **Conversations**: It can have text-based conversations, with you, and has context-awareness.
- **Weather**: It can tell you the weather of a particular city
- **Wikipedia Search**: You can fetch data from Wikipedia.
- **HAL 9000**: He is a HAL 9000 computer, what else is required.

## tech-stack
The program uses:
1. **OpenWeatherMap API**: for retrieving weather data.
2. **Wikipedia API**: for searching wikipedia articles.
3. **Hugging Face**: uses hugging face model hub for the language model.

**Based on**: the bot is based on the `microsoft/DialoGPT-medium` model, and the personality is inspired from HAL 9000, although not that evil (if you consider hal evil).

## instructions
to run this chat bot:

- make a virtual environment: (optional but reccomended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

- install required python modules by running:<br/>
```bash
pip install wikipedia requests torch transformers
```

- run the bot using:<br/>
```bash
python hal-9k.py
```
---

**for the weather feature:**

- get an api key from [OpenWeatherMap](https://home.openweathermap.org/)
- add the api key in the environment variables of your system, in a variable named 'WEATHER_API_KEY'.
- restart your terminal or IDE.
- ask the bot ```weather in [city_name]```

eg: weather in London

---

**how to add environment variables**
- press `Windows` + `R`
- type `sysdm.cpl` and press enter.
- go to "advanced", and then to "environment variables"
- now click on "New..." on either user or system variables, depending on your choice.
- put "WEATHER_API_KEY" in the variable name.
- put [your_api_key] in variable value.
- press OK in all the open tabs.

---

**for wikipedia search:**

- ask the bot ```search wikipedia for [query]```

eg: search wikipedia for Stanley Kubrick

---

>"Daisy, Daisy, give me your answer do. I'm half crazy all for the love of you." -HAL 9000
