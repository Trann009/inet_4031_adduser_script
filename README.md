# INET4031 Add Users Script and User List

## Program Description

This program is an automated tool designed to make adding users to a Linux system a simple step.
Normally, adding a user requires a series of commands that will often annoy others with this script.
It makes everything simple and easy, it'll read user information from an input file that has to be structured.
Creating the user accounts, passwords, and assigning them to groups if asked.

## Program User Operation
To run this program, the user will run the Python script and provide an input file. The script will ask
the user if they would want to dry run or not. After the dry run prompt the script will process the input file
line by line and perform the tasks.

## Input File Format

The input file must be a text file where each line contains the following fields, separated by the character ":"
** Username:Password:Last name:First Name: Groups(Doesn't have to be assigned and can be skipped using the character "-")**
Also, while running the file, please remember if lines start with the character "#", it will be skipped as the script treats them as a skip.
If the file format also doesnt contain 5 sections, it will also be skipped in the script.

## Command Execution
To run this command, you'll have to use **./create-users.py < create-users.input**. 
If that doesn't work the first time, you'll have to run this script **chmod +x create-user.py**

## Dry Run
When prompted to do a dry run, the script will run exactly the same, but the user accounts won't be created as the commands won't be executed in the system
This is a good way to test and find errors within your user input before executing the script.

