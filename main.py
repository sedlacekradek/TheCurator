from textblob import TextBlob
import requests
import random
from flask import Flask, session, render_template, request
import secrets


## CONSTANTS ###
FIND_PAINTING_API = 'https://collectionapi.metmuseum.org/public/collection/v1/search?isHighlight=true&departmentId=11&q=""'
PAINTING_INFO_API = "https://collectionapi.metmuseum.org/public/collection/v1/objects"


## EMOTION DETECTION ###
def emotion_analysis(input_text):
    """
    polarity (-1,1) the lower the number, the more negative
    subjectivity (0,1) 0 - objective, 1 - subjective
    """
    blob_text = TextBlob(input_text)
    sentiment = blob_text.sentiment
    return sentiment


## FLASK SET-UP ###
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


## API ###
response_painting = requests.get(FIND_PAINTING_API)
data_department = response_painting.json()


def is_repeated(item):
    """
    prevents users from seeing the same painting repeatedly
    """
    if len(session["recent"]) > 20:
        del session["recent"][0:6]
    if item in session["recent"]:
        return True
    else:
        session["recent"].append(item)
        return False


def load_painting():
    # get api data
    random_painting = random.choice(data_department["objectIDs"])
    response = requests.get(f"{PAINTING_INFO_API}/{random_painting}")
    data = response.json()
    if is_repeated(data["title"]):
        return load_painting()
    else:
        # painting data
        session["image_pic_big"] = data["primaryImage"]
        session["image_pic_small"] = data["primaryImageSmall"]
        session["image_title"] = data["title"]
        session["image_date"] = data["objectDate"]
        session["image_medium"] = data["medium"]
        session["image_dimensions"] = data["dimensions"]
        session["image_located"] = data["repository"]
        # artist data
        session["artist_name"] = data["artistDisplayName"]
        session["artist_link"] = data["artistULAN_URL"]
        session["artist_nationality"] = data["artistNationality"]
        session["artist_born"] = data["artistBeginDate"]
        session["artist_death"] = data["artistEndDate"]


### FLASK MAIN ###
@app.route("/", methods=["POST", "GET"])
def home():
    session["recent"] = []
    load_painting()
    return render_template(
        'index.html',
        subjectivity=0,
        polarity=0,
        picture=session["image_pic_small"],
        picture_big=session["image_pic_big"])


@app.route("/next")
def next_picture():
    load_painting()
    return render_template(
        'next_picture.html',
        subjectivity=0,
        polarity=0,
        picture=session["image_pic_small"],
        picture_big=session["image_pic_big"])


@app.route("/evaluate", methods=["POST", "GET"])
def evaluate():
    if request.method == "POST":
        review_text = request.form.get("review-text")
        sentiment = emotion_analysis(review_text)
        polarity = (list(sentiment)[0])
        polarity = round(((polarity+1)/2)*100, 2)  # convert to 0-100%, rounded
        subjectivity = round((list(sentiment)[1])*100, 2)  # convert to %, rounded
    return render_template(
        'bar_section.html',
        subjectivity=subjectivity,
        polarity=polarity)


@app.route("/reply", methods=["POST", "GET"])
def give_reply():
    if request.method == "POST":
        import chatbot
        question = request.form.get("question-text")
        bot_answer = chatbot.answer(question)
    return render_template('answer.html', answer=bot_answer)


@app.route("/retrain")
def retrain():
    import chatbot
    chatbot.retrain()
    return render_template(
        'index.html',
        subjectivity=0,
        polarity=0,
        picture=session["image_pic_small"],
        picture_big=session["image_pic_big"])


## TO TEST LOCALLY ###
# if __name__ == "__main__":
#     from waitress import serve
#     print("localhost:8080")
#     serve(app, host='0.0.0.0', port=8080)


# if __name__ == "__main__":
#     app.run(debug=True)
