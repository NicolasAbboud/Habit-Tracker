# Import curses module
import curses

# A list of strings for the main menu options
main_menu: list = ["List My Habits", "Analyze My Habits", "Create New Habit", "Save and Quit"]

# A list of strings for the filtering options
filter_menu: list = ["Filter by:","Today's Habits", "Periodicity of Habits", "\n"]

# A list of strings for individual habit's menu options
one_habit_menu: list = ["Mark as Completed", "Show Details", "Delete Habit"]

# A list of strings for the analytics menu options
analytics_menu: list = ["Get the Longest Streak of All Habits (ordered)",
                        "Get the Commitment Rate of All Habits (ordered)",
                        "Get Struggling Habits"]

# A tuple of strings for the possible states of the program
state: tuple = ("MAIN", "LIST_HABITS", "TODAY_HABITS", "PERIODICITY_HABITS",
                 "ANALYTICS", "ONE_HABIT", "HABIT_DETAILS" , "CREATE_NEW_HABIT")


# A function to print the main menu on the screen
def print_main_menu(stdscr: curses.window, selected_row_index: int) -> None:
    """
    Prints the main menu on the screen.
    
    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    selected_row_index (int): The index of the currently selected menu option

    Returns
    -------
    None
    """

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()
    
    for index, row in enumerate(main_menu):
        # Calculate the x and y coordinates for the center of the screen
        x = w//2 - len(row)//2
        y = h//2 - len(main_menu)//2 + index
        # Check if the current index matches the selected row index
        if index == selected_row_index:
            # Change the color of the selected row
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        # Otherwise, add the menu option to the screen without any change in color
        else:
            stdscr.addstr(y, x, row)
    # Update the screen
    stdscr.refresh()

# A function to print the "list my habits menu" on the screen
def print_list_my_habits_menu(stdscr: curses.window, selected_row_index: int, all_habits: list) -> None:
    """
    Prints the "list my habits menu" on the screen.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    selected_row_index (int): The index of the currently selected menu option
    all_habits (list): A list of strings that represent the names of all the habits

    Returns
    -------
    None
    """
    
    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()

    for index, row in enumerate(filter_menu + ["ALL of My Habits:\n",] + all_habits):
        # Calculate the x and y coordinates for the center of the screen
        x = w//2 - len(row)//2
        y = h//2 - len(filter_menu)//2 + index
        # Check if the current index matches the selected row index and the index is not 0, 3, or 4
        if index == selected_row_index and (index != 0 or index != 3 or index  != 4):
            # Change the color of the selected row
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        # Otherwise, add the menu option to the screen without any change in color
        else:
            stdscr.addstr(y, x, row)
    # Update the screen
    stdscr.refresh()


# A function to print the habits for today on the screen
def print_today_habits_menu(stdscr: curses.window, selected_row_index: int, today_habits: list) -> None:
    """
    Prints the habits for today on the screen.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    selected_row_index (int): The index of the currently selected habit
    today_habits (list): A list of strings representing the habits for today

    Returns
    -------
    None
    """

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()

    for index, row in enumerate(["Today's Habits:", "\n"] + today_habits):
        # Calculate the x and y coordinates for the center of the screen
        x = w//2 - len(row)//2
        y = h//2 - (len(today_habits) + 2)//2 + index
        # Check if the current index matches the selected row index
        if index == selected_row_index and index != 0:
            # Change the color of the selected row
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        # Otherwise, add the menu option to the screen without any change in color
        else:
            stdscr.addstr(y, x, row)
    # Update the screen
    stdscr.refresh()

# A function to print the habits by their periodicity on the screen
def print_habits_by_periodicity_menu(stdscr: curses.window, selected_row_index: int, daily_habits: list, weekly_habits: list) -> None:
    """
    Prints the habits by their periodicity on the screen.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    selected_row_index (int): The index of the currently selected habit
    daily_habits (list): A list of strings representing the daily habits
    weekly_habits (list): A list of strings representing the weekly habits

    Returns
    -------
    None
    """

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()

    for index, row in enumerate(["Daily Habits:", "\n"] + daily_habits + ["\n", "\n", "Weekly Habits:", "\n"] + weekly_habits):
        # Calculate the x and y coordinates for the center of the screen
        x = w//2 - len(row)//2
        y = h//2 - (len(daily_habits + weekly_habits) + 6)//2 + index
        # Check if the current index matches the selected row index
        if index == selected_row_index:
            # Change the color of the selected row
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        # Otherwise, add the menu option to the screen without any change in color
        else:
            stdscr.addstr(y, x, row)
     # Update the screen
    stdscr.refresh()


# A function to print the menu for a single habit on the screen
def print_one_habit_menu(stdscr: curses.window, selected_row_index: int) -> None:
    """
    Prints the menu for a single habit on the screen.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    selected_row_index (int): The index of the currently selected menu option

    Returns
    -------
    None
    """

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()
    
    for index, row in enumerate(one_habit_menu):
        # Calculate the x and y coordinates for the center of the screen
        x = w//2 - len(row)//2
        y = h//2 - len(one_habit_menu) + index
        # Check if the current index matches the selected row index
        if index == selected_row_index:
            # Change the color of the selected row
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        # Otherwise, add the menu option to the screen without any change in color
        else:
            stdscr.addstr(y, x, row)
    # Update the screen
    stdscr.refresh()


# A function to print the analytics menu on the screen
def print_analytics_menu(stdscr: curses.window, selected_row_index: int) -> None:
    """
    Prints the analytics menu on the screen.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    selected_row_index (int): The index of the currently selected menu option

    Returns
    -------
    None
    """

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()

    for index, row in enumerate(analytics_menu):
        # Calculate the x and y coordinates for the center of the screen
        x = w//2 - len(row)//2
        y = h//2 - len(analytics_menu) + index
        # Check if the current index matches the selected row index
        if index == selected_row_index:
            # Change the color of the selected row
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        # Otherwise, add the menu option to the screen without any change in color
        else:
            stdscr.addstr(y, x, row)
    # Update the screen
    stdscr.refresh()


# A function to print a message when a habit is marked as completed
def print_marked_completed(stdscr: curses.window) -> None:
    """
    Prints a message when a habit is marked as completed.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses

    Returns
    -------
    None
    """

    # The message to be printed
    string: str = "Marked as completed successfully!"
    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()
    # Calculate the x and y coordinates for the center of the screen
    x = w//2 - len(string)//2
    y = h//2
    # Add the message to the screen
    stdscr.addstr(y, x, string)
    # Update the screen
    stdscr.refresh()


# A function to print a message when a habit is deleted
def print_delete(stdscr: curses.window) -> None:
    """
    Prints a message when a habit is deleted successfully.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses

    Returns
    -------
    None
    """
    # The message to be printed
    string: str = "Deleted the habit successfully!"
    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()
    # Calculate the x and y coordinates for the center of the screen
    x = w//2 - len(string)//2
    y = h//2
    # Add the message to the screen
    stdscr.addstr(y, x, string)
    # Update the screen
    stdscr.refresh()


# A function to print the details of a habit on the screen
def print_habit_details(stdscr: curses.window, details:str) -> None:
    """
    Prints the details of a habit on the screen.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    details (str): A string containing the details of the habit

    Returns
    -------
    None
    """

    # Split the details string by newline characters
    strings: list = details.split('\n')
    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()
    for index, row in enumerate(strings):
        # Calculate the x and y coordinates for the center of the screen
        x = w//2 - len(row)//2
        y = h//2 - len(strings) + index
         # Add the string to the screen
        stdscr.addstr(y, x, row)
     # Update the screen
    stdscr.refresh()


# A function to print the longest streaks of all habits on the screen
def print_longest_streaks(stdscr: curses.window, streaks: list) -> None:
    """
    Prints the longest streaks of all habits on the screen.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    streaks (list): A list of strings representing the longest streaks of all habits

    Returns
    -------
    None
    """

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()
    for index, row in enumerate(streaks):
        # Calculate the x and y coordinates for the center of the screen
        x = w//2 - len(row)//2
        y = h//2 - len(streaks) + index
        # Add the streak to the screen
        stdscr.addstr(y, x, row)
    # Update the screen
    stdscr.refresh()
    # Wait for the user to press a key
    key = stdscr.getch()
    # If the user presses the left arrow key, finish
    while(key != curses.KEY_LEFT):
        key = stdscr.getch()



# A function to print the commitment rates of all habits on the screen
def print_commitment_rates(stdscr: curses.window, rates: list) -> None:
    """
    Prints the commitment rates of all habits on the screen.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    rates (list): A list of strings representing the commitment rates of all habits

    Returns
    -------
    None
    """

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()

    for index, row in enumerate(rates):
        # Calculate the x and y coordinates for the center of the screen
        x = w//2 - len(row)//2
        y = h//2 - len(rates) + index
        # Add the commitment rate to the screen
        stdscr.addstr(y, x, row)
        # Update the screen
    stdscr.refresh()
    # Wait for the user to press a key
    key = stdscr.getch()
    # If the user presses the left arrow key, finish
    while(key != curses.KEY_LEFT):
        key = stdscr.getch()


# A function to print the struggling habits on the screen
def print_struggling_habits(stdscr: curses.window, struggling: list) -> None:
    """
    Prints the struggling habits on the screen.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    struggling (list): A list of strings representing the struggling habits

    Returns
    -------
    None
    """

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()
    for index, row in enumerate(struggling):
        # Calculate the x and y coordinates for the center of the screen
        x = w//2 - len(row)//2
        y = h//2 - len(struggling) + index
        # Add the habit to the screen
        stdscr.addstr(y, x, row)
    # Update the screen
    stdscr.refresh()
    # Wait for the user to press a key
    key = stdscr.getch()
    # If the user presses the left arrow key, finish
    while(key != curses.KEY_LEFT):
        key = stdscr.getch()


# A function to get a string from the user
def get_string(stdscr: curses.window, y: int, x: int) -> str:
    """
    Gets a string from the user.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    y (int): The y coordinate for the input
    x (int): The x coordinate for the input

    Returns
    -------
    str: The string entered by the user
    """
    
    # Hide the cursor
    curses.curs_set(0)
    # Get the first key pressed by the user
    key: chr = stdscr.getkey()
    # An empty list to store the characters
    string: list = []
    # Loop until the user presses the enter key or the right arrow key
    while (key != '\n' and  key != 'KEY_RIGHT'):
        # If the key is the backspace key and the string is not empty
        if (key == curses.KEY_BACKSPACE or key == '\b') and len(string) != 0:
            # Delete the last character from the string
            del string[len(string) - 1]
            # Delete the last line from the screen
            stdscr.deleteln()
            # Add the updated string to the screen
            stdscr.addstr(y, x, "".join(string))
         # Otherwise, if the key is a valid character
        else:
            # Append the key to the string
            string.append(key)
            # Add the updated string to the screen
            stdscr.addstr(y, x, "".join(string))
        # Update the screen
        stdscr.refresh()
        # Get the next key pressed by the user
        key: chr = stdscr.getkey()
    # Return the string list as a single str object
    return "".join(string)


# A function to print the periodicity choices on the screen
def print_periodicity_choice(stdscr: curses.window, y: int, x: int, current_row_index: int) -> None:
    """
    Prints the periodicity choices on the screen, either "DAILY" or "WEEKLY".

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    y (int): The y coordinate for the choices
    x (int): The x coordinate for the choices
    current_row_index (int): The index of the currently selected choice

    Returns
    -------
    None
    """

    # The choices as a list of strings
    choices: list = ["DAILY", "WEEKLY"]

    for index, row in enumerate(choices):
        # Check if the index matches the current row index
        if  index == current_row_index:
            # Change the color of the selected choice
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y + index, x, row)
            stdscr.attroff(curses.color_pair(1))
        # Otherwise, add the choice to the screen without any change in color
        else:
            stdscr.addstr(y + index, x, row)
    # Update the screen
    stdscr.refresh()


# A function to print the create new habit page on the screen
def print_create_new_habit(stdscr: curses.window, selected_row_index: int) -> tuple:
    """
    Prints the create new habit page on the screen.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses
    selected_row_index (int): The index of the currently selected menu option

    Returns
    -------
    tuple: A tuple of strings containing the name and description of the new habit
    """

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()
    # Calculate the x and y coordinates for the center of the screen
    x = w//2 - len("Enter habit name:")//2
    y = h//2 - 6//2

    # Add the prompt for the habit name to the screen
    stdscr.addstr(y, x, "Enter habit name:")
    name: str = get_string(stdscr, y + 1, x)
    stdscr.refresh()
    
    # Add the prompt for the habit description to the screen
    stdscr.addstr(y + 2, x, "Enter habit description:")
    description: str = get_string(stdscr, y + 3, x)
    stdscr.refresh()

    # Return the name and description of the new habit
    return name, description


# A function to print a message when a habit is created
def print_created(stdscr: curses.window) -> None:
    """
    Prints a message when a habit is created.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses

    Returns
    -------
    None
    """

    # The message to be printed
    string: str = "Habit was created successfully!"

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()
    # Calculate the x and y coordinates for the center of the screen.
    x = w//2 - len(string)//2
    y = h//2
    # Add the message to the screen.
    stdscr.addstr(y, x, string)
    # Update the screen.
    stdscr.refresh()


# A function to print a message when the data is saved
def print_saved(stdscr: curses.window) -> None:
    """
    Prints a message when the data is saved.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses

    Returns
    -------
    None
    """

    # The message to be printed
    string: str = "Saved data successfully!"

    # Get the height and width of the screen
    h, w = stdscr.getmaxyx()
    # Calculate the x and y coordinates for the center of the screen.
    x = w//2 - len(string)//2
    y = h//2
    # Add the message to the screen.
    stdscr.addstr(y, x, string)
    # Update the screen
    stdscr.refresh()

