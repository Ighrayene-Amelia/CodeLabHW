string = input("Please enter your own String : ")
def reverse(string):
    string = string[::-1]
    return string
  
print ("The reversed string is : ")
print (reverse(string))