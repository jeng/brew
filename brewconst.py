# Copyright (c) 2009 Jeremy English <jhe@jeremyenglish.org>

# Permission to use, copy, modify, distribute, and sell this software
# and its documentation for any purpose is hereby granted without fee,
# provided that the above copyright notice appear in all copies and
# that both that copyright notice and this permission notice appear in
# supporting documentation.  No representations are made about the
# suitability of this software for any purpose.  It is provided "as
# is" without express or implied warranty.

# Created: 26-March-2009 

class BrewConst:
    def __init__(self, evph=1, efficiency = 0.65,
            grain_temp = 70, grain_sheat_lbs = 0.05,
            mash_ratio=1.25):
        """ EVPH evaporation rate per hour in gallons. EFFICIENCY efficiency of the brew setup,
            GRAIN_TEMP default room temperature of 70F, GRAIN_SHEAT_LBS Specific heat for 1 pound
            of grain. The default mash ratio is 1.25 qt/lb. You can adjust this for a thicker
            or thinner mash. """
        self.evph = evph
        self.efficiency = efficiency
        self.grain_temp = grain_temp
        self.grain_sheat_lbs = grain_sheat_lbs
        self.mash_ratio = mash_ratio

DEF_BREW_CONST = BrewConst()
