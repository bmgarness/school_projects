#!/usr/bin/python3
'''
Homework Assignment #1
CS0008
Benjamin Garness (bmg74@pitt.edu)
02/1/16
'''

#Module variables to hold course names.
# Remember, these are 'read-only' when used inside of functions
CS100 = 'CS100 - Introduction to Programming'
CS200 = 'CS200 - Advanced Programming'
CS300 = 'CS300 - Super Advanced Programming'


def main():
    '''This is the main function. The function needs to read in the student's
    name. It should store variables representing the total number of courses
    taken and the total number of grade points earned. 
    
    The function should ask if the student has taken CS100. If not, the function
    should immediately print the following message:
        <StudentName> needs to take all 3 CS courses to graduate.
    
    Otherwise, if they finished CS100, the program should add 1 to the courses
    taken, determine the grade points earned and add it to the total 
    grade points earned. Only if CS100 was completed should the program then 
    ask whether CS200 is taken, and if so, increment the number of courses taken
    and the grade points earned.
    
    Again, if CS200 was taken, it should then ask whether CS300 is taken, 
    and repeat the steps with CS100 and CS200 (increment the number of 
    courses taken and the grade points earned. 
    
    Finally, as long as CS100 is completed, the main function should call
    the check_graduation function to calculate the students GPA and determine
    if they can graduate.
    '''
    prompt = input('Enter the student\'s full name: ')
    courses_taken = 0
    grade_points = 0
    if is_course_taken(CS100):
        courses_taken += 1
        grade_points += get_grade_points()
        if is_course_taken(CS200):
            courses_taken += 1
            grade_points += get_grade_points()
            if is_course_taken(CS300):
                courses_taken += 1
                grade_points += get_grade_points()
    else:
        return print('{} needs to take all 3 CS courses to graduate'.format(prompt))            
    check_graduation(prompt, courses_taken, grade_points)
        
   
def is_course_taken(coursename):
    '''
    This function will ask whether the the student has taken the specified
    course and will return a boolean True or False depending on their answer.
    
    An affirmative answer can be any of the following:
        Yes, Y, yes, y
        
    Any other response should be treated as a No and should return False.    
    '''
    prompt = input('Has the student taken {}? '.format(coursename))
    y1 = 'Yes'
    y2 = 'yes'
    y3 = 'Y'
    y4 = 'y'
    if prompt == y1 or prompt == y2 or prompt == y3 or prompt == y4:
        return True
    else:
        return False
        
    

    
def get_grade_points():
    '''
    This function will ask what grade a student received and return the
    numeric point value associated with that grade.
    
    'A' -> 4
    'B' -> 3
    'C' -> 2
    'D' -> 1
    'F' or any other input -> 0
    
    Note that this function should be case sensitive. An 'A' response from
    the user should return 4 but an 'a' response is not equivalent and should
    return 0.
    '''
    prompt = input('What grade did the student earn? ')
    if prompt == 'A':
        return 4
    elif prompt == 'B':
        return 3
    elif prompt == 'C':
        return 2
    elif prompt == 'D':
        return 1
    else:
        return 0
    
def check_graduation(name, courses_taken, grade_points):
    '''This function checks a student's courses and GPA and determines if they
    can graduate. Graduation requires that all 3 courses are finished and
    that the students GPA (total grade points / total courses) be above 2.5.
    
    First, the function should print the following message:
        <StudentName>:  Courses taken: <Courses>. GPA <GPA>.
    There should be a tab after the colon and before Courses and GPA needs
    to have 3 decimal places.
    
    If all graduation requirements are met, the function should print:
        Graduation Approved.
    
    If all required courses are finished but the GPA requirement is not met the 
    function should print:
        Graduation Not Approved. GPA must be above 2.5
        
    Finally, if the student still has courses remaining, the function should 
    print:
        Graduation Not Approved. <CoursesLeft> courses remaining
    '''
    output = '{}: Courses taken: {}. GPA {:.3f}'
    grade_point_average = 0.0
    if courses_taken == 0:
        courses_taken = 1
    grade_point_average = grade_points / courses_taken
    courses_left = 3 - courses_taken
    print(output.format(name, courses_taken, grade_point_average))
    if (courses_taken == 3) and (grade_point_average > 2.5):
          print('Graduation Approved')
    elif courses_taken == 3 and grade_point_average <= 2.5:
          print('Graduation Not Approved. GPA must be above 2.5')
    else:
          print('Graduation Not Approved. {} courses remaining'.format(courses_left))
    

main()  # This is where the main() function is called
