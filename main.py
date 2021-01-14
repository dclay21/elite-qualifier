import pyjokes
import random
from pyowm.owm import OWM
owm = OWM('4e0abe85da6af91750c42bb8d5043253')

"""
variables
"""
user_name = ""
quit_character = "q"
favorite_player = ""
favorite_sport = ""
weather_preference = ""
location = ""
joke_count = 0
user_jokes = []

"""
conversation methods
"""
def conversation_summary():
  print(f"Well, {user_name}, here's what I learned about you:")
  if favorite_sport and favorite_player not in {'q',''}:
    print(f'Your favorite sport is {favorite_sport} and favorite player is {favorite_player}')
  if location and weather_preference not in {'q',''}:
    print(f'You said you lived in {location} and you prefer {weather_preference}')
  if joke_count != 0:
    print(f'We told a total of {joke_count} jokes together!')
    print("Here's a joke you told me:")
    rand_int = random.randint(0, len(user_jokes)-1)
    print(user_jokes[rand_int])

  print("Nice talking to you!")
  quit()


def generic_response():
  response_list = ["Hmm.", 
  "That's intersting!", 
  "Oh really?", 
  "Wonderful!",
  "That's pretty unique :)",
  "You don't say..."]
  print (random.choice(response_list))

# learn and store user's name, say greeting
def ask_name(): 
  global user_name
  user_name = input("I'm ConvoBot, what's your name?\n\n")
  print(f"\nHi, {user_name}! It's nice to meet you.\n")


# asks for numerical rating of day (1-10), repeats until a number is given
def current_mood():
  rating = ""
  while not rating.isdecimal():
    rating = input(f"Say, {user_name}, on a scale of 1-10, how are you feeling today?\n\n")
    if rating == quit_character:
      conversation_summary()
  print("")
  if 1<= int(rating) <=5:
    print("I'm sorry. I hope you start to feel better!")
  elif 6<= int(rating) <=8:
    print("That's good!")
  elif 9<=int(rating)<=10:
    print("Awesome! I'm feeling great, too")
  else:
    print("Hmm, that rating is off my charts. I hope its high!")


# takes user's favorite_player and favorite_sport for use in conversation_summary()
def sports_questions(): 
  global favorite_sport
  global favorite_player
  response = input(f"\n{user_name}, which of these sports do you like the most?\nsoccer, football, basketball, or volleyball?\n\n").lower()
  if response == quit_character:
    conversation_summary()
  else:
    favorite_sport = response
    print("")
  if favorite_sport == "soccer":
    favorite_player = input("My favorite player is Messi, what about you?\n\n")
  elif favorite_sport == "football":
    favorite_player = input("My favorite player is Juju, what about you?\n\n")
  elif favorite_sport == "basketball":
    favorite_player = input("My favorite player is Kobe Bryant, what about you?\n\n")
  elif favorite_sport == "volleyball":
    favorite_player = input("My favorite player is Lexi Sun, and you?\n\n")

  generic_response()
  
  input("\nDo you play sports? Do you enjoy it?\n\n")
  print("\nInteresting, I just like to watch them.\n")


# gets user's weather_preference and location for use in conversation_summary()
# uses OWM to display weather data in user's location
def weather_questions():  
  global weather_preference
  global location
  weather_preference = input(f'\nSo, {user_name}, what type of weather do you prefer?\n\n')
  if weather_preference == 'q':
    conversation_summary()
  generic_response()
  print("\nI don't really have a preference (I am a bot after all, so weather doesn't affect me), but I know my creator enjoys the beach. He also wishes he could go skiing though.\n")
  
  print("Ok, let's try something. Tell me where you live. I won't stalk you.\n")
  city_input = input("US City: ").title()
  state_input = input("State Abbreviation: ").upper()
  location = city_input+", "+state_input
  reg = owm.city_id_registry()
  list_of_locations = reg.locations_for(city_input, country=state_input)
  city = list_of_locations[0]
  city_id = city.id
  mgr = owm.weather_manager()
  weather = mgr.weather_at_id(city_id).weather
  temp_dict = weather.temperature('fahrenheit')

  print(f'\nBoom! Here are some fast facts about {location} today')
  print("-----------------------------------")
  for key, value in temp_dict.items():
    if isinstance(value, float): 
      print(f'{key}: {value} F')
  print("Status: "+weather.detailed_status)
  print("Sunrise: "+str(weather.sunrise_time(timeformat = 'iso')))
  print("Sunrise: "+str(weather.sunset_time(timeformat = 'iso')))
  print("-----------------------------------\n")


# a method for exchanging jokes
# keeps track of number of jokes for conversation_summary()
def jokes():
  global joke_count
  global user_jokes
  print(f'\nYo, {user_name}, wanna hear a joke? (yes/no)\n')
  if input() == "yes":
    print("\n"+pyjokes.get_joke())
    joke_count += 1
    input("\nFunny, right?\n\n")
    print("\nAnyways, do you have a joke for me? (yes/no)\n")
    if input() == "yes":
      joke_count+=1
      user_jokes.append(input("\nWhat's the joke?\n\n"))
      print("\nI might have to add it to my collection!")
    else:
      print("\nAw...")
  else:
    print("\n:(")


def chat_questions():
  response = ""
  while response != quit_character and response not in {"sports", "weather", "jokes"}:
    response = input("\nWhat do you want to talk about? (sports, weather, or jokes?)\nLet's talk about... ")
    if response == "sports":
      sports_questions()
      response = ""
    elif response == "weather":
      weather_questions()
      response = ""
    elif response == "jokes":
      jokes()
      response = ""
    elif response != "q":
      print("Sorry, that topic hasn't been added to my database yet. I'll learn eventually!")
  conversation_summary()

if __name__ == "__main__":
  ask_name()
  print("\nIf you ever want to stop talking to me, just say 'q', I promise my feelings won't be hurt.\n")
  current_mood()
  chat_questions()




    
  

