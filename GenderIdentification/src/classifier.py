import csv
import pprint
import random
import nltk
import sys
import pickle

# Function to Open the CSV
def loadCsv(filename):
    lines = csv.reader(open(filename, "rt"))
    sds = list(lines)
    return sds

# Function for K-fold Validation
def kfoldCrossValidation(docs,k,classifierType):
    if(classifierType == 'Max Entropy'):
        kLimit = int(round(len(docs)/10,0))
        lowerBound = 0
        upperBound = kLimit
        tSet = []
        vSet = []
        for j in range(0,int(len(docs))):
            if( j < lowerBound or j >= upperBound):
                tSet.append(docs[j])
            else:
                vSet.append(docs[j])
        classifierToSave = nltk.MaxentClassifier.train(tSet)
    else:
        random.shuffle(docs) # Shuffle the instances
        print('>> Starting ' + str(k) + '-fold Validation for ' + classifierType);
        kLimit = int(round(len(docs)/k,0))
        maxAccuracy = 0
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
            tempAccuracy = nltk.classify.accuracy(classifier, vSet)
            print ('>> Fold ' + str(i) + ' -> Training Set Size: ' + str(len(tSet)) + ', Validation Set Size: ' + str(len(vSet)) 
                   + ' Accuracy: ' + str(tempAccuracy))
            if(tempAccuracy >= maxAccuracy):
                classifierToSave = classifier
            accuracy = accuracy + tempAccuracy
        accuracy = accuracy/k
        print('>> Total Accuracy: ' + str(accuracy))
    return classifierToSave


# Get Total Number of Arguments
total_arguments = len(sys.argv)

# Get the Argument List
input_arguments = str(sys.argv)

#if(total_arguments <= 3):
#    raise Exception("Error Less than Two Arguments; Usage: 'python classifier.py '<Data Directory>' '<O'")
#else:
#    input_arguments = str(sys.argv)
    
dataDir = 'C:\\Users\\Jake\\Desktop\\genID\\biggerdata.csv'
sds = loadCsv(dataDir)

# Remove Headers, and shuffle data set.
headers = sds[0]
sds.pop(0)
random.shuffle(sds)
    
# The List used for the Data Set
dataSet = []

# Convert Data to Proper Classes
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

###########################################################################
# For Manual Splitting: Split into Training Set and Validation Set
# Calculate Split Ratio and Split Limits 
## limit = int(round(len(dataSet)/10,0))
## validationSet = dataSet[0:limit]
## trainingSet = dataSet[limit:len(dataSet)]
# To Print:
## print('Validation Length: ' + str(len(validationSet)))
## print('Training Length: ' + str(len(trainingSet)))
# To Classify:
## classifier = nltk.NaiveBayesClassifier.train(trainingSet)
## classifier = nltk.svm.train(trainingSet)
## print(nltk.classify.accuracy(classifier, validationSet))
##########################################################################

# However, We shall Work with Cross Validation By Default

# Print Data Set Length
print('Data Set Length: ' + str(len(dataSet)))
print ('---------------------------')

# Get Classifier
# nb_class = kfoldCrossValidation(dataSet,int(10),'Naive Bayes')
nb_class = kfoldCrossValidation(dataSet,int(10),'Max Entropy')

# Save Classifier
f = open('C:\\Users\\Jake\\Desktop\\genID\\genID.pickle', 'wb')
pickle.dump(nb_class, f)
f.close()