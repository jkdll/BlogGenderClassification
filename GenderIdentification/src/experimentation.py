from textblob import TextBlob

noun_sing = 'NN'
noun_plu = 'NNS'
proper_noun = 'NNP'
modal = 'MD'
base_verb = 'VB'
preposition = 'IN'
pronoun = 'PRP'

text = """ The titular threat of The Blob has always struck me as the ultimate
movie monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly describes
it--"assimilating flesh on contact. Snide comparisons to gelatin be damned, it's
a concept with the most devastating of potential consequences, not unlike the
grey goo scenario proposed by technological theorists fearful of artificial
intelligence run rampant.
"""

blob = TextBlob(text)
# [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

#for sentence in blob.sentences:
    #print(sentence.sentiment.polarity)
# 0.060
# -0.341

blob.translate(to="es")  # 'La amenaza titular de The Blob...'
  

def prepositions(text):
    return noOfTags(text, preposition)    

def pronouns(text):
    return noOfTags(text, pronoun)

 
def noOfTags(text, pos):
    i = 0
    blob = TextBlob(text)
    for tag in blob.tags:
        if tag[1] == pos:
            i += 1 
    return i

print(prepositions(text))
print(pronouns(text))