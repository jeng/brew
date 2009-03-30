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
