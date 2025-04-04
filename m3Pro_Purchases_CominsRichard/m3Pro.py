# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:17:56 2025

@author: cominsr6423
"""

"""
This program allows the user to calculate tuijtion costs depending on the course taken.
02/27/2025
CSC-121 m3Pro-Purchases
Richard Comins
"""

import m3_function as fn
stu_names = ["Zakari Watson", "Jerome Williams", "Dominique Ross", 
             "Diana Shepard", "Yoko Mayo", "Rashad AShmed", "Susan Jones"]

courses = ["Mat 035(]Concepts of Algebra)", "CTI 115(Computer System Foundations)", 
           "BAS 120 Intro to Analytics", "CSC 121 Python Programming"]

tuition = [460, 520.98, 500, 783.88]

def main():
    
    fn.course_display(courses,tuition)
    
    choice = 0

    while choice != 3:
        
        fn.menu()
        
        choice = int( input("Enter choice "))
        
        if choice == 1:
            
            money_owed = fn.calc_tuition(courses, tuition, stu_names)
            print()# display results
            fn.tuition_display (stu_names,money_owed)
            
        elif choice == 2:
            
            # display list of students

            for index, value in enumerate(stu_names):

                print(index+1, value)# display list of names

            # ask the user to enter student number

            print()
            stu_num = int(input("Enter student number: "))

            total_tuition = 0
            reg_courses = []
        
            # check what courses the student is taking
            for i in range(len(courses)):
            
               answer = input(f'Is {stu_names[stu_num-1]} taking {courses[i]} (y for yes ? ')
           
               # check
               if answer == 'y':
                   # add the tuition
                   reg_courses.append(i)
                   total_tuition += tuition[i]

            # display courses student is registered in
            print(f"{'course name':<40}{'tuition'}")
            print('-'*50)

            for i in reg_courses:
                print(f"{courses[i]:<40}{tuition[i]}")
            print('-'*50)
            print(f"{'Total Cost':<45}${total_tuition}")

                

                

            

    
            
        elif choice == 3:
            
            print('Bye')
        else:
            
            print('Invalid Entry')
    
    


    


main()
    
    
   
