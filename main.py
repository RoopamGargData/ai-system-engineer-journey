#from utils import greet
from utils import clean_text,save_json_result
user_text = input("Enter Text:-   ")  # user se runtime input lena

cleaned = clean_text(user_text)  # input process karna

if cleaned:
    save_json_result(cleaned)
    print("Saved JSON : ",cleaned)

else:
    print("Invalid input")
