import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
        _direction (Point): An instance of Point.
        _player: An instance of Cycle.
    """

    def __init__(self, keyboard_service, player):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._player = player

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if self._keyboard_service.is_key_down(self._player.keys["left"]):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        if self._keyboard_service.is_key_down(self._player.keys["right"]):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        if self._keyboard_service.is_key_down(self._player.keys["up"]):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        if self._keyboard_service.is_key_down(self._player.keys["down"]):
            self._direction = Point(0, constants.CELL_SIZE)
        
        self._player.turn_head(self._direction)
