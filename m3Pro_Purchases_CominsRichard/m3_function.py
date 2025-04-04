# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:23:09 2025

@author: cominsr6423
"""

def course_display(courses,tuition):
    """
    Parameters
    ----------
    courses : list of courses
    tuition : list of tutions

    Returns
    -------
    None.

    """
    
    print(f"{'course name':<40}{'tuition'}")
    print('-'*50)
    # start the loop
    for i in range(len(courses)):
        
        print(f"{courses[i]:<40}${tuition[i]}")
    
def menu():
    '''
    displays menu displays a list of choices
    Returns
    -------
    None.

    '''
    
    print('\n1) Calculate Tution for All Students')
    print('2) Calculate Tution Specific Students')
    print('3) Exit\n')

def calc_tuition(courses,tuition,stu_names):
    '''
    Parameters
    ----------
    courses : a list of courses offered
    tuition : the cost of each course
    stu_names : a list of student names

    Returns
    -------
    money_owed : The amount of money owed based on the tuition 

    '''
    
    money_owed = [] # reference money student owes
    
    for name in stu_names:
        
        # create running total 
        total_tuition = 0
        
        # check what courses the student is taking
        for i in range(len(courses)):
            
           answer = input(f'Is {name} taking {courses[i]} (y for yes ? ')
           
           # check
           if answer == 'y':
               # add the tuition
               total_tuition += tuition[i]
        
        # append total tution for student to money_owed list
        money_owed.append(total_tuition)
    
    return money_owed

def tuition_display (stu_names,money_owed):
    '''
    Parameters
    ----------
    stu_names : TYPE string listing of students
        DESCRIPTION.
    money_owed : TYPE Float depicting cost of selected courses
        DESCRIPTION.

    Returns
    -------
    None.

    '''

    
    print(f"{'Student Name':<40}{'Tuition'}")
    print('-'*50)
    # start the loop
    for i in range(len(stu_names)):
        
        print(f"{stu_names[i]:<40}${money_owed[i]}")