# Battle-ships
Battleships is a terminal game, wich runs in the Code Institute mock terminal on Heroku. In the game you take turns against the computer makng attempts to find, and sink the ships on the opponents board. [Try it out here!](https://battle-ships-by-justin-f9c8a95e0da7.herokuapp.com/)
![A mockup of deployed game](/assets/images/mockup.png)

# How to play
Battleships is a well known elimination game. Both players have ships placed on a board. The objective is to sink all of your oponents ships. You can not see your oponents ships so it is a guessing game. When you hit an opponents ship it is marked on the board with an "x". Misses are marked with an "o".
The winner is the first to sink all the opponents ships.


# Features

* Random ship placement
  - Ships are placed randomly on players and computers board.
  - The ships positions are not visible

![picture of the playing boards](/assets/images/board.png)

  - Play against the computer
  - Accepts user input

* Input validation
  - You can not enter numbers and letters outside of the board size
  - Must enter a letter and a number
  - You can not enter the same guess more than once

![Picture of input validation](/assets/images/Input-validation.png)

## Future Features
* Allow players to select board size and number of ships
* Players can position ships themselves
* Have ships larger than 1 space
* The ability to play against a friend
# Testing
* I passed my code through the PEP8 linter and recieved a few warnings due to trailing white spaces and some extra blank lines. After Some small changes it paassed through without issues
* Tested the input validation by feeding it values outside of the board size and making the same guess twice.
* Tested the game in ide terminal and Code Institues Heroku terminal

## Bugs
* At first i had incorrectly assigned the input placement of a letter first and a number second in the input to the x and y axis on the board so guesses would not show up where they were supposed to. All i had to do was switch the x and y values.
* I forgot to add input validation to stop making the same guess twice. I noticed once i had finished the game, the computer had much fewer registered guesses on the board due to making the same guess twice. I have now added to the input validation so this problem is fixed.

## Deployment
This game was deployed using Code Institutes mock terminal for Heroku

* Steps for deployment
  - Fork or clone the repositry
  - Create a new Heroku app
  - Choose python and nodejs build packs
  - Link the Heroku app to the repositry
  - Click o deploy

## Credits
* Code Institute for the deployment terminal
* Code Institutes Portfolio Project 3 Scope [tutorial](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)
* Marcus Nilson - A friend who has experience as a software developer
