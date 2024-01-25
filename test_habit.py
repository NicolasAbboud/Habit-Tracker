# Import Habit, HabitsDB, datetime, and timedelta classes
from habit import Habit
from database import HabitsDB
from datetime import datetime, timedelta

# Import the json and pytest modules
import json
import pytest


# A test class for the Habit class
class TestHabit:

    # A setup method that runs before each test method
    def setup_method(self):
        self.db: HabitsDB = HabitsDB("test_data.json")
        self.habit = Habit("Read", "Read for 1 hour", "DAILY")
    

    # A method to test the mark_completed method
    def test_mark_completed(self):
        self.habit.mark_completed()
        assert len(self.habit.completed_dates) == 1 and isinstance(self.habit.completed_dates[0], datetime)


    # A method to test the get_longest_streak method
    def test_get_longest_streak(self):
        longest_streak = self.db.user_habits[0].get_longest_streak()
        assert longest_streak == 18
        longest_streak = self.db.user_habits[1].get_longest_streak()
        assert longest_streak == 17
        longest_streak = self.db.user_habits[2].get_longest_streak()
        assert longest_streak == 7
        longest_streak = self.db.user_habits[3].get_longest_streak()
        assert longest_streak == 3
        longest_streak = self.db.user_habits[4].get_longest_streak()
        assert longest_streak == 4


    # A method to test the get_current_streak method
    def test_get_current_streak(self):
        current_streak = self.habit.get_current_streak()
        assert current_streak == 0

        self.db.user_habits[0].completed_dates.append(datetime.now() - timedelta(days = 1))
        self.db.user_habits[0].completed_dates.append(datetime.now())
        current_streak = self.db.user_habits[0].get_current_streak()
        assert current_streak == 2

        for i in range(0, 5):
            self.db.user_habits[1].completed_dates.append(datetime.now() + timedelta(days = i))
        current_streak = self.db.user_habits[1].get_current_streak()
        assert current_streak == 5

        for i in range(0, 1):
            self.db.user_habits[3].completed_dates.append(datetime.now() + timedelta(days = 7*i))
        current_streak = self.db.user_habits[3].get_current_streak()
        assert current_streak == 1


    # A method to test the get_commitment_rate method
    def test_get_commitment_rate(self):
        commitment_rate = self.db.user_habits[0].get_commitment_rate()
        total_number_of_dates = (datetime.today() - self.db.user_habits[0].creation_date).days + 1
        number_of_completed_dates = 23
        assert commitment_rate - float(number_of_completed_dates/total_number_of_dates*100) <= 0.1

        commitment_rate = self.db.user_habits[2].get_commitment_rate()
        total_number_of_dates = (datetime.today() - self.db.user_habits[2].creation_date).days + 1
        number_of_completed_dates = 17
        assert commitment_rate - float(number_of_completed_dates/total_number_of_dates*100) <= 0.1

        commitment_rate = self.db.user_habits[3].get_commitment_rate()
        total_number_of_dates = int((datetime.today() - self.db.user_habits[3].creation_date).days/7) + 1
        number_of_completed_dates = 3
        assert commitment_rate - float(number_of_completed_dates/total_number_of_dates*100) <= 0.1
        
        commitment_rate = self.db.user_habits[4].get_commitment_rate()
        total_number_of_dates = int((datetime.today() - self.db.user_habits[4].creation_date).days/7) + 1
        number_of_completed_dates = 4
        assert commitment_rate - float(number_of_completed_dates/total_number_of_dates*100) <= 0.1


    
    # A method to test the get_negligence_rate method
    def test_get_negligence_rate(self):
        negligence_rate = self.db.user_habits[0].get_negligence_rate()
        total_number_of_dates = (datetime.today() - self.db.user_habits[0].creation_date).days + 1
        number_of_completed_dates = 23
        assert negligence_rate - (100 - float(number_of_completed_dates/total_number_of_dates*100)) <= 0.1

        negligence_rate = self.db.user_habits[2].get_negligence_rate()
        total_number_of_dates = (datetime.today() - self.db.user_habits[2].creation_date).days + 1
        number_of_completed_dates = 17
        assert negligence_rate - (100 - float(number_of_completed_dates/total_number_of_dates*100)) <= 0.1
        
        negligence_rate = self.db.user_habits[3].get_negligence_rate()
        total_number_of_dates = int((datetime.now().date() - self.db.user_habits[3].creation_date.date()).days/7) + 1
        number_of_completed_dates = 3
        assert negligence_rate - (100 - float(number_of_completed_dates/total_number_of_dates*100)) <= 0.1
        
        negligence_rate = self.db.user_habits[4].get_negligence_rate()
        total_number_of_dates = int((datetime.now().date() - self.db.user_habits[4].creation_date.date()).days/7) + 1
        number_of_completed_dates = 4
        assert negligence_rate - (100 - float(number_of_completed_dates/total_number_of_dates*100)) <= 0.1
    

    # A method to test the get_habit_details method
    def test_get_habit_details(self):
        self.habit.creation_date = datetime.today() - timedelta(days = 1)
        self.habit.mark_completed()
        string = self.habit.get_habit_details()
        print(self.habit.get_commitment_rate())
        assert string == f"""Habit: Read\nDescription: Read for 1 hour\nPeriodicity: DAILY\nCreation Date: {self.habit.creation_date}\nCommitment Rate: 50.0%\nNegligence Rate: 50.0%\nCurrent Streak: 1\nLongest Streak: 1"""
