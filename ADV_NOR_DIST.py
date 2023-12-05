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
def print_loading_message(message):
    print(message, end='', flush= False)
    for i in range(3):
        time.sleep(0.2)
        print('.', end=' ', flush=False)
    time.sleep(0.1)
    print(message)