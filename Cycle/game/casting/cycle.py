import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A cycle that leaves a trail behind.
    
    The responsibility of Cycle is to move itself.
    """
    def __init__(self, player_color, position, keys):
        """Constructs a new Cycle.

        Args:
            player_color (Color): Player's color.
            position (Point): Player's initial position.
            keys (dict): Dictionary with the movement keys.
        """
        super().__init__()
        self._position = position
        self._segments = []
        self._color = player_color
        self._prepare_body()        
        self.keys = keys
        self.growth = 0

    def get_segments(self):
        """Get the segments of the Cycle.

        Returns:
            list: A list of Actors.
        """
        return self._segments

    def move_next(self):
        """Moves the Cycle."""
        for segment in self._segments:
            segment.move_next()
        
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Gets the head of the Cycle.
        
        Returns:
            Actor: An Actor that represents the head of the Cycle.
        """
        return self._segments[0]

    def grow_trail(self, number_of_segments):
        """Grows the Cycle by the specified 
        number of segments.

        Args:
            number_of_segments (int): Number of segments to add to the Cycle.
        """
        for i in range(number_of_segments):
            self.growth += 1
            trail = self._segments[-1]
            velocity = trail.get_velocity()
            offset = velocity.reverse()
            position = trail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._color)
            if self.growth % 2 == 0:
                self._segments.append(segment)

    def turn_head(self, velocity):
        """Turns the Cycle head by changing
        the velocity.
        """
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """Prepare every segment of the Cycle."""
        x = self._position.get_x()
        y = self._position.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x, y - i * constants.CELL_SIZE)
            velocity = Point(0, 1 * constants.CELL_SIZE)
            text = "5" if i == 0 else "#"

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._color)
            self._segments.append(segment)
