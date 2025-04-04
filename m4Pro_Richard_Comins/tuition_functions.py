# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 12:29:00 2025

@author: cominsr6423
"""


# This program menu driven and displays course information .
# March 16, 2025
# CSC-121 m4Pro 
# Lester Roberts


def display_courses(courses):
    """Displays the list of available courses with their tuition fees."""
    print("\nAvailable Courses")
    print("=" * 50)
    print(f"{'Course Code':<10}{'Course Name':<30}{'Tuition ($)':>10}")
    print("=" * 50)

    for code, details in courses.items():
        print(f"{code:<10}{details['name']:<30}{details['tuition']:>10.2f}")
    
    print("=" * 50)

def get_course_info(course_code, courses):
    """Displays course details if the course exists, otherwise notifies the user."""
    if course_code in courses:
        details = courses[course_code]
        print("\nCourse Found:")
        print("=" * 50)
        print(f"Course Code: {course_code}")
        print(f"Course Name: {details['name']}")
        print(f"Tuition: ${details['tuition']:.2f}")
        print("=" * 50)
    else:
        print("\nCourse not found. Please enter a valid course code.")

def display_students(students):
    """Displays the list of students with corresponding numbers."""
    print("\nStudent List")
    print("=" * 30)
    
    for idx, student in enumerate(students.keys(), 1):
        print(f"{idx}. {student}")
    
    print("=" * 30)

def get_student_info(student, students, courses):
    """Displays student details, including registered courses and total tuition."""
    if student in students:
        print("\nStudent Information")
        print("=" * 50)
        print(f"Student Name: {student}")
        print("Registered Courses:")

        total_tuition = 0
        for course_code in students[student]:
            course_name = courses[course_code]["name"]
            tuition = courses[course_code]["tuition"]
            total_tuition += tuition
            print(f"  - {course_code} ({course_name}) - ${tuition:.2f}")

        print(f"\nTotal Tuition: ${total_tuition:.2f}")
        print("=" * 50)
    else:
        print("\nStudent not found.")

def calculate_student_tuition(students, courses):
    """Calculates and displays the number of courses and total tuition for each student."""
    print("\nStudent Tuition Summary")
    print("=" * 60)
    print(f"{'Student Name':<25}{'Courses':<10}{'Total Tuition ($)':>15}")
    print("=" * 60)

    total_college_tuition = 0
    for student, course_list in students.items():
        num_courses = len(course_list)
        total_tuition = sum(courses[code]["tuition"] for code in course_list)
        total_college_tuition += total_tuition
        print(f"{student:<25}{num_courses:<10}{total_tuition:>15.2f}")

    print("=" * 60)
    print(f"{'Total Tuition for All Students:':<35}${total_college_tuition:.2f}")
    print("=" * 60)

def calculate_course_tuition(students, courses):
    """Calculates and displays the number of students per course and total tuition generated."""
    print("\nCourse Tuition Summary")
    print("=" * 50)
    print(f"{'Course Code':<10}{'Enrolled Students':<20}{'Total Tuition ($)':>15}")
    print("=" * 50)

    course_enrollment = {code: 0 for code in courses.keys()}  # Initialize counts

    for course_list in students.values():
        for code in course_list:
            course_enrollment[code] += 1

    for code, count in course_enrollment.items():
        total_tuition = count * courses[code]["tuition"]
        print(f"{code:<10}{count:<20}{total_tuition:>15.2f}")

    print("=" * 50)

#    main()