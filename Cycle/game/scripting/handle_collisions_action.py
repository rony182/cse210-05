import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the other cycle, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (bool): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
            
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments or with the 
        other cycle's.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycles = []
        for i in range(2):
            cycles.append(cast.get_actor("cycles", i))

        heads = []
        segments = []
        for cycle in cycles:
            heads.append(cycle.get_segments()[0])
            segments.append(cycle.get_segments()[1:])
            
        
        for head in heads:
            # Iterate through both Cycle bodies
            for segment in segments:
                # Iterate through whole Cycle body
                for seg in segment:
                    # Check if head and body collide
                    if head.get_position().equals(seg.get_position()):
                        self._is_game_over = True
                        return
 
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycles = cast.get_actors("cycles")
            for cycle in cycles:
                segments = cycle.get_segments()
                cycle.set_color(constants.WHITE)
                for segment in segments:
                    segment.set_color(constants.WHITE)
    
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)
    
    def get_is_game_over(self):
        """Get the game over status.

        Returns:
            bool: whether the game is over or not.
        """
        return self._is_game_over