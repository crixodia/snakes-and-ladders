class Token(object):
    def __init__(self, name: str):
        self.name = name
        self.pos = 1

    def __str__(self) -> str:
        return f"[{self.pos}] {self.name}"
