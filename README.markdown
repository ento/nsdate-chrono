NSDate+Chrono
===================================

NSDate+Chrono is a port of [incanter-chrono][1] for the Cocoa framework.
incanter-chrono in turn is a wrapper around [Joda Time][2] for clojure.

[1]: http://liebke.github.com/incanter/chrono-api.html
[2]: http://joda-time.sourceforge.net/

Requirements
-----------------------------------

The library is tested under the following operating systems.

 - Snow Leopard (Max OS X 10.6)
 - iPhone OS 3.1.3

It's likely to work under older versions too.

How to use
-----------------------------------

Just add NSDate+Chrono.{h,m} to your project and
import the header where you want to use the API.


Tests
-----------------------------------

Tests are located in the `test` directory.
Open the `test.xcodeproj` with Xcode, run build and debug and
the test results will be output to the console.

All tests are experimentally written in Python, using the
PyObjC bridge.

License
------------------------------------

NSDate+Chrono is distributed under the MIT license.
See `license.txt` for the licensing terms.