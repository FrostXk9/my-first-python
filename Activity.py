greeting = 'hello world'

print(greeting)

def check_name(username):
    if username == "":
        print('username is to long or you have not inserted your name')
    else:
        print(f"Hello {username}")


# print(check_name(input()))


# A function allowing the user to concat two strings and once entered 
# text writes to file
def concat(w1, w2):
    w1 = input()
    w2 = input()
    
    result = w1+ ' ' + w2
    
    myfile = open('myText.txt', 'w')
    
    myfile.write(result)
    
    myfile.close()
    
    if w1 == 0 and w2 == 0:
        print("Seems as if you have entered nothing to concatenate")
    else:
        print(result)   

print(concat('', ''))