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

#Dry Yeast
SAFALE_04 = Yeast('Safale-04', 'ale', False, lowTemp=68, highTemp=74)
COOPERS_ALE = Yeast('Coopers Ale', 'ale', False)

# White labs yeast as of 15-April-2009 
#Liquid Ale Yeast
WLP001 = Yeast('California Ale WLP001', 'ale', True, lowTemp= 68, highTemp=73)
WLP002 = Yeast('English Ale WLP002', 'ale', True, lowTemp= 65, highTemp=68)
WLP004 = Yeast('Irish Ale WLP004', 'ale', True, lowTemp= 65, highTemp=68)
WLP005 = Yeast('British Ale WLP005', 'ale', True, lowTemp= 65, highTemp=70)
WLP006 = Yeast('Bedford WLP006', 'ale', True, lowTemp= 65, highTemp=70)
WLP007 = Yeast('Dry English Ale WLP007', 'ale', True, lowTemp= 65, highTemp=70)
WLP008 = Yeast('East Coast Ale WLP008', 'ale', True, lowTemp= 68, highTemp=73)
WLP009 = Yeast('Australian Ale WLP009', 'ale', True, lowTemp= 65, highTemp=70)
WLP011 = Yeast('European Ale WLP011', 'ale', True, lowTemp= 65, highTemp=70)
WLP013 = Yeast('London Ale WLP013', 'ale', True, lowTemp= 66, highTemp=71)
WLP022 = Yeast('Essex Ale WLP022', 'ale', True, lowTemp= 66, highTemp=70)
WLP023 = Yeast('Burton Ale WLP023', 'ale', True, lowTemp= 68, highTemp=73)
WLP026 = Yeast('Premium Bitter Ale WLP026', 'ale', True, lowTemp= 67, highTemp=70)
WLP028 = Yeast('Edinburgh Scottish Ale WLP028', 'ale', True, lowTemp= 65, highTemp=70)
WLP029 = Yeast('German Ale/ Kolsch WLP029', 'ale', True, lowTemp= 65, highTemp=69)
WLP036 = Yeast('Dusseldorf Alt WLP036', 'ale', True, lowTemp= 65, highTemp=69)
WLP037 = Yeast('Yorkshire Square Ale WLP037', 'ale', True, lowTemp= 65, highTemp=7)
WLP038 = Yeast('Manchester Ale WLP038', 'ale', True, lowTemp= 65, highTemp=7)
WLP039 = Yeast('Nottingham Ale WLP039', 'ale', True, lowTemp= 66, highTemp=70)
WLP041 = Yeast('Pacific Ale WLP041', 'ale', True, lowTemp= 65, highTemp=68)
WLP051 = Yeast('California Ale V WLP051', 'ale', True, lowTemp= 66, highTemp=70)
WLP060 = Yeast('American Ale Yeast WLP060', 'ale', True, lowTemp= 68, highTemp=72)
WLP072 = Yeast('French WLP072', 'ale', True, lowTemp= 63, highTemp=73)
WLP080 = Yeast('Cream Ale Blend WLP080', 'ale', True, lowTemp= 65, highTemp=70)
WLP099 = Yeast('Super High Gravity Ale WLP099', 'ale', True, lowTemp= 65, highTemp=69)
WLP300 = Yeast('Hefeweizen Ale WLP300', 'ale', True, lowTemp= 68, highTemp=72)
WLP320 = Yeast('American Hefeweizen Ale WLP320', 'ale', True, lowTemp= 65, highTemp=69)
WLP351 = Yeast('Bavarian Weizen WLP351', 'ale', True, lowTemp= 66, highTemp=70)
WLP380 = Yeast('Hefeweizen IV Ale WLP380', 'ale', True, lowTemp= 66, highTemp=70)
WLP400 = Yeast('Belgian Wit Ale WLP400', 'ale', True, lowTemp= 67, highTemp=74)
WLP410 = Yeast('Belgian Wit II Ale WLP410', 'ale', True, lowTemp= 67, highTemp=74)
WLP500 = Yeast('Trappist Ale WLP500', 'ale', True, lowTemp= 65, highTemp=72)
WLP510 = Yeast('Belgian Bastogne Ale WLP510', 'ale', True, lowTemp= 66, highTemp=72)
WLP515 = Yeast('Antwerp Ale WLP515', 'ale', True, lowTemp= 67, highTemp=70)
WLP530 = Yeast('Abbey Ale WLP530', 'ale', True, lowTemp= 66, highTemp=72)
WLP540 = Yeast('Abbey IV Ale WLP540', 'ale', True, lowTemp= 66, highTemp=72)
WLP545 = Yeast('Belgian Strong Ale WLP545', 'ale', True, lowTemp= 66, highTemp=7)
WLP550 = Yeast('Belgian Ale WLP550', 'ale', True, lowTemp= 68, highTemp=78)
WLP565 = Yeast('Belgian Saison I WLP565', 'ale', True, lowTemp= 68, highTemp=75)
WLP566 = Yeast('Belgian Saison II WLP566', 'ale', True, lowTemp= 68, highTemp=78)
WLP568 = Yeast('Belgian Style Saison Ale Blend WLP568', 'ale', True, lowTemp= 70, highTemp=80)
WLP570 = Yeast('Belgian Golden Ale WLP570', 'ale', True, lowTemp= 68, highTemp=75)
WLP575 = Yeast('Belgian Style Ale Yeast WLP575', 'ale', True, lowTemp= 68, highTemp=75)

#Liquid Wine Mead Cider
WLP700 = Yeast('Flor Sherry WLP700', 'ale', True, lowTemp=70, highTemp=100)
WLP705 = Yeast('Sake WLP705', 'ale', True, lowTemp=70 , highTemp=100)
WLP715 = Yeast('Champagne WLP715', 'ale', True, lowTemp= 70, highTemp=75)
WLP718 = Yeast('Avize Wine WLP718', 'ale', True, lowTemp= 60, highTemp=90)
WLP720 = Yeast('Sweet Mead/Wine WLP720', 'ale', True, lowTemp= 70, highTemp=75)
WLP727 = Yeast('Steinberg-Geisenheim Wine WLP727', 'ale', True, lowTemp= 50, highTemp=90)
WLP730 = Yeast('Chardonnay White Wine WLP730', 'ale', True, lowTemp= 50, highTemp=90)
WLP735 = Yeast('French White Wine WLP735', 'ale', True, lowTemp= 60, highTemp=90)
WLP740 = Yeast('Merlot Red Wine WLP740', 'ale', True, lowTemp= 60, highTemp=90)
WLP749 = Yeast('Assmanshausen Wine WLP749', 'ale', True, lowTemp= 50, highTemp=90)
WLP750 = Yeast('French Red Wine WLP750', 'ale', True, lowTemp= 60, highTemp=90)
WLP760 = Yeast('Cabernet Red Wine WLP760', 'ale', True, lowTemp= 60, highTemp=90)
WLP770 = Yeast('Suremain Burgundy Wine WLP770', 'ale', True, lowTemp= 60, highTemp=90)
WLP775 = Yeast('English Cider WLP775', 'ale', True, lowTemp= 68, highTemp=75)

#Liquid Lager 
WLP800 = Yeast('Pilsner Lager WLP800', 'lager', True, lowTemp= 50, highTemp=55)
WLP802 = Yeast('Czech Budejovice Lager WLP802', 'lager', True, lowTemp= 50, highTemp=55)
WLP810 = Yeast('San Francisco Lager WLP810', 'lager', True, lowTemp= 58, highTemp=65)
WLP820 = Yeast('Oktoberfest/Marzen Lager WLP820', 'lager', True, lowTemp= 52, highTemp=58)
WLP830 = Yeast('German Lager WLP830', 'lager', True, lowTemp= 50, highTemp=55)
WLP833 = Yeast('German Bock Lager WLP833', 'lager', True, lowTemp= 48, highTemp=55)
WLP838 = Yeast('Southern German Lager WLP838', 'lager', True, lowTemp= 50, highTemp=55)
WLP840 = Yeast('American Lager WLP840', 'lager', True, lowTemp= 50, highTemp=55)
WLP862 = Yeast('Cry WLP862', 'lager', True, lowTemp= 68, highTemp=74)
WLP885 = Yeast('Zurich Lager WLP885', 'lager', True, lowTemp= 50, highTemp=55)
WLP940 = Yeast('Mexican Lager WLP940', 'lager', True, lowTemp= 50, highTemp=55)

#Wyeast as of 15-April-2009 
WYEAST_1272  = Yeast('American Ale II', 'ale', True, lowTemp= 60, highTemp=72)
WYEAST_1010  = Yeast('American Wheat', 'ale', True, lowTemp= 58, highTemp=74)
WYEAST_1214  = Yeast('Belgian Ale', 'ale', True, lowTemp= 68, highTemp=78)
WYEAST_1388  = Yeast('Belgian Strong Ale', 'ale', True, lowTemp= 64, highTemp=80)
WYEAST_3278  = Yeast('Belgian Lambic Blend', 'ale', True, lowTemp= 63, highTemp=75)
WYEAST_1762  = Yeast('Belgian Abby Ale II', 'ale', True, lowTemp= 65, highTemp=75)
WYEAST_2112  = Yeast('California Lager', 'ale', True, lowTemp= 58, highTemp=68)
WYEAST_2206  = Yeast('Bavarian Lager', 'ale', True, lowTemp= 46, highTemp=58)
WYEAST_2308  = Yeast('Munich Lager', 'ale', True, lowTemp= 48, highTemp=56)
WYEAST_2633  = Yeast('Octoberfest Lager Blend', 'ale', True, lowTemp= 48, highTemp=58)
WYEAST_3068  = Yeast('Weihenstephan Weizen', 'ale', True, lowTemp= 64, highTemp=75)
WYEAST_3522  = Yeast('Belgian Ardennes', 'ale', True, lowTemp= 65, highTemp=85)
WYEAST_3942  = Yeast('Belgian Wheat', 'ale', True, lowTemp= 64, highTemp=74)
WYEAST_1275  = Yeast('Thames Valley Ale', 'ale', True, lowTemp= 62, highTemp=72)
WYEAST_1332  = Yeast('Northwest Ale', 'ale', True, lowTemp= 65, highTemp=75)
WYEAST_1318  = Yeast('London Ale III', 'ale', True, lowTemp= 64, highTemp=74)
WYEAST_1335  = Yeast('British Ale II', 'ale', True, lowTemp= 63, highTemp=75)
WYEAST_1338  = Yeast('European Ale', 'ale', True, lowTemp= 62, highTemp=72)
WYEAST_1728  = Yeast('Scottish Ale', 'ale', True, lowTemp= 55, highTemp=75)
WYEAST_2565  = Yeast('Klsch', 'ale', True, lowTemp= 56, highTemp=70)
WYEAST_5112  = Yeast('Brettanomyces bruxellensis', 'ale', True, lowTemp= 60, highTemp=75)
WYEAST_5526  = Yeast('Brettanomyces lambicus', 'ale', True, lowTemp= 60, highTemp=75)
WYEAST_5335  = Yeast('Lactobacillus', 'ale', True, lowTemp= 60, highTemp=95)
WYEAST_5733  = Yeast('Pediococcus', 'ale', True, lowTemp= 60, highTemp=95)
WYEAST_1007  = Yeast('German Ale', 'ale', True, lowTemp= 55, highTemp=68)
WYEAST_1968  = Yeast('London ESB Ale', 'ale', True, lowTemp= 64, highTemp=72)
WYEAST_2000  = Yeast('Budvar Lager', 'lager', True, lowTemp= 48, highTemp=56)
WYEAST_2001  = Yeast('Urquell Lager', 'lager', True, lowTemp= 48, highTemp=58)
WYEAST_2007  = Yeast('Pilsen Lager', 'lager', True, lowTemp= 48, highTemp=56)
WYEAST_2035  = Yeast('American Lager', 'lager', True, lowTemp= 48, highTemp=58)
WYEAST_2042  = Yeast('Danish Lager', 'lager', True, lowTemp= 46, highTemp=56)
WYEAST_2124  = Yeast('Bohemian Lager', 'lager', True, lowTemp= 48, highTemp=58)
WYEAST_2278  = Yeast('Czech Pils ', 'lager', True, lowTemp= 50, highTemp=58)
WYEAST_1028  = Yeast('London Ale', 'ale', True, lowTemp= 60, highTemp=72)
WYEAST_3056  = Yeast('Bavarian Wheat Blend', 'ale', True, lowTemp= 64, highTemp=74)
WYEAST_1056  = Yeast('American Ale', 'ale', True, lowTemp= 60, highTemp=72)
WYEAST_3333  = Yeast('German Wheat', 'ale', True, lowTemp= 63, highTemp=75)
WYEAST_3638  = Yeast('Bavarian Wheat', 'ale', True, lowTemp= 64, highTemp=75)
WYEAST_1084  = Yeast('Irish Ale', 'ale', True, lowTemp= 62, highTemp=72)
WYEAST_3724  = Yeast('Belgian Saison', 'ale', True, lowTemp= 70, highTemp=95)
WYEAST_3787  = Yeast('Trappist High Gravity', 'ale', True, lowTemp= 64, highTemp=78)
WYEAST_3944  = Yeast('Belgian Witbier', 'ale', True, lowTemp= 62, highTemp=75)
WYEAST_1098  = Yeast('British Ale', 'ale', True, lowTemp= 64, highTemp=72)
WYEAST_1099  = Yeast('Whitbread Ale', 'ale', True, lowTemp= 64, highTemp=75)
WYEAST_1187  = Yeast('Ringwood Ale', 'ale', True, lowTemp= 64, highTemp=74)
