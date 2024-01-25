# Import Habit, HabitsDB, datetime, and timedelta classes
from habit import Habit
from database import HabitsDB
from datetime import datetime, timedelta

# Import the analytics, json, and pytest modules
import analytics
import json
import pytest


# Create a HabitsDB object with the testing data
db: HabitsDB = HabitsDB("test_data.json")


# A function to test the get_all_habits function 
def test_get_all_habits():
    all_habits = analytics.get_all_habits(db)
    assert all_habits == ["Coding", "Exercise", "Learn German", "Go to Church", "Call a Relative"]


# A function to test the get_habits_of_today function
def test_get_habits_of_today():
    db.user_habits[3].completed_dates.append(datetime.today() - timedelta(days = 7))
    db.user_habits[4].completed_dates.append(datetime.today() - timedelta(days = 7))
    today_habits = analytics.get_habits_of_today(db)
    assert today_habits == ["Coding", "Exercise", "Learn German", "Go to Church", "Call a Relative"]


# A function to test the get_habits_by_periodicity function
def test_get_habits_by_periodicity():
    daily = analytics.get_habits_by_periodicity(db, "DAILY")
    weekly = analytics.get_habits_by_periodicity(db, "WEEKLY")
    assert daily == ["Coding", "Exercise", "Learn German"] and weekly == ["Go to Church", "Call a Relative"]


# A function to test the get_longest_streak_of_all_habits function
def test_get_longest_streak_of_all_habits():
    longest_streaks = analytics.get_longest_streak_of_all_habits(db)
    assert longest_streaks == [str({"Coding": 18}), str({"Exercise": 17}), str({"Learn German": 7}), str({"Call a Relative": 4}), str({"Go to Church": 2})]


# A function to test the get_commitment_rate_of_all_habits function
def test_get_commitment_rate_of_all_habits():
    # For each habit in the database, create a dictionary with the habit name and the commitment rate
    rate_0 = {db.user_habits[0].name: db.user_habits[0].get_commitment_rate()}
    rate_1 = {db.user_habits[1].name: db.user_habits[1].get_commitment_rate()}
    rate_2 = {db.user_habits[2].name: db.user_habits[2].get_commitment_rate()}
    rate_3 = {db.user_habits[3].name: db.user_habits[3].get_commitment_rate()}
    rate_4 = {db.user_habits[4].name: db.user_habits[4].get_commitment_rate()}
    
    # Create a list of the dictionaries and sort it by the commitment rate in descending order
    rates = sorted([rate_0, rate_1, rate_2, rate_3, rate_4], key = lambda x: x[list(x.keys())[0]], reverse = True)
    # Convert each dictionary to a string and store it in the same list
    for i in range(len(rates)):
        rates[i] =str(rates[i])

    commitment_rates = analytics.get_commitment_rate_of_all_habits(db)
    assert commitment_rates == rates


# A function to test the get_struggling_habits function
def test_get_struggling_habits():
    # For each habit in the database, create a dictionary with the habit name and the negligence rate
    rate_0 = {db.user_habits[0].name: db.user_habits[0].get_negligence_rate()}
    rate_1 = {db.user_habits[1].name: db.user_habits[1].get_negligence_rate()}
    rate_2 = {db.user_habits[2].name: db.user_habits[2].get_negligence_rate()}
    rate_3 = {db.user_habits[3].name: db.user_habits[3].get_negligence_rate()}
    rate_4 = {db.user_habits[4].name: db.user_habits[4].get_negligence_rate()}
    # Create a list of the dictionaries
    rates = [rate_0, rate_1, rate_2, rate_3, rate_4]
    # Create a list of the habit names that have a negligence rate higher than 30%
    struggles = [name for rate in rates for name, value in rate.items() if value > 30]

    struggling_habits = analytics.get_struggling_habits(db)
    assert struggling_habits == struggles