# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20221380 / w1956374
# Date: 13/12/2022

# Part 03

Credits = [0, 20, 40, 60, 80, 100, 120]  # list of valid credits
boolean = True
#slight modification on part 2 
progress=[] 
trailer=[]
retriever=[]
exclude=[]


def input_credits(feedback): # user defined function for input validation
    while True:
        try:
            number=int(input(feedback))
        except ValueError:
            print("Integer required")
            continue

        else:   
            if number not in Credits:
                print("Out of range.")
                continue
        
            return number
        
def  text_file():#user defined function for part 3 
    seperator=", " #https://youtu.be/xlkf9eECcSw
    file=open("part3_file.txt","w") #function to open the file opened in write mode
    file.write("\nPart 3:")
    for i in range (len(progress)):#traverse through the nested list and write it to the file
        clear_prog=seperator.join(map(str,progress[i]))#clears the brackets
        file.write("\nProgress - ")
        file.write(clear_prog)
        i+=1
    for i in range (len(trailer)):
        clear_trailer=seperator.join(map(str,trailer[i]))
        file.write("\nProgress (module trailer) - ")
        file.write(clear_trailer)
        i+=1
    for i in range (len(retriever)):
        clear_retriever=seperator.join(map(str,retriever[i]))
        file.write("\nModule retriever - ")
        file.write(clear_retriever)
        i+=1
    for i in range (len(exclude)):
        clear_exc=seperator.join(map(str,exclude[i]))
        file.write("\nExclude - ")
        file.write(clear_exc)
        i+=1
    file.close()#close the text file

def print_file():       #user defined function to print the text file
        file=open("part3_file.txt")   #function to open text file in default read mode
        content=file.read()#to read everything on txt file 
        print(content)
        file.close()    #close the text file
        

while boolean == True:  # at start the condition is true so loops
    Pass = input_credits("Please enter your credits at pass : ")
    defer = input_credits("Please enter your credits at defer : ")
    fail = input_credits("Please enter your credits at fail : ")
    
    total = Pass + defer + fail
    if total != 120: #when its either more or less than 120
        print("Total incorrect.")
    elif Pass == 120:
        print("Progress")
        progress.append([Pass,defer,fail])#adds the 3 input data to the specific list as a nested list
    elif Pass == 100: 
        print("Progress (module trailer)")
        trailer.append([Pass,defer,fail])
    elif fail in range(61):
        print("Do not progress – module retriever")
        retriever.append([Pass,defer,fail])
    else:
        print("Exclude")
        exclude.append([Pass,defer,fail])
        
    text_file()    #calling the user defined function to write to file  
    while True:   #infinite loop to continue or exit 
        retry = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:")
        retry = retry.lower()
        if retry == "y":
            break  #breaks out of this loop 
        elif retry == "q":
            print_file() #calling the user defined function to read text file 
            boolean = False  # main while loop condition false so ends
            break #breaks out of this loop aswell 
        elif retry != "y" or retry != "q":
            print("\nInvalid input try again.")  #prompts again for input
                

