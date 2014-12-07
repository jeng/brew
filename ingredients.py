# Copyright (c) 2009 Jeremy English <jhe@jeremyenglish.org>

# Permission to use, copy, modify, distribute, and sell this software
# and its documentation for any purpose is hereby granted without fee,
# provided that the above copyright notice appear in all copies and
# that both that copyright notice and this permission notice appear in
# supporting documentation.  No representations are made about the
# suitability of this software for any purpose.  It is provided "as
# is" without express or implied warranty.

# Created: 06-April-2009 

from grains import *

class Ingredient:
    """Class used to define the ingredients (grains) for a recipe.
    When creating the ingredient you can specify the amounts in
    prectange or poinds."""
    def __init__(self, grain, percent=0.0, lbs=0):
        if not isinstance(grain, Grains):
            raise TypeError, "grain must be an instance of a Grain object."
        self.grain = grain
        self.percent = percent
        self.lbs = lbs
