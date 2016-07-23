#Benjamin Garness
#CS 0008
#hw 5

class Murder:

    def __init__(self, suspect, victim, weapon, location):
        self.__weapon = weapon
        self.__location = location
        self.__victim = victim
        self.__suspect = suspect

    def __str__(self):
        return 'Victim: {}, Suspect: {}, Weapon: {}, Location: {}'.format(self.__victim, self.__suspect,
                                                                          self.__weapon, self.__location)
    def get_weapon(self):
        return self.__weapon

    def get_location(self):
        return self.__location

    def get_suspect(self):
        return self.__suspect

    def get_victim(self):
        return self.__victim

    def set_weapon(self, weapon):
        self.__weapon = weapon

    def set_location(self, location):
        self.__location = location

    def set_suspect(self, suspect):
        self.__suspect = suspect

    def set_victim(self, victim):
        self.__victim = victim
