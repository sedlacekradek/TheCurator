from textblob import TextBlob
import requests
import random
from flask import Flask, session, render_template
import secrets
from flask_session import Session

## CONSTANTS ###
FIND_PAINTING_API = 'https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&departmentId=11&q=""'
PAINTING_INFO_API = "https://collectionapi.metmuseum.org/public/collection/v1/objects"


## FLASK SET-UP ###
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
recent_list = []


### FLASK MAIN ###
@app.route("/")
def home():
    return render_template("index.html")


# ## EMOTION DETECTION ###
# def emotion_analysis(input_text):
#     """
#     polarity (-1,1) the lower the number, the more negative
#     subjectivity (0,1) 0 - objective, 1 - subjective
#     """
#     blob_text = TextBlob(input_text)
#     sentiment = blob_text.sentiment
#     return sentiment
#
#
## HELPER FUNCTIONS ###
# def is_repeated(item, recent):
#     if len(recent) > 20:
#         del recent[:5]
#     if item in recent:
#         return True
#     else:
#         recent.append(item)
#         return False
#
#
# ## API DATA ###
# def find_painting():
#     # get random painting
#     response_painting = requests.get(FIND_PAINTING_API)
#     data_department = response_painting.json()
#     painting = random.choice(data_department["objectIDs"])
#     if is_repeated(painting, recent_list):
#         return find_painting()
#     else:
#         return painting
#
#
# # get api data
# random_painting = find_painting()
# response = requests.get(f"{PAINTING_INFO_API}/{random_painting}")
# data = response.json()
# # painting data
# image_pic_big = data["primaryImage"]
# image_pic_small = data["primaryImageSmall"]
# image_title = data["title"]
# image_date = data["objectDate"]
# image_medium = data["medium"]
# image_dimensions = data["dimensions"]
# image_located = data["repository"]
# # artist data
# artist_name = data["artistDisplayName"]
# artist_link = data["artistULAN_URL"]
# artist_nationality = data["artistNationality"]
# artist_born = data["artistBeginDate"]
# artist_death = data["artistEndDate"]


### CHATBOT ###
#chatbot.py






## TO TEST LOCALLY ###
# if __name__ == "__main__":
#     from waitress import serve
#     print("localhost:8080")
#     serve(app, host='0.0.0.0', port=8080)


if __name__ == "__main__":
    app.run(debug=True)
