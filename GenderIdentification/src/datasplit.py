import pprint
import shutil
import os
import csv
import xml.etree.ElementTree as ET
import codecs
from os import path
from features import FeatureVector

# Returns a list of lists given a chunk size.
lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
        

src = 'C:\\Users\\Jake\\Desktop\\genID\\blogsfull';
filenames = next(os.walk(src))[2]

femaleFiles = [];
maleFiles = [];

if not os.path.exists('C:\\Users\\Jake\\Desktop\\genID\\bloggroups'):
    os.makedirs('C:\\Users\\Jake\\Desktop\\genID\\bloggroups')

males = 0
females = 0

for f in filenames:
    namevals = f.split('.');
    authorID = namevals[0];
    authorSex = namevals[1];
    if(authorSex == 'female'):
        femaleFiles.append(str(src) + "\\" + str(f))
        females = females + 1
    if(authorSex == 'male'):
        maleFiles.append(str(src) + "\\" + str(f))
        males = males + 1

total = males + females;
groups = total/500;
groups = round(groups,0)
groupedFemales = lol(femaleFiles,250)  # Group of 250 Female Files
groupedMales = lol(maleFiles,250)      # Group of 250 Male Files

print(str(len(groupedFemales)) + " -- " + str(len(groupedMales)))

for i in range(int(groups)):
    grouppath = 'C:\\Users\\Jake\\Desktop\\genID\\bloggroups\\group' + str(i)
    if not os.path.exists(grouppath):
        os.makedirs(grouppath)
    for femaleFile in groupedFemales[i]:
        shutil.copy(femaleFile, grouppath)
    for maleFile in groupedMales[i]:
        shutil.copy(maleFile, grouppath)
    print('Group: ' + str(i))
