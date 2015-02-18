import re
import os
import xml.etree.ElementTree as ET
import codecs
from os import path
from features import FeatureVector

blogsDir = 'C:\\Users\\Jake\\Desktop\\genID\\blogssmall';
filenames = next(os.walk(blogsDir))[2]

# print filenames;
# Feature will be of form:
# [Author ID, Post ID, ... , Target Gender]

counter = 0
mpa = dict.fromkeys(range(32))
dataset = [];

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
        dataset.append([authorID                    #1
                        , postcount                    #2
                        ,feature.prepositionAv()    #3
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
    print("ID,Post Count,Prepositions,Pronouns,Articles,Hyperlinks,BlogWords,Assent,Polarity,Subjectivity,fMeasure,EmotiCons,Gender");
    for d in dataset:
        print(str(d[0]) + "," + str(d[1]) 
                + "," + str(d[2]) + "," + str(d[3]) 
                + "," + str(d[4]) + "," + str(d[5]) + "," 
                + str(d[6]) + "," + str(d[7]) + "," 
                + str(d[8]) + "," + str(d[9]) + "," 
                + str(d[10]) + "," + str(d[11]) + "," + str(d[12]));
        print("\n");
        
print("Read: " + str(counter) + " Files and " + str(postcount) + " Posts");
# var = raw_input("Waiting...");
