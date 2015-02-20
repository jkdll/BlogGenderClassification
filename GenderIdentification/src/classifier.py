import csv
import pprint
import random
import nltk

# Function to Open the CSV
def loadCsv(filename):
    lines = csv.reader(open(filename, "rt"))
    sds = list(lines)
    return sds

# Function for K-fold Validation
# 
def kfoldCrossValidation(docs,k,classifierType):
    random.shuffle(docs) # Shuffle the instances
    print('>> Starting ' + str(k) + '-fold Validation for ' + classifierType);
    kLimit = int(round(len(docs)/k,0))
    # print('K Limit: ' + str(kLimit))
    accuracy = 0;
    for i in range(0,int(k)):
        lowerBound = i*kLimit
        upperBound = ((i+1)*kLimit)
        # print('Bounds : ' + str(lowerBound) + ',' + str(upperBound))
        tSet = []
        vSet = []
        for j in range(0,int(len(docs))):
            if( j < lowerBound or j >= upperBound):
                tSet.append(docs[j])
            else:
                vSet.append(docs[j])
        # print('>> Training Set Size: ' + str(len(tSet)))
        # print('>> Validation Set Size: ' + str(len(vSet)))
        classifier = nltk.NaiveBayesClassifier.train(tSet)
        tempAccuracy = nltk.classify.accuracy(classifier, validationSet)
        print ('>> Fold ' + str(i) + ' -> Training Set Size: ' + str(len(tSet)) + ', Validation Set Size: ' + str(len(vSet)) 
               + ' Accuracy: ' + str(tempAccuracy))
        accuracy = accuracy + tempAccuracy
    accuracy = accuracy/k
    print('>> Total Accuracy: ' + str(accuracy))
    
dataDir = 'C:\\Users\\Jake\\Desktop\\genID\\biggerdata.csv'
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
limit = int(round(len(dataSet)/10,0))

# Split into Training Set and Validation Set (TODO: Amend for Cross-Validation)
validationSet = dataSet[0:limit]
trainingSet = dataSet[limit:len(dataSet)]

# Example for Cross Validation ... validationSet = dataSet[i*limit:(i+1)*limit]

print('Data Set Length: ' + str(len(dataSet)))
print('Validation Length: ' + str(len(validationSet)))
print('Training Length: ' + str(len(trainingSet)))

print ('---------------------------')

# kfoldCrossValidation(dataSet,int(10),'Naive Bayes')
# classifier = nltk.NaiveBayesClassifier.train(trainingSet)
# classifier = nltk.svm.train(trainingSet)
# print(nltk.classify.accuracy(classifier, validationSet))

    