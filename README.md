Author
------
Ryan Wagner
rkwagner@ucsd.edu
http://github.com/rkwagner

Description
-----------
Given a set of notes listed by the user, outputs a sound file that
potentially resembles music.

Strategy
--------
Using the Python "waves" package and a dictionary, reads input to convert
to frequencies to be output by the program.

Dependencies
------------
None

Side Effects
------------
Generates a file named by the user

Sample I/O
----------
$ python mu.py
Filename>zelda
Notes>a#,3,500  f,3,800 r,0,100 a#,3,300 a#,3,300 c,4,200 d,4,200 
d#,4,200 f,4,800 r,0,100 f,4,200 f,4,200 f#,4,200 g#,4,200 a#,4,800 r,0,50 
a#,4,200 a#,4,200 g#,4,200 f#,4,200 g#,4,100 r,0,200 f#,4,200 f,4,800 
f,4,800 d#,4,200 d#,4,200 f,4,200 f#,4,800 f,4,300 d#,4,300 c#,4,200 
c#,4,200 d#,4,200 f,4,600 d#,4,200 c#,4,200 c,4,300 d,4,200 e,4,600 g,4,300
f,4,300 f,3,150 f,3,150 f,3,400 f,3,150 f,3,150 f,3,400 f,3,400 f,3,400

Output: zelda.wav
