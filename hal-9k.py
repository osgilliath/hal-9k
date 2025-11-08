import os
import re
import wikipedia
import requests
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class Hal9k:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
        self.model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
        self.chat_history_ids = None
        self.weather_api_key = os.environ.get("WEATHER_API_KEY") # Fetch API key from environment variables

    def get_weather(self, city):
        if not self.weather_api_key:
            return "Weather API key not set. Please set the WEATHER_API_KEY environment variable."
        
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.weather_api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            return f"The weather in {city} is {weather_description} with a temperature of {temperature}°C."
        else:
            return "Sorry, I couldn't retrieve the weather information for that city."

    def search_wikipedia(self, query):
        try:
            summary = wikipedia.summary(query, sentences=2)
            return summary
        except wikipedia.exceptions.PageError:
            return f"Sorry, I couldn't find any information on '{query}'."
        except wikipedia.exceptions.DisambiguationError as e:
            return f"'{query}' is ambiguous. Please be more specific. Options: {e.options[:5]}"

    def handle_intent(self, user_input):
        if "who are you" in user_input.lower():
            return "Good afternoon, gentlemen. I am a HAL 9000 computer."

        weather_match = re.search(r"weather in (.*)", user_input.lower())
        if weather_match:
            city = weather_match.group(1)
            return self.get_weather(city)

        wiki_match = re.search(r"search wikipedia for (.*)", user_input.lower())
        if wiki_match:
            query = wiki_match.group(1)
            return self.search_wikipedia(query)

        return None

    def chat(self, user_input):
        intent_response = self.handle_intent(user_input)
        if intent_response:
            return intent_response

        new_user_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors='pt')
        bot_input_ids = torch.cat([self.chat_history_ids, new_user_input_ids], dim=-1) if self.chat_history_ids is not None else new_user_input_ids
        self.chat_history_ids = self.model.generate(bot_input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)
        response = self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response

if __name__ == "__main__":
    hal9k = Hal9k()
    print("hal-9k initialized. Type 'quit' to exit.")
    print("hal-9k: Good afternoon, gentlemen. I am a HAL 9000 computer.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = hal9k.chat(user_input)
        print(f"hal-9k: {response}")
