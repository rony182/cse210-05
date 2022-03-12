import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service, player):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._player=player

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if self._player=='player1':
            # left
            if self._keyboard_service.is_key_down('a'):
                self._direction = Point(-constants.CELL_SIZE, 0)
            
            # right
            if self._keyboard_service.is_key_down('d'):
                self._direction = Point(constants.CELL_SIZE, 0)
            
            # up
            if self._keyboard_service.is_key_down('w'):
                self._direction = Point(0, -constants.CELL_SIZE)
            
            # down
            if self._keyboard_service.is_key_down('s'):
                self._direction = Point(0, constants.CELL_SIZE)
            
            snake = cast.get_first_actor("snakes")
            snake.turn_head(self._direction)
            
        if self._player=='player2':
            if self._keyboard_service.is_key_down('j'):
              self._direction = Point(-constants.CELL_SIZE, 0)

            # right
            if self._keyboard_service.is_key_down('l'):
                self._direction = Point(constants.CELL_SIZE, 0)

            # up
            if self._keyboard_service.is_key_down('i'):
                self._direction = Point(0, -constants.CELL_SIZE)

            # down
            if self._keyboard_service.is_key_down('k'):
                self._direction = Point(0, constants.CELL_SIZE)

            snake2 = cast.get_second_actor("snakes")
            snake2.turn_head(self._direction)
            
    
