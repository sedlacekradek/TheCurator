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
                    "What is up"
                ],
                "responses": [
                    "Hello, welcome to our gallery.",
                    "Good to see you again!",
                    "Welcome art lover, how can I help?"
                ]
            },

            {
                "tag": "goodbye",
                "patterns": [
                    "Cya",
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
                    "What is the name of this painting?",
                    "What is the name of the picture?",
                    "What is the name of this picture?",
                    "What is the name of this piece?",
                    "What is the name of the piece?",
                    "What is it called?",
                    "What is this called?",
                    "What is the piece called?",
                    "What is this piece called?",
                    "What is the painting called?",
                    "What is this painting called?",
                    "What am I looking at?",
                    "What is the title of the painting?",
                    "What is the title of this painting?",
                    "What is the title of the piece?",
                    "What is the title of this piece?",
                    "What is the title of the art?",
                    "What is the title of this art?",
                    "What is the title?",
                    "What is the name?",
                    "Is it a famous painting?",
                    "Is this a famous painting?",
                    "How is it called?"
                    "How is this called?"
                    "How is the painting called?"
                    "How is this painting called?"
                    "How is this piece called?"
                    "How is the piece called?"
                ],
                "responses": [
                    f"Glad you asked, this painting is called {main.session['image_title']}.",
                    f"The title of the painting is {main.session['image_title']}.",
                    f"The name of this painting is {main.session['image_title']}."
                ]
            },

            {
                "tag": "date",
                "patterns": [
                    "how old is the painting",
                    "how old is this painting",
                    "how old is the piece?",
                    "how old is this piece?",
                    "how old is this?",
                    "how old is it?",
                    "when was it painted?",
                    "when was this painted?",
                    "when was the painting painted?",
                    "when was this painting painted?",
                    "when was this piece painted?",
                    "when was it created?",
                    "when was this created?",
                    "when was the painting created?",
                    "when was this painting created?",
                    "when was the piece created?",
                    "when was this piece created?",
                    "when was it made?",
                    "when was this made?",
                    "when was the painting made?",
                    "when was this painting made?",
                    "when was the piece made?",
                    "when was this piece made?",
                    "in what year was it made?",
                    "in what year was this made?",
                    "in what year was this piece made?",
                    "in what year was the piece made?",
                    "in what year was the painting made?",
                    "in what year was this painting made?",
                    "age?",
                    "when did the painter make this?",
                    "when did the painter make it?",
                    "from what century is the painting?",
                    "from what century is this painting?",
                    "from what century is the piece?",
                    "from what century is this piece?",
                    "from what century is this?",
                    "from what century is it?",
                    "is it old?"
                    "from what period is it?"
                    "from what period is this?"
                    "from what year is it?"
                    "from what year is this?"
                ],
                "responses": [
                    f"The painting was made in {main.session['image_date']}.",
                    f"This piece of art was made back in {main.session['image_date']}."
                ]
            },

            {
                "tag": "medium",
                "patterns": [
                    "what is the medium of this painting?",
                    "what is the medium of the painting?",
                    "what is the medium of this piece?",
                    "what is the medium of the piece?",
                    "what is the medium of this art?",
                    "what is the medium of the art?",
                    "painted on?",
                    "what type of painting is this?",
                    "what type of painting is iz?",
                    "what type of art is this?",
                    "what type of art is it?",
                    "is it a canvas painting?",
                    "is this a canvas painting?",
                    "what material was used?",
                    "on what material is it painted?"
                    "on what material is this painted?"
                    "how was this painted?"
                    "how was it painted?"
                    "how did he make it?"
                    "how did he make this?"
                    "what technique was used?"
                    "what technique did the painter use?"
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
                    "how big is this painting?",
                    "how big is this piece?",
                    "how big is the piece?",
                    "how big is this?",
                    "how big is it?",
                    "is it big or small?",
                    "what is the size of this?",
                    "what is the size of this painting?",
                    "what is the size of the painting?",
                    "what is the size of this piece?",
                    "what is the size of the piece?",
                    "how big is it?"
                    "how big is this?"
                    "how big is the painting?"
                    "how big is this painting?"
                    "how big is this?"
                    "how big is this piece?"
                    "what is the size?"
                    "what are the dimensions?"
                    "what are the dimensions of this painting?"
                    "what are the dimensions of the painting?"
                    "what are the dimensions of this piece?"
                    "what are the dimensions of the piece?"
                    "what are the dimensions of this?"
                    "what are the dimensions of it?"
                ],
                "responses": [
                    f"The exact dimensions of this painting are {main.session['image_dimensions']}",
                    f"The dimensions of this beautiful piece are {main.session['image_dimensions']}"
                ]
            },

            {
                "tag": "repository",
                "patterns": [
                    "where is the painting stored?",
                    "where is this painting stored?",
                    "where is this piece stored?",
                    "where is the piece stored?",
                    "where is it located?",
                    "where is this located?",
                    "in what museum can I see this?",
                    "in what museum can I see it?",
                    "Is it in Europe or in America?",
                    "where can I find this painting?"
                    "where can I find the painting?"
                    "I would like to see the painting."
                    "I would like to see this painting."
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
                    "Who painted it?",
                    "Who painted this painting?",
                    "Who painted the painting?",
                    "Who painted this picture?",
                    "Who painted the picture?",
                    "Who painted this piece?",
                    "Who painted the piece?",
                    "Who made this?",
                    "Who made it?",
                    "Who made this painting?",
                    "Who made the painting?",
                    "Who made this picture?",
                    "Who made the picture?",
                    "Who made this piece?",
                    "Who made the piece?",
                    "Who crated this painting?",
                    "Who crated the painting?",
                    "Who crated this?",
                    "Who crated it?",
                    "Who crated this piece?",
                    "Who crated the piece?",
                    "Do we know the author?",
                    "Do we know the painter?",
                    "Do we know the artist?",
                    "name of the painter?",
                    "name of this painter?",
                    "name of the artist?",
                    "name of this artist?",
                    "Who is credited with this?"
                    "Who is credited with it?"
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
                    "tell me more about this artist.",
                    "tell me more about the author.",
                    "tell me more about this author.",
                    "tell me more about the painter.",
                    "tell me more about this painter.",
                    "tell me more about him.",
                    "When was the author born?",
                    "When was this author born?",
                    "When was he born?",
                    "When was the painter born?",
                    "When was this painter born?",
                    "When was the artist born?",
                    "When was this artist born?",
                    "Where did the painter live?",
                    "Where did this painter live?",
                    "Where did the author live?",
                    "Where did this author live?",
                    "Where did the artist live?",
                    "Where did this artist live?",
                    "Where did he live?",
                    "what other works did the artist create?",
                    "what other works did this artist create?",
                    "what other works did the author create?",
                    "what other works did this author create?",
                    "what other works did the painter create?",
                    "what other works did this painter create?",
                    "what other works did he create?",
                    "other works of his?",
                    "famous artist?",
                    "famous author?",
                    "famous painter?",
                    "more about this painter?",
                    "more about this author?",
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
                    "what nationality was the artist?",
                    "what nationality was this artist?",
                    "what nationality was the painter?",
                    "what nationality was this painter?",
                    "what nationality was the author?",
                    "what nationality was this author?",
                    "what nationality was he?",
                    "where was the artist from?",
                    "where was this artist from?",
                    "where was he from?",
                    "where the painter from?",
                    "where this painter from?",
                    "where the author from?",
                    "where this author from?",
                    "where did the painter live?",
                    "where did this painter live?",
                    "where did the artist live?",
                    "where did this artist live?",
                    "where did he live?",
                    "where did the author live?",
                    "where did this author live?",
                    "in what country did the painter live?",
                    "in what country did this painter live?",
                    "in what country did the author live?",
                    "in what country did this author live?",
                    "in what country did the painter live?",
                    "in what country did this painter live?",
                    "in what country did he live?",
                    "From what country or state is this from?",
                    "From what country or state is it from?",
                    "Is this European art?"
                    "where is it from?",
                    "where is this from?",
                    "where is the painting from?",
                    "where is this painting from?",
                    "where is this piece from?",
                    "where is the piece from?",
                    "from what country is this from?",
                    "from what country is it from?",
                    "from what country is the painting from?"
                    "from what country is this painting from?"
                    "from what country is the piece from?"
                    "from what country is this piece from?"
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
                    "When was this artist born?",
                    "When was the author born?",
                    "When was this author born?",
                    "When was he born?",
                    "When was the painter born?",
                    "When was this painter born?",
                    "From what period is this painting?",
                    "From what period is the painting?",
                    "How old was the author when he made this?",
                    "How old was this author when he made this?",
                    "How old was he when he made this?",
                    "How old was the painter he made this?",
                    "How old was this painter he made this?",
                    "How old was the artist he made this?",
                    "How old was this artist he made this?",
                    "In what year was the painter born?",
                    "In what year was this painter born?",
                    "In what year was the author born?",
                    "In what year was this author born?",
                    "In what year was he born?",
                    "In what year was the artist born?",
                    "In what year was this artist born?",
                ],
                "responses": [
                    f"Excellent question, the painter was born in {main.session['artist_born']}.",
                    f"I hope you will find it interesting that the painter was born in {main.session['artist_born']}."
                ]
            },

            {
                "tag": "artist_death",
                "patterns": [
                    "In what year did the painter die?",
                    "In what year did this painter die?",
                    "In what year did the artist die?",
                    "In what year did this artist die?",
                    "In what year did the author die?",
                    "In what year did this author die?",
                    "In what year did he die?",
                    "long did the artist live?",
                    "long did this artist live?",
                    "long did the painter live?",
                    "long did this painter live?",
                    "long did he live?",
                    "long did the author live?",
                    "long did this author live?",
                    "How did the painter die?",
                    "How did this painter die?",
                    "How did the artist die?",
                    "How did this artist die?",
                    "How did the author die?",
                    "How did this author die?",
                    "How did he die?",
                ],
                "responses": [
                    f"The painter died in {main.session['artist_death']}.",
                    f"The artist left us in {main.session['artist_death']}."
                ]
            },
        ]
    }

    return intents
