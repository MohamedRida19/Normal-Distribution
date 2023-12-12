#import the libraries
import numpy as np
import seaborn as sns
import time
import matplotlib.pyplot as plt

#set the default values
default_loc_var = 0
default_scale_var = 1
default_graph_color = "blue"
default_font_type = "Arial"
default_font_size = 16
default_font_color = "red"
default_threshold = 3.5
default_size = 100

#creating loading function
def print_loading_message(message1, message2):
    print(message1, end='', flush= False)
    for i in range(3):
        time.sleep(0.2)
        print('.', end=' ', flush=False)
    time.sleep(0.1)
    print(message2)

#creating numeric inputs function
def numeric_user_input(message, default=None):
    while True:
        try:
            user_input = float(input(message).strip())
            print_loading_message("Checking the input!", "Done!")
            return user_input if user_input > 0 else (default if default is not None else print("Customizing option applied") or default)
        except ValueError:
            print("Invalid input. Try again and input a numerical positive value!")

# creating string input function
def string_user_input(mes1, default=None):
    user_input = input(mes1).strip()
    print_loading_message("Checking the input!", "Done!")
    try:
        if not user_input:
            print("Using default options")
            return default if default is not None else print("Customizing option applied") or default
        elif not user_input.replace('.', '').isdigit():
            print("Customizing options applied")
            return user_input
        else:
            print("What?? Anyways default options applied")
            return default if default is not None else print("Customizing option applied") or default
    except NameError:
        pass

#print welcome messages
print('welcome to our program of buildings figures!')#print "welcome_message"
time.sleep(0.5)#waiting 200ms befor passing this line
print('thank you for your trying my program!')
time.sleep(0.5)#waiting 500ms befor passing this line

#set the try except block for handling errors
try:
    #get from the user the number of attepmts
    user_attempts = int(input('how many times you want to try this? (only positif integer numbers)\n'))
    print_loading_message("Checking the input!", "Done!")
    i = 0
    #adding for in loop based on the user attempts
    for i in range(user_attempts):
        #ask the user if he want to change the options
        change_options = str(input("do you want to change the options (yes/no)?\n"))
        #get the inputs from the user if he wants to change the options
        if change_options== "yes":
            time.sleep(0.3)
            print("Starting with: Graph options")
            loc_var = numeric_user_input("I want the value of loc (where is the bell start, recommended 0):\n", default = default_loc_var)
            scale_var = numeric_user_input("I want the value of scale(how flat is the graph, recommende 1):\n", default = default_scale_var)
            size_var = numeric_user_input("set the size value!\n",default= default_size)
                
            graph_color = string_user_input("Choose the color of the graph (skip this by pressing enter)\n", default_graph_color)
            threshold = numeric_user_input("add the threshold value(required!).\n", default=default_threshold)
            
                
            time.sleep(0.3)
            print("Moving on: text options")
            time.sleep(0.1)
            font_type = string_user_input("you can set the font type (skip this by pressing enter):\n", default_font_type)
                
            font_size = numeric_user_input("set the font size pls(recommended 16pts):\n", default = default_font_size)

            font_color = string_user_input("you can set the font color (skip this by pressing etner):\n", default_font_color)

            
        elif change_options == 'no':
            print("Default settings applied!")
            pass
        else:
            print("I cannot understand this! default settings applied!")    
            pass
        #adding the figure's code
        print_loading_message("Calculating DATA!", "Creating new figure done!") 
        time.sleep(0.2)
        data = np.random.normal(loc = loc_var if change_options == "yes" else default_loc_var , scale= scale_var if change_options == "yes" else default_scale_var, size= default_size )
        
        mean_value = np.mean(data)
        std_value = np.std(data)
        plt.axvline(x = mean_value, color = "red", linestyle = "--", label = f"MEAN: {mean_value:.2f}")
        plt.axvline(x = mean_value + std_value, color = "orange", linestyle = "--", label = f"STD: {std_value:.2f}")

        above_threshold = np.sum(threshold < data)
        pourcentage_above_threshold = (above_threshold / (size_var if change_options == "yes" else default_size)) *100
        plt.axvline(x= (threshold if change_options == "yes" else default_threshold), color = "green", linestyle= "--", label = f'THRESHOLD: {pourcentage_above_threshold: .2f}%')
        plt.annotate('threshold', xy = (threshold, 0), xytext= (0,10), textcoords = 'offset points', ha = "center", color = "black")

        sns.histplot(data, kde = True, linewidth = 0, color = graph_color if change_options == "yes" else default_graph_color, fill = 0)
        #adding the title to the figure
        text_options = {'font' : font_type if change_options == "yes" else default_font_type, 'size' : font_size if change_options == "yes" else default_font_size, 'color' : font_color if change_options == "yes" else default_font_color}
        plt.xlabel("Values")
        plt.ylabel("Frequency")
        plt.title("NORMAL DISTRIBUTION", **text_options)
        plt.legend()
        plt.show()
        time.sleep(0.3)
        print(f"excuting_times: {i+1}")

    time.sleep(0.3)
    print('program excuting has been finished, exit applying now!')#tell the user that the program has beeing done his attempts
    time.sleep(0.3)
    exit()
    
except ValueError as ve:
    print(f"Incorrect input: {ve}. Pls try again!")
    exit()
except KeyboardInterrupt as kbi:
    print(f"Something wrong: {kbi}. Pls try again!")
    exit()