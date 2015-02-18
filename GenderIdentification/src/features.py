import math
from textblob import TextBlob
from collections import defaultdict
from turtledemo.chaos import line
import re

class FeatureVector:


    def __init__(self, text):
        regex = "[^a-zA-Z0-9-/']"
        #The blog post itself
        self.text = text
        #POS tagging on text sequence
        self.tags = TextBlob(text).tags
        #filter out unnecessary characters and return list of whole words
        self.listOfWords = [re.sub(regex, '', x) for x in text.split() if re.sub(regex, '', x)]     
        
    #Frequency of the prepositions in the text
    def prepositions(self):
        i = 0
        for tag in self.tags:
            if tag[1] == 'IN':
                i += 1 
        return i
    
    #Weighted average of the prepositions in the text
    def prepositionAv(self):
        if len(self.listOfWords) == 0:
            return 0
        else:
            return round(self.prepositions()/len(self.listOfWords),4)
    
    #Frequency of the pronouns in the text
    def pronouns(self):
        i = 0
        for tag in self.tags:
            if tag[1] == 'PRP':
                i += 1 
        return i
    
    #Weighted average of the pronouns in the text
    def pronounsAv(self):
        if len(self.listOfWords) == 0:
            return 0
        else:
            return round(self.pronouns()/len(self.listOfWords),4)
    
    #Frequency of articles in the text
    def articles(self):
        i = 0
        regex = "[^a-zA-Z0-9]"
        for word in self.listOfWords:
            word = re.sub(regex, '', word)
            if word.lower() in {"a", "an", "the"}:
                i += 1
        return i
    
    #Weighted average of the articles in the text
    def articlesAv(self):
        if len(self.listOfWords) == 0:
            return 0
        else:
            return round(self.articles()/len(self.listOfWords),4)
    
    #Frequency of the hyperlinks in the text
    def hyperlinks(self):
        i = 0
        regex = "[^a-zA-Z0-9]"
        for word in self.listOfWords:
            word = re.sub(regex, '', word)
            if word == 'urlLink':
                i += 1
        return i
    
    #Weighted average of the hyperlinks in the text
    def hyperlinksAv(self):
        if len(self.listOfWords) == 0:
            return 0
        return round(self.hyperlinks()/len(self.listOfWords),4)
    
    #Frequency of so-called "blog words" in text
    def blogWords(self):
        regex1 = '[^a-zA-Z0-9-/]'
        regex2 = '[^a-zA-Z0-9-\'\"/]'
        filename = 'blogwords.txt'
        i = 0
        textblob = TextBlob(" ".join(self.listOfWords))
        #load blog words text file
        blogWords_file = open(filename, 'r')
        #line represents a blog word
        for line in blogWords_file:
            #Remove non-alphanumeric characters in sequence
            line = re.sub(regex2, ' ', line)
            #array of words in line
            lineArray = [x.lower() for x in line.split()]
            #entry represents an n-gram instance of the input text
            for entry in textblob.ngrams(n = len(lineArray)):
                entry = [re.sub(regex1, '', x).lower() for x in entry]
                if lineArray == entry:
                    i += 1
        return i    
    
    #Weighted average of "blog words" in text
    def blogWordsAv(self):
        if len(self.listOfWords) == 0 :
            return 0
        return round(self.blogWords()/len(self.listOfWords),4)
    
    #Frequency of negation words in text
    def assent(self):
        i = 0
        regex = '[^a-zA-Z0-9]'
        filename = 'negation.txt'
        with open(filename) as f:
            content = f.readlines()
            content = [re.sub(regex, '', x).lower() for x in content]
        for word in self.listOfWords:
            word = re.sub(regex, '', word)
            if word.lower() in content:
                i += 1
        return i;
    
    #Weighted average of negation words in text
    def assentAv(self):
        if len(self.listOfWords) == 0:
            return 0
        return round(self.assent()/len(self.listOfWords),4)

    def sentiment(self):
        sentiment = TextBlob(self.text).sentiment
        #sentiment = {'polarity' : arr.polarity, 'subjectivity' : arr.subjectivity}
        return sentiment;

    def polarity(self):
        sentiment = TextBlob(self.text).sentiment
        return round(sentiment.polarity,4);

    def subjectivity(self):
        sentiment = TextBlob(self.text).sentiment
        return round(sentiment.subjectivity,4);

    def fMeasure(self):
        pos_array = TextBlob(self.text).pos_tags

        # get pos tag frequencies
        d = defaultdict(int)
        for word, tag in pos_array:
            d[tag] += 1

        # calculate F-measure
        f = (0.5 * ((d['NN'] + d['JJ'] + d['IN'] + d['DT']) - (d['PRP'] + d['VB'] + d['RB'] + d['UH']) + 100))/100

        return round(f,4);

    def emotiCount(self):
        text = self.text;
        text = (text.replace("&lt;", "<"));
        text = (text.replace("&gt;", ">"));

        # detects :) :( :p :P :D :o :O :S :/ :@ :| :] :[ :} :{
        #
        # (or with '8', '=', ';' instead of ':' and also with added '-')
        #
        regex = re.compile('[:|8|=|;]\'*-*[\)\(\]\[}{p<>3PDoOS//@/|]')
        emoList = regex.findall(text)

        filter = re.compile("[^:8=;\-\)\(\]\[}{<>3//@/|a-zA-Z0-9-/']")
        retext = [re.sub(filter, '', t) for t in text.split() if re.sub(filter, '', t)]
        if len(retext) == 0:
            return 0
        else:
            return len(emoList)/len(retext);

text_male = "Today on IAG we're pumped to announce that we're an ambassador for this year's GQ " \
       "Man of The Year party in Hollywood, Dec 4th! We'll be covering the event on social " \
       "media and showing you guys all things dapper. I wanted to pair this hollywood-sign " \
       "editorial I took on my last CA trip with the announcement because they both exude " \
       "the same message- follow your dreams, reach for the top and be confident! As an " \
       "influencer for menswear I'm honored GQ and Hugo Boss presented this opportunity " \
       "to me because now I feel like a man of the year myself! It's definitely inspired " \
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

#featureVec_m = FeatureVector(text_male)
#featureVec_f = FeatureVector(text_fem)

#print("Weighted average values: \n")
#print("Prepositions: "+str(featureVec.prepositionAv()))
#print("Hyperlinks: "+str(featureVec.hyperlinksAv()))
#print("Pronouns: "+str(featureVec.pronounsAv()))
#print("Prepositions: "+str(featureVec.prepositionAv()))
#print("Articles: "+str(featureVec.articlesAv()))
#print ("Sentiment: " +str(featureVec.sentiment()))

#print("Male F-measure: " + str(featureVec_m.fMeasure()))
#print("Male Emoticons: " + str(featureVec_m.emotiCount()))
#print("Male Prepositions: " + str(featureVec_m.prepositionAv()))
#print("Male Pronouns: " + str(featureVec_m.pronounsAv()))
#print("Male Articles: " + str(featureVec_m.articlesAv()))
#print("Male Hyperlinks: " + str(featureVec_m.hyperlinksAv()))
#print("Male Blog words: " + str(featureVec_m.blogWordsAv()))
##print("Male Sentiment: " + str(featureVec_m.sentiment()))
#print("\n")
#print("Female F-measure: " + str(featureVec_f.fMeasure()))
#print("Female Emoticons: " + str(featureVec_f.emotiCount()))
#print("Female Prepositions: " + str(featureVec_f.prepositionAv()))
#print("Female Pronouns: " + str(featureVec_f.pronounsAv()))
#print("Female Articles: " + str(featureVec_f.articlesAv()))
##print("Female Hyperlinks: " + str(featureVec_f.hyperlinksAv()))
#print("Female Blog words: " + str(featureVec_f.blogWordsAv()))
#print("Female Sentiment: " + str(featureVec_f.sentiment()))