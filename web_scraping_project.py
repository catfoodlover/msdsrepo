# -*- coding: utf-8 -*-
"""
This is my scraping project
"""
from bs4 import BeautifulSoup
import requests
r = requests.get("http://shop.strikezoneonline.com/")
soup = BeautifulSoup(r.content)

print(soup.prettify())

links = soup.find_all('a')
for a in links: 
    print '%s: %s'%(a.text.strip(),a['href'])

r2 = requests.get("http://shop.strikezoneonline.com/Category/Magic_the_Gathering.html")
soup2 = BeautifulSoup(r2.content)

print(soup2.prettify())

links2 = soup2.find_all('a')
for a in links2: 
    print '%s: %s'%(a.text.strip(),a['href'])

rsingles = requests.get("http://shop.strikezoneonline.com/Category/Magic_the_Gathering_Singles.html")
soupsingles = BeautifulSoup(rsingles.content)
print(soupsingles.prettify())

rbuylist = requests.get("http://shop.strikezoneonline.com/Buy_List.html")
soupbuylist = BeautifulSoup(rbuylist.content)
print(soupbuylist.prettify())

rbuylist2 = requests.get("http://shop.strikezoneonline.com/BuyList/Games.html")
soupbuylist2 = BeautifulSoup(rbuylist2.content)
print(soupbuylist2.prettify())

rbuylist3 = requests.get("http://shop.strikezoneonline.com/BuyList/Magic_the_Gathering.html")
soupbuylist3 = BeautifulSoup(rbuylist3.content)
print(soupbuylist3.prettify())

rsingles = requests.get("http://shop.strikezoneonline.com/BuyList/Magic_the_Gathering_Singles.html")
soupsingles = BeautifulSoup(rsingles.content)
print(soupsingles.prettify())

links = soupsingles.find_all('a')
print links
linklist = []

print linklist

for a in links:
    linklist.append((a['href']))



unwanted =['http://shop.strikezoneonline.com/BuyList/Portal.html',
'http://shop.strikezoneonline.com/BuyList/Portal_Second_Age.html',
'http://shop.strikezoneonline.com/BuyList/Portal_Three_Kingdoms.html',
'http://shop.strikezoneonline.com/BuyList/Premium_Deck_Fire_and_Lightning.html',
'http://shop.strikezoneonline.com/BuyList/Premium_Deck_Graveborn.html',
'http://shop.strikezoneonline.com/BuyList/Premium_Deck_Slivers.html',
'http://shop.strikezoneonline.com/BuyList/Promotional_Cards.html',
'http://shop.strikezoneonline.com/BuyList/Unglued.html',
'http://shop.strikezoneonline.com/BuyList/Unhinged.html',
'http://shop.strikezoneonline.com/BuyList/Unlimited.html',
'http://shop.strikezoneonline.com/BuyList/Urza_s_Destiny.html',
'http://shop.strikezoneonline.com/BuyList/Urza_s_Legacy.html',
'http://shop.strikezoneonline.com/BuyList/Urza_s_Saga.html',
'http://shop.strikezoneonline.com/BuyList/Vanguard.html',
'http://shop.strikezoneonline.com/BuyList/Visions.html',
'http://shop.strikezoneonline.com/BuyList/Weatherlight.html',
'http://shop.strikezoneonline.com/BuyList/Torment.html',
'http://shop.strikezoneonline.com/BuyList/Starter_1999.html',
'http://shop.strikezoneonline.com/BuyList/Stronghold.html',
'http://shop.strikezoneonline.com/BuyList/Tempest.html',
'http://shop.strikezoneonline.com/BuyList/The_Dark.html',
'http://shop.strikezoneonline.com/BuyList/Scourge.html',
'http://shop.strikezoneonline.com/BuyList/Revised.html',
'http://shop.strikezoneonline.com/BuyList/Planechase.html',
'http://shop.strikezoneonline.com/BuyList/Planechase_2012.html',
'http://shop.strikezoneonline.com/BuyList/Odyssey.html',
'http://shop.strikezoneonline.com/BuyList/Onslaught.html',
'http://shop.strikezoneonline.com/BuyList/Nemesis.html',
'http://shop.strikezoneonline.com/BuyList/Modern_Event_Deck_2014.html',
'http://shop.strikezoneonline.com/BuyList/Mercadian_Masques.html',
'http://shop.strikezoneonline.com/BuyList/Mirage.html',
'http://shop.strikezoneonline.com/BuyList/Legends.html',
'http://shop.strikezoneonline.com/BuyList/Legions.html',
'http://shop.strikezoneonline.com/BuyList/Judgment.html',
'http://shop.strikezoneonline.com/BuyList/Invasion.html',
'http://shop.strikezoneonline.com/BuyList/Homelands.html',
'http://shop.strikezoneonline.com/BuyList/Ice_Age.html',
'http://shop.strikezoneonline.com/BuyList/From_the_Vault__Angels.html',
'http://shop.strikezoneonline.com/BuyList/From_the_Vault__Annihilation.html',
'http://shop.strikezoneonline.com/BuyList/From_the_Vault__Dragons.html',
'http://shop.strikezoneonline.com/BuyList/From_the_Vault__Exiled.html',
'http://shop.strikezoneonline.com/BuyList/From_the_Vault__Legends.html',
'http://shop.strikezoneonline.com/BuyList/From_the_Vault__Realms.html',
'http://shop.strikezoneonline.com/BuyList/From_the_Vault__Relics.html',
'http://shop.strikezoneonline.com/BuyList/From_the_Vault__Twenty.html',
'http://shop.strikezoneonline.com/BuyList/Exodus.html',
'http://shop.strikezoneonline.com/BuyList/Fallen_Empires.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Ajani_VS_Nicol_Bolas.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Divine_VS_Demonic.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Elspeth_VS_Kiora.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Elspeth_VS_Tezzeret.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Elves_VS_Goblins.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Garruk_VS_Liliana.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Heros_VS_Monsters.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Izzet_VS_Golgari.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Jace_VS_Chandra.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Jace_VS_Vraska.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Knights_VS_Dragons.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Phyrexia_VS_the_Coalition.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Sorin_VS_Tibalt.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Speed_VS_Cunning.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Venser_VS_Koth.html',
'http://shop.strikezoneonline.com/BuyList/Duel_Deck_Zendikar_VS_Eldrazi.html',
'http://shop.strikezoneonline.com/BuyList/Conspiracy.html',
'http://shop.strikezoneonline.com/BuyList/Commander_2013.html',
'http://shop.strikezoneonline.com/BuyList/Commander_2014.html',
'http://shop.strikezoneonline.com/BuyList/Commander_Singles.html',
'http://shop.strikezoneonline.com/BuyList/Commander_s_Arsenal.html',
'http://shop.strikezoneonline.com/BuyList/Chronicles.html',
'http://shop.strikezoneonline.com/BuyList/Beta.html',
'http://shop.strikezoneonline.com/BuyList/Archenemy.html',
'http://shop.strikezoneonline.com/BuyList/Alliances.html',
'http://shop.strikezoneonline.com/BuyList/Alpha.html',
'http://shop.strikezoneonline.com/BuyList/Anthologies.html',
'http://shop.strikezoneonline.com/BuyList/Apocalypse.html',
'http://shop.strikezoneonline.com/BuyList/Magic_the_Gathering.html',
'http://shop.strikezoneonline.com/BuyList/Magic_the_Gathering_Singles.html',
'http://shop.strikezoneonline.com/BuyList/4th_Edition.html',
'http://shop.strikezoneonline.com/BuyList/5th_Edition.html',
'http://shop.strikezoneonline.com/BuyList/Classic_6th_Edition.html',
'http://shop.strikezoneonline.com/BuyList/7th_Edition.html',
'http://shop.strikezoneonline.com/BuyList/Prophecy.html',
'http://shop.strikezoneonline.com/BuyList/Planeshift.html',
'http://shop.strikezoneonline.com/BuyList/Games.html',
'http://shop.strikezoneonline.com/BuyList/Ugin_s_Fate.html',
'/BuyList/Games.html']
 
import re
import pandas as pd
import numpy as np

newlist = []

for dex in range(len(linklist)):
    if re.match('(.*)/BuyList/(.*)',linklist[dex]):
        newlist.append(linklist[dex])

#run this twice
for dex in range(len(unwanted)):
   try:
       newlist.remove(unwanted[dex])
   except:
       pass
   
#gives you a list of the unique links
modernSets = set(newlist)
modernSets = list(modernSets)

print modernSets

columns = ['Name', 'Number', 'Rarity', 'Details', 'Quantity', 'Price', 'Junk']
bigframe = pd.DataFrame(columns = columns)

for i in range(len(modernSets)):
    Msingles = requests.get(modernSets[i])
    Msoupsingles = BeautifulSoup(Msingles.content)
    table = Msoupsingles.find('table', {'class': 'ItemTable'})
    foils = table.find_all('td')
    alldata = []
    for z in foils:
        alldata.append(z.text.strip())

    columns = ['Name', 'Number', 'Rarity', 'Details', 'Quantity', 'Price', 'Junk']
    index = np.arange(len(alldata)/7) # array of numbers for the number of samples
    df = pd.DataFrame(columns=columns, index = index)
    for val, item in enumerate(alldata):
        df.ix[val/7,val%7] = item
        df.drop(df.index[[0]])
    
    bigframe = pd.concat([bigframe, df], axis =0)

bigframe.shape

    

