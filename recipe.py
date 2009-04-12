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
from grains import *
from ingredients import *
from batchsparge import *
from extractNeeded import *
from brewconv import *
from hops import *
from report import runReport

class Recipe:
    def __init__(self, name="", tg=0.0, boiltime=1, grain_bill=[], vol=5, 
                 mash_temp=153, hops=[], yeast=[], notes=""):
        self.tg = tg
        self.grain_bill = grain_bill
        self.vol = vol
        self.name = name
        self.boiltime = boiltime
        self.mash_temp = mash_temp
        self.hops = hops
        self.yeast = yeast
        self.notes = notes

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
        text = '*%s\n' % (self.name)

        text = text +  "\nRecipe for a %f gallon batch\n" % (self.vol)
    
        text = text + "\n+Grains\n\n"

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
            text = text +  "|%s|%s|%s|%s|\n" % (str(i.grain),
                                                lbss + ' lbs',
                                                ozs + ' oz',
                                                ps)
        
        sg = sg_of_grain_bill(self.vol,self.grain_bill)        
        text = text + "\nog: %s (%d Plato)\n" % (round_sg(sg), sg_to_plato(sg))

        preboil = self.vol + trube + (self.boiltime * EVPH)
        bog = sg_of_grain_bill(preboil, self.grain_bill)
        text = text + "bg: %s (%d Plato) for %f gallons\n" % (round_sg(bog),sg_to_plato(bog),preboil)

        text = text + "\n+Hops\n\n"

        tibu = 0.0
        
        for i in self.hops:
            n = ibu(i.woz, i.hop.aa, bog, i.time, self.vol)
            text = text + "%s IBU|%d|\n" %( str(i), n)
            tibu = n + tibu

        text = text + "Total IBUs = %5.3f\n" % (tibu)

        text = text + "\n+Yeast\n\n"

        for i in self.yeast:
            text = text + i + '\n'
            

        sw, br, hv = batch_sparge_nums(tlbs,self.vol)
        text = text + "\n+Brewing Instructions\n\n"

        swt = strike_water_temp(tlbs, sw, self.mash_temp)
        sw, br, hv = batch_sparge_nums(tlbs,preboil)
        
        swq = gal_to_qt(sw)
        hvq = gal_to_qt(hv)
        brq = gal_to_qt(br)
        
        t   = sw + hv + br
        tq  = gal_to_qt(t)

        text = text +  "You will need %.4f gallons (or %.4f qt) of \
%3.1fF or %3.1fC strike water.\n" % (sw, swq, swt, fah_to_cel(swt))
        text = text + "Mash at %3.2fF (%3.2fC) until complete.\n" % (self.mash_temp, fah_to_cel(self.mash_temp))

        text = text + "\nUsing the batch sparge method.\n"
        text = text +  "You will need to add %.4f gallons \
(or %.4f qt) of water before the runoff.\n" % (br, brq)
        text = text +  "You will need %.4f gallons (or %.4f qt) of sparge water.\n" % (hv, hvq)
        text = text + "\nPre-Boil Volume: %.3f\n" % (preboil)
        text = text + "Length of the boil: %.3f hours\n" % (self.boiltime)

        text = text +  "\nTotal amount of water needed %.4f gallons (or %.4f qt)\n" % (t, tq)
        text = text + "\n+Notes\n\n"

        for i in self.notes.split('\n'):
            text = text + i.strip() + '\n'

        runReport('pdf', text=text, filename='%s.pdf' % (self.name.replace(" ", "-")))
        



