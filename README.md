# hotel_project

Introductory project to learn Python.

## Overview

This project is an introduction to Python and object oriented programming. My goals are to gain an understanding of object oriented programming, learn how to effectively use my programming platform (VScode) as well as the language (Python), and to create a basic hotel reservation service. 

## Things I Learned

There were a variety of new concepts that I covered while working on this project, some of which were:

- Object oriented programming
- Creating and reading JSON files
- Command line interfaces
- Programming process
- Basic data structures
- Unit testing
- Source code control

## Future Improvements

- I would like to have used my sub classes more than I did (room, guest, etc) to allow the reservations to provide some of the information for themselves. Having gotten more used to working with objects, looking back I realize that I could have used my classes more effectively.
- Currently when a command is within the input given, it activates even if the input has more characters/words than wanted.   Ex: input: 'find reservation blah blah blah' will still activate the 'find reservation' function
- There are many places in my code where functions or code still remain even if it is not being used so I would like to clean that up for readability and bug fixing purposes.
- Currently when the program is stopped, the reservations and other data are not saved and so when it is restarted, the data from the previous use doesn't load. A working reservation system would need that data to be serialized.

## How to Run

when in the project folder enter 'python3 command.py'
type 'help' for commands when prompted by '>>'