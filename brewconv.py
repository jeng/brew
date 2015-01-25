# Copyright (c) 2009 Jeremy English <jhe@jeremyenglish.org>

# Permission to use, copy, modify, distribute, and sell this software
# and its documentation for any purpose is hereby granted without fee,
# provided that the above copyright notice appear in all copies and
# that both that copyright notice and this permission notice appear in
# supporting documentation.  No representations are made about the
# suitability of this software for any purpose.  It is provided "as
# is" without express or implied warranty.

# Created: 26-March-2009 


from decimal import Decimal, ROUND_HALF_UP

def abw(og, fg):
    """Return the amount of alcohol by weight using the original and
    final gravity."""
    return (76.08 * (og-fg))/(1.775-og)


def abv(og, fg):
    """Returns the amount of alcohol by volume using the original and
    final gravity."""
    return abw(og, fg) * (fg / 0.794)

def float_div(n,d):
    """Alway make sure that the denominator is a floating point
    number."""
    return n/float(d)

def gallon_to_oz(gal):
    """Return the number of ounces in a certain number of gallons."""
    return gal * 128

def oz_to_gallon(oz):
    """Convert from ounces to gallons."""
    return float_div(oz,128)

def num_bottles(gal,bs_oz=12):
    """Returns the number of bottles you would need for a batch of so
    many gallons. You can pass the size of the bottles in ounces.  The
    default bottle size is 12oz."""
    return float_div(gallon_to_oz(gal), bs_oz)
	
def gal_left_bottle(gal,nb,bs_oz=12):
    """Returns the amount of liquid you have left after filling nb
    bottles of bs_oz bottle size."""
    return oz_to_gallon(gallon_to_oz(gal) - (nb * bs_oz))

def fah_to_cel(f):
    """Convert from fahrenheit to celsius."""
    return round( (f - 32) * float_div(5,9))

def cel_to_fah(c):
    """Convert from celsius to fahrenheit."""
    return round((c * float_div(9,5)) + 32)

def sg_to_gu(sg):
    """Convert from a specific gravity to a gravity unit."""
    return (sg - 1) * 1000

def gu_to_sg(gu):
    """Convert from a gravity unit to the specific gravity."""
    return float_div(gu,1000) + 1

def sg_to_plato(sg):
    """Convert from specific gravity to plato."""
    return 259 - (259/sg)

def plato_to_sg(plato):
    """Convert from plato to specific gravity."""
    return float_div(259, (259-plato))

def round_to_the(num, place):
    """Rounds a floating point number to a certain degree of
    accuracy. 1 is for ones place, 10 is for the tens place, 100 is
    for the hundreds place, etc."""
    adj = Decimal(str(float_div(1,place)))
    f  = Decimal(str(num)).quantize(adj, ROUND_HALF_UP)
    return f

def round_sg(sg):
    """Return a pretty version of the specific gravity"""
    return str(round_to_the(sg,1000))

def calc_sg_post_boil(v1, v2, og):
    """Calculate your starting gravity after the boil by passing your
    pre-boil volume as v1, your post-poil volume as v2 and the
    original gravity of the wort prior to boiling."""
    gu = float_div(v1, v2) * sg_to_gu(og)
    return gu_to_sg(gu)

def water_weight(gal):
    """Returns the weight of water for so many gallons at 60F or
    15.5C."""
    return gal * 8.338

def grain_absorption(gal,lbs,ar=0.1):
    """Returns the amount of water left after some is absorbed by so
    many pounds of grain. You can pass an absorption rate but the
    default is 0.1."""
    return gal - (lbs * ar)

def qt_to_gal(qt):
    """Convert from quarts to gallons."""
    return float_div(qt,4)

def gal_to_qt(gal):
    """Convert from gallons to quarts."""
    return gal * 4

def strike_water(lbs, mash_ratio=1.25):
    """Returns the amount of strike water, in gallons, that you need
    for a certain amount of grain. The default mash ratio is 1.25
    qt/lb. You can adjust this for a thicker or thinner mash."""
    return qt_to_gal(lbs * mash_ratio)

def hour_to_min(hour):
    return hour * 60

def min_to_hour(min):
    return float_div(min,60)


def lbs_to_oz(lbs):
    return lbs * 16

def oz_to_lbs(oz):
    return float_div(oz,16)

def gallon_to_liters(gal):
    return gal * 3.7854118

def liters_to_gallon(liters):
    return liters/3.7854118
