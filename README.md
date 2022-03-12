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

python3 cycle
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
            +-- actor.py
            +-- cast.py
            +-- score.py
            +-- cycle.py
        +-- directing   
            +-- director.py
        +-- scripting
            +-- action.py
            +-- control_actors_action.py
            +-- handle_collisions_action.py
            +-- draw_actors_action.py
            +-- move_actors_action.py
            +-- script.py
        +-- services
            +-- keyboard_service.py
            +-- video_service.py
        +-- shared   
            +-- color.py
            +-- point.py
  +-- __main__.py       (entry point for program)
  +-- constants.py
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors (CSE210 winter 2022: Team 08)
* Kwazeme Ogubie (ogu21006@byui.edu)
* A. Belén Chaparro (cha21065@byui.edu)
* Fabrizio Carlassara (car21101@byui.edu)
* Rony Nickson Calderon Sara (cal21043@byui.edu)
* 
