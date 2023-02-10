# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import *
from tkinter import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'initiating, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# turtle drawing
def drawing(type_of_action=[], colours=[], cursor_widths=[],  circle_radii=[], distance_of_moves=[], angle_of_turns=[]):
    line_num = 0
    circle_num = 0
    turn_num = 0
    pendown()
    for each_move in range(len(type_of_action)):
        print(each_move)
        # changing general/unspecified things
        pensize(6)
        color("black")
        # checking for each type of line and drawing it
        if type_of_action[each_move] == "line":
            forward(distance_of_moves[line_num])
            line_num += 1
        elif type_of_action[each_move] == "circle":
            circle(circle_radii[circle_num])
            circle_num += 1
        elif type_of_action[each_move] == "turn":
            right(angle_of_turns[turn_num])
            turn_num += 1
    # exiting gracefully
    done()


def front_end():
    # setting up tkinter
    screen = Tk()
    title("draw a pic m8")
    # creating the widgets
    # fonts
    the_header = Label(screen, text="Alistairs Tkinter-turtle integration", font=header_font)
    # start making your lines button
    create_individual_lines = Button(screen, text="create lines individually", command=single_line_feature_creation)
    # create a pattern instead button
    create_pattern = Button(screen, text="create lines using pattern", command=create_your_pattern)
    # placing on the screen
    create_individual_lines.grid(row=3, column=1, sticky=E)
    create_pattern.grid(row=3, column=2, sticky=W)
    the_header.grid(row=1, column=1, columnspan=2)
    # exiting gracefully
    screen.mainloop()


def create_your_pattern():
    print("create your pattern")


def single_line_feature_creation():
    # create the features of each line
    print("customise your lines")
    global move_type, move_type_value
    # general variables
    move_type = IntVar()
    move_type_value = IntVar()
    line_input = Toplevel()

    # general title
    new_window_title = Label(line_input, text="Modify your movements", font=("Times", 32))
    # choosing the type of movement
    type_of_movement = Frame(line_input)
    movement_type_title = Label(type_of_movement, text="Choose the Type of Movement", font=subtitle_font)
    line_type = Radiobutton(type_of_movement, text="line", variable=move_type, value=1)
    rotation_type = Radiobutton(type_of_movement, text="rotate", variable=move_type, value=2)
    circle_type = Radiobutton(type_of_movement, text="circle", variable=move_type, value=3)
    # general title implemented
    new_window_title.grid(row=1, column=1)
    # frame for radiobuttons (and radiobuttons with their title) implemented
    type_of_movement.grid(row=2, column=1, rowspan=4)
    movement_type_title.grid(row=1, column=1)
    line_type.grid(row=2, column=1)
    rotation_type.grid(row=3, column=1)
    circle_type.grid(row=4, column=1)

    # frame for the values that shall be assigned
    values = Frame(line_input)
    # subtitle
    choose_amount_of_movement = Label(values, text="Choose Amount of Movement", font=subtitle_font)
    # choose the value spinbox
    line_value = Spinbox(values, from_=-360, to=360, font=spinbox_font, textvariable=move_type_value)
    #sutitle
    choose_width = Label(values, text = "choose line width", font= subtitle_font)

    # dedicate values

    # function for button
    def dedicate_the_movement():
        move_type_list.append(assign_type(move_type.get()))
        line_input.destroy()
        find_where_to_append()
        drawing(move_type_list, colours_list, cursor_widths_list, circle_radii_list, distance_of_moves_list, angle_of_turns_list)
        print(move_type_list, distance_of_moves_list, angle_of_turns_list, circle_radii_list)

    #button to dedicate
    dedicate_values = Button(values, text="create movement", command=dedicate_the_movement)
        
    # value spinbox implemented
    values.grid(row=6, column=1)
    choose_amount_of_movement.grid(row=1, column=1)
    dedicate_values.grid(row=5, column=1)
    # actual spinbox implementations now
    line_value.grid(row=2, column=1)
    choose_width.grid(row=3, column=1)
    line_input.mainloop()
       
       
def find_where_to_append():
    if move_type.get() == 1:
        distance_of_moves_list.append(move_type_value.get())
        return
    if move_type.get() == 2:
        angle_of_turns_list.append(move_type_value.get())
        return
    if move_type.get() == 3:
        circle_radii_list.append(move_type_value.get())
        return


def assign_type(type):
    if type == 1:
        return "line"
    if type == 2:
        return "turn"
    if type == 3:
        return "circle"


def main():
    front_end()


if __name__ == '__main__':
    print_hi('main program')
    # more general variables
    header_font = "Times 30 underline"
    subtitle_font = "Times 16"
    spinbox_font = "Times 20"
    # variables that will go into the function
    move_type_list = []
    colours_list = []
    cursor_widths_list = []
    circle_radii_list = []
    distance_of_moves_list = []
    angle_of_turns_list = []
    # initiation
    main()
