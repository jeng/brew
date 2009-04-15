from brewconv import *

#Most of this information comes from http://www.mrmalty.com/pitching.php

def pitching_rate(sg, vol, yeastType='ale'):
    """Return the number of yeast cells needed for a vol gallon batch
    of wort, with sg starting gravity, and a yeast type of ale or
    lager."""
    ml = gallon_to_liters(vol) * 1000.00
    if yeastType == 'ale':
        cells = 750000 #million
    else:
        cells = 1500000 #million for lagers
    p = sg_to_plato(sg)
    return p * cells * ml

def number_of_yeast_tubes(sg, vol, yeastType='ale'):
    """Return the number of yeast tubes needed based on 100 billion
    viable yeast cells per tube."""
    return pitching_rate(sg, vol, yeastType) / 100000000000

def starter_size(sg, vol, yeastType='ale'):
    """Return the size of the starter in liters."""
    cells = pitching_rate(sg, vol, yeastType)
    scale = int(cells/1000000000)
    if scale in range(0,150):
        return 1
    elif scale in range(150, 200):
        return 2
    elif scale in range(200, 400):
        return 4
    else:
        return 20 #about 5 gallons
    
def grams_dry_yeast(sg, vol, yeastType='ale'):
    """Return the number of grams of dry yeast needed assuming 20
    billion viable cells per gram."""
    return pitching_rate(sg, vol, yeastType) / 20000000000

class Yeast:
    def __init__(self,name, type, liquid, lowTemp=65, highTemp=75):
        self.name = name
        self.type = type
        self.liquid = liquid
        self.lowTemp = lowTemp
        self.highTemp = highTemp

    def cells_needed(self,sg,vol):
        return pitching_rate(sg, vol, yeastType=self.type)

    def amount_needed(self,sg,vol):
        if self.liquid:
            return (number_of_yeast_tubes(sg,vol,yeastType=self.type), starter_size(sg,vol,yeastType=self.type))
        else:
            return (grams_dry_yeast(sg,vol,yeastType=self.type), 0) #no starter for dry yeast

    def __str__(self):
        return self.name

WLP002 = Yeast('English Ale WLP002', 'ale', True)
SAFALE_04 = Yeast('Safale-04', 'ale', False)
COOPERS_ALE = Yeast('Coopers Ale', 'ale', False)

