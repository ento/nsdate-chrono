#
#  nsdate_chronoAppDelegate.py
#  nsdate-chrono
#
#  Created by ento on 3/20/10.
#  Copyright Moonshine Project Corporation 2010. All rights reserved.
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
