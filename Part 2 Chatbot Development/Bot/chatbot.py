#import database


grettings_list = ["hi", "Hi","HI", "How are you?"]
query_list = ["hi", "Hi","HI", "How are you?"]

class Medusa:
    def __init__(self) -> None:
        pass
    
    def enquiry(self, user_text:str):
        if user_text in grettings_list:
            return "Hello, how are you?"
        elif user_text in query_list:
            
            return "sd"
        else:
            return "Sorry, I didn't understand that."