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
from grains import *
from ingredients import *

def amount_needed(tg,gal,ppg):
    """Return the amount of material needed for a certain gallon batch,
    with a certain target gravity, given the materials Points per
    Pound per Gallon."""
    gu = sg_to_gu(tg)
    return float_div(gu * gal, ppg)

amount_of_dme_needed = lambda tg, gal: amount_needed(tg, gal, DME_PPG)
amount_of_lme_needed = lambda tg, gal: amount_needed(tg, gal, LME_PPG)

def lbs_needed_by_percent(tg,gal,grains):
   """Taken the target gravity, the gallons of water used for this
    batch, the type of grain and the percentage of the grain to use
    tell me the amount I need in pounds."""
   lbs = []
   gu = sg_to_gu(tg)
   gut = gu * gal #find the total points needed
   for i in grains:
       ig = i.percent * gut #find the Ingredients gravity
       ln = float_div(ig, float(i.grain)) #find the lbs needed
       lbs.append(ln)
    
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


def sg_of_grain_bill(gal,grain_bill):
    """Pass in your grains using the grains name plus the number of
    pounds used. After all the grains are passed in pass the gallons
    of water for the batch.

    Ex. sg_to_grain_bill((TWO_ROW_PALE_ALE_MALT,7),
    (DARK_CRYSTAL_120L, 1.5), 5)"""
    
    tppg = 0
    for i in grain_bill:
        ppg = float(i.grain) * i.lbs
        tppg = tppg + ppg

    return gu_to_sg(float_div(tppg, gal))
