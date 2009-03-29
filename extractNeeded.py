# Copyright (c) 2009 Jeremy English <jhe@jeremyenglish.org>

# Permission to use, copy, modify, distribute, and sell this software
# and its documentation for any purpose is hereby granted without fee,
# provided that the above copyright notice appear in all copies and
# that both that copyright notice and this permission notice appear in
# supporting documentation.  No representations are made about the
# suitability of this software for any purpose.  It is provided "as
# is" without express or implied warranty.

# Created: 26-March-2009 

from brewconv import *

MY_EFFICIENCY = 0.70

DME_PPG = 42
LME_PPG = 36
LAGER_MALT_PPG = 37
WILLIAMSON_AMERICAN_PALE_DME = 32 #That is about what I recived with
                                  #the last batch

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


def amount_needed(tg,gal,ppg):
    """Return the amount of material needed for a certain gallon batch,
    with a certain target gravity, given the materials Points per
    Pound per Gallon."""
    gu = sg_to_gu(tg)
    return float_div(gu * gal, ppg)

amount_of_dme_needed = lambda tg, gal: amount_needed(tg, gal, DME_PPG)
amount_of_lme_needed = lambda tg, gal: amount_needed(tg, gal, LME_PPG)

def lbs_needed_by_percent(tg,gal,*grains):
   """Taken the target gravity, the gallons of water used for this
    batch, the type of grain and the percentage of the grain to use
    tell me the amount I need in pounds."""
   lbs = []
   gu = sg_to_gu(tg)
   for i in grains:
       grain,percent = i
#       pgu = gu * percent
#       n = amount_needed(gu_to_sg(pgu), gal, float(grain))
       n = amount_needed(tg, gal, float(grain))
       lbs.append(n * percent)
    
   return lbs

def points_pound_gallon(og, gal, lbs):
    """Return the Points per Pound per Gallon of a batch with an
    original gravity of og, gal gallons and lbs pounds of material."""
    gu = sg_to_gu(og)
    return  float_div(gu * gal, lbs)

def mash_efficiency(*args):
    """Calculate the efficiency of your mash by passing the ppg for
    your batch or the original gravity, gallons and pounds of
    materials."""
    assert 1 == len(args) or len(args) == 3
    if len(args) == 1:
        #calculate using ppg
        ppg = args[0]
    else:
        og  = args[0]
        gal = args[1]
        lbs = args[2]
        ppg = points_pound_gallon(og,gal,lbs)

    return float_div(ppg,LAGER_MALT_PPG)

def print_percent(f):
    n = int(round_to_the(f,100) * 100)
    return "%d%s" % (n,'%')


def sg_of_grain_bill(gal,*grain_bill):
    """Pass in your grains using the grains name plus the number of
    pounds used. After all the grains are passed in pass the gallons
    of water for the batch.

    Ex. sg_to_grain_bill((TWO_ROW_PALE_ALE_MALT,7),
    (DARK_CRYSTAL_120L, 1.5), 5)"""
    
    tp   = 0
    tlbs = 0
    for i in grain_bill:
        grain,lbs = i
        ppg = float(grain)
        tppg = ppg
        tp = tp + (tppg * lbs)
        tlbs = tlbs + lbs

    avppg = float_div(tp,tlbs)

    return gu_to_sg(float_div(tlbs * avppg, gal))
