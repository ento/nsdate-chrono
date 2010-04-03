//
//  NSDate+Chrono.h
//  app
//
//  Created by ento on 3/14/10.
//  Copyright 2010 Moonshine Project Corporation. All rights reserved.
//

#import <Foundation/Foundation.h>

NSString* unitToComponentKey(NSCalendarUnit unit);

@interface NSDate (Chrono)
+ (NSInteger)unitInSecond:(NSCalendarUnit)unit;
- (id)initWithComponents:(int)year, ...;
- (NSDate*)later:(NSCalendarUnit)unit;
- (NSDate*)later:(NSCalendarUnit)unit amount:(NSInteger)amount;
- (NSTimeInterval)between:(NSDate*)other;
- (NSTimeInterval)between:(NSDate*)other unit:(NSCalendarUnit)unit;
- (NSDate*)beginningOf:(NSCalendarUnit)unit;

- (NSInteger)tillNext:(NSCalendarUnit)nextUnit;
- (NSInteger)tillNext:(NSCalendarUnit)nextUnit unit:(NSCalendarUnit)countUnit;

@end