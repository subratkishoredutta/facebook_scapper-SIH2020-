# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:33:06 2020

@author: Asus
"""

import JATAYUscrapes as JaS
import location as loc
import pandas as pd
location = loc.loadLOC_data()
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('NAKHYATRAtracks.json')
firebase_admin.initialize_app(cred)
db=firestore.client()


URL='https://www.facebook.com/sauraja.sarkar'

def tracks(URL):
    postimestamp,loctime = JaS.getPOSTdateANDtime(URL)
    places= loctime['location'].unique()
    ref=[None]*100
    j=0
    for place in places:
        name='CAM'+str(j+1)
        lat,long=location[place]
        timestamp=''
        for i in range(len(loctime)):
            if loctime['location'].iloc[i]==place:
                timestamp+=loctime['date'].iloc[i]+", "
        timestamp=timestamp[:-2]
        res={'state':True,
             '_latitude':lat,
             '_longitude':long,
             'timestamp':timestamp}
        ref[j]=db.collection('Nakhyatra').document(name)
        ref[j].set(res)
        j+=1

tracks(URL)



















































'''
train = [
('I love this sandwich.', 'pos'),
('this is an amazing place!', 'pos'),
('I feel very good about these beers.', 'pos'),
('this is my best work.', 'pos'),
("what an awesome view", 'pos'),
('I do not like this restaurant', 'neg'),
('I am tired of this stuff.', 'neg'),
("I can't deal with this", 'neg'),
('he is my sworn enemy!', 'neg'),
('my boss is horrible.', 'neg'),
('Dharm Rakshati Rakshit','pos'),
('It is a crime for these unemployed youth to dream of building green Jamuguri Chatia along with being established through agricultural work in Sor area. Local Asâ€¦ See more','pos'),
('Aishe Ghosh didi is comparing "internships" to "Child labour". My Goodness . This is the reason why thousands of industries in Bengal were forced to shut dâ€¦ See more','neg'),
('jhooth_bole_kawa_kate ..','neg')	,
("You may forget what you lie, social media don't!Image courtesy -  #skindoctor","pos")	,
("From nowonwards before making any film/webseries on Indian Army the producers will have to obtain 'NOC' from Defence Ministry before the telecast of movie/documentary.",'pos'),
('Ahinsa Param Dharm ; Dharm Hinsha Tathaiv Sa.','pos')	,
('Best wishes on your birthday brother! Party is pending','pos'),	
('Good morning to all with good wishes of a good day!','pos'),
("This is where the problem lies. People don't understand the meaning of diversity and inclusiveness.Remember how the Hindi speaking belt reacted to the word Haramzada? Well it is commonly used in almost every bengali household but not as a slang like in north and this not just one word but there are many more  where my North Indian mates will get offended. We we must learn to respect every culture & custom and learn it. East Indians, North Indian, South Indians have a very diâ€¦ See more","pos"),
("Mahadev","neutral"),
("Haram ka paisa hai jahan udana hai,Jitna udana hai udao.",'neg'),
("I was thinking about four years that there is a ' BJP ' government in Assam, I came to know that the government of ' hanging in jÄá¹…iáºÄta ' is in Assam." ,"neg"	),
("Couldn't buy a bike for lock down but I believe that I will open all the shops on July 30/31th and then buy the address ","neutral"),
("BJP government in both states. But the difference is the sky.May Yogiji win. à¥¤May the good people be destroyed. à¥¤	","negative"),
("In Uttar Pradesh, the one who has been arrested by one of the benefits of a person in Uttar Pradesh in Uttar Pradesh, was destroyed by the house administration.","neg"	),
("It's a great match.(possible by this bÄ“gamajÄna supporter)","neutral"),	
("The Pride of Assam #Shaw #Shaw #against #will #will #will #will.#Brother _ Shiva was the reign of #1714 _ Christian to #1744 _ Christian.During the reign of #brother _ Shiva, his second wife, #om _ bara'Ä'ikuraraÄ« _ Bara'Ä'ikuraraÄ« #1734 _ Christ.","neutral"),	
("...Swiss Alps Mantra Meditation...The holy name of Krishna is so attractive that anyone who chants it â€” including aâ€¦ See more","neutral"),
("Follow The Truth#Hinduism_For_All	","neutral"),
("Those were the days	",'pos'),
("Respect (. â› á´— â›.)","neutral"),
("Rachel Green * FACE PALM*","neutral"),
 ("F.R.I.E.N.D.Shttps://instagram.com/cineophiles?igshid=6woi2iw3lcze	","neutral"),
("y'all can celebrate your 1Di am gonna celebrate Mr bend-a-dick cum-a-batch 	",'pos'),
("Ten minutes of brilliant Sherlock moments to mark the showâ€™s 10th anniversary today 	","neutral"),
("wrong. Pythagoras just said ' sum of squares of perpendicular and base is equal to square of hypotenuse'Here Euclids theorem ' sum of two sides of a triangle is greater than 3rd side' is coming into play, not Pythagoras' theorem.thanks Vivian Das Barman for the mathematician's name",'pos'),
("FDT!ishe kehte hai freedom of speechIndia mai freedom of speech is ' kunal kamra zinda hai na'"	,"neg"	),
("People in the streets of Chicago had a message for the president who is sending federal officers to crack down on protesters.	",'pos'),
("I have got this theory. Mechanical Engineers are Avatars.",'pos'),
("Pope Knows me (â—â€¢á´—â€¢â—)",'pos'),
("You dare? YOU ACTUALLY DARE?","neutral"),
("Iqbal Choudhury","neutral"),
("SpongeBob SquarePants and Rick n Morty too ( aye aye captain)*_* *_* *_* *_* *_* *_* *_* *_* *_* *_*	","neutral"),
("The kind of date I want (â—â€¢á´—â€¢â—)	","neutral"),
("S U C K    S Q U E E Z E     B A N G B L O WNothing erotic, just the engineering name of how your Car ENGINE operates. Saying this to conform how INNOCENT souls are we Engineers. â€¦ See more	","neutral"),
("Bhakts be like ' yeh orwellian aur Goebbels Gobar kya hai reh? Maa ko gaali de deta ...kamse kam Samaj toh ati"	,"hate"),
("In BJP's Orwellian regime, not only is propaganda adopted as a strategy, it is advertised with such unashamed brazenness. No doubt they study the techniques of â€¦ See more	" ,"neg"	),
("asie chutiye hai apne desh vasi. if getting offended was a sport in Olympics, har Indian Micheal Phelps hota	" ,"neg"	),
("REPORT THIS PIC for obscenity White dick on black pussy, facebook hai ya pornhub." ,"neg"	),
("What would you name this kitten.	","neutral"),
("Corona cases are rising. The primary reason is that people don't wear masks in public. Maybe because they are tired of wearing their regular masks of being happy, nice and polite.Yeah you fucking cunts I am talking about those two faced mofos!	"	,"hate"),
("baby if he watches porn and you're dating him, he lowered his standards for you.	",'pos'),
("LULz	","neutral"),
("Kartik Jha Subham Jaiswal Mohit Kundu aisa gaali dega future mai apna Atul Singh Rajput bhai	","neutral"),
("Chacha xd","neutral"),
("these people commenting are ignorant fools, just like your HRD ministry	"	,"hate"),
("You madadalians you win.	","neutral"),
("50% of earthling would be dead to be precise	","neutral"),
("NOW? NOW?Y'all madafuckers need to Understand that SUICIDE WAS A BIG ISSUE IN INDIA! Y'ALL MOFOS NEED MOVIE STARS TO DIE TO MASTURBATE OVER MENTAL HEALTH IMPORTANCE?BITCH ASS NIGGAS! â€¦ See more	",'pos'),
("Terrible news  #restinpeace	","neutral"),
("Iqbal Choudhury","neutral"),
("Astagfirullah!Me shareef boy. ;_;  Me donno how to flort.","neutral"),	
("Iqbal Choudhury	","neutral"),
("This is adorable","pos"),
("I guess we are better than making meme on the girl from DU scandal. Tomorrow you shall become internet psychologist again, if she commits suicide from internet bullying.",'pos')
("Thank you Reshmi Aich and Subrat Kishor Dutta for nominating me to continue the chain of ' Art and Artist'.Here's few of my collections, though few even got cropped but somehow managed to get a collage.So I request all the artist out there to carry forward the chain. Thank you ","pos")]


'''
