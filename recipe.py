from grains import *
from ingredients import *
from batchsparge import *
from extractNeeded import *
from brewconv import *

class Recipe:
    def __init__(self, name="", tg=0.0, boiltime=1, grain_bill=[], vol=5, mash_temp=153):
        self.tg = tg
        self.grain_bill = grain_bill
        self.vol = vol
        self.name = name
        self.boiltime = boiltime
        self.mash_temp = mash_temp

    def add_to_grain_bill(self,ingredient):
        self.grain_bill.append(ingredient)

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
            p = int(float_div(i.lbs,tlbs) * 100)
            ps = "%d%s"  % (p, '%')
            lbss = "%.3f" % (i.lbs)
            print "%s %s %s" % (str(i.grain).ljust(40,' '), lbss.rjust(7,' '), ps)
        
        sg = sg_of_grain_bill(self.vol,self.grain_bill)
        print "\nog: %s\n" % (round_sg(sg))

        preboil = self.vol + trube + (self.boiltime * EVPH)
        sw, br, hv = batch_sparge_nums(tlbs,self.vol)
        print "Batch Sparge Information"
        print "========================"
        swt = strike_water_temp(tlbs, sw, self.mash_temp)
        print "Strike water temperature %3.1fF or %3.1fC" % (swt, fah_to_cel(swt))
        print "Pre-Boil Volume: %.3f" % (preboil)
        batch_sparge_info(tlbs, preboil)

        
