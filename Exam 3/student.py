class Student:
    
    def __init__(self, name, graduation_year, major):
        self.__name = name
        self.__graduation_year = graduation_year
        self.__major = major        
        
    def __str__(self):
        return '{} will graduate in {} with a degree in {}'.format(
            self.__name, self.__graduation_year, self.__major   
        )
        
    def get_name(self):
        return self.__name
        
    def get_graduation_year(self):
        return self.__graduation_year
        
    def get_major(self):
        return self.__major
        
    def set_major(self, major):
        self.__major = major
