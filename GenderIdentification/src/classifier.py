import csv
import pprint
import random
import nltk

def loadCsv(filename):
    lines = csv.reader(open(filename, "rt"))
    sds = list(lines)
    return sds

dataDir = 'C:\\Users\\Jake\\Desktop\\genID\\data152.csv'
sds = loadCsv(dataDir)

# Remove Headers, and shuffle data set.
headers = sds[0]
sds.pop(0)
print(sds[0])
random.shuffle(sds)

# The List used for the Data Set
dataSet = []

# Convert to Proper Classes
for d in sds:
    featureIQ = {}
    featureIQ[headers[0]] = float(d[0])
    featureIQ[headers[1]] = float(d[1])
    featureIQ[headers[2]] = float(d[2])
    featureIQ[headers[3]] = float(d[3])
    featureIQ[headers[4]] = float(d[4])
    featureIQ[headers[5]] = float(d[5])
    featureIQ[headers[6]] = float(d[6])
    featureIQ[headers[7]] = float(d[7])
    featureIQ[headers[8]] = float(d[8])
    featureIQ[headers[9]] = float(d[9])
    dataSet.append([featureIQ,str(d[10])])

# Calculate Split Ratio and Split Limits (TODO: Amend for Cross-Validation)
p = len(dataSet)/20
p = int(round(p,0))
limit = int(p)

# Split into Training Set and Validation Set (TODO: Amend for Cross-Validation)
validationSet = dataSet[0:limit]
trainingSet = dataSet[limit:len(dataSet)]

# Example for Cross Validation ... validationSet = dataSet[i*limit:(i+1)*limit]

print('Data Set Length: ' + str(len(dataSet)))
print('Validation Length: ' + str(len(validationSet)))
print('Training Length: ' + str(len(trainingSet)))

classifier = nltk.NaiveBayesClassifier.train(trainingSet)
print(nltk.classify.accuracy(classifier, validationSet))

