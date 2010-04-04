#
#  tests.py
#
#  Copyright (c) 2010 ento.
#  See the file license.txt for copying permission.
#

from Foundation import *
import unittest

DateFormatter = NSDateFormatter.alloc().init()

DateFormatter.setDateStyle_(NSDateFormatterShortStyle)
DateFormatter.setTimeStyle_(NSDateFormatterFullStyle)
DateFormatter.setLenient_(True)

def dateFromString(dateString):
    return DateFormatter.dateFromString_(dateString)
    
def asDate(date_or_str):
    if isinstance(date_or_str, basestring):
        return dateFromString(date_or_str)
    return date_or_str
    
class ChronoTestCase(unittest.TestCase):
    def setUp(self):
        self._day_one_string = "11/21/08 11:21:48 AM JST"    
        self.day_one = dateFromString(self._day_one_string)
        self._christmas_string = "12/25/07 03:00:02 AM JST"
        self.christmas = dateFromString(self._christmas_string)
        self._new_years_string = "1/1/08 00:00:00 AM JST"
        self.new_years = dateFromString(self._new_years_string)
        
    def assertEqualDate(self, date_or_str, another_date_or_str):
        self.assertEqual(asDate(date_or_str), asDate(another_date_or_str))

class LaterTestCase(ChronoTestCase):
    def test_hello(self):
        self.assertEqualDate(self.day_one, self._day_one_string)
        self.assertTrue(True)
        
    def test_later_year(self):
        self.assertEqualDate("11/21/09 11:21:48 AM JST",
                             self.day_one.later_amount_(NSYearCalendarUnit, 1))
        
    def test_later_month(self):
        self.assertEqualDate("10/21/08 11:21:48 AM JST",
                             self.day_one.later_amount_(NSMonthCalendarUnit, -1))
        
    def test_later_day(self):
        self.assertEqualDate("11/24/08 11:21:48 AM JST",
                             self.day_one.later_amount_(NSDayCalendarUnit, 3))
        
    def test_later_hour(self):
        self.assertEqualDate("11/21/08 12:21:48 PM JST",
                             self.day_one.later_amount_(NSHourCalendarUnit, 1))
        
    def test_later_minute(self):
        self.assertEqualDate("11/21/08 13:01:48 AM JST",
                             self.day_one.later_amount_(NSMinuteCalendarUnit, 100))
        
    def test_later_second(self):
        self.assertEqualDate("11/21/08 11:21:49 AM JST",
                             self.day_one.later_amount_(NSSecondCalendarUnit, 1))
        
    def test_omit_amount(self):
        self.assertEqualDate(self.christmas.later_(NSSecondCalendarUnit),
                             self.christmas.later_amount_(NSSecondCalendarUnit, 1))
        party = dateFromString("12/31/07 22:00:00 PM JST")
        later_party = dateFromString("12/31/07 23:00:00 PM JST")
        self.assertEqualDate(later_party, party.later_(NSHourCalendarUnit))
        
class BetweenTestCase(ChronoTestCase):
    def test_omit_unit(self):
        start = dateFromString("1/1/09 10:10:10 AM JST")
        end = dateFromString("1/1/09 10:10:15 AM JST")
        self.assertEqual(start.between_(end), 5)
        
    def test_minutes_between(self):
        start = dateFromString("1/1/09 10:10:10 AM JST")
        end = dateFromString("1/1/09 10:20:10 AM JST")
        self.assertEqual(start.between_unit_(end, NSMinuteCalendarUnit), 10)
        
    def test_days_between(self):
        self.assertEqual(int(self.christmas.between_unit_(self.new_years, NSDayCalendarUnit)), 6)
        
    def test_years_between(self):
        start = dateFromString("1/1/2009 10:10:10 AM JST")
        end = dateFromString("1/1/2109 10:10:10 AM JST")
        self.assertEqual(int(start.between_unit_(end, NSYearCalendarUnit)), 99)
        
class BeginningOfTestCase(ChronoTestCase):
    def test_beginning_of_month(self):
        self.assertEqualDate(dateFromString("12/1/07 00:00:00 AM JST"), self.christmas.beginningOf_(NSMonthCalendarUnit))

    def test_beginning_of_day(self):
        self.assertEqualDate(dateFromString("12/25/07 00:00:00 AM JST"), self.christmas.beginningOf_(NSDayCalendarUnit))

    def test_beginning_of_year(self):
        self.assertEqualDate(dateFromString("1/1/07 00:00:00 AM JST"), self.christmas.beginningOf_(NSYearCalendarUnit))

    def test_beginning_of_hour(self):
        self.assertEqualDate(dateFromString("12/25/07 03:00:00 AM JST"), self.christmas.beginningOf_(NSHourCalendarUnit))

    def test_beginning_of_minute(self):
        self.assertEqualDate(dateFromString("12/25/07 03:00:00 AM JST"), self.christmas.beginningOf_(NSMinuteCalendarUnit))

    def test_beginning_of_second(self):
        self.assertEqualDate(dateFromString("12/25/07 03:00:02 AM JST"), self.christmas.beginningOf_(NSSecondCalendarUnit))

class TillNextTestCase(ChronoTestCase):
    #    self._day_one_string = "11/21/08 11:21:48 AM JST"
    def test_second_till_next_second(self):
        self.assertEqual(1, self.day_one.tillNext_unit_(NSSecondCalendarUnit, NSSecondCalendarUnit))

    def test_second_till_next_minute(self):
        self.assertEqual(12, self.day_one.tillNext_unit_(NSMinuteCalendarUnit, NSSecondCalendarUnit))

    def test_minute_till_next_hour(self):
        self.assertEqual(38, self.day_one.tillNext_unit_(NSHourCalendarUnit, NSMinuteCalendarUnit))

    def test_hour_till_next_day(self):
        self.assertEqual(12, self.day_one.tillNext_unit_(NSDayCalendarUnit, NSHourCalendarUnit))

    def test_day_till_next_month(self):
        self.assertEqual(9, self.day_one.tillNext_unit_(NSMonthCalendarUnit, NSDayCalendarUnit))

    def test_day_till_next_year(self):
        self.assertEqual(40, self.day_one.tillNext_unit_(NSYearCalendarUnit, NSDayCalendarUnit))

    def test_second_till_next_minute_no_unit_amount(self):
        self.assertEqual(12, self.day_one.tillNext_(NSMinuteCalendarUnit))
        
class InitWithComponentsTestCase(ChronoTestCase): pass
