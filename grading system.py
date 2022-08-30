print('\n\t\t\t\t\t\t\t\tTechnological University Of Mandalay \t\t\t\t\t\t\t\t\n')
print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTo Calculate Grades\t\t\t\t\t\t\t\n')


def grading(marks):
    for i in range(0, len(marks), 1):
        mark = marks[i]
        mark = int(mark)
        if 80 <= mark <= 100:
            grades.append('A')
        elif 60 <= mark <= 79:
            grades.append('B')
        elif 40 <= mark <= 59:
            grades.append('C')
        elif mark <= 3:
            grades.append('D')
        else:
            grades.append('E')


def getmark(sub):
    for i in range(0, 6):
        marks.append(input('Enter '+sub[i]+ ' marks: '))
    return marks


while True:
    grades = []
    marks=[]
    year = input('Enter Year:  ')
    if year == 'first':
        name=input('Enter Student Name: ')
        roll=input('Enter Roll Number: ')
        sub = ['myanmar', 'english', 'mathematics',
            'physics', 'chemstry', 'IT']
        grading(getmark(sub))
        print('\n\nStudent Name: ' + name)
        print('Roll Number:'+roll)
        print('Grades: ')
        for i in range(0,6,1):
            print(sub[i]+'\t'+grades[i])
    

    elif year=='second':
        name=input('Enter Student Name: ')
        roll=input('Enter Roll Number: ')
        sub = ['english', 'mathematics',
            'physics', 'chemstry', 'IT','majo 1']
        grading(getmark(sub))
        print('\n\nStudent Name: ' + name)
        print('Roll Number:'+roll)
        print('Grades: ')
        for i in range(0,6,1):
            print(sub[i]+'\t'+grades[i])

    elif year=='third':
        name=input('Enter Student Name: ')
        roll=input('Enter Roll Number:')
        sub = ['english', 'mathematics',
        'physics','major 2','IT','major 1']
        grading(getmark(sub))
        print('\n\nStudent Name: ' + name)
        print('Roll Number:'+roll)
        print('Grades: ')
        for i in range(0,6,1):
            print(sub[i]+'\t'+grades[i])

    elif year=='fourth':
        name=input('Enter Student Name: ')
        roll=input('Enter Roll Number: ')
        sub = ['english', 'mathematics',
            'major 3', 'major 2', 'IT','majo 1']
        grading(getmark(sub))
        print('\n\nStudent Name: ' + name)
        print('Roll Number:'+roll)
        print('Grades: ')
        for i in range(0,6,1):
            print(sub[i]+'\t'+grades[i])

    else:
        print("Enter year only: ")
        continue

    opt = input('Do you want to calculate more(y/n)?')
    if opt == 'y':
        continue
    else:
        break

