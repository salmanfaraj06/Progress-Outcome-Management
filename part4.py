# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221380 / w1956374
# Date: 13/12/2022

# Part 04

Credits = [0, 20, 40, 60, 80, 100, 120]  # list of valid credits
p_count = 0    # pass
mt_count = 0    # module trailer
mr_count = 0    # module retriever
e_count = 0     # Exclude
boolean = True
unique_id=[]    #empty list to store stuent id and check 
outcomes={}    #empty dictionary for part 4

def input_credits(Values): # user defined function for input validation
    while True:
        try:
            number=int(input(Values))
        except ValueError:
            print("Integer required")
            continue

        else:   
            if number not in Credits:
                print("Out of range.")
                continue
        
            return number
        

while boolean:  # at start the condition is true so loops 
    while True:
        student_id=input("Please enter student ID :") #variable to store student ids 
        if student_id in unique_id: #checks if the id already exists 
            print("This id has already been entered. try again! ")
        else:
            unique_id.append(student_id) #if its not in list then adds it 
            break
# calling the user defined function for input validation  
    Pass = input_credits("Please enter your credits at pass : ")
    defer = input_credits("Please enter your credits at defer : ")
    fail = input_credits("Please enter your credits at fail : ")
    
    total = Pass + defer + fail
    if total != 120:
        print("Total incorrect.")
    elif Pass == 120:
        print("Progress")
        p_count += 1
        result = ("Progress")
        # student id is key and oucome plus inputs are values   
        outcomes[student_id] = result +' - '+str(Pass) + ', '+str(defer) + ', '+str(fail) 
    elif Pass == 100:
        print("Progress (module trailer)")
        mt_count += 1
        result = ("Progress (module trailer)")
        outcomes[student_id] = result +' - '+str(Pass) + ', '+str(defer) + ', '+str(fail)
    elif fail in range(61):
        print("Do not progress – module retriever")
        mr_count += 1
        result = ("Module retriever")
        outcomes[student_id] = result +' - '+str(Pass) + ', '+str(defer) + ', '+str(fail)
    else:
        print("Exclude")
        e_count += 1
        result =("Exclude")
        outcomes[student_id] = result +' - '+str(Pass) + ', '+str(defer) + ', '+str(fail)


    while True:
        retry = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        retry = retry.lower()
        if retry == "y":
            break #break out of this while loop
        elif retry == "q":
            for key, value in outcomes.items(): #looping through dictionary items
                print(key+" : "+ value, end="  ")
            boolean = False  # main while loop condition false so ends
            break  #break out of this while loo
        elif retry != "y" or retry != "q":
            print("\nInvalid input try again.")







