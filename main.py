# Import Habit class and PERIODICITY tuple from habit module
from habit import Habit, PERIODICITY
# Import HabitsDB class from database module
from database import HabitsDB
# Import analytics module
import analytics
# Import menus module
import menus
# Import curses module
import curses
# Import time module
import time

# Create a database object (HabitsDB)
db: HabitsDB = HabitsDB("database.json")



def main(stdscr) -> None:
    """
    Runs the main loop of the program using curses.

    ...

    Parameters
    ----------
    stdscr (curses.window): The standard screen object for curses

    Returns
    -------
    None
    """

    # The color pair for the selected menu option
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    # Set the current index to zero
    current_row_index: int = 0
    # Set the current habit index to zero
    current_habit_index: int = 0
    # Set the current state to main menu
    state: str = menus.state[0]
    # Set the last state to None
    last_state: str = None
    
    # Get the habits for today
    today_habits: list = analytics.get_habits_of_today(db)
    # Get all the habits
    all_habits: list = analytics.get_all_habits(db)
    # Get the daily habits
    daily_habits: list = analytics.get_habits_by_periodicity(db, "DAILY")
    # Get the weekly habits
    weekly_habits: list = analytics.get_habits_by_periodicity(db, "WEEKLY")
    
    # Start the main loop
    while 1:
        # Check if the current state is main
        if state == menus.state[0]: # Main
            # Hide the cursor
            curses.curs_set(0)
            # Print the main menu on the screen
            menus.print_main_menu(stdscr, current_row_index)
            # Get the key pressed by the user
            key = stdscr.getch()
            # Check the key pressed by the user
            if key == curses.KEY_UP and current_row_index > 0:
                current_row_index -= 1
            elif key == curses.KEY_DOWN and current_row_index < 3:
                current_row_index += 1
            elif key == curses.KEY_ENTER or key in [10, 13] or key == curses.KEY_RIGHT:
                # If the current index is zero
                if current_row_index == 0:
                    # Change the state to list habits
                    state = menus.state[1]
                    current_row_index = 1
                    current_habit_index = 0
                # If the current index is one
                elif current_row_index == 1:
                    # Change the state to analytics
                    state = menus.state[4]
                    current_row_index = 0
                # If the current index is two
                elif current_row_index == 2:
                    # Change the state to create new habit
                    state = menus.state[7]
                    current_row_index = 0
                # If the current index is three
                elif current_row_index == 3:
                    # Save the database to a JSON file and break the while loop
                    db.save("database.json")
                    stdscr.clear()
                    menus.print_saved(stdscr)
                    curses.napms(2000)
                    break

            # Clear the screen
            stdscr.clear()
        
        # If the current state is list habits
        elif state == menus.state[1]: #LIST_HABITS
            # Get the length of the menu options and the habits
            length: int =  len(menus.filter_menu + all_habits) + 1
            # Hide the cursor
            curses.curs_set(0)
            # Print the list habits menu on the screen
            menus.print_list_my_habits_menu(stdscr, current_row_index, all_habits)
            # Get the key pressed by the user
            key = stdscr.getch()
            # Check the key pressed by the user
            if key == curses.KEY_UP and current_row_index > 1:
                if current_row_index != 5:
                    current_row_index -= 1
                else:
                    current_row_index -= 3
                    current_habit_index = 0

            elif key == curses.KEY_DOWN and current_row_index < length - 1:
                if current_row_index != 2:
                    current_row_index += 1
                else:
                    current_row_index += 3

            elif key == curses.KEY_ENTER or key in [10, 13] or key == curses.KEY_RIGHT:
                # If the current index is one
                if current_row_index == 1:
                    # Change the state to today habits
                    state = menus.state[2]
                    current_row_index = 2
                    current_habit_index = 0
                # If the current index is two
                elif current_row_index == 2:
                    # Change the state to filter habits
                    state = menus.state[3]
                    current_row_index = 2
                    current_habit_index = 0
                # If the current index is greater than four
                elif current_row_index > 4:
                    # Get the habit object by its name
                    current_habit_index = db.get_habit(all_habits[current_row_index - 5])
                    last_state = state
                    # Change the state to habit details
                    state = menus.state[5]
                    current_row_index = 0

            elif key == curses.KEY_LEFT:
                state = menus.state[0]
                current_row_index = 0
                current_habit_index = 0

            # Clear the screen
            stdscr.clear()

        
        # If the current state is today habits
        elif state == menus.state[2]: #TODAY_HABITS
            # Hide the cursor
            curses.curs_set(0)
            # Print the today habits menu on the screen
            menus.print_today_habits_menu(stdscr, current_row_index, today_habits)
            # Get the key pressed by the user
            key = stdscr.getch()
           # Check the key pressed by the user
            if key == curses.KEY_UP and current_row_index > 2:
                current_row_index -= 1

            elif key == curses.KEY_DOWN and current_row_index < 1 + len(today_habits):
                current_row_index += 1

            elif (key == curses.KEY_ENTER or key in [10, 13] or key == curses.KEY_RIGHT) and current_row_index > 1:
                # Get the habit object by its name
                current_habit_index = db.get_habit(today_habits[current_row_index - 2])
                last_state = state
                # Change the state to habit details
                state = menus.state[5]
                current_row_index = 0

            elif key == curses.KEY_LEFT:
                state = menus.state[1]
                current_row_index = 1
                current_habit_index = 0

            # Clear the screen
            stdscr.clear()

        
        # If the current state is periodicity habits
        elif state == menus.state[3]: #PERIODICITY_HABITS
            # Hide the cursor
            curses.curs_set(0)
            # Print the habits by periodicity menu on the screen
            menus.print_habits_by_periodicity_menu(stdscr, current_row_index, daily_habits, weekly_habits)
            # Get the key pressed by the user
            key = stdscr.getch()
            # Check the key pressed by the user
            if key == curses.KEY_UP and current_row_index > 2:
                if current_row_index == 1 + len(daily_habits) + 5:
                    current_row_index -= 5
                else:
                    current_row_index -= 1

            elif key == curses.KEY_DOWN and current_row_index < 5 + len(daily_habits + weekly_habits):
                if current_row_index == len(daily_habits) + 1:
                    current_row_index += 5
                else:
                    current_row_index += 1

            elif key == curses.KEY_ENTER or key in [10, 13] or key == curses.KEY_RIGHT:
                if current_row_index < 2 + len(daily_habits):
                    # Get the habit object's index by its name
                    current_habit_index = db.get_habit(daily_habits[current_row_index - 2])
                else:
                    # Get the habit object's index by its name
                    current_habit_index = db.get_habit(weekly_habits[current_row_index - (len(daily_habits) + 7)])
                last_state = state
                # Change the state to habit details
                state = menus.state[5]
                current_row_index = 0

            elif key == curses.KEY_LEFT:
                state = menus.state[1]
                current_row_index = 1
                current_habit_index = 0

            # Clear the screen
            stdscr.clear()

        # If the current state is analytics
        elif state == menus.state[4]: #ANLYTICS
            # Hide the cursor
            curses.curs_set(0)
            # Print the analytics menu on the screen
            menus.print_analytics_menu(stdscr, current_row_index)
            # Get the key pressed by the user
            key = stdscr.getch()
            # Check the key pressed by the user
            if key == curses.KEY_UP and current_row_index > 0:
                current_row_index -= 1

            elif key == curses.KEY_DOWN and current_row_index < 2:
                current_row_index += 1

            elif key == curses.KEY_ENTER or key in [10, 13] or key == curses.KEY_RIGHT:
                # If the current index is zero
                if current_row_index == 0:
                    # Clear the screen
                    stdscr.clear()
                    # Print the longest streaks of all habits on the screen
                    menus.print_longest_streaks(stdscr, analytics.get_longest_streak_of_all_habits(db))
                # If the current index is two
                elif current_row_index == 1:
                    # Clear the screen
                    stdscr.clear()
                    # Print the commitment rates of all habits on the screen
                    menus.print_commitment_rates(stdscr, analytics.get_commitment_rate_of_all_habits(db))
                # If the current index is two
                elif current_row_index == 2:
                    # Clear the screen
                    stdscr.clear()
                    # Print the struggling habits on the screen
                    menus.print_struggling_habits(stdscr, analytics.get_struggling_habits(db))

            elif key == curses.KEY_LEFT:
                current_row_index = 0
                state = menus.state[0]

            # Clear the screen
            stdscr.clear()
        

        # If the current state is one habit
        elif state == menus.state[5]: #ONE_HABIT
            # Hide the cursor
            curses.curs_set(0)
            # Print the one habit menu on the screen
            menus.print_one_habit_menu(stdscr, current_row_index)
            # Get the key pressed by the user
            key = stdscr.getch()
            # Check the key pressed by the user
            if key == curses.KEY_UP and current_row_index > 0:
                current_row_index -= 1

            elif key == curses.KEY_DOWN and current_row_index < 2:
                current_row_index += 1

            elif key == curses.KEY_ENTER or key in [10, 13] or key == curses.KEY_RIGHT:
                # If the current index is zero
                if current_row_index == 0:
                    # Mark the current habit as completed
                    db.user_habits[current_habit_index].mark_completed()
                    # Clear the screen
                    stdscr.clear()
                    # Print a message that the habit is marked as completed
                    menus.print_marked_completed(stdscr)
                    # Wait for three seconds
                    time.sleep(3)
                    # Clear the screen
                    stdscr.clear()
        
                # If the current index is one
                elif current_row_index == 1:
                    # Change the state to habit details
                    state = menus.state[6]
                 # If the current index is two
                elif current_row_index == 2:
                    # Delete the current habit from the database
                    db.delete_habit(db.user_habits[current_habit_index].name)
                    # Clear the screen
                    stdscr.clear()
                    # Print a message that the habit is deleted
                    menus.print_delete(stdscr)
                    # Wait for three seconds
                    time.sleep(3)
                    # Update the lists of habits
                    today_habits: list = analytics.get_habits_of_today(db)
                    all_habits: list = analytics.get_all_habits(db)
                    daily_habits: list = analytics.get_habits_by_periodicity(db, "DAILY")
                    weekly_habits: list = analytics.get_habits_by_periodicity(db, "WEEKLY")
                    # Clear the screen
                    stdscr.clear()

            elif key == curses.KEY_LEFT:
                current_row_index = 2
                state = last_state
                last_state = None

            # Clear the screen
            stdscr.clear()
        

        # If the current state is habit details
        elif state == menus.state[6]: #HABIT_DETAILS
            # Hide the cursor
            curses.curs_set(0)
            # Get the details of the current habit
            details: str = db.user_habits[current_habit_index].get_habit_details()
            # Print the habit details on the screen
            menus.print_habit_details(stdscr, details)
            # Get the key pressed by the user
            key = stdscr.getch()
            # Check the key pressed by the user
            if key == curses.KEY_LEFT:
                state = menus.state[5]
            
            # Clear the screen
            stdscr.clear()
        

        # If the current state is create new habit
        elif state == menus.state[7]: #CREATE_NEW_HABIT
            # Get the name and description for the new habit from the user
            habit_data: tuple = menus.print_create_new_habit(stdscr, current_row_index)
            key = None
            # Get the height and width of the screen
            h, w = stdscr.getmaxyx()
            # Calculate the x and y coordinates for the center of the screen
            x = w//2 - len("Enter Habit Name:")//2
            y = h//2 - 6//2
            # Print the prompt for choosing the habit periodicity
            stdscr.addstr(y + 4, x, "Choose Habit Periodicity:")
            # Start the loop
            while True:
                # Print the options for the habit periodicity
                menus.print_periodicity_choice(stdscr, y + 5, x, current_row_index)
                # Get the key pressed by the user
                key = stdscr.getch()
                # Check the key pressed by the user
                if key == curses.KEY_UP and current_row_index > 0:
                    current_row_index -= 1

                elif key == curses.KEY_DOWN and current_row_index < 1:
                    current_row_index += 1

                elif key == curses.KEY_ENTER or key in [10, 13] or key == curses.KEY_RIGHT:
                    # If the current index is zero
                    if current_row_index == 0:
                        # Create a new habit object with the given data and daily periodicity
                        new_habit = Habit(str(habit_data[0]), str(habit_data[1]), PERIODICITY[0])
                        db.user_habits.append(new_habit) 
                        break
                    # Otherwise,  # If the current index is one
                    else:
                        # Create a new habit object with the given data and weekly periodicity
                        new_habit = Habit(str(habit_data[0]), str(habit_data[1]), PERIODICITY[0])
                        db.user_habits.append(new_habit)
                        break

            # Update the lists of habits
            today_habits: list = analytics.get_habits_of_today(db)
            all_habits: list = analytics.get_all_habits(db)
            daily_habits: list = analytics.get_habits_by_periodicity(db, "DAILY")
            weekly_habits: list = analytics.get_habits_by_periodicity(db, "WEEKLY")
            # Flush the input buffer
            curses.flushinp()
            # Clear the screen
            stdscr.clear()
            # Print a message that the habit is created
            menus.print_created(stdscr)
            # Wait for three seconds
            time.sleep(3)
            # Clear the screen
            stdscr.clear()
            # Set the current index to zero
            current_row_index = 0
            # Change the state to main menu
            state = menus.state[0]        
            


# Check if "main.py" file is the one being run
if __name__ == "__main__":
    # Use the curses wrapper to run the main function
    curses.wrapper(main)
    # End the curses window
    curses.endwin()









