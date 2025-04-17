# import matplotlib.pyplot as plt

# Every student has a name and a 3 digit id number.
# Every assignment has a name, a point value, and a 5 digit id number.
# Except quiz 8 has a 4 digit assignment ID
# Every submission has a student id, an assignment id, and a percentage of the points earned for the assignment.
# The total number of points for all the assignments is 1000. 
# Every student submitted every assignment, there were no missing submissions. 

import os
import matplotlib.plt as plt 
def read_students():
    with open('./data/students.txt', "r") as f:
        out = f.read().split('\n')
        res = {i[:3]:i[3:] for i in out}
        res.update({i[3:]:i[:3] for i in out})
    f.close()
    return res
    
def read_assignments():
    assignments = []
    temp = []
    with open('./data/assignments.txt', "r") as f:
        out = f.read().split('\n')
    f.close()
    return out

def read_submissions():
    path = './data/submissions'    
    files = [f for f in os.listdir('./data/submissions')]
    out = []
    for f in files:
        with open(f'{path}/{f}', "r") as file:
            out.append(file.read().split('|'))
            out = [[i[0], i[1], int(i[2])] for i in out]
        file.close()
    return out

def get_student_grade():
    name = input("What is the student's name: " )
    if name in students:
        total = 0
        length = 0
        for i in submissions:
            if i[0] == students[name]:
                total+=i[2]
                length+=1
        print(f"{total//length:.0f}%")
    else:
        print('Student not found')

def get_assignment_stats():
    assignment = input("What is the assignment name: ")
    if assignment in assignments:
        results = []
        for i in submissions:
            if i[1] == assignments[assignment]['hw_id']:
                results.append(i)
        
        points = [i[2] for i in results] 
        print(points)
        print(f"Min: {min(points)}%")
        print(f"Avg: {sum(points)//len(points)}%")
        print(f"Max: {max(points)}%")
    else:
        print('Assignment not found')

def display_assignments():
    assignment = input("What is the assignment name: ")
    if assignment in assignments:
        results = []
        for i in submissions:
            if i[1] == assignments[assignment]['hw_id']:
                results.append(i)
        
        points = [i[2] for i in results] 
        plt.hist(points, bins=[0,25,50,75,100])
        plt.show()

    else:
        print('Assignment not found')


def menu():
    arr = ['Student grade', 'Assignment statistics', 'Assignment graph']
    for i, ele in enumerate(arr):
        print(f'{i+1}. {ele}')
    num_sel = input('\nEnter your selection ')
    if num_sel == '1':
        get_student_grade()
    elif num_sel == '2':
        get_assignment_stats()
    elif num_sel == '3':
       display_assignments()
    else:
        print('Wrong Selection')

def data_acq():
    global students
    global submissions
    global assignments
    students = read_students()
    unsorted_assignments = read_assignments()
    assignments = {title:{ 'hw_id':hw_id, "points":points} for (title, hw_id, points) in zip(unsorted_assignments[::3], unsorted_assignments[1::3], unsorted_assignments[2::3])}
    submissions = read_submissions()

def main():
    data_acq()
    menu()
    # print(assignments)



if __name__ == '__main__':
    main()