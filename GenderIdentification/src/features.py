from textblob import TextBlob

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
        return i/len(listOfWords);
         

text = '''
urlLink urlLink urlLink urlLink The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''
featureVec = FeatureVector(text)

print("Weighted average values: \n")
print("Prepositions: "+str(featureVec.prepositionAv()))
print("Hyperlinks: "+str(featureVec.hyperlinksAv()))
print("Pronouns: "+str(featureVec.pronounsAv()))
print("Prepositions: "+str(featureVec.prepositionAv()))
print("Articles: "+str(featureVec.articlesAv()))