'''
Gülnur Uzun, Alper Tanrıkulu

Q2

(30 points) 7 students took 2 exams, the top three students will get AA. You were provided with the list of exam marks, 
use Python string operations, mathematical operations and loops to find average of two exam marks for each student and choose 
top 3 students programmatically. Announce the top 3 students to the audience:
List = [‘Ayşe: 75-78’, ‘Berk: 80-60’, ‘Can: 58-61’, ‘Didem: 34-45’,’Erdem: 32-37’, ‘Fatih: 69-75’, ‘Gül: 54-63’]

'''

List = ["Ayşe: 75-78",
        "Berk: 80-60",
        "Can: 58-61",
        "Didem: 34-45",
        "Erdem: 32-37",
        "Fatih: 69-75",
        "Gül: 54-63"]
names = []  
mean_grades = []
for i in range(len(List)):
    List1 = List[i].split(": ") # Created a new list that is appear in for loop and then disappears
    grades = List1[1].split("-") # to reach the exam marks
    avg = (int(grades[0])+int(grades[1]))/2 # to calculate the averages
    mean_grades.append(avg)
    names.append(List1[0]) # 0th index of List1 is refers to names
#print(names)
#print(mean_grades)

for i in range(3):
    max_value = max(mean_grades) # to find having maximumum average grade
    max_index = mean_grades.index(max_value) # index of value having highest value
    print(f"{i+1}. student with the highest score is {names[max_index]}: {mean_grades[max_index]}") # to print the highest average grade

    names.pop(max_index) # deleted the name having highest average grade to reach the second highest average grade
    mean_grades.pop(max_index) # deleted the average grade having highest average grade to reach the second highest average grade

