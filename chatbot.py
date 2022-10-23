import numpy as np
import tflearn
import random
import intents
from tensorflow.python.framework import ops
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
import nltk
nltk.download('punkt')

### DATA TO LISTS ###
data = intents.give_intents()
all_words = []
all_tags = []
pattern_words = []
pattern_labels = []


for intent in data['intents']:
    for pattern in intent['patterns']:
        words = nltk.word_tokenize(pattern)  # each word as a separate unit: "What up mate?" -> [what, up, mate, ?]
        all_words.extend(words)  # extend -> add words directly, does not create a list inside a list
        pattern_words.append(words)  # append -> creates a list of lists
        pattern_labels.append(intent["tag"])

    if intent['tag'] not in all_tags:
        all_tags.append(intent['tag'])

all_words = [stemmer.stem(w.lower()) for w in all_words if w != "?"]  # stemmer finds stems of words: whats -> what, happening -> happen
all_words = sorted(list(set(all_words)))  # 1) set - removes duplicates and converts to set datatype, 2) list - converts back to list datatype 3) sorted - sort words
all_tags = sorted(all_tags)


### BAG OF WORDS (BOW) ###
# BOW -> compare words in pattern with all_words and create BOW with len of all_words -> output eg: [0,1,1,1,0,0,1,0]
# order of words in sentence is lost
training = []
output = []
# list of 0s representing each tag, 0s will be replaced by 1 for tag that matches our BOW (-> marks the correct answer)
out_empty = [0 for _ in range(len(all_tags))]

# create bag of words for each pattern
for index, words_in_pattern in enumerate(pattern_words):
    bag = []
    words = [stemmer.stem(w) for w in words_in_pattern]
    # check against all_words and add 1 or 0 accordingly
    for w in all_words:
        if w in words:
            bag.append(1)
        else:
            bag.append(0)

    output_row = out_empty[:]  # creates hard copy of list

    # marks correct answer for the model
    #e.g. [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] -> correct is tag with index 8
    output_row[all_tags.index(pattern_labels[index])] = 1

    training.append(bag)  # bag of words for given pattern
    output.append(output_row)  # correct answer for given pattern

# convert to np.array
training = np.array(training)
output = np.array(output)


### MODEL SETUP ###
net = tflearn.input_data(shape=[None, len(training[0])])  # placeholder for input; always None + array shape (-> in this case - number of words )
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")  # len(output[0]) -> number of possible results
net = tflearn.regression(net)  # regression layer with default parameters

model = tflearn.DNN(net)  # deep neural network model init
model.load("models/model01.tflearn")


def retrain():
    # todo: should unload model before training
    ops.reset_default_graph()
    model.fit(training, output, n_epoch=175, batch_size=24, show_metric=True)
    model.save("models/model01.tflearn")


### DATA FOR PREDICTION ###
def bag_of_words(input_string, all_words):
    """
    creates new bag of words for user input
    """
    new_bag = [0 for _ in range(len(all_words))]

    input_words = nltk.word_tokenize(input_string)
    input_words = [stemmer.stem(word.lower()) for word in input_words]

    for w in input_words:
        for w_index, word in enumerate(all_words):
            if word == w:
                new_bag[w_index] = 1

    return np.array(new_bag)


## GIVE ANSWER ###
def answer(user_input):
    user_input = user_input
    results = model.predict([bag_of_words(user_input, all_words)])[0]
    results_index = np.argmax(results)  # select the most probable option
    # print(results[results_index])
    tag = all_tags[results_index]

    # if bot over 30% sure
    if results[results_index] > 0.3:
        data = intents.give_intents()
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        return random.choice(responses)  # pick random answer for given tag
    # if not sure
    else:
        return "I am not sure if I understand. Could you please rephrase?"