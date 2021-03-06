
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
from recipe import Recipe
from grains import *
from hops import *
from ingredients import *
from yeast import *

BrewchezBitter = Recipe(name="Brewchez Bitter", tg=1.044, boiltime=1, vol=5.5, mash_temp=154,
                        grain_bill = [Ingredient(TWO_ROW_PALE_ALE_MALT, percent=0.90),
                                      Ingredient(DARK_CRYSTAL_120L,     percent=0.07),
                                      Ingredient(ROAST_BARLEY,          percent=0.03)],
                        hops = [HopAddition(KENT_GOLDINGS,   1, 60),
                                HopAddition(KENT_GOLDINGS, 0.5, 30),
                                HopAddition(KENT_GOLDINGS, 0.5, 10),
                                HopAddition(KENT_GOLDINGS, 0.25, 1)],
                        yeast = [WLP002, SAFALE_04])
    
TittabawaseeBrownAle = Recipe(name="Tittabawasee Brown Ale", tg=1.050, boiltime=1, vol=5, mash_temp=154,
                              grain_bill = [Ingredient(TWO_ROW_PALE_ALE_MALT, percent=0.85),
                                            Ingredient(MEDIUM_CRYSTAL_60L_75L, percent=0.12),
                                            Ingredient(CHOCOLATE_MALT, percent=0.03)],
                              hops = [HopAddition(Hop('Nugget',0.10), 0.5, 60),
                                      HopAddition(Hop('Willamette',0.05), 0.75, 30),
                                      HopAddition(Hop('Willamette',0.05), 0.75, 15)],
                              yeast = [COOPERS_ALE, WLP009])

GoldenSlumbersBitter = Recipe(name="Golden Slumbers Bitter", tg=1.035, boiltime=1, vol=5.5, mash_temp=154,
                              grain_bill = [Ingredient(TWO_ROW_PALE_ALE_MALT, lbs=8)],
                              hops = [HopAddition(FUGGLES, 1.00, 60),
                                      HopAddition(FUGGLES, 1.00, 1)],
                              yeast = [WLP002, SAFALE_04],
                              notes ="""This is my first recipe. Trying to be dead simple and to brew a
                              summer bitter. This is also going to be my first all grain brew. Another
                              reason to keep it simple.""")

MooseDrool = Recipe(name="Moose Drool", tg=1.052, boiltime=1.16, vol=3, mash_temp=154,
                    grain_bill = [Ingredient(TWO_ROW_PALE_ALE_MALT, percent=0.8689),
                                  Ingredient(DARK_CRYSTAL_120L, percent=0.1006),
                                  Ingredient(CHOCOLATE_MALT, percent=0.0282),
                                  Ingredient(BLACK_PATENT_MALT, percent=0.0024)],
                    hops = [HopAddition(KENT_GOLDINGS, 0.5, 60),
                            HopAddition(WILLAMETTE, 0.3, 10),
                            HopAddition(LIBERTY, 0.60, 1)],
                    yeast = [WLP002],
                    brew_const = BrewConst(
                           efficiency=0.50,
                           evph=0.5,
                           grain_temp=68,
                           mash_ratio=1),
                    trub=0,
                    notes = """The Can You Brew It recipes follow the same rules as the Previous 
                               Jamil Show recipes and the recipes in Brewing Classic Styles. 70%
                               efficiency, 6 gallons at the end of boil, rager for hops, hop pellets, 
                               etc. All in the book around page 41.""")


AmericanStout = Recipe(name="American Stout", tg=1.063, boiltime=1.16, vol=3, mash_temp=152,
                       grain_bill = [Ingredient(TWO_ROW_PALE_ALE_MALT, percent=0.8235),
                                     Ingredient(ROAST_BARLEY, percent=0.05882),
                                     Ingredient(CHOCOLATE_MALT, percent=0.05882),
                                     Ingredient(MEDIUM_CRYSTAL_60L_75L, percent=0.05882)],
                       hops = [HopAddition(MAGNUM, 0.66, 60),
                               HopAddition(CASCADE, 1, 5)],
                       yeast = [WLP001],
                       brew_const = BrewConst(
                           efficiency=0.50, #Really :|
                           evph=0.5,
                           grain_temp=68,
                           mash_ratio=1),
                       trub=0, #I didn't really have any.  The default was 1 gallon
                       notes ="""
http://www.homebrewtalk.com/f12/jamils-american-stout-397211/

Mash temp hit at about 151 initially. I made a change so that the grain
temperature could be passed in.  The default was 70 but the ambient temp that
day had to be around 67-68.

Also ended up with 4 gallons instead of three.  The evaporation rate and the
amount of trub left over were to high for my setup.  """)


DoubleIPA = Recipe(name="Double IPA",
                       tg=1.090, vol=5, mash_temp=152,
                       grain_bill = [Ingredient(TWO_ROW_PALE_ALE_MALT, percent=0.8169),
                                     Ingredient(MUNICH_MALT, percent=0.0704),
                                     Ingredient(BISCUIT_VICTORY_MALT, percent=0.0563),
                                     Ingredient(DARK_CRYSTAL_120L, percent=0.0282),
                                     Ingredient(MEDIUM_CRYSTAL_60L_75L, percent=0.0282)],
                       hops = [HopAddition(MAGNUM, 1.5, 60),
                               HopAddition(CHINOOK, 1, 30),
                               HopAddition(AMARILLO, 0.5, 20),
                               HopAddition(SIMCOE, 0.5, 20),
                               HopAddition(CITRA, 0.25, 20),
                               HopAddition(EAST_KENT_GOLDINGS, 0.5, 0)],
                       yeast = [WLP001],
                       notes = """Dry-Hop: 1/2 oz. Citra, 1/2 oz. East Kent Goldings, 1/2 oz. Sapphir""")
