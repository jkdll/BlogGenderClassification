import math
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
        f = (0.5 * ((d['NN'] + d['JJ'] + d['IN'] + d['DT']) - (d['PRP'] + d['VB'] + d['RB'] + d['UH'])))

        return f;

    def normfMeasure(self):
        pos_array = TextBlob(self.text).pos_tags

        # get pos tag frequencies
        d = defaultdict(int)
        for word, tag in pos_array:
            d[tag] += 1

        # calculate F-measure
        f = (0.5 * ((d['NN'] + d['JJ'] + d['IN'] + d['DT']) - (d['PRP'] + d['VB'] + d['RB'] + d['UH'])))
        listOfWords = self.text.split()
        measure = f/(len(listOfWords)/2)
        #measure = math.pow(f/(len(listOfWords)/2), 2)

        return measure;

    def emotiCount(self):

        # detects :) :( :p :P :D :o :O :S :/ :@ :| :] :[ :} :{
        #
        # (or with '8', '=', ';' instead of ':' and also with added '-')
        #
        # WHAT ABOUT .img EMOTICONS?
        regex = re.compile('[:|8|=|;]-*[\)\(\]\[}{pPDoOS//@/|]')
        emoList = regex.findall(self.text)
        listOfWords = self.text.split()
        return len(emoList)/len(listOfWords);



text_male = "Today on IAG we’re pumped to announce that we’re an ambassador for this year’s GQ " \
       "Man of The Year party in Hollywood, Dec 4th! We’ll be covering the event on social " \
       "media and showing you guys all things dapper. I wanted to pair this hollywood-sign " \
       "editorial I took on my last CA trip with the announcement because they both exude " \
       "the same message- follow your dreams, reach for the top and be confident! As an " \
       "influencer for menswear I’m honored GQ and Hugo Boss presented this opportunity " \
       "to me because now I feel like a man of the year myself! It’s definitely inspired " \
       "me to keep showcasing editorials about fashion, lifestyle and travel. Over the " \
       "course of the next two weeks be on the look out for my Man of The Year coverage " \
       "and my journey to the red carpet in Hollywood! so pumped!"

text_fem = "SERIOUSLY, THOUGH, there's something about the sunniest of days (Errrr... " \
           "February? Is that you?) that makes me want to bring out all my black vestigial " \
           "items at one go. Well, black has always been my safety net, but it is particularly " \
           "effective on bright days. Now, before you dismiss this post as just another ramble " \
           "(which it is), I'd like to justify myself by attempting at a pathetic explanation: " \
           "I think black stands out on nice days. On the other hand, I prefer wearing colour in " \
           "dull, cloudy weather, because not only does that also stand out, but it lifts my mood " \
           "a little. Think about it... I must be at least a little bit right... no?"

#print(blob.ngrams(n=1));
#print(blob.ngrams(n=2));
#print(blob.ngrams(n=3));

featureVec_m = FeatureVector(text_male)
featureVec_f = FeatureVector(text_fem)

#print("Weighted average values: \n")
#print("Prepositions: "+str(featureVec.prepositionAv()))
#print("Hyperlinks: "+str(featureVec.hyperlinksAv()))
#print("Pronouns: "+str(featureVec.pronounsAv()))
#print("Prepositions: "+str(featureVec.prepositionAv()))
#print("Articles: "+str(featureVec.articlesAv()))
#print ("Sentiment: " +str(featureVec.sentiment()))
print("Male F-measure: " + str(featureVec_m.fMeasure()))
print("Male Normalised F-measure: " + str(featureVec_m.normfMeasure()))
print("Male Emoticons: " + str(featureVec_m.emotiCount()))

print("Female F-measure: " + str(featureVec_f.fMeasure()))
print("Female Normalised F-measure: " + str(featureVec_f.normfMeasure()))
print("Female Emoticons: " + str(featureVec_f.emotiCount()))