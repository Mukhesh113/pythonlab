#dictionaries_1
students={1:'Mukhesh',
              2:'Mani',
              3:'Prudhvi',
              4:'Phanith',
              5:'Vamsi',
              }
print('students:',students)

'''sample output:
students: {1: 'Mukhesh', 2: 'Mani', 3: 'Prudhvi', 4: 'Phanith', 5: 'Vamsi'}
  '''
#dictionaries_2
students={1:'Mukhesh', 2:'Mani', 3:'Prudhvi'}
students[4]='Phanith'
students[5]='Vamsi'
students[6]='Madhu'
print('final dict:',students)

'''sample output:
final dict: {1: 'Mukhesh', 2: 'Mani', 3: 'Prudhvi', 4: 'Phanith', 5: 'Vamsi', 6: 'Madhu'}  '''

#dictionaries_3
dict={1:'key', 2:'lock', 3:'solution'}
print('before update:',dict)
dict[2]='problem'
print('after update:',dict)

'''sample output:
before update: {1: 'key', 2: 'lock', 3: 'solution'}
after update: {1: 'key', 2: 'problem', 3: 'solution'}  '''

#dictionaries_4
keys=['name','place','color']
values=['mirchi','guntur','red']
zip()
data=dict(zip(keys,values))
print('dictionary:',data)

'''sample output:
dictionary: {'name': 'mirchi', 'place': 'guntur', 'color': 'red'} '''

#dictionaries_5
employees={
    1:{'name':'priya','department':'CSE','salary':100000},
    2:{'name':'shankar','departmrnt':'mechanical','salary':100000},
    3:{'name':'maheswar','department':'EEE','salary':100000}
    }
print('employees:',employees)

'''sample output:
employees: {1: {'name': 'priya', 'department': 'CSE', 'salary': 100000}, 2: {'name': 'shankar', 'departmrnt': 'mechanical', 'salary': 100000}, 3: {'name': 'maheswar', 'department': 'EEE', 'salary': 100000}} '''
    
#dictionaries_6

