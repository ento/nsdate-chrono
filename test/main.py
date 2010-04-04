#
#  main.py
#
#  Copyright (c) 2010 ento.
#  See the file license.txt for copying permission.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import nsdate_chronoAppDelegate

# pass control to AppKit
AppHelper.runEventLoop()
