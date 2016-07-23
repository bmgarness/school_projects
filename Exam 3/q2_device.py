#Exam 3
#Benjamin Garness
#bmg74

class device:

    def __init__(self, device_type, memory, screen_size):
        self.__device_type = device_type
        self.__memory = int(memory)
        self.__screen_size = float(screen_size)

    def __str__(self):
        return '{} has {} GB of memory and its screen is {} inches'.fomat(
            self.__device_type, self.__memory, self.__screen_size
            )

    def get_device_type(self):
        return self.__device_type

    def get_memory(self):
        return self.__memory

    def get_screen_size(self):
        return self.__screen_size

    def set_device_type(self, device_type):
        self.__device_type = device_type

    def set_memory(self, memory):
        if memory < 1:
            self.__memory = 1
        elif memory > 16:
            self.__memory = 16
        else:
            self.__memory = int(memory)

    def set_screen_size(self, screen_size):
        self.__screen_size = float(screen_size)
        
