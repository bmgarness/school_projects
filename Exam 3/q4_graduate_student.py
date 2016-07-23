#Exam 3
#Benjamin Garness
#bmg74

import student

class GraduateStudent(student.Student):

    def __init__(self, name, graduation_year, major, thesis_title, advisor):

        super().__init__(name, graduation_year, major)
        self.__thesis_title = thesis_title
        self.__advisor = advisor

    def __str__(self):
        response = super().__str__()
        response += ' is advised by {} and is researching {}'.format(
            self.__advisor, self.__thesis_title
            )
        return response

    def get_thesis_title(self):
        return self.__thesis_title

    def get_advisor(self):
        return self.__advisor


def main():
    grad_list = [GraduateStudent('Ben', '2016', 'Math', 'I am very smart', 'Your Mom'),
                 GraduateStudent('Max', '2015', 'Physics', 'I am very smart', 'Your Mom'),
                 GraduateStudent('Josh', '2014', 'Engineer', 'I am very smart', 'Your Mom')
        ]

    for i in grad_list:
        print(i)

main()
    
