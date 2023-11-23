class Snake(object):
    def __init__(self, head: int, tail: int, id: int):
        """
        Initializes a new Snake instance.

        Args:
            head (int): The head position of the snake.
            tail (int): The tail position of the snake.
            id (int): The unique identifier for the snake.
        """
        self.id = id
        self.head = head
        self.tail = tail
