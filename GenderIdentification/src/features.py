from textblob import TextBlob
from collections import defaultdict
from turtledemo.chaos import line
import re

class FeatureVector:

    

    def __init__(self, text):
        self.text = text
        
    #Weighted average of the prepositions in the text
    def prepositionAv(self):
        i = 0
        tagList = TextBlob(self.text).tags
        for tag in tagList:
            if tag[1] == 'IN':
                i += 1 
        return i/len(tagList)
    
    #Weighted average of the pronouns in the text
    def pronounsAv(self):
        i = 0
        tagList = TextBlob(self.text).tags
        for tag in tagList:
            if tag[1] == 'PRP':
                i += 1 
        return i/len(tagList) 
    
    #Weighted average of the hyperlinks in the text
    def hyperlinksAv(self):
        i = 0
        listOfWords = self.text.split()
        for word in listOfWords:
            if word == 'urlLink':
                i += 1
        return i/len(listOfWords)
    
    #Weighted average of the articles in the text
    def articlesAv(self):
        i = 0
        listOfWords = self.text.split()
        for word in listOfWords:
            if word in {"a", "an", "the"}:
                i += 1
        return i/len(listOfWords)
    
    #return number of so-called "blog words" in text
    def blogWords(self):
        filename = 'blogwords.txt'
        i = 0
        textblob = TextBlob(self.text)
        blogWords_file = open(filename, 'r')
        #line represents a blog word
        for line in blogWords_file:
            #Remove new line escape sequence
            line = re.sub(r'[^a-zA-z0-9\'\"-/]', ' ', line)
            #array of words in line
            lineArray = [x.lower() for x in line.split()]
            #entry represents an n-gram instance of the input text
            for entry in textblob.ngrams(n = len(lineArray)):
                entry = [x.lower() for x in entry]
                if lineArray == entry:
                    i += 1
        return i    
    
    #return number of 
    def assent(self):
        i = 0
        filename = 'negation.txt'
        listOfWords = self.text.split()
        with open(filename) as f:
            content = f.readlines()
            content = [x.replace('\n','').lower() for x in content]
        for word in listOfWords:
            if word.lower() in content:
                i += 1
        return i;

    def sentiment(self):
        sentiment = TextBlob(self.text).sentiment
        #sentiment = {'polarity' : arr.polarity, 'subjectivity' : arr.subjectivity}
        return sentiment;

    def polarity(self):
        sentiment = TextBlob(self.text).sentiment
        return sentiment.polarity;

    def subjectivity(self):
        sentiment = TextBlob(self.text).sentiment
        return sentiment.subjectivity;

    def fMeasure(self):
        pos_array = TextBlob(self.text).pos_tags

        # get pos tag frequencies
        d = defaultdict(int)
        for word, tag in pos_array:
            d[tag] += 1

        # calculate F-measure
        f = 0.5 * ((d['NN'] + d['JJ'] + d['IN'] + d['DT']) - (d['PRP'] + d['VB'] + d['RB'] + d['UH']))

        return f;

    def emotiCount(self):

        # detects :) :( :p :P :D :o :O :S :/ :@ :| :] :[ :} :{
        #
        # (or with '8', '=', ';' instead of ':' and also with added '-')
        #
        # WHAT ABOUT .img EMOTICONS?
        regex = re.compile('[:|8|=|;]-*[\)\(\]\[}{pPDoOS//@/|]')
        emoList = regex.findall(self.text)
        return len(emoList);



text = "Hello my friend :) :-) you're ok :---) :P :@ 8-| =] foooooo :[ bar subar ;-)?"

#print(blob.ngrams(n=1));
#print(blob.ngrams(n=2));
#print(blob.ngrams(n=3));

featureVec = FeatureVector(text)

#print("Weighted average values: \n")
#print("Prepositions: "+str(featureVec.prepositionAv()))
#print("Hyperlinks: "+str(featureVec.hyperlinksAv()))
#print("Pronouns: "+str(featureVec.pronounsAv()))
#print("Prepositions: "+str(featureVec.prepositionAv()))
#print("Articles: "+str(featureVec.articlesAv()))
#print ("Sentiment: " +str(featureVec.sentiment()))
#print("F-measure: " + str(featureVec.fMeasure()))
print("Emoticons: " + str(featureVec.emotiCount()))