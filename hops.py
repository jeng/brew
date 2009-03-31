from brewconv import *
from math import e

def aau(woz, aa):
    """Calculate Alpha Acid Units by using the weight of the hops in
    ounces and the Alpha acid percent. Pass the Alpha Acid percent as
    a floating point number, i.e. 50% = 0.50"""
    return woz * (100 * aa)

def utilization(time,og):
    """Calculate the utilization of a hop by considering it's boil
    time and the gravity of the boil. It's best to use the preboil
    gravity adjusted to the volume of your boil. The time is measured
    in minutes.  For more information see How To Brew by John Palmer
    Ch 5.5."""
    fg = 1.65 * (0.000125**(og-1))
    ft = (1 - e**(-0.04 * time))/4.15
    return fg * ft

def ut_table():
    """Generate a utilization table."""
    ogr = []
    s = "     "
    for og in range(30,130,10):
        tg = float_div(og,1000) + 1
        ogr.append(tg)
        s = s + round_sg(tg) + " "

    print s
    print '-' * len(s)

    for t in range(0,125,5):
        st = str(t).ljust(4,' ') + '|'
        s = st
        for og in ogr:
            s = s + round_sg(utilization(t,og)) + " "
        print s

def ibu(woz, aa, og, time, vol):
    """Calculates the International Bittering Units of a hop
    addition. woz is the weight of the hop in ounces, aa is the Alpha
    Acid percent (this should be a floating point number i.e. 50% =
    0.50), og is the original gravity of the boil, time is the amount
    of time in minutes that this hop will be boiled and vol is the
    volume in gallons of the batch."""
    return float_div(aau(woz,aa) * utilization(time,og) * 74.89, vol)

class HopAddition:
    def __init__(self, hop, woz, time):
        """Create the class by passing in an instance of a hop class,
        the weight in ounces and the length of time(in minutes) to
        boil the hop."""
        self.hop = hop
        self.woz = woz
        self.aau = aau(woz,hop.aa)
        self.time = time

    def __str__(self):
        sn  = self.hop.name.ljust(30,' ')
        so  = '%3.3f oz'   % (self.woz)
        sa  = '%3.3f%s aa' % (self.hop.aa * 100, '%')
        sau = '%5.3f aau'  % (self.aau)
        sm  = '@ %4d min'  % (self.time)
        return '%s %s %s %s %s' % (sn, so.rjust(11,' '), sa.rjust(12,' '),
                                   sau.rjust(14,' '), sm.rjust(11,' '))

class Hop:
    def __init__ (self,name, aa):
        """Pass in the name of the hop and the Alpha Acid percent
        (this should be a floating point number i.e. 50% = 0.50)"""
        self.name = name
        self.aa = aa

AMARILLO              = Hop("Amarillo", 0.095)
AQUILA                = Hop("Aquila", 0.07)
B_C_GOLDINGS          = Hop("B. C. Goldings", 0.05)
BANNER                = Hop("Banner", 0.1)
BRAMLING_CROSS        = Hop("Bramling Cross", 0.065)
BREWERS_GOLD          = Hop("Brewer'S Gold", 0.09)
BULLION               = Hop("Bullion", 0.075)
CASCADE               = Hop("Cascade", 0.06)
CENTENNIAL            = Hop("Centennial", 0.105)
CHALLENGER            = Hop("Challenger", 0.085)
CHINOOK               = Hop("Chinook", 0.13)
CLUSTER               = Hop("Cluster", 0.065)
COLUMBUS              = Hop("Columbus", 0.15)
COMET                 = Hop("Comet", 0.1)
CRYSTAL               = Hop("Crystal", 0.03)
DOMESIC_HALLERTAU     = Hop("Domesic Hallertau", 0.039)
EAST_KENT_GOLDINGS    = Hop("East Kent Goldings", 0.05)
EROICA                = Hop("Eroica", 0.12)
FIRST_GOLD            = Hop("First Gold", 0.075)
FUGGLES               = Hop("Fuggles", 0.048)
GALENA                = Hop("Galena", 0.13)
GLACIER               = Hop("Glacier", 0.055)
GOLDINGS              = Hop("Goldings", 0.05)
HALLERTAU_MITTELFRUH  = Hop("Hallertau Mittelfruh", 0.0375)
HALLERTAU_HERSBRUCKER = Hop("Hallertau Hersbrucker", 0.04)
HERALD                = Hop("Herald", 0.12)
HERSBRUCKER           = Hop("Hersbrucker", 0.04)
HORIZON               = Hop("Horizon", 0.125)
HULLER_BITTERER       = Hop("Huller Bitterer", 0.0575)
KENT_GOLDINGS         = Hop("Kent Goldings", 0.05)
LIBERTY               = Hop("Liberty", 0.04)
LUBLIN                = Hop("Lublin", 0.045)
MAGNUM                = Hop("Magnum", 0.14)
MILLENIUM             = Hop("Millenium", 0.155)
MOUNT_HOOD            = Hop("Mount Hood", 0.05)
NEWPORT               = Hop("Newport", 0.155)
NORTHDOWN             = Hop("Northdown", 0.086)
NORTHERN_BREWER       = Hop("Northern Brewer", 0.085)
NUGGET                = Hop("Nugget", 0.13)
OLYMPIC               = Hop("Olympic", 0.12)
OMEGA                 = Hop("Omega", 0.1)
ORION                 = Hop("Orion", 0.07)
PACIFIC_GEM           = Hop("Pacific Gem", 0.15)
PERLE                 = Hop("Perle", 0.09)
PHOENIX               = Hop("Phoenix", 0.1)
PIONEER               = Hop("Pioneer", 0.09)
PRIDE_OF_RINGWOOD     = Hop("Pride Of Ringwood", 0.1)
PROGRESS              = Hop("Progress", 0.0625)
RECORD                = Hop("Record", 0.065)
SAAZ                  = Hop("Saaz", 0.038)
SANTIAM               = Hop("Santiam", 0.065)
SATUS                 = Hop("Satus", 0.13)
SIMCOE                = Hop("Simcoe", 0.13)
SPALT                 = Hop("Spalt*", 0.045)
STERLING              = Hop("Sterling", 0.055)
STICKLEBRACT          = Hop("Sticklebract", 0.115)
STRISSELSPALT         = Hop("Strisselspalt", 0.035)
STYRIAN_GOLDINGS      = Hop("Styrian Goldings", 0.055)
SUPER_ALPHA           = Hop("Super Alpha", 0.13)
SUPER_STYRIANS        = Hop("Super Styrians", 0.09)
TALISMAN              = Hop("Talisman", 0.08)
TARGET                = Hop("Target", 0.115)
TETTNANGER            = Hop("Tettnanger", 0.045)
TOMAHAWK              = Hop("Tomahawk", 0.15)
ULTRA                 = Hop("Ultra", 0.045)
VANGUARD              = Hop("Vanguard", 0.05)
WARRIOR               = Hop("Warrior", 0.16)
WHITBREAD_GOLDING     = Hop("Whitbread Golding", 0.06)
WILLAMETTE            = Hop("Willamette", 0.055)
WYE_TARGET            = Hop("Wye Target", 0.1)
YAMHILL_GOLDINGS      = Hop("Yamhill Goldings", 0.04)
YAKIMA_CLUSTER        = Hop("Yakima Cluster", 0.07)
YEOMAN                = Hop("Yeoman", 0.0725)
ZENITH                = Hop("Zenith", 0.09)
ZEUS                  = Hop("Zeus", 0.15)
