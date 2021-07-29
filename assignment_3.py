# Evangelista, Elyson
from collections import namedtuple


student_info = namedtuple('student_info', 'first last assignment exam')
StudentRoster = []


def student_format(student):
    """Returns given namedtuple as str in specified format."""
    s = student
    return '{0}, {1}, {2}, {3}'.format(s[0], s[1], s[2], s[3])


def remove_space(user_inputs):
    """Removes any instances of 'space' from the user's input."""
    return user_inputs.replace(" ", "")


def find_duplicate(student_list):
    """
    Checks if there are duplicate first names in the given sorted list. If duplicate names are found, function stores
    all duplicates in list, sorts by last name and prints. List is appended to index position where first duplicate was
    found.
    """
    place_holder = student_info('null', 'null', '0', '0')
    current = place_holder
    dupe = []
    final = []
    for student in student_list:
        previous = current
        current = student
        if current.first == previous.first:
            if previous in final:
                dupe.append(final.pop())
            dupe.append(student)
        elif current.first != previous.first:
            if len(dupe) > 1:
                dupe.sort(key=lambda x: x[1])
                for student_dupe in dupe:
                    final.append(student_dupe)
                final.append(student)
                dupe = []
            else:
                final.append(student)
    if len(dupe) > 1:
        dupe.sort(key=lambda x: x[1])
        for student_dupe in dupe:
            final.append(student_dupe)
    for student_final in final:
        print(student_format(student_final))


def add_student(user_inputs):
    """ Adds student to StudentRoster as a namedtuple from user's input """
    no_space = (remove_space(user_inputs))
    student_tuple = student_info._make(no_space.split(","))
    StudentRoster.append(student_tuple)


def delete_student(user_inputs):
    """
    Deletes specified student from StudentRoster. If either not given first and last name arguments or too many
    arguments, the function prints error message. If the number of items in the StudentRoster
    stays the same the function prints error message that no student was found with the name
     """
    no_space = (remove_space(user_inputs))
    first_last = no_space.split(",")
    if len(first_last) != 2:
        print("Invalid number of arguments, please only enter first and last name")
    else:
        first_n, last_n = first_last[0], first_last[1]
        original_count = len(StudentRoster)
        for student in StudentRoster:
            if student.first == first_n:
                if student.last == last_n:
                    StudentRoster.remove(student)
        if original_count == len(StudentRoster):
            print("Error! No student with that name was found in the roster.")


def find_by_name(command, name):  # fine
    """Finds student based on first or last name based on command argument and given name argument"""
    if command == 'FindByFName':
        for student in StudentRoster:
            if name == student.first:
                print(student_format(student))
    elif command == 'FindByLName':
        for student in StudentRoster:
            if name == student.last:
                print(student_format(student))


def get_average(value):  # fine
    """
    Gets the average value of Assignments or Exams based on specified value arguments 'Assignments' and 'Exam'.
    Student iterator values based on global list StudentRoster.
    """
    average_assignment = 0
    average_exam = 0
    student_count = 0
    if value == 'Assignment':
        for student in StudentRoster:
            student_count += 1
            average_assignment += int(student.assignment)
        if student_count == 0:
            print(0)
        else:
            calc = average_assignment/student_count
            print('{:.2f}'.format(calc))
    elif value == 'Exam':
        for student in StudentRoster:
            student_count += 1
            average_exam += int(student.exam)
        if student_count == 0:
            print(0)
        else:
            calc = average_exam/student_count
            print('{:.2f}'.format(calc))


def sort_roster(sorting_argument):
    """
    Function sorts global list StudentRoster based on given arguments. If argument is 'Name', function sorts
    StudentRoster based on first name, if multiple students have the same first name, they are sorted based on last
    name. If argument is 'Assignment', list is sorted from descending order based on namedtuple,
    student_info.assignment. If argument is "Exam, list is sorted from descending order based on namedtuple,
    student_info.exam
    """
    if sorting_argument == 'Name':
        StudentRoster.sort(key=lambda x: x[0])
        find_duplicate(StudentRoster)
    elif sorting_argument == 'Assignment':
        StudentRoster.sort(reverse=True, key=lambda x: x[2])
        for student in StudentRoster:
            print(student_format(student))
    elif sorting_argument == 'Exam':
        StudentRoster.sort(reverse=True, key=lambda x: x[3])
        for student in StudentRoster:
            print(student_format(student))


def GradeManager():
    """
    Function takes user input to execute a variety of commands. Commands include 'AddStudent', 'DeleteStudent',
    'SortRoster', FindByFName', 'FindByLName', 'PrintRoster', 'GetRoster', 'PrintRoster', and 'Quit'.
    """
    quit_program = False
    while quit_program is False:
        user_input = input('$ ')
        n = user_input.find(' ')  # separates argument and command
        if user_input[:n] == 'AddStudent':
            add_student(user_input[n + 1:])
        elif user_input[:n] == 'DeleteStudent':
            delete_student(user_input[n+1:])
        elif user_input[:n] == 'SortRoster':
            sort_roster(user_input[n+1:])
        elif user_input[:n] == 'FindByFName':
            find_by_name('FindByFName', user_input[n+1:])
        elif user_input[:n] == 'FindByLName':
            find_by_name('FindByLName', user_input[n+1:])
        elif user_input[:n] == 'GetAverage':
            get_average(user_input[n+1:])
        elif user_input == 'PrintRoster':
            for student in StudentRoster:
                print(student_format(student))
        elif user_input == 'Quit':  # test
            quit_program = True

