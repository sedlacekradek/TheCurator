import main
import importlib


def give_intents():
    importlib.reload(main)
    intents = {
        "intents": [

            {
                "tag": "greeting",
                "patterns": [
                    "Hi",
                    "How are you",
                    "Is anyone there?",
                    "Hello",
                    "Good day",
                    "Whats up"
                ],
                "responses": [
                    "Hello, welcome to our gallery.",
                    "Good to see you again!",
                    "Hi there, how can I help?"
                ]
            },

            {
                "tag": "goodbye",
                "patterns": [
                    "cya",
                    "See you later",
                    "Goodbye",
                    "I am leaving",
                    "Have a good day",
                    "Bye",
                    "Farewell"
                ],
                "responses": [
                    "Please visit us again, have a great day.",
                    "Thank you for your visit.",
                    "Goodbye!"
                ]
            },

            {
                "tag": "title",
                "patterns": [
                    "What is the name of the painting?",
                    "What is it called?",
                    "What am I looking at?",
                    "What is the title of the painting?",
                    "Whats the name.",
                    "What is the title?",
                    "Is it a famous painting?"
                ],
                "responses": [
                    f"This painting is called {main.session['image_title']}.",
                    f"The title of the painting is {main.session['image_title']}.",
                    f"The name of this painting is {main.session['image_title']}."
                ]
            },

            {
                "tag": "date",
                "patterns": [
                    "how old is the painting",
                    "when was it painted?",
                    "in what year was it made?",
                    "age?",
                    "when did the painter make this?",
                    "when was it made?",
                    "from what century is the painting?",
                    "is it old?"
                ],
                "responses": [
                    f"The painting was made in {main.session['image_date']}.",
                    f"This piece of art was made back in {main.session['image_date']}."
                ]
            },

            {
                "tag": "medium",
                "patterns": [
                    "the medium of this picture?",
                    "painted on?",
                    "what type of painting is this?",
                    "canvas painting?",
                    "material was used?",
                    "on what material is it painted?"
                    "how was this painted?"
                    "how did he make it?"
                ],
                "responses": [
                    f"This beautiful painting is actually {main.session['image_medium']}.",
                    f"The artist decided to go for {main.session['image_medium']}.",
                    f"The master used {main.session['image_medium']}."
                ]
            },

            {
                "tag": "dimensions",
                "patterns": [
                    "size?",
                    "dimensions?",
                    "how big is the painting?",
                    "is it big or small?",
                    "whats the size of this?",
                    "how big?"
                    "what is the size?"
                    "what are the dimensions?"
                ],
                "responses": [
                    f"The exact dimensions of this painting are {main.session['image_dimensions']}",
                    f"Glad you asked, the dimensions of this beautiful piece are {main.session['image_dimensions']}"
                ]
            },

            {
                "tag": "repository",
                "patterns": [
                    "painting stored?",
                    "where it located?",
                    "in what museum can I see this?",
                    "Is it in Europe or in America?",
                    "where can I find this painting?"
                ],
                "responses": [
                    f"Good questions, this painting is currently located in {main.session['image_located']}.",
                    f"If you would like to see the painting, please visit {main.session['image_located']}."
                ]
            },

            {
                "tag": "artist",
                "patterns": [
                    "Who painted this?",
                    "Who made this?",
                    "Who crated this painting?",
                    "Do we know the author?",
                    "whats the name of the painter?",
                    "what is the name of the artist?",
                    "Who is credited with this?"
                ],
                "responses": [
                    f"This masterpiece was created by {main.session['artist_name']}.",
                    f"This is one of the finest works of {main.session['artist_name']}."
                ]
            },

            {
                "tag": "artist_info",
                "patterns": [
                    "tell me more about the artist.",
                    "When was the author born?",
                    "Where did the painter live?",
                    "other works did the artist create?",
                    "famous artist?",
                    "more about this painter?",
                    "more info.",
                    "find more info?"
                    "where can I find more info?",
                    "Is there more info?",
                    "I want more info.",
                ],
                "responses": [
                    f"Please follow this link to learn more about the artist {main.session['artist_link']}.",
                    f"If you would like to learn more, please visit {main.session['artist_link']}."
                ]
            },

            {
                "tag": "artist_nationality",
                "patterns": [
                    "nationality was the artist?",
                    "the artist from?",
                    "where painter live?",
                    "what country did the painter live?",
                    "From what country or state is this from?",
                    "Is this European art?"
                    "Where was he from?",
                    "where is it from?",
                    "from what country is this from?",
                    "from what country is the painting from?"
                ],
                "responses": [
                    f"The master behind this beautiful painting was  {main.session['artist_nationality']}.",
                    f"The painter was {main.session['artist_nationality']}, who would have guessed."
                ]
            },

            {
                "tag": "artist_born",
                "patterns": [
                    "When was the artist born?",
                    "From what period is this painting?",
                    "How old was the author when he made this?",
                    "In what year was the painter born?",
                    "When was he born?"
                ],
                "responses": [
                    f"Excellent question, the painter was born in {main.session['artist_born']}.",
                    f"I hope you will find it interesting that the painter was born in {main.session['artist_born']}."
                ]
            },

            {
                "tag": "artist_death",
                "patterns": [
                    "artist die?",
                    "In what year did the painter die?",
                    "long did the artist live?",
                    "How did the painter die?",
                ],
                "responses": [
                    f"The painter died in {main.session['artist_death']}.",
                    f"The artist left us in {main.session['artist_death']}."
                ]
            },
        ]
    }

    return intents
