'''
Created on Feb 6, 2015

@author: James
'''
import unittest
from src.features import FeatureVector

class Test(unittest.TestCase):

    def test_blogWords_zero(self):
        text = "My name is James Zammit"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(0, noBlogWords)
        
    def test_blogWords_unigram_one(self):
        text = "But first, let me take a selfie"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(1, noBlogWords)
        
    def test_blogWords_unigram_two(self):
        text = "Anakin Skywalker grabbed his lightsaber and caused a genocide"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(2, noBlogWords)
        
    def test_blogWords_unigram_punc(self):
        text = "U fkin wot m8?"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(4, noBlogWords)   
        
    def test_blogWords_bigram_one(self):
        text = "James doesn't care about political correctness, or does he?"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(1,noBlogWords)
        
    def test_blogWords_bigram_two(self):
        text = "I have a serious wardrobe malfunction. It feels like a black hole"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(2,noBlogWords)
    
    def test_blogWords_trigram_one(self):
        text = "Lately I feel like i'm jumping the shark"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(1,noBlogWords)
    
    def test_blogWords_combined_two(self):
        text = "Lately I feel like i'm jumping the shark haha"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(2,noBlogWords)
    
    def test_blogWords_combined_three(self):
        text = "haha stop being a troll and talk about dog-whistle politics"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(3,noBlogWords)

    def test_assent_none(self):
        text = "This pie is delicious"
        noAssentWords = FeatureVector(text).assent()
        
        self.assertEqual(0,noAssentWords)
        
    def test_assent_one(self):
        text = "This pie Doesn't taste so good"
        noAssentWords = FeatureVector(text).assent()
        
        self.assertEqual(1,noAssentWords)
        
    def test_assent_three(self):
        text = "This pie Doesn't taste so good. I can't comprehend with the yuckiness of this mess. It's so disgusting and not good"
        noAssentWords = FeatureVector(text).assent()
        
        self.assertEqual(3,noAssentWords)    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()