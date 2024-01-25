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

![image_7](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/738ebe2a-e0c4-4835-b314-de9744271008)  

#### Show Details of a Habit
Select the "Show Details" choice.  

![image_8](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/374e3000-ed78-4f7a-8d6c-c376dc20c77c)  

#### Delete a Habit
Select "Delete Habit" choice.  

![image_9](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/64e9b219-1887-41d7-8ce9-002fe0aa4ec5)  

### Habit Analytics
From the main menu, select the second choice "Analyze My Habits". You will get:  

![image_10](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/e859ff6c-e2ed-46f9-82fe-61b2ca9ef6ff)  

### Create a New Habit
From the main menu, select the third choice "Create New Habit".  

![image_11](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/58846d22-5862-4847-9627-7c846182cbae)  

![image_12](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/1464d0e1-aaf9-4077-96d2-99ab67138d35)  

![image_13](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/1dac3da6-e6b5-4036-9d7c-91db094cdb0d)  

![image_14](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/0af09bc7-0c11-4939-937e-621aa1a3c6a1)  

### Save and Quit
From the main menu, select the last choice "Save and Quit".

![image_15](https://github.com/NicolasAbboud/Habit-Tracker/assets/143742395/975645cf-45a4-4eff-bfcb-e5953611258f)  



## Tests

Open your terminal window and change the directory to your habit tracker folder.  
To test the Habit class, type the following:  

````commandline
pytest test_habit.py
````

To test the analytics module, type the following:  

````commandline
pytest test_analytics.py
````

Thank you for using the app.


