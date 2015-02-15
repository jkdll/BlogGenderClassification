__author__ = 'JB'

from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
    ("amor", "spanish"),
    ("perro", "spanish"),
    ("playa", "spanish"),
    ("sal", "spanish"),
    ("oceano", "spanish"),
    ("love", "english"),
    ("dog", "english"),
    ("beach", "english"),
    ("salt", "english"),
    ("ocean", "english")
]
test = [
    ("ropa", "spanish"),
    ("comprar", "spanish"),
    ("camisa", "spanish"),
    ("agua", "spanish"),
    ("telefono", "spanish"),
    ("clothes", "english"),
    ("buy", "english"),
    ("shirt", "english"),
    ("water", "english"),
    ("telephone", "english")
]

def extractor(word):
    feats = {}
    last_letter = word[-1]
    print(last_letter)
    feats["last_letter({0})".format(last_letter)] = True
    return feats

def sentiment(self):
        arr = TextBlob(self.text).sentiment
        sentiment = {'polarity' : arr.polarity, 'subjectivity' : arr.subjectivity}
        return sentiment

print(extractor("python"))  # {'last_letter(n)': True}

text = 'I love burgers :D'
sentiment = TextBlob(text).sentiment
print(sentiment)

lang_detector = NaiveBayesClassifier(train, feature_extractor=extractor)

print(lang_detector.accuracy(test))
print(lang_detector.show_informative_features(5))
