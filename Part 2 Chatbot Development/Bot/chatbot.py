import database
import random

grettings_list = ["hi", "Hi","HI", "Hello"]

query_list = ["From which country do we have the most customers?",
              "Most customers country wise?",
                "richest people"  

            ]


grettings_answer_random = ["I am good, How are you?", "I am fine, How can I help you?","Can't complain !"]

class Medusa:
    def __init__(self) -> None:
        pass
    
    def enquiry(self, user_text:str):
        if user_text == "How are you?":
            return random.choice(grettings_answer_random)
        
        elif user_text in grettings_list:
            return " Hey there! How are yout today? "

        elif user_text in query_list:
            text = database.get_most_order_countrywise()            
            return f'We have the most customers from {text}. 🔝' 
        else:
            return "Sorry, I didn't understand that."