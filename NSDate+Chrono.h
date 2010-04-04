//
//  NSDate+Chrono.h
//
//  Copyright (c) 2010 ento.
//  See the file license.txt for copying permission.

#import <Foundation/Foundation.h>

NSString* unitToComponentKey(NSCalendarUnit unit);

@interface NSDate (Chrono)

// Port of: (var) units-in-seconds
// Number of seconds in each unit
+ (NSInteger)unitInSecond:(NSCalendarUnit)unit;

// Port of: (NSDate+Chrono specific)
// [[NSDate alloc] initWithComponents: year, month, day, nil];
- (id)initWithComponents:(int)year, ...;

// Port of: (function) later
// Returns a date that is later than the-date by amount units.
// Amount is one if not specified.
- (NSDate*)later:(NSCalendarUnit)unit;
- (NSDate*)later:(NSCalendarUnit)unit amount:(NSInteger)amount;

// Port of: (function) time-between
// How many units between self and other? Units defaults to seconds.
- (NSTimeInterval)between:(NSDate*)other;
- (NSTimeInterval)between:(NSDate*)other unit:(NSCalendarUnit)unit;

// Port of: (function) beginning-of
// Return a date at the beginning of the month, year, day, etc. from self.
- (NSDate*)beginningOf:(NSCalendarUnit)unit;

// Port of: (NSDate+Chrono specific)
// How many units left till next date, later than self by one unit?
// Units to count the time defaults to seconds.
- (NSInteger)tillNext:(NSCalendarUnit)nextUnit;
- (NSInteger)tillNext:(NSCalendarUnit)nextUnit unit:(NSCalendarUnit)countUnit;

@end
