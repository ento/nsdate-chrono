#
#  nsdate_chronoAppDelegate.py
#
#  Copyright (c) 2010 ento.
#  See the file license.txt for copying permission.
#

import unittest
from Foundation import *
from AppKit import *
import tests

class testtest(unittest.TestCase):
    def test_hello(self):
        self.assertTrue(False)
        NSLog("It works!")

class nsdate_chronoAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
        
        suite = unittest.TestLoader().loadTestsFromModule(tests)
        unittest.TextTestRunner(verbosity=2).run(suite)
