# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 12:27:51 2025

@author: cominsr6423
"""


## This program menu driven and displays course information .
# March 24, 2025
# CSC-121 m4Pro 
# Richard Comins

#import sys
from tuition_functions import (display_courses, get_course_info, display_students, get_student_info, calculate_student_tuition, calculate_course_tuition)

# Global dictionary of students and their registered courses
students = {"Zakari Watson": ["MAT 035", "CSC 121"], "Jerome Williams": ["CTI 115", "BAS 120"], "Dominique Ross": ["CSC 121"], "Diana Shepard": ["MAT 035", "BAS 120", "CSC 121"], "Yoko Mayo": ["CTI 115"], "Rashad Ahmed": ["BAS 120", "CSC 121"], "Susan Jones": ["MAT 035", "CTI 115"]}

# Course data
courses = {"MAT 035": {"name": "Concepts of Algebra", "tuition": 460}, "CTI 115": {"name": "Computer System Foundations", "tuition": 520.98}, "BAS 120": {"name": "Intro to Analytics", "tuition": 500}, "CSC 121": {"name": "Python Programming", "tuition": 783.88}}


def main():
    """Menu-driven program that handles student tuition calculations."""
    choice = 0
    while choice !='6':
        print("\nMAIN MENU")
        print("1. Display Course List")
        print("2. Display Course Information")
        print("3. Display Student Information")
        print("4. Display Student Tuition Summary")
        print("5. Display Course Tuition Summary")
        print("6. Exit Program")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == '1':
            display_courses(courses)
        elif choice == '2':
            course_code = input("\nEnter the course code (e.g., MAT 035): ").strip()
            get_course_info(course_code, courses)
        elif choice == '3':
            display_students(students)
            student_num = input("\nEnter the student number: ").strip()
            if student_num.isdigit() and 1 <= int(student_num) <= len(students):
                get_student_info(list(students.keys())[int(student_num) - 1], students, courses)
            else:
                print("\nInvalid student number. Please try again.")
        elif choice == '4':
            calculate_student_tuition(students, courses)
        elif choice == '5':
            calculate_course_tuition(students, courses)
        elif choice == '6':
            print("\nProgram will now stop. Goodbye!\n")
           # choice = 6
          
        
            
            # sys.exit()
                        
            
            #break
        else:
            print("\nInvalid option! Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
