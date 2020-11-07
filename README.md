# Jugaad75   :rocket:

Jugaad + 75   ==   Proxy helper +  Attendance tracker

This is a web app consisting of automatic attendance tracker and proxy helper made in Django.

## Application in Today's World  :bulb:

Most of us are lazy in noting down our attendance in course lectures which may lead to less than 75% attendance and even  lower grades.

Even many apps are already there but no one solves the problem by making it __automatic__ .
This webapp solves this problem and you dont need to care about tracking your attendance count .

It has also additional features which can solve all the edge cases in our attendance even proxies and changed venue of lectures.


## Attendance tracker  :books:
    User need to enroll in a class using its classroom code
    User can update their time table and select lecture's location from map.
    This is an automatic tracker which uses gps in the background to get the users location and check whether the user is in the lecture or not during that lecture's duration.
    Lecture wise attendance going on can be viewed. 
    Provided manual control in cases of unusual cases of scheduling of lectures.
    

## Proxy helper  :boom:
    Present members can see the absentee list and can claim for marking proxy for them.
    Proxy helps to increse the attendance of absentee.
    Our Model ensures that only one person claims for one absentee.
    Provided manual control in cases of proxy not sucessfull.
