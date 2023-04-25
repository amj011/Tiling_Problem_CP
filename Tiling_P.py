import tkinter as tk
from tkinter.font import Font
import time

# Dynamic Programming Solution
def count_ways_dp(n, m):
    # Create a table to store the number of ways to tile each width up to n
    table = [0] * (n + 1)
    # Set the base case values
    table[0] = 1
    table[1] = 1
    # Fill in the rest of the table using dynamic programming
    for i in range(2, n + 1):
        if i < m:
            table[i] = 1
        elif i == m:
            table[i] = 2
        else:
            table[i] = table[i - 1] + table[i - m]
    # Return the number of ways to tile a width of n
    return table[n]

# Divide and Conquer Solution
def count_ways_dc(n, m):
    if n < m:
        return 1
    if n == m:
        return 2
    # Divide the problem into two subproblems and recursively solve them
    return count_ways_dc(n - 1, m) + count_ways_dc(n - m, m)

# Backtracking with Recursion Solution
def count_ways_bt(n, m):
    if n < m:
        return 1
    if n == m:
        return 2
    # Use backtracking with recursion to explore all possible tiling arrangements
    num_ways = 0
    for i in range(m, n + 1):
        num_ways += count_ways_bt(n - i, m)
    return num_ways

# GUI code
def calculate_ways():
    # Get the user input for the width and tile size from the text entry widgets
    n = int(width_entry.get())
    m = int(tile_entry.get())
    # Get the user choice for the method from the radio buttons
    method = var.get()

    start_time = time.time()

    # Calculate the number of ways to tile the width using the chosen method
    if method == 1:
        num_ways = count_ways_dp(n, m)
        method_str = "Dynamic Programming"
        time_c=" O(n) "
    elif method == 2:
        num_ways = count_ways_dc(n, m)
        method_str = "Divide and Conquer"
        time_c=" O(n^2) "
    else:
        num_ways = count_ways_bt(n, m)
        method_str = "Backtracking with Recursion"
        time_c=" O(2^n) "

    end_time = time.time()

    # Update the result label with the number of ways and method used
    result_label.config(text="Method :: {}\n\nTime Complexity :: {}\n\nNumber of ways :: {}\n\nTime taken :: {} seconds".format(method_str,time_c, num_ways, round(end_time - start_time, 6)))

# Create a GUI window
window = tk.Tk()
window.title("Tiling Problem")

# Set the font size for the window
font = Font(family="Helvetica", size=12)

# Set the size of the window
window.geometry("500x300")

width_label = tk.Label(window, text="Enter the width to be tiled:", font=font)
width_label.pack()
width_entry = tk.Entry(window, font=font)
width_entry.pack()

tile_label = tk.Label(window, text="Enter the width of the tile:", font=font)
tile_label.pack()
tile_entry = tk.Entry(window, font=font)
tile_entry.pack()

var_label = tk.Label(window, text="Enter the Approach you want :", font=font)
var_label.pack()
var = tk.Entry(window, font=font)
var.pack()




calculate_button = tk.Button(window, text="Calculate", font=font, command=calculate_ways, width=10)
calculate_button.pack(pady=10)

result_label = tk.Label(window, text="", font=font)
result_label.pack()


window.mainloop()
