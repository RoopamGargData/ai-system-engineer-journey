import logging
import json
import requests

logging.basicConfig(
    filename="api.log",
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        data = response.json()    #json parse
        #file save

        with open ("data.json","w")as f :   
            json.dump(data,f)

            logging.info("Data saved successfully")

    else:
        logging.error(f"Status code error:{response.status_code}")

except Exception as e:
    logging.error(f"Exception occured: {e}")
    
