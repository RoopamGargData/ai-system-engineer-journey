#from utils import greet
from utils import clean_text,save_json_result,log_message

log_message("Program Started")

user_text = input("Enter Text:-   ")  # user se runtime input lena

log_message(f"User entered:{user_text}")

cleaned = clean_text(user_text)  # input process karna

if cleaned:
    save_json_result(cleaned)
    log_message(f"Saved cleaned text: {cleaned}")
    print("Saved JSON : ",cleaned)

else:
    log_message("Invalid input")
    print("Invalid input")
