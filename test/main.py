#
#  main.py
#  nsdate-chrono
#
#  Created by ento on 3/20/10.
#  Copyright Moonshine Project Corporation 2010. All rights reserved.
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
