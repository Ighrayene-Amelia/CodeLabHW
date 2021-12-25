with open('student_names.txt', 'r') as file: 
     content =file.readlines()
     n=int(input('type your number'))
     print (content[:n]) 