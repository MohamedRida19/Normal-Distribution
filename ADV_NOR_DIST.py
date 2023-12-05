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

#creating loading function
def print_loading_message(message1, message2):
    print(message1, end='', flush= False)
    for i in range(3):
        time.sleep(0.2)
        print('.', end=' ', flush=False)
    time.sleep(0.1)
    print(message2)

#creating numeric inputs function
def numeric_user_input(message, default = None):
    while True:
        try:
            user_input = float(input(message).strip())
            print_loading_message("Checking the input!", "Done!")
            return user_input if user_input > 0 else default
        except ValueError:
            print("Invalid input. Try again and input a numerical postive value!")

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
        change_options = str(input("do you want to change the options (yes/no)?\n")).lower().split()
        #get the inputs from the user if he wants to change the options
        try:
            if change_options== "yes":
                time.sleep(0.3)
                print("Starting with: Graph options")
                loc_var = numeric_user_input("I want the value of loc (where is the bell start, recommended 0):\n", default = default_loc_var)
                scale_var = numeric_user_input("I want the value of scale(how flat is the graph, recommende 1):\n", default = default_scale_var)
                
                graph_color = str(input("Choose the color of the graph (skip this by pressing enter)\n")).strip()
                print_loading_message("Cheking the input!", "Done!")
                if not graph_color:
                    print("Default options applied!")
                    graph_color = default_graph_color
                elif not graph_color.replace('.','').isdigit():
                    print("Customizing options applied!")
                    pass
                else:
                    print('What! Anyways default settings applied.')
                
                time.sleep(0.3)
                print("Moving on: text options")
                time.sleep(0.1)
                font_type = str(input("you can set the font type (skip this by pressing enter):\n")).lower().strip()
                print_loading_message("Cheking the input!", "Done!")
                if not font_type:
                    print("default options applied!")
                    font_type = default_font_type
                elif not font_type.replace('.','').isdigit():
                    print("Customizing options applied!")
                    pass
                else:
                    print("What? Anyways default settings applied")
                
                font_size = numeric_user_input("set the font size pls(recommended 16pts):\n", default = default_font_size)

                font_color = str(input("you can set the font color (skip this by pressing etner):\n")).lower().strip()
                print_loading_message("Checking the input!", "Done!")
                if not font_color:
                    print("Default options applied!")
                    font_color = default_font_color
                elif not font_color.replace('.','').isdigit():
                    print("Customizing options applied!")
                    pass
                else :
                    print("What! Anyways default settings applied.")
            elif change_options == 'no':
                print("Default settings applied!")
                pass
            else:
                print("I cannot understand this! default settings applied!")    
                pass
            #adding the figure's code
            print_loading_message("Calculating DATA!", "Creating new figure done!") 
            data = np.random.normal(loc = loc_var if change_options == "yes" else default_loc_var , scale= scale_var if change_options == "yes" else default_scale_var, size= 1000)
            sns.histplot(data, kde = True, linewidth = 0, color = graph_color if change_options == "yes" else default_graph_color)
            #adding the title to the figure
            text_options = {'font_type' : font_type if change_options == "yes" else default_font_type, 'font_size' : font_size if change_options == "yes" else default_font_size, 'font_color' : font_color if change_options == "yes" else default_font_color}
            plt.title("NORMAL DISTRIBUTION", **text_options)
            plt.show()
        except ValueError as ve:
            print()
except ValueError as ve:
    print()

except KeyboardInterrupt as kbi:
    print()