# Import datetime and timedelta classes from datetime module
from datetime import datetime, timedelta

# Constant tuple for the possible periodicity values
PERIODICITY: tuple = ("DAILY", "WEEKLY") 

# Habit class to represent a habit
class Habit:
    """ 
    Habit class to represent a personal habit.

    ...
       
    Atrributes
    ----------
    name: str
        The name of the habit.
    description: str
        A brief description of the habit.
    periodicity: str
        The frequency of the habit, either "DAILY" or "WEEKLY".
    creation_date: datetime
        The creation date and time of the habit object.
    completed_dates: list
        A list to store when the dates when the habit was completed.
       
    Methods
    -------
    mark_completed():
        Adds the current date and time to the completed_dates list if it is not
        already there.
    get_longest_streak():
        Returns the longest streak of consecutive dates of habit completions, 
        according to the periodicity of the habit.
    get_current_streak():
        Returns the current streak of consecutive dates of habit completions, 
        according to the periodicity of the habit.
    get_commitment_rate():
        Returns the percentage of dates when the habit was completed to the
        total numbers of dates, according to the periodicity of the habit.
    get_negligence_rate():
        Returns the percentage of dates when the habit was not completed to
        the total number of dates, according to the periodicity of the habit.
    get_habit_details():
        Returns a string that contains the details of a habit object,
        including its name, description, periodicity, creation date, commitment rate,
        negligence rate, current streak, and longest streak. 
    """

    # A constructor method to initialize a habit object
    def __init__(self, name: str, description: str, periodicity: str) -> None:
        """
        Constructs all the necessary attributes for the Habit object.

        ...

        Parameters
        ----------
        name: str
            The name of the habit.
        description: str
            A brief description of the habit.
        periodicity: str
            The frequency of the habit, either "DAILY" or "WEEKLY".
        """

        self.name: str = name
        self.description: str = description
        self.periodicity: str = periodicity
        self.creation_date: datetime = datetime.today()
        self.completed_dates: list = []
    
    # A method to mark the habit as completed for the current date and time.
    def mark_completed(self) -> None:
        """  
        Adds the current date and time to the completed_dates list if it is not
        already there.

        ...

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
  
        today = datetime.today()
        if today not in self.completed_dates:
            self.completed_dates.append(today)
    
    # A method to get the longest streak of consecutive habit completions.
    def get_longest_streak(self) -> int:
        """
        Returns the longest streak of consecutive dates of habit completions, 
        according to the periodicity of the habit.
        
        ...

        Parameters
        ----------
        None

        Returns
        -------
        int: the longest streak of the Habit object
        """
        
        # Check if the completed_dates list is empty
        if len(self.completed_dates) == 0:
            return 0

        # Check if the completed_dates list has only one element
        elif len(self.completed_dates) == 1:
            return 1

        # Otherwise, initialize two variables to store the current and longest streaks
        else:
            current_streak: int = 1
            longest_streak: int = 1

            # Check if the periodicity of the habit is "DAILY"
            if self.periodicity == PERIODICITY[0]:
                # Loop through the completed_dates list from the second element
                for d in range(1, len(self.completed_dates)):
                    # Calculate the difference between the current and previous dates
                    difference = self.completed_dates[d].date() - self.completed_dates[d-1].date()
                    # Check if the difference is one day
                    if difference == timedelta(days = 1):
                        current_streak += 1
                    # Check if the difference is more than one day
                    elif difference > timedelta(days = 1):
                        # Update the longest streak
                        if current_streak > longest_streak:
                            longest_streak = current_streak
                        current_streak = 1

            # Check if the periodicity of the habit is "WEEKLY"
            elif self.periodicity == PERIODICITY[1]:
                # Loop through the completed_dates list from the second element
                for d in range(1, len(self.completed_dates)):
                    # Calculate the difference between the current and previous date
                    difference = self.completed_dates[d].date() - self.completed_dates[d-1].date()
                    # Check if the difference is one week
                    if difference == timedelta(days = 7):
                        current_streak += 1
                    # Check if the difference is less than one week
                    elif difference < timedelta(days = 7):
                        pass
                    # Check if the difference is more than one week
                    elif difference > timedelta(days = 7):
                        # Update the longest streak
                        if current_streak > longest_streak:
                            longest_streak = current_streak
                        current_streak = 1

            if current_streak > longest_streak:
                longest_streak = current_streak
            # Return the longest streak
            return longest_streak
    
    # A method to get the currnet streak of consecutive habit completions
    def get_current_streak(self) -> int:
        """
        Returns the current streak of consecutive dates of habit completions, 
        according to the periodicity of the habit.
        
        ...

        Parameters
        ----------
        None

        Returns
        -------
        int: the current streak of the Habit object.
        """
        
        # Check if the completed_dates list is empty
        if len(self.completed_dates) == 0:
            return 0
        
        # Check if the completed_dates list has only one element
        elif len(self.completed_dates) == 1:
            return 1

        # Otherwise, initialize a variable to store the current streak
        else:
            current_streak = 1
            # Check if the periodicity of the habit is "DAILY"
            if self.periodicity == PERIODICITY[0]:
                # Loop through the completed_dates list from the last element backwards
                for d in reversed(range(0, len(self.completed_dates) - 1)):
                    # Calculate the difference between the current and previous dates
                    difference = self.completed_dates[d + 1].date()  - self.completed_dates[d].date()
                    # Check if the difference is one day
                    if difference == timedelta(days = 1):
                        current_streak += 1
                    # Check if the difference is more than one day
                    elif difference > timedelta(days = 1):
                        # If yes, return the current streak
                        return current_streak 
                # No interruptions, return the current streak  
                return current_streak
            
            # Check if the periodicity of the habit is "WEEKLY"
            elif self.periodicity == PERIODICITY[1]:
                # Loop through the completed_dates list from the last element backwards
                for d in reversed(range(len(self.completed_dates) - 1)):
                    # Calculate the difference between the current and previous dates
                    difference = self.completed_dates[d + 1].date()  - self.completed_dates[d].date()
                    # Check if the difference is one week
                    if difference == timedelta(weeks = 1):
                        current_streak += 1
                    # Check if the difference is more than one week
                    elif difference > timedelta(weeks = 1):
                        # If yes, return the current streak
                        return current_streak
                # No interruptions, return the current streak  
                return current_streak
    
    # A method to get the commitment rate of the habit
    def get_commitment_rate(self) -> float:
        """
        Returns the percentage of dates when the habit was completed to the 
        total number of dates, according to the periodicity of the habit. 
        
        ...

        Parameters
        ----------
        None

        Returns
        -------
        float: the percentage of completed dates
        """
        
        # Get the creation and current dates of the habit
        first_date: datetime =  self.creation_date.date()
        last_date: datetime = datetime.now().date()

        # Check if the periodicity of the habit is "DAILY"
        if self.periodicity == PERIODICITY[0]:
            # Calculate the total number of days since the creation of the habit
            total_dates: int = (last_date - first_date).days + 1
            # Get the number of dates when the habit was completed
            checked_dates: int = len(self.completed_dates)
            # Calculate the commitment rate as the ratio of checked dates to total dates
            commitment_rate: float = checked_dates/total_dates
            # Return the commitment rate as a percentage
            return float(commitment_rate*100)
        
        # Check if the periodicity of the habit is "WEEKLY"
        elif self.periodicity == PERIODICITY[1]:
            # Calculate the total number of weeks since the creation of the habit
            total_dates: int = int((last_date - first_date).days/7) + 1
            # Get the number of dates when the habit was completed
            checked_dates: int = len(self.completed_dates)
            # Calculate the commitment rate as the ratio of checked dates to total dates
            commitment_rate: float = checked_dates/total_dates
            # Return the commitment rate as a percentage
            return float(commitment_rate*100)
         # Otherwise, return an error value
        else:
            return -1.0

    
    # A method to get the negligence rate of the habit
    def get_negligence_rate(self) -> float:
        """
        Returns the percentage of dates when the habit was not completed to the
        total number of dates, according to the periodicity of the habit.
        
        ...

        Parameters
        ----------
        None

        Returns
        -------
        float: the percentage of not completed dates
        """

        # Get the commitment rate of the habit
        rate: float = self.get_commitment_rate()
        # Calculate the negligence rate as the complement of the commitment rate
        negligence_rate: float = 100.0 - self.get_commitment_rate()
        # Check for error
        if negligence_rate > 100:
            # Return error value
            return -1.0
        # Return the negligence rate as a percentage
        return float(negligence_rate)
    

    def get_habit_details(self) -> str:
        """
        Returns a string that contains the details of a habit object,
        including its name, description, periodicity, creation date, commitment rate,
        negligence rate, current streak, and longest streak.
        
        ...

        Parameters
        ----------
        None

        Returns
        -------
        string: contains the details of the habit object
        """

        # Use the f-string formatting to insert the values and return the string
        return f"""Habit: {self.name}\nDescription: {self.description}\nPeriodicity: {self.periodicity}\nCreation Date: {self.creation_date}\nCommitment Rate: {self.get_commitment_rate()}%\nNegligence Rate: {self.get_negligence_rate()}%\nCurrent Streak: {self.get_current_streak()}\nLongest Streak: {self.get_longest_streak()}"""
                
