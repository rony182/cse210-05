# Cycle
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them. You play this game 
on a simulated terminal, with a textual interface.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 snake 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Cicle               (source code for game)
  +-- game              (specific game classes)
        +-- casting
            +-- actor (#)
            +-- cast
            +-- score
            +-- snake
        +-- directing   
            +-- director
        +-- scripting
            +-- action
            +-- control_actors_action
            +-- draw_actors_action
            +-- move_actors_action
            +-- script
        +-- services
            +-- keyboard_service
            +-- video_service
        +-- shared   
            +-- color
            +-- point 
  +-- __main__.py       (entry point for program)
  +-- constants
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* TODO: Add your name and email here
