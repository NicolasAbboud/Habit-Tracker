# Habit Tracker Application

This application will help users track and maintain their desired behaviors and will facilitate habit formation for them by tracking their 
habits and providing them with tools to analyze those habits. 


## Why do you need it?

- A habit tracker application can make your goals feel more attainable by breaking them down into small, daily actions that you can track and measure.

- A habit tracker application can keep you focused by reminding you of your habits and helping you avoid distractions and temptations. It can also help you create a consistent routine and schedule for your habits.

- A habit tracker application can help you to eliminate bad habits and develop healthy ones.


## Installation

### Python 3.9.0 
First of all, you have to download the python 3.9.0 version on your operating system. You can download this from python's [official website](https://www.python.org/downloads/).

### The needed packages

Curses for Windows:
````commandline
pip install windows-curses
````

Pytest:
````commandline
pip install pytest
```` 


## Usage

Open your terminal window and change the directory to your habit tracker folder.  
Type the following:

````commandline
python main.py
````

Now the programming is running and you should see the main menu.  

![image_1](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/ff825ed6-051e-49a9-aefd-d51be36e8e1b)  

To navigate the menus, use the arrow keys:  
UP Key to move to the upper choice.  
DOWN Key to move to the lower choice.  
RIGHT Key or ENTER Key to select a choice.
LEFT Key to go back.

### Viewing Your Habits
Select the first choice "List My Habits", you will get this:  

![image_2](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/6c34c4e8-7ee5-4455-98cd-c005075045d8)  

Now you can easily see all of your habits. You can filter them. Select "Today's Habits" to get the habits you should complete today or select "Periodicity of Habits" to get the Habits divided by their periodicity, "DAILY" and "WEEKLY".

![image_3](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/c75bd93c-0889-4d02-95b0-fe0dd477d0f6)  

![image_4](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/fd190f36-3165-438d-8406-d61d94da7aec)  

### Operations on Individual Habits
Select the habit on which you want to do an operation.  

![image_5](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/c32500c8-e7a6-457a-ab68-713d5b553174)  

You will get the following screen:  

![image_6](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/b9c82d64-cc22-4e02-8527-1a4748630f2d)  

#### Mark as Completed
Select the "Mark as Completed" choice.











## Tests

'''shell
pytest .
'''

Note: This is not enough, you should put more effort to it.


