//
//  NSDate+Chrono.m
//
//  Copyright (c) 2010 ento.
//  See the file license.txt for copying permission.

#import "NSDate+Chrono.h"

static NSDictionary *UnitSeconds()
{
    static NSDictionary *dict = NULL;
    if(dict == NULL)
    {
        dict = [[NSDictionary alloc] initWithObjectsAndKeys:
                [NSNumber numberWithInt:0e100],    [NSNumber numberWithInt:NSEraCalendarUnit],
                [NSNumber numberWithInt:31557600], [NSNumber numberWithInt:NSYearCalendarUnit],
                [NSNumber numberWithInt:2592000],  [NSNumber numberWithInt:NSMonthCalendarUnit],
                [NSNumber numberWithInt:86400],    [NSNumber numberWithInt:NSDayCalendarUnit],
                [NSNumber numberWithInt:3600],     [NSNumber numberWithInt:NSHourCalendarUnit],
                [NSNumber numberWithInt:60],       [NSNumber numberWithInt:NSMinuteCalendarUnit],
                [NSNumber numberWithInt:1],        [NSNumber numberWithInt:NSSecondCalendarUnit],
                [NSNumber numberWithInt:604800],   [NSNumber numberWithInt:NSWeekCalendarUnit],
                [NSNumber numberWithInt:86400],    [NSNumber numberWithInt:NSWeekdayCalendarUnit],
                [NSNumber numberWithInt:604800],   [NSNumber numberWithInt:NSWeekdayOrdinalCalendarUnit],
                nil];
    }
    return [[dict retain] autorelease];
}

static NSArray *ClockUnits()
{
    static NSArray *array = NULL;
    if(array == NULL)
    {
        array = [[NSArray alloc] initWithObjects:
                 [NSNumber numberWithInt:NSYearCalendarUnit],
                 [NSNumber numberWithInt:NSMonthCalendarUnit],
                 [NSNumber numberWithInt:NSDayCalendarUnit],
                 [NSNumber numberWithInt:NSHourCalendarUnit],
                 [NSNumber numberWithInt:NSMinuteCalendarUnit],
                 [NSNumber numberWithInt:NSSecondCalendarUnit],
                 nil];
    }
    return [[array retain] autorelease];
}

NSString* unitToComponentKey(NSCalendarUnit unit) {
    switch (unit) {
        case NSSecondCalendarUnit:
            return @"second";
            break;
        case NSMinuteCalendarUnit:
            return @"minute";
            break;
        case NSHourCalendarUnit:
            return @"hour";
            break;
        case NSDayCalendarUnit:
            return @"day";
            break;
        case NSMonthCalendarUnit:
            return @"month";
            break;
        case NSYearCalendarUnit:
            return @"year";
            break;
        case NSEraCalendarUnit:
            return @"era";
            break;
        case NSWeekCalendarUnit:
            return @"week";
            break;
        case NSWeekdayCalendarUnit:
            return @"weekday";
            break;
        case NSWeekdayOrdinalCalendarUnit:
            return @"weekdayOrdinal";
            break;
        default:
            break;
    }
    return nil; 
}


@implementation NSDate (Chrono)

+ (NSInteger)unitInSecond:(NSCalendarUnit)unit {
    return [(NSNumber*)[UnitSeconds() objectForKey:[NSNumber numberWithInt:unit]] integerValue];
}

- (id)initWithComponents:(int)year, ... {
    int compValue;
    va_list argumentList;
    NSArray *units = ClockUnits();
    NSDateComponents *comps = [[NSDateComponents alloc] init];
    if (year) {            
        [comps setYear:year];
        NSInteger unitIndex = 1;
        va_start(argumentList, year);          // Start scanning for arguments after firstObject.
        while (compValue = va_arg(argumentList, int)) {
            NSString *key = unitToComponentKey([(NSNumber*)[units objectAtIndex:unitIndex] integerValue]);
            [comps setValue:[NSNumber numberWithInt:compValue] forKey:key];
            unitIndex++;
        }
        va_end(argumentList);
    }
    NSDate *theDate = [[NSCalendar currentCalendar] dateFromComponents:comps];
    self = [self initWithTimeIntervalSinceReferenceDate:[theDate timeIntervalSinceReferenceDate]];
    return self;
}

- (NSDate*)later:(NSCalendarUnit)unit {
    return [self later:unit amount:1];
}

- (NSDate*)later:(NSCalendarUnit)unit amount:(NSInteger)amount {
    NSCalendar *calendar = [NSCalendar currentCalendar];
    NSDateComponents *comps = [[[NSDateComponents alloc] init] autorelease];
    [comps setValue:[NSNumber numberWithInteger:amount] forKey:unitToComponentKey(unit)];
    return [calendar dateByAddingComponents:comps toDate:self options:0];
}

- (NSTimeInterval)between:(NSDate*)other {
    return [self between:other unit:NSSecondCalendarUnit];
}

- (NSTimeInterval)between:(NSDate*)other unit:(NSCalendarUnit)unit {
    /*
    NSCalendar *calendar = [NSCalendar currentCalendar];
    NSDateComponents *comps = [calendar components:fullComps
                                          fromDate:self
                                            toDate:other
                                           options:0];
    NSDate *date = [calendar dateFromComponents:comps];
    NSTimeInterval secs = [date timeIntervalSinceReferenceDate];
     */
    //NSTimeInterval secs = abs([self timeIntervalSinceReferenceDate] - [other timeIntervalSinceReferenceDate]);
    NSDate *later = [self laterDate:other];
    NSDate *earlier = [self earlierDate:other];
    NSTimeInterval secs = [later timeIntervalSinceDate:earlier];
    if (unit == NSSecondCalendarUnit) {
        return secs;
    }
    return secs / [NSDate unitInSecond:unit];
}

- (NSDate*)beginningOf:(NSCalendarUnit)unit {
    NSCalendar *calendar = [NSCalendar currentCalendar];
    NSDateComponents *comps = [calendar components:NSYearCalendarUnit | NSMonthCalendarUnit | NSDayCalendarUnit | NSHourCalendarUnit | NSMinuteCalendarUnit | NSSecondCalendarUnit
                                          fromDate:self];
    NSDictionary *unitSeconds = UnitSeconds();
    NSNumber *dropSecs = [unitSeconds objectForKey:[NSNumber numberWithInt:unit]];
    for (NSNumber *clockUnit in ClockUnits()) {
        NSNumber *secs = (NSNumber*)[unitSeconds objectForKey:clockUnit];
        if ([secs integerValue] < [dropSecs integerValue]) {
            NSString *key = unitToComponentKey([clockUnit integerValue]);
            NSInteger zeroValue = 0;
            if ([clockUnit integerValue] == NSDayCalendarUnit || [clockUnit integerValue] == NSMonthCalendarUnit) {
                zeroValue = 1;
            }
            [comps setValue:[NSNumber numberWithInt:zeroValue] forKey:key];
        }
    }
    return [calendar dateFromComponents:comps];
    /*
    NSInteger unitSecs = [NSDate unitInSecond:unit];
    return [NSDate dateWithTimeIntervalSinceReferenceDate:unitSecs * floor([self timeIntervalSinceReferenceDate] / unitSecs)];
     */
}

- (NSInteger)tillNext:(NSCalendarUnit)nextUnit {
    return [self tillNext:nextUnit unit:NSSecondCalendarUnit];
}

- (NSInteger)tillNext:(NSCalendarUnit)nextUnit unit:(NSCalendarUnit)countUnit {
    return [[[self later:nextUnit] beginningOf:nextUnit] between:self unit:countUnit];
}


@end
