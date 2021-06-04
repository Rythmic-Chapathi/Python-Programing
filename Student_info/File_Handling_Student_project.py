run=True

def exit_pog():
    global run
    run=False
def add_student():
    
    name=input("Enter your name ")
    
    m1 = int(input("Enter marks of subject 1 "))
    m2 = int(input("Enter marks of subject 2 "))
    m3 = int(input("Enter marks of subject 3 "))
    
    f = open("students.txt","a")
    
    f.write(name+","+str(m1)+","+str(m2)+","+str(m3)+" \n")

    print('Congratulations! Your student is now added so our database.')

    f.close()

def get_marks():
    search= input('Enter the student names to find percentage')
    f = open("students.txt","r")
    lines=f.readlines()
    for line in lines:
        data = line.split(',')
        if data[0]==search:
            sum=int(data[1])+int(data[2])+int(data[3].replace(' \n',""))
            percentage= int((sum/300)*100)
            print(data[0],'Has a percentage of',percentage,'%')
    f.close()


    


while run:

    print("Welcome to The Grade Portal of Rithwik K Official University")
    print("Please choose any one option")
    print("1:Add Student")
    print("2:Get percentage of a perticular student")
    print("3: Exit")

    option=int(input("Enter your option "))

    print("the option is ",option ,"\n")

    if option==1:
        add_student()

    elif option==2:
        get_marks()
        

    elif option==3:
        exit_pog()
       
    else:
        print('INVALID')