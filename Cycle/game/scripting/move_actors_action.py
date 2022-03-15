from game.scripting.action import Action
from game.scripting.handle_collisions_action import HandleCollisionsAction

class MoveActorsAction(Action):
    """An update action that moves all the cycles.
    
        The responsibility of MoveActorsAction is to move all the cycles 
        that have a velocity greater than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cycles = cast.get_actors("cycles")

        for cycle in cycles:
            cycle.move_next()

            # Trails' growth
            # game_over = HandleCollisionsAction().get_is_game_over()
            # if not game_over:
            cycle.grow_trail(1)