# This is where the information for items will be


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"item: {self.name}, description: {self.description}"

    def __repr__(self):
        return f"{repr(self.name)}"

    def add(self):
        return f"\nYou added the {self.name} to your inventory"

    def drop(self):
        return f"\nYou dropped {self.name}"
