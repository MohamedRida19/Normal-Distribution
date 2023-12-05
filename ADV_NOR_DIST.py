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