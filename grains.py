from brewconst import *

def typical_ppg(ppg,eff=MY_EFFICIENCY):
    return ppg * eff

class Grains:
    def __init__(self,maxPPG, des):
        self.ppg = typical_ppg(maxPPG)
        self.des = des

    def __str__(self):
        return self.des

    def __int__(self):
        return int(self.ppg)
        
    def __float__(self):
        return self.ppg

DME_PPG = 42
LME_PPG = 36
LAGER_MALT_PPG = 37
WILLIAMSON_AMERICAN_PALE_DME = 32 #That is about what I recived with
                                  #the last batch
TWO_ROW_LAGER_MALT     = Grains( 37, 'Two Row Lager Malt')
SIX_ROW_BASE_MALT      = Grains( 35, 'Six Row Base Malt')
TWO_ROW_PALE_ALE_MALT  = Grains( 38, 'Two Row Pale Ale Malt')
BISCUIT_VICTORY_MALT   = Grains( 35, 'Biscuit Victory Malt')
VIENNA_MALT            = Grains( 35, 'Vienna Malt')
MUNICH_MALT            = Grains( 35, 'Munich Malt')
BROWN_MALT             = Grains( 32, 'Brown Malt')
DEXTRIN_MALT           = Grains( 32, 'Dextrin Malt')
LIGHT_CRYSTAL_10L_15L  = Grains( 35, 'Light Crystal 10l 15l')
PALE_CRYSTAL_25L_40L   = Grains( 34, 'Pale Crystal 25l 40l')
MEDIUM_CRYSTAL_60L_75L = Grains( 34, 'Medium Crystal 60l 75l')
DARK_CRYSTAL_120L      = Grains( 33, 'Dark Crystal 120l')
SPECIAL_B              = Grains( 31, 'Special B')
CHOCOLATE_MALT         = Grains( 28, 'Chocolate Malt')
ROAST_BARLEY           = Grains( 25, 'Roast Barley')
BLACK_PATENT_MALT      = Grains( 25, 'Black Patent Malt')
WHEAT_MALT             = Grains( 37, 'Wheat Malt')
RYE_MALT               = Grains( 29, 'Rye Malt')
OATMEAL_FLAKED         = Grains( 32, 'Oatmeal Flaked')
CORN_FLAKED            = Grains( 39, 'Corn Flaked')
BARLEY_FLAKED          = Grains( 32, 'Barley Flaked')
WHEAT_FLAKED           = Grains( 36, 'Wheat Flaked')
RICE_FLAKED            = Grains( 38, 'Rice Flaked')
MALTO_DEXTRIN_POWDER   = Grains( 40, 'Malto Dextrin Powder')
SUGAR_CORN             = Grains( 46, 'Sugar Corn')
