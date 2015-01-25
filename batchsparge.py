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
from brewconst import *
from extractNeeded import *

def batch_sparge_nums(lbs, v, brew_const=DEF_BREW_CONST):
    """Given the amount of grains to use in pounds and the pre-boil
    volume in gallons this function will return the amount of strike
    water, water to add before first runnings and the amount of sparge
    water to use to get your target volume. In that order."""
    hv = float_div(v,2)
    sw = strike_water(lbs, mash_ratio=brew_const.mash_ratio)

    #Amount of water left after the mash
    am = grain_absorption(sw, lbs)

    #Amount to add before the run off
    #We want to reach half of the target volume.
    br = hv - am

    #if we have more than half of our target volume left
    #then adjust our sparge water
    if br < 0:
        br = 0
        hv = v - am

    return (sw, br, hv)
    

def batch_sparge_info(lbs, v):
    """Given the amount of grains to use in pounds and the pre-boil
    volume in gallons this function will print out the amount of strike
    water, water to add before first runnings and the amount of sparge
    water to use to get your target volume."""

    sw, br, hv = batch_sparge_nums(lbs,v)

    swq = gal_to_qt(sw)
    hvq = gal_to_qt(hv)
    brq = gal_to_qt(br)
    
    t   = sw + hv + br
    tq  = gal_to_qt(t)

    print "You will need %.4f gallons (or %.4f qt) of strike water." % (sw, swq)
    print "You will need to add %.4f gallons (or %.4f qt) of water before the runoff." % (br, brq)
    print "You will need %.4f gallons (or %.4f qt) of sparge water." % (hv, hvq)
    print "Total amount of water needed %.4f gallons (or %.4f qt)" % (t, tq)
                   

def strike_water_temp(lbs,mash_vol,mash_temp, brew_const=DEF_BREW_CONST):
    a = lbs * brew_const.grain_sheat_lbs
    b = mash_vol
    c = a + b
    return ((c * mash_temp) - (a * brew_const.grain_temp)) / b

