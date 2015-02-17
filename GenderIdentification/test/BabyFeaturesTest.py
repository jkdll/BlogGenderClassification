'''
Created on Feb 6, 2015

@author: James
'''
import unittest
from src.features import FeatureVector

class Test(unittest.TestCase):

    def test_preposition_zero(self):
        text = "The fridge is closed"
        noPrepositions = FeatureVector(text).prepositions()

        self.assertEqual(0, noPrepositions)
        
    def test_preposition_one(self):
        text = "The food in the fridge has expired"    
        noPrepositions = FeatureVector(text).prepositions()

        self.assertEqual(1, noPrepositions)
        
    def test_preposition_two(self):
        text = "Did the ball go OUT OUT OUT  \"OUT\"? Or did it stay in?"
        noPrepositions = FeatureVector(text).prepositions()
        
        self.assertEquals(5, noPrepositions)
        
    def test_preposition_eight(self):
        text = "My first post was hardly interesting, probably because everytime i pressed return the page went down, causing a severe lack of eye-appealing one-line comments.  Such as this.  And this.  Man I hope George Bush doesn't win. I'm not saying that John Kerry will solve all our problems, but I think he'll do a better job.  If any of you are reading this, I need some help. What kind of digital camera should I get? I'm a tad bit clueless, and I need one before September 11th, when I am to be attending the Franz Ferdianand concert. "
        noPrepositions = FeatureVector(text).prepositions()
        
        self.assertEquals(8, noPrepositions)
        
    def test_articles_zero(self):
        text = "There are no articles in this sentence"
        noArticles = FeatureVector(text).articles()
        
        self.assertEquals(0, noArticles)
        
    def test_articles_one(self):
        text = "There is \"AN' article in this sentence"
        noArticles = FeatureVector(text).articles()
        
        self.assertEquals(1, noArticles)
        
    def test_articles_two(self):
        text = "THe sandwich my mother made is 'a' work of art"    
        noArticles = FeatureVector(text).articles()
        
        self.assertEquals(2, noArticles)
        
    def test_articles_five(self):
        text="A wise man once said that the universe is \"an\" apple and a?! banana falling from the tree"
        noArticles = FeatureVector(text).articles()
        
        self.assertEquals(5, noArticles)
        
    def test_hyperlinks_zero(self):
        text = "There are no hyperlinks in this sentence"
        noHyperlinks = FeatureVector(text).hyperlinks()
        
        self.assertEquals(0, noHyperlinks)
    
    def test_hyperlinks_one(self):
        text = """hey~ feelin alil sick @ the moment. whats up? my dad still aint emailed me yet... ugh...  xoxo~kd
     
    urlLink clickity clickity click!"""
        noHyperlinks = FeatureVector(text).hyperlinks()
        
        self.assertEquals(1, noHyperlinks)  
        
    def test_hyperlinks_two(self):
        text = """LUKAS SCHWARZACHER (Variety) TOKYO Traditionally, Japanese summer fairs and festivals that start in the evening and last until the small hours are called matsuri.  Leave it to Fuji Television Network to bring the venerable custom into the modern world of movies. Its first seven-day Movie King event runs from Aug. 21 in the wide-open area of Odaiba along Tokyo's waterfront, which houses Fuji TV's headquarters. The fest is an extravaganza to consolidate Fuji TV's already strong status as Japan's foremost movie-oriented network. Highlights include special-edition screenings of "Star Wars," "The Empire Strikes Back" and "Return of the Jedi." Lucasfilm has granted exclusive approval for the screenings, the first since their theatrical release here in 1997. A preview of "Resident Evil: Apocalypse" with an appearance by star Milla Jovovich ( urlLink news ) plus a Stephen Chow Night featuring "Shaolin Soccer" and the popular Hong Kong thesp himself complement screenings of Fuji TV-produced pics to be released later this year. Among those are Shinji Aoyama's psycho-thriller "Lakeside Murder Case," and "Swing Girls" by Shinobu Yaguchi ("Waterboys") about an all-girl high school big band, both favorites among this fall's releases. Odaiba houses one of Tokyo's most modern multiplexes, the Mediage Cinema, host to most of the showings. To top it off, all 24 parts of season three of TV skein "24" will be screened back-to-back, with only one brief intermission. This calls for some sake afterwards. "It's all about fun and about building up our brand," explains Chihiro Kameyama, head of Fuji TV's motion picture department and chief organizer of Movie King. Although not an official film festival, the event could establish itself as Tokyo's prime audience-oriented film event of the year. Given the continuing struggle of the Tokyo Intl. Film Festival for relevance and public acceptance, the competition from across town could become stronger than wished for. "It's an interesting concept, and Fuji TV has the power to pull in the crowds," observes a film distribution exec. Being part of the all-summer Adventure King festival and amusement park staged annually by Fuji TV also helps. Last year's installment of this assortment of Fuji TV content-based attractions chalked up 3.5 million visitors over less than two months urlLink. """
        noHyperlinks = FeatureVector(text).hyperlinks()
        
        self.assertEquals(2, noHyperlinks)  
        
    def test_hyperlinks_three(self):
        text = """Well, it sure as hell doesn't help.      John Kerry's going to be on The Daily Show tonight. Man, Jon Stewart gets better guests than Conan does. And Conan's got that sweet NBC spot. This is very strange... maybe it's that Jon is funnier? Ah well, who gives a shit.      You know what I realized?  John  Kerry,  John  Edwards... John  Flansburgh,  John  Linnell. Cha, like we wouldn't notice. Nice shot at scoring a piece of the pie, Democratic presidential ticket.       There are too many Johns in my life right now... I have to take one of them out or something.       No wonder Comedy Central is owned by MTV, they run the same movies over and over just as MTV runs the same videos over and over. I've seen Dogma seventy thousand times over the last couple of months.   SOLD OUT! Cat's Cradle Carrboro, NC SAT, SEP 11  urlLink?@:><" Franz Ferdinand    urlLink The Delays   urlLink The Futureheads  Doors: 8:00 pmShow: 9:00 pm SOLD OUT!!  That's right. Sold out... I've seen a bunch of unlucky bastards trying to find tickets over the internet. Good luck kids, I'll wait for youz inside. """
        noHyperlinks = FeatureVector(text).hyperlinks()
        
        self.assertEquals(3, noHyperlinks)  
        
    def test_hyperlinks_ten(self):
        text = "urlLink urlLink??? urlLink! urlLink urlLink urlLink urlLink urlLink urlLink urlLink"
        noHyperlinks = FeatureVector(text).hyperlinks()
        
        self.assertEquals(10, noHyperlinks)  
        
    def test_blogWords_zero(self):
        text = "My name is James Zammit"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(0, noBlogWords)
        
    def test_blogWords_unigram_one(self):
        text = "Can I take a selfie?"
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
        text = "Lately I feel like i'm 'jumping the shark' haha"
        noBlogWords = FeatureVector(text).blogWords()
        
        self.assertEqual(2,noBlogWords)
    
    def test_blogWords_combined_three(self):
        text = "haha stop being a troll and talk about ?dog-whistle politics?"
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
        text = "This pie Doesn't taste so good. I can't comprehend with the yuckiness of this mess. It's so disgusting and 'not' good"
        noAssentWords = FeatureVector(text).assent()
        
        self.assertEqual(3,noAssentWords)

    def test_assent_four(self):
        text="""I guess i'm pretty much indifferent about school starting. I CANT change that it's going to come. I love change. I'm NoT afraid of it like other ppl. I feel that things can only get better in my life, i DONT like my past so i hope my future is better. That is how i feel about pretty much everything. Life is NeveR stopping. It always changes, so i guess since i CAN'T change it i should make the best out of it. """
        noAssentWords = FeatureVector(text).assent()
        
        self.assertEqual(5,noAssentWords)
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()