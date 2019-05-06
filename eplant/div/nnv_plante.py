import serial
import time
import tweepy
import random
import safygiphy
import giphypop
import warnings
from giphypop import translate
from collections import Counter
import string

warnings.filterwarnings("ignore")

var = 0
count = 0

ser = serial.Serial('COM4', 115200, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False) # raPI /dev/ttyACM0 MAC: /dev/tty.usbmodem1422
ser.flushInput()
ser.flushOutput()

WORDS1 = ("red", "blue", "green", "yellow", "black", "white", "grey", "pink")
WORDS2 = ("python", "jumble", "easy", "difficult", "answer",  "xylophone", "drum", "silly", "mad", "happy", "sad")
WORDS3 = ("dog", "cat", "cow", "horse", "pig",  "chinchilla", "elephant", "sheep", "snake")
HASTAG = ("#plantbot","#microbit","#python","#hourofcode","#giphy", "#digiplant", "#eplant", " ", " ", " ")
VERB = ("swim","ride","walk","fly","drink","watch","run","drive","sleep","bath","burn","eat","love")
NOUN = ("cat","car","dog","horse","pig","apple","banana","rosine","bike","bird","book","frog","cow","elephant","xylophone","drum","heart","house",
        "tent","bus","airplaine","snake","mountain","city","river","flower")



COLOUR = ("red","blue","green","yellow","black","white","grey","pink","purple","rainbow")

ADJECTIVE = ("dry","dead","sad","unhappy","badday", "angry")
ADJECTIVE2 = ("fine", "happy", "good", "cool", "nice", "alive")

nat_word = """Animism Aquatic Arctic Array Autumn Awareness Awesome Barren Beauty Bees Biodegradable Boulder Bountiful Brilliant Brook
            Buoyancy Butte Butterfly Buzz Celestial Cliff Climate Clouds Coastal Color Combustible Commercial Commune Conifer Conservation
            Conspicuous Contiguous Cordillera Cosmography Crater Crucial Current Deft Demise Deplorable Desert Destructive Disposable
            Dynamic Earthquake Earthy Eclipse Ecological Efficient Electrifying Endangered Endemic Enigmatic Environment Erosion
            Escarpment Esker Evergreen Exclusive Fall Fallow Farming Fertile Fibrous Fierce Flood Fog Foliage Forest Glacier Gorgeous
            Grassland Gravity Growth Gusty Habitat Hail Healthy Hibernate Horizon Hurricane Hygienic Iceberg Imitation Indigenous Innate
            Intense Intimate Juniper Keen Land Land form Leaves Logging Magical Magnificence Magnificent Marine Massif Meteor Migratory
            Mimesis Moon Mountains Mushroom Nascent Native Natural Nature Neglected Nurture Organism Original Pantheism Parasitic Passionate
            Peaceful Peaks Pinnacle Planet Pollutant Popular Prairie Predator Preservation Pristine Productive Protection Quiet Radioactive
            Range Renewable Representation Reproductive Reserve Resilient Resources Restorative Ridge River Rock Rotting Safe Sanctuary
            Sane Scenic Season Sediment Serene Serenity Shelter Shore Smells Snow Solar Soluble Sounds Spatial Splendid Spring Staunch
            Stream Stunning Taint Tarn Temperate Terrain Toxic Tropical Tsunami Typical Ultimate Undeveloped Unique Uplifting Uproot
            Value Variety Versatile Vigilant Visible Vista Volcano Vulnerable Warmth Weather Wildlife Winter Worldwide Xeriscape
            Yielding Zealous Zero-tolerant"""


nat_split = nat_word.split( )

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  cfg = { 
    "consumer_key"        : "code",
    "consumer_secret"     : "code",
    "access_token"        : "code",
    "access_token_secret" : "code" 
    }  

  api = get_api(cfg)
  status = api.update_status(status=tweet)
  print(tweet)
#  print len(tweet)
  print(" ")
  print("Ready for new Tweet!")
  print(" ")

try:
  while True:
#    nature_words()
    data = ser.readline().rstrip()
    data_dec = (data.decode('utf-8'))
    data_dec_s = data_dec.split(":")
    x,y = data_dec_s[0], data_dec_s[1]
    y = int(y)
    if 20 <= y <= 399:
      adj = random.choice(ADJECTIVE)
      img = translate(adj, api_key='api_key')
      print(x, y, adj)
      print(img.url)
      print(img.bitly)
      tweet = "Twitterplanten på NNV: Hjelp! @nordnorskviten " + " Jeg trenger vann med en gang! " + "Tilfeldig gif: " + adj + " " + img.bitly
      main()
    elif y > 400:
        adj2 = random.choice(ADJECTIVE2)
        img2 = translate(adj2, api_key='api_key')
        print(x, y, adj2)
        print(img2.url)
        print(img2.bitly)
        tweet = "Twitterplanten på NNV: Hurra, jeg trenger ikke vann nå! " + "Tilfeldig gif: " + adj2 + " " + img2.bitly
        main()

finally:
    ser.close()
  
