# cd StigmaBuild
# .py

# regular


# This class is the one responsible for holding data on main screen
class StigmaBuild:
    def __init__(self, character_class, level):
        self.character_class = character_class
        self.level = level
        self.slots = [None] * 12


    def set_class(self):
        new_class = input("Choose class here: ")
        self.character_class = new_class

    #add limit from 20 to 65
    def set_level(self):
        new_level = int(input("Set level here: "))
        self.level = new_level


    def add_stigma(self):

        first_free_slot = self.first_free_current_slot()

        add_stigma = input("Stigma name: ")
        self.slots[first_free_slot] = add_stigma

        
    # нужно выяснить какой ближайший индекс этого говна свободен чтобы запиздячить туда стигму
    def first_free_current_slot(self):
        for index in range(len(self.slots)):
            if self.slots[index] is None:
                print("Here's your first free to put stigma")
                return index


    def __str__(self):
        return f"""
        {self.character_class}
        {self.level}
        {self.slots}
        """