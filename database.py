# Import Habit class and PERIODICITY tuple from habit module
from habit import Habit, PERIODICITY
# Import date class from datetime module
from datetime import datetime
# Import os module
import os
# Import json module
import json

# A class to represent a database of habits
class HabitsDB:
    """ HabitsDB Class to store and manage a list of Habit objects.

        ...
       
        Atrributes
        ----------
        user_habits: list
            A list of Habit objects that stores the user's habits.
        here_path: str
            The path of the current file.
        json_file_name: str
            The name of the JSON file that stores the habits data.
       
        Methods
        -------
        from_Habit_to_dict(habit):
            Converts a Habit object to a dictionary.
        from_dict_to_Habit(habit_dict):
            Converts a dictionary to a Habit object.
        save(json_file):
            Saves the user_habits list to a JSON file.
        create_habit():
            Creates a new habit and adds it to the user_habits list.
        get_habit(habit_name):
            Returns the index of a habit in the user_habits list by its name, or -1 if not found.
        delete_habit(habit_name):
            Deletes a habit from the user_habits list by its name.
    """

    # A constructor method to initialize a HabitsDB object
    def __init__(self, file_name):
        """
        Constructs all the necessary attributes for the HabitsDB object.

        ...

        Parameters
        ----------
        None
        """

        # An empty list to store the user's habits as Habit objects
        self.user_habits: list = []  
        # Get the path of the current file
        self.here_path = os.path.dirname(os.path.abspath(__file__))
        # Join the path with the name of the JSON file and store it in a variable
        self.json_file_name = os.path.join(self.here_path, file_name)
        
        # Check if the JSON file exists
        if os.path.exists(self.json_file_name):
            # Open JSON file and load it as a list of dictionaries
            with open(self.json_file_name, "r") as file:
                habits_list: list = json.load(file)
    
                # Convert each dictionary to a Habit object and append it to the list
                for habit_dict in habits_list:
                    habit = self.from_dict_to_Habit(habit_dict)
                    self.user_habits.append(habit)
            


    # A method to convert a Habit object to a dictionary
    def from_Habit_to_dict(self, habit: Habit) -> dict:
        """
        Converts a Habit object to a dictionary and returns it.

        ...

        Parameters
        ----------
        habit (Habit): A Habit object to be converted to a dictionary

        Returns
        -------
        dict: A dictionary that contains the attributes of the Habit object
        """

        # Return a dictionary
        return {
            "name": habit.name,
            "description": habit.description,
            "periodicity": habit.periodicity,
            "creation_date": habit.creation_date.isoformat(),
            "completed_dates": [d.isoformat() for d in habit.completed_dates]
        }
    
    # A method to convert a dictionary to a Habit object
    def from_dict_to_Habit(self, habit_dict: dict) -> Habit:
        """
        Converts a dict object to a Habit object and returns it.
        
        ...

        Parameters
        ----------
        habit_dict (dict): A dictionary that contains the attributes of a Habit object

        Returns
        -------
        Habit: A Habit object that has the same attributes as the dictionary
        """

        # Create a Habit object using the name, description, and periodicity values from the dictionary
        habit: Habit = Habit(
            name = habit_dict["name"],
            description = habit_dict["description"],
            periodicity = habit_dict["periodicity"],
        )
        # Set the creation_date attribute of the Habit object
        habit.creation_date = datetime.fromisoformat(habit_dict["creation_date"])
        # Set the completed_dates attribute of the Habit object
        habit.completed_dates = [datetime.fromisoformat(d) for d in habit_dict["completed_dates"]]
        # Return the Habit object
        return habit
    
    # A method to save the user_habits list to a JSON file
    def save(self, json_file: str) -> None:
        """
        Dumps (saves) the user_habits list to the JSON file.
        
        ...

        Parameters
        ----------
        json_file (str): The name of the JSON file to save the data

        Returns
        -------
        None
        """

        # Convert each Habit object in the user_habits list to a dictionary
        greater_list: list = [self.from_Habit_to_dict(habit) for habit in self.user_habits]
        # Open the JSON file in write mode and dump the list of dictionaries to it.
        with open(json_file, "w") as file:
            json.dump(greater_list, file, indent = 4)
    
    # A method to get the index of a habit in the user_habits list by its name
    def get_habit(self, habit_name: str) -> int:
        """
        Returns the index of the habit by searching for it in the user_habits list by its name.
        
        ...

        Parameters
        ----------
        habit_name (str): The name of the habit to search for

        Returns
        -------
        int: The index of the habit in the user_habits list, or -1 if not found
        """

        for i in range(len(self.user_habits)):
             # Check if the name attribute of the current Habit object matches the habit_name
            if self.user_habits[i].name == habit_name:
                # Return the index
                return i
        # If the loop ends without finding a match, return -1
        return -1
        
    # A method to delete a habit from the user_habits list by its name
    def delete_habit(self, habit_name: str) -> None:
        """
        Deletes a habit from the user_habits list by its name.
        
        ...

        Parameters
        ----------
        habit_name (str): The name of the habit to delete

        Returns
        -------
        None
        """

        # Get the index of the habit in the user_habits list using the get_habit method
        index = self.get_habit(habit_name)
        # Check if the index is valid and the habit does exist
        if index >= 0:
            # Delete the Habit object
            del self.user_habits[index]
            

