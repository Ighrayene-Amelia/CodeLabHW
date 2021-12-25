with open('student_names.txt', 'r') as file: 
     content =file.readlines()
     X = input('type the name')
     if X in content :
         print('true')
     else :
         print ('x not found')