# Final Project for IS4010
This tool is a Workout Tracker. It will remember exercises, the weight used, and the repetitions done. This solves the problem of difficulty with tracking the last weight used for an exercise.

This program requires the dependencies FreeSimpleGUI and
The program can be run in VSCode or off of a batch file. To create the batch file, do the following:
1. open Notepad and enter this code (enter your own file path):
```@echo off
python "C:/Users/USERNAME/FinalProject/Python/WorkoutTracker.py
pause
```
2. save the text file as a batch file (.bat)
3. save the batch file to your home screen and run it from there or run it from file explorer

An of the code usage is:
Exercise: Bench Press
Weight: 135
Reps: 5
This would save "Bench Press" with weight of 135 and reps of 5
If you return and enter:
Exercise: Bench Press
Weight: 155
Reps: 2
It will overwrite the "Bench Press" exercise to have weight of 155 and reps of 2

Limitations:
Currently the program will only record one instance of an exercise and will not record a history. In the future this could be corrected by having the program create a comma seperated file so a history could be easily observed in Excel.

Future ideas:
1. The program could make suggestions, such as a 1 rep max to try for based on what weight the user achieves for multiple reps
2. The program could compute % weight increases on lifts over set periods of time (1 month, 1 year, 2 years, etc)
3. The GUI could be improved to be cleaner (EX: use capital letters) and look better (with more color and maybe visuals)