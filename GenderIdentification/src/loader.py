import re
import os
import csv
import xml.etree.ElementTree as ET
import codecs
from os import path
from features import FeatureVector

blogsDir = 'C:\\Users\\Jake\\Desktop\\genID\\bloggroups\\group7';
filenames = next(os.walk(blogsDir))[2]

# print filenames;
# Feature will be of form:
# [Author ID, Post ID, ... , Target Gender]

counter = 0
mpa = dict.fromkeys(range(32))
dataset = [];
with open('C://Users//Jake//Desktop//genID//data7.csv', 'a') as csvfile:
        fieldnames = ['PrepositionFrequency'
                      ,'PronounFrequency'
                      ,'ArticleFrequency'
                      ,'HyperlinkFrequency'
                      ,'BlogwordFrequency'
                      ,'AssentWordFrequency'
                      ,'Polarity'
                      ,'Subjectivity'
                      ,'fmeasure'
                      ,'emoticons'
                      ,'gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

for f in filenames:
    namevals = f.split('.');
    authorID = namevals[0];
    authorSex = namevals[1];
    # Test_file = open(blogdir + '\\' + f,'r');
    # print("Opening" + authorID + " as " + str(counter));
    
    with open (blogsDir + '\\' + f, "r", encoding="latin-1") as myfile:
        data = myfile.read().replace('&','&amp;').translate(mpa); # Opens the file and maps control Symbols
    xmlTree = ET.fromstring(data);
    postcount = 0;
    for post in xmlTree.findall('post'):
        feature = FeatureVector(post.text);
        dataset.append([feature.prepositionAv()    #3
                        ,feature.pronounsAv()        #4
                        ,feature.articlesAv()        #5
                        ,feature.hyperlinksAv()        #6        
                        ,feature.blogWordsAv()        #7
                        ,feature.assentAv()            #8
                        ,feature.polarity()            #9
                        ,feature.subjectivity()        #10
                        ,feature.fMeasure()            #11
                        ,feature.emotiCount()        #12
                        ,authorSex]);                #13
        postcount = postcount + 1;
    #print (authorID + " , " + authorSex + ">>> ");
    counter = counter + 1; 
    # print("ID,Post Count,Prepositions,Pronouns,Articles,Hyperlinks,BlogWords,Assent,Polarity,Subjectivity,fMeasure,EmotiCons,Gender");
for d in dataset:
        with open('C://Users//Jake//Desktop//genID//data.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'PrepositionFrequency' : str(d[0])
                             ,'PronounFrequency' : str(d[1])
                             ,'ArticleFrequency' : str(d[2])
                             ,'HyperlinkFrequency' : str(d[3])
                             ,'BlogwordFrequency' : str(d[4])
                             ,'AssentWordFrequency' : str(d[5])
                             ,'Polarity' : str(d[6])
                             ,'Subjectivity' : str(d[7])
                             ,'fmeasure' : str(d[8])
                             ,'emoticons' : str(d[9])
                             ,'gender' : str(d[10])})
        
print("Read: " + str(counter) + " Files and " + str(postcount) + " Posts");
# var = raw_input("Waiting...");
