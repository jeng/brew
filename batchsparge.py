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
from extractNeeded import *

def batch_sparge_nums(lbs,v):
    """Given the amount of grains to use in pounds and the pre-boil
    volume in gallons this function will return the amount of strike
    water, water to add before first runnings and the amount of sparge
    water to use to get your target volume. In that order."""
    hv = float_div(v,2)
    sw = strike_water(lbs)

    #Amount of water left after the mash
    am = grain_absortion(sw, lbs)

    #Amount to add before the run off
    br = hv - am

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
                   

def recipe_info(name,gal,*grain_bill):
    trube = 0.5
    evph = 1 #evaperation rate per hour
    boiltime = 1 #boil time in hours

    print name
    print "=" * len(name)
    
    tlbs = 0
    print "\nRecipe for a %d gallon batch\n" % (gal)
    
    print "Grains:"
    print "======="
    for i in grain_bill:
        grain,lbs = i
        tlbs = lbs + tlbs
        
    for i in grain_bill:
        grain,lbs = i
        ppg = float(grain)
        p = int(float_div(lbs,tlbs) * 100)
        ps = "%d%s"  % (p, '%')
        lbss = "%.3f" % (lbs)
        print "%s %s %s" % (str(grain).ljust(40,' '), lbss.rjust(7,' '), ps)
        
    sg = sg_of_grain_bill(gal,*grain_bill)
    print "\nog: %s\n" % (round_sg(sg))

    preboil = gal + trube + (boiltime * evph)
    print "Batch Sparge Information"
    print "========================"
    print "Pre-Boil Volume: %.3f" % (preboil)
    batch_sparge_info(tlbs, preboil)
