# Copyright (c) 2009 Jeremy English <jhe@jeremyenglish.org>

# Permission to use, copy, modify, distribute, and sell this software
# and its documentation for any purpose is hereby granted without fee,
# provided that the above copyright notice appear in all copies and
# that both that copyright notice and this permission notice appear in
# supporting documentation.  No representations are made about the
# suitability of this software for any purpose.  It is provided "as
# is" without express or implied warranty.

# Created: 06-April-2009 

from brewconst import *

def typical_ppg(ppg, eff):
    return ppg * eff

class Grain:
    def __init__(self,maxPPG, des, brew_const=DEF_BREW_CONST):
        if not isinstance(brew_const, BrewConst):
            raise TypeError, "brew_const must be an instance of a BrewConst"
        self.ppg = typical_ppg(maxPPG, brew_const.efficiency)
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
TWO_ROW_LAGER_MALT     = Grain( 37, 'Two Row Lager Malt')
SIX_ROW_BASE_MALT      = Grain( 35, 'Six Row Base Malt')
TWO_ROW_PALE_ALE_MALT  = Grain( 38, 'Two Row Pale Ale Malt')
BISCUIT_VICTORY_MALT   = Grain( 35, 'Biscuit Victory Malt')
VIENNA_MALT            = Grain( 35, 'Vienna Malt')
MUNICH_MALT            = Grain( 35, 'Munich Malt')
BROWN_MALT             = Grain( 32, 'Brown Malt')
DEXTRIN_MALT           = Grain( 32, 'Dextrin Malt')
LIGHT_CRYSTAL_10L_15L  = Grain( 35, 'Light Crystal 10l 15l')
PALE_CRYSTAL_25L_40L   = Grain( 34, 'Pale Crystal 25l 40l')
MEDIUM_CRYSTAL_60L_75L = Grain( 34, 'Medium Crystal 60l 75l')
DARK_CRYSTAL_120L      = Grain( 33, 'Dark Crystal 120l')
SPECIAL_B              = Grain( 31, 'Special B')
CHOCOLATE_MALT         = Grain( 28, 'Chocolate Malt')
ROAST_BARLEY           = Grain( 25, 'Roast Barley')
BLACK_PATENT_MALT      = Grain( 25, 'Black Patent Malt')
WHEAT_MALT             = Grain( 37, 'Wheat Malt')
RYE_MALT               = Grain( 29, 'Rye Malt')
OATMEAL_FLAKED         = Grain( 32, 'Oatmeal Flaked')
CORN_FLAKED            = Grain( 39, 'Corn Flaked')
BARLEY_FLAKED          = Grain( 32, 'Barley Flaked')
WHEAT_FLAKED           = Grain( 36, 'Wheat Flaked')
RICE_FLAKED            = Grain( 38, 'Rice Flaked')
MALTO_DEXTRIN_POWDER   = Grain( 40, 'Malto Dextrin Powder')
SUGAR_CORN             = Grain( 46, 'Sugar Corn')
