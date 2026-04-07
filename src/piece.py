from src.config import SHAPES, COLORS

# --- PIECE CLASS ---
# Represents a falling tetromino
class Piece:
    def __init__(self, x, y, shape_type):
        """
        Initialize a new piece with position, shape, and rotation.
        :param x: initial horizontal position.
        :type x: int.
        :param y: initial vertical position.
        :type y: int.
        :param shape_type: identifier of the piece shape.
        :type shape_type: int.
        :returns: None.
        :rtype: None.
        """
        self.x = x
        self.y = y
        self.shape_type = shape_type
        self.rotation = 0
        self.shape_variants = SHAPES[shape_type]
        self.color = COLORS[shape_type]

    @property
    def shape(self):
        """
        Return the current rotation variant of the piece.
        :param: none.
        :type: none.
        :returns: current shape configuration based on rotation.
        :rtype: list[str].
        """
        return self.shape_variants[self.rotation % len(self.shape_variants)]

    def rotate(self):
        """
        Rotate the piece clockwise.
        :param: none.
        :type: none.
        :returns: None.
        :rtype: None.
        """
        self.rotation = (self.rotation + 1) % len(self.shape_variants)

    def rotate_back(self):
        """
        Rotate the piece counterclockwise to restore the last rotation.
        :param: none.
        :type: none.
        :returns: None.
        :rtype: None.
        """
        self.rotation = (self.rotation - 1) % len(self.shape_variants)