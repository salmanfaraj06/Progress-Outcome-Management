# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221380 / w1956374
# Date: 13/12/2022


# Part 02 List (extension)
Credits = [0, 20, 40, 60, 80, 100, 120]  # list of valid credits
p_count = 0  # pass
mt_count = 0  # module trailer
mr_count = 0  # module retriever
e_count = 0  # Exclude
boolean = True
#create empty list to store the inputs
progress=[] 
trailer=[]
retriever=[]
exclude=[]


def print_histogram():  # user defined function to print the histogram
    print("-" * 64)
    print("Histogram")
    print("Progress", p_count, " : ", '*' * p_count)  
    print("Trailer", mt_count, "    : ", '*' * mt_count)   # multiply stars to the respective outcome
    print("Retriever", mr_count, ": ", '*' * mr_count)  
    print("Excluded", e_count, ": ", '*' * e_count, "\n")  
    print(p_count+mt_count+mr_count+e_count, "outcomes in total.")
    print("-" * 64,"\n")
    
def print_part2():    #user defined function to print the list entension 
    print("Part 2:")    #list extension
    seperator=", "      #https://youtu.be/xlkf9eECcSw
    for i in range (len(progress)):     #traverse through the nested list and prints removing the bracket 
        print("Progress -",seperator.join(map(str,progress[i])))
    for i in range (len(trailer)):
        print("Progress (module trailer) -",seperator.join(map(str,trailer[i])))
    for i in range (len(retriever)):
        print("Module retriever  -",seperator.join(map(str,retriever[i])))
    for i in range (len(exclude)):
        print("Exclude -",seperator.join(map(str,exclude[i])))
    print("-"*64,"\n")            

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
        
while boolean == True: # at start the condition is true
    Pass = input_credits("\nPlease enter your credits at pass : ")  #calling the function to get credits 
    defer = input_credits("Please enter your credits at defer : ")
    fail = input_credits("Please enter your credits at fail : ")
    
    total = Pass + defer + fail
    if total != 120: #when its either more or less than 120
        print("Total incorrect.")
    elif Pass == 120:
        print("Progress")
        p_count += 1  #increment the progress count
        progress.append([Pass,defer,fail])  #adds the 3 input data to the specific list as a nested list
    elif Pass == 100: 
        print("Progress (module trailer)")
        mt_count += 1
        trailer.append([Pass,defer,fail])
    elif fail in range(61):
        print("Do not progress – module retriever")
        mr_count += 1
        retriever.append([Pass,defer,fail])
    else:
        print("Exclude")
        e_count += 1
        exclude.append([Pass,defer,fail])

    #multiple outcomes
    while True:  #infinite loop to get multiple outcomes 
        retry = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        retry = retry.lower()
        if retry == "y":
            break  #breaks out of this while loop  
        elif retry == "q":
            print_histogram()  # calling the user defined histogram function
            print_part2()
            boolean = False  # main while loop condition false so ends 
            break  #breaks out of this while loop  
        elif retry != "y" or retry != "q":
            print("\nInvalid input try again.")     #loops again prompting for y or q 
            
