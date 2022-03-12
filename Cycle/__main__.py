import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.score import Score2
from game.casting.snake import Snake

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("snakes", Snake(constants.BLUE))
    cast.add_actor("scores", Score())
    cast.add_actor("snakes", Snake(constants.RED))
    cast.add_actor("scores", Score2())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service, 'player1'))
    script.add_action("input", ControlActorsAction(keyboard_service, 'player2'))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)
    


if __name__ == "__main__":
    main()
