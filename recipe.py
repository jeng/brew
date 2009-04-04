from grains import *
from ingredients import *
from batchsparge import *
from extractNeeded import *
from brewconv import *
from hops import *

class Recipe:
    def __init__(self, name="", tg=0.0, boiltime=1, grain_bill=[], vol=5, mash_temp=153, hops=[], yeast=[]):
        self.tg = tg
        self.grain_bill = grain_bill
        self.vol = vol
        self.name = name
        self.boiltime = boiltime
        self.mash_temp = mash_temp
        self.hops = hops
        self.yeast = yeast

    def add_to_grain_bill(self,ingredient):
        self.grain_bill.append(ingredient)

    def add_hops(self,hop):
        self.hops.append(hop)

    def add_yeast(self,yeast):
        self.yeast.append(yeast)

    def set_lbs_by_percent(self):
        """Call this function to set pounds of the grain bill to match
        their percentages."""
        nlbs = lbs_needed_by_percent(self.tg, self.vol, self.grain_bill)
        for i in range(len(nlbs)):
            self.grain_bill[i].lbs = nlbs[i]

    def total_lbs(self):
        tlbs = 0
        for i in self.grain_bill:
            tlbs = i.lbs + tlbs
        return tlbs

    def report(self):
        if len(self.grain_bill) <= 0:
            raise "We needed some grains for the recipe."
    
        trube = 0.5
        
        print self.name
        print "=" * len(self.name)
    

        print "\nRecipe for a %f gallon batch\n" % (self.vol)
    
        print "Grains:"
        print "======="

        if self.grain_bill[0].percent > 0:
            if self.tg == 0:
                raise "When specifing ingredients by percent a target gravity is needed."
            else:
                self.set_lbs_by_percent()
    
        tlbs = self.total_lbs()
        
        for i in self.grain_bill:
            ppg = float(i.grain)
            p = float_div(i.lbs,tlbs) * 100.0
            ps = "%3.3f%s"  % (p, '%')
            lbss = "%.3f" % (i.lbs)
            ozs  = "%5.3f" % (lbs_to_oz(i.lbs))
            print "%s %s %s  %s" % (str(i.grain).ljust(40,' '),
                                    lbss.rjust(7,' ') + ' lbs',
                                    ozs.rjust(9,' ') + ' oz',
                                    ps.rjust(7,' '))
        
        sg = sg_of_grain_bill(self.vol,self.grain_bill)        
        print "\nog: %s (%d Plato)" % (round_sg(sg), sg_to_plato(sg))

        preboil = self.vol + trube + (self.boiltime * EVPH)
        bog = sg_of_grain_bill(preboil, self.grain_bill)
        print "bg: %s (%d Plato) for %f gallons\n" % (round_sg(bog),sg_to_plato(bog),preboil)

        print "Hops:"
        print "====="

        tibu = 0.0
        
        for i in self.hops:
            n = ibu(i.woz, i.hop.aa, bog, i.time, self.vol)
            print "%s IBU %d" %( str(i), n)
            tibu = n + tibu

        print "Total IBUs = %5.3f" % (tibu)

        print "\nYeast:"
        print "======"

        for i in self.yeast:
            print i
            

        sw, br, hv = batch_sparge_nums(tlbs,self.vol)
        print "\nBrewing Instructions:"
        print "========================="
        print "Using the batch sparge method."
        print "Mash at %3.2fF (%3.2fC) until complete." % (self.mash_temp, fah_to_cel(self.mash_temp))
        swt = strike_water_temp(tlbs, sw, self.mash_temp)
        print "Strike water temperature %3.1fF or %3.1fC" % (swt, fah_to_cel(swt))
        print "Pre-Boil Volume: %.3f" % (preboil)
        print "Length of the boil: %.3f hours" % (self.boiltime)
        batch_sparge_info(tlbs, preboil)

        
BrewchezBitter = Recipe(name="Brewchez Bitter", tg=1.044, boiltime=1, vol=5.5, mash_temp=154,
                        grain_bill = [Ingredient(TWO_ROW_PALE_ALE_MALT, percent=0.90),
                                      Ingredient(DARK_CRYSTAL_120L,     percent=0.07),
                                      Ingredient(ROAST_BARLEY,          percent=0.03)],
                        hops = [HopAddition(KENT_GOLDINGS,   1, 60),
                                HopAddition(KENT_GOLDINGS, 0.5, 30),
                                HopAddition(KENT_GOLDINGS, 0.5, 10),
                                HopAddition(KENT_GOLDINGS, 0.25, 1)],
                        yeast = ['WLP002', 'Safale-04'])
    
TittabawaseeBrownAle = Recipe(name="Tittabawasee Brown Ale", tg=1.050, boiltime=1, vol=5, mash_temp=154,
                              grain_bill = [Ingredient(TWO_ROW_PALE_ALE_MALT, percent=0.85),
                                            Ingredient(MEDIUM_CRYSTAL_60L_75L, percent=0.12),
                                            Ingredient(CHOCOLATE_MALT, percent=0.03)],
                              hops = [HopAddition(Hop('Nugget',0.10), 0.5, 60),
                                      HopAddition(Hop('Willamette',0.05), 0.75, 30),
                                      HopAddition(Hop('Willamette',0.05), 0.75, 15)],
                              yeast = ["Coopers Ale", "Yeast Lab Australian Ale"])

GoldenSlumbersBitter = Recipe(name="Golden Slumbers Bitter", tg=1.035, boiltime=1, vol=5, mash_temp=154,
                              grain_bill = [Ingredient(TWO_ROW_PALE_ALE_MALT, lbs=8)],
                              hops = [HopAddition(FUGGLES, 1.00, 60),
                                      HopAddition(FUGGLES, 1.00, 15)],
                              yeast = ["WLP002", "Safale-04"])
                              
