# Jugaad75   :rocket:

Jugaad + 75   ==   Proxy helper +  Attendance tracker

This is a web app consisting of automatic attendance tracker and proxy helper made in Django.

## Why this project? :bulb:

Eveyone of us has wanted to bunk a few classes during college days but we don't know whether we have enough attendance record for that.
Most of us are lazy in noting down our attendance in course lectures which may lead to less than 75% attendance and even  lower grades.

There are some apps already there to help you track your attendance manually, but let's face it that's a lot of effort.
This webapp solves this problem by making it __automatic__ so you dont need to worry about tracking your attendance count everyday.

Now let's move on to the fun part, marking proxies.
You tell few friends to mark your proxy and after the class you have to ask each one of them if they did or not.
Then there is a problem of more than 1 student marking proxy together and getting caught.
This app has a feature to counter these problems.

## Attendance tracker  :books:
    User need to enroll in a class using its classroom code
    User can update their time table and select lecture's location from map.
    This is an automatic tracker which uses gps in the background to get the users location and 
    checks whether the user is in the lecture or not during that lecture's duration.
    Accordingly the user's attendance record is updates automatically.
    Also manual controls have been provided to icrease/decrease attendance in unusual cases.

## Proxy helper  :boom:
    Present members can see the absentee list and can claim to mark a proxy for a student.
    The student's own attendance record gets updated accordingly and his name is removed from absentee list.
    This model ensures that only one person claims for one absentee.
