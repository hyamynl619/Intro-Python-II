# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self. description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.contents = []

    def __str__(self):
        return f"\nname:{self.name}\ndescription: {self.description}\n"

    def __repr__(self):
        return f"\nRoom({repr(self.name), repr(self.description)})"
