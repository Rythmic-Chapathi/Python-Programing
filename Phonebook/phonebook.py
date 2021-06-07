run =True

def exit():
    global run
    run=False
def add():
    name = input('Persons name')
    number = input('Persons phone number')
    a = open('phonebook.txt','a')
    a.write('\n'+name+':'+number)
    a.close
def read():
    a = open('phonebook.txt','r')
    b = a.readlines()
    print(b)
    a.close
    


while run:

    print('1.) Add a number')
    print('2.) Show phonebook')
    print('3.) Exit')


    option=int(input("Enter your option "))

    print("the option is ",option ,"\n")

    if option==3:
        exit()

    elif option==1:
        add()
    elif option==2:
        read()
        
