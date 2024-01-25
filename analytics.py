# Import HabitsDB class from database module
from database import HabitsDB
# Import Habit class from habit module
from habit import Habit
# Import datetime and timedelta classes from datetime module
from datetime import datetime, timedelta


# A function to get the names of all habits
def get_all_habits(db: HabitsDB) -> list:
    """
    Returns a list of the names of all the habits in the database.

    ...

    Parameters
    ----------
    db (HabitsDB): The database object containing the user habits

    Returns
    -------
    list: A list of strings representing the names of all habits
    """
    return list(map(lambda habit: habit.name, db.user_habits))


# A function to get the names of the habits for today
def get_habits_of_today(db: HabitsDB) -> list:
    """
    Returns a list of the names of the habits that are due today.

    ...

    Parameters
    ----------
    db (HabitsDB): The database object containing the user habits

    Returns
    -------
    list: A list of strings representing the names of the habits for today
    """
    return list(map(lambda habit: habit.name, filter(lambda habit: habit.periodicity == "DAILY" or (habit.periodicity == "WEEKLY"
        and datetime.today().date() - habit.completed_dates[len(habit.completed_dates) - 1].date()) == timedelta(days = 7), db.user_habits)))


# A function to get the names of the habits by their periodicity
def get_habits_by_periodicity(db: HabitsDB, p: str) -> list:
    """
    Returns a list of the names of the habits with the given periodicity.

    ...

    Parameters
    ----------
    db (HabitsDB): The database object containing the user habits
    p (str): The periodicity to filter by, either "DAILY" or "WEEKLY"

    Returns
    -------
    list: A list of strings representing the names of the habits by the given periodicity
    """
    return list(map(lambda habit: habit.name, filter(lambda habit: habit.periodicity == p, db.user_habits)))


# A function to get the longest streaks of all habits
def get_longest_streak_of_all_habits(db: HabitsDB) -> list:
    """
    Returns a list of strings representing dictionaries containing the names
    and the longest streaks of the all habits, sorted in descending order.

    ...

    Parameters
    ----------
    db (HabitsDB): The database object containing the user habits

    Returns
    -------
    list: A list of strings representing dictionaries of the form {habit_name : longest_streak}, sorted by the longest_streak value
    """
    return list(map(str, sorted(list(map(lambda habit: {habit.name : habit.get_longest_streak()},
        db.user_habits)), key = lambda x: x[list(x.keys())[0]], reverse = True)))


# A function to get the struggling habits
def get_struggling_habits(db: HabitsDB ) -> list:
    """
    Returns a list of the names of the habits that have a negligence rate greater than 30.

    ...

    Parameters
    ----------
    db (HabitsDB): The database object containing the user habits

    Returns
    -------
    list: A list of strings representing the names of the struggling habits
    """
    return list(map(lambda habit: habit.name, filter(lambda habit: habit.get_negligence_rate() > 30,
        db.user_habits)))


# A function to get the commitment rates of all habits
def get_commitment_rate_of_all_habits(db: HabitsDB) -> list:
    """
    Returns a list of strings representing dictionaries containing the names
    and commitment rates of all the habits, sorted in descending order.

    ...

    Parameters
    ----------
    db (HabitsDB): The database object containing the user habits

    Returns
    -------
    list: A list of strings representing dictionaries of the form {habit_name : commitment_rate},
    sorted by the commitment_rate value
    """
    return list(map(str, sorted(list(map(lambda habit: {habit.name : habit.get_commitment_rate()},
        db.user_habits)), key = lambda x: x[list(x.keys())[0]], reverse = True)))
    

        




