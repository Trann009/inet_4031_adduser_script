#!/usr/bin/python3

# INET4031
# Sean Tran-Nguyen
# March 22nd 2026
# March 22nd 2026

#Import os helps provide a portable way to use OS functionality like creating, path manipluation, running processes, etc. All the normal stuff that could happen in an OS.
#Import re helps finding specific patterns in text and string manipulation. Could be used to find certain words, letters, or even splitting them up by a letter.
#Import sys helps interact with the python interpreter.
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPT"
#The input asks if you would want to Dry Run or not asking for user input. 
#The input file reads the file that is directed towards it and reads all the lines.
def main():
    answer = input("Would you like to dry-run (Y-N) : ")
    input_file = "create-users.input"
    with open(input_file, 'r') as f:
       for line in f:

        #It counts the lines in the code then proceeds to run it that many times. If the line has a # it'll skip the entire line.
        #The important part is WHY it is looking for a particular characer - what is that character being used for?
        match = re.match("^#",line)

        #The code is splitting up using the character ":" because it needs the username,password,lastname, first name, and group.
        fields = line.strip().split(':')

        # Doesnt allow for match or fields to = 5 as this would mean that it doesnt have enough fields for it to be processed since it would basically be invalid. 
        #If the statement were to become true then it would skip that entire line.
        #The IF statement relies on the first two parts of the code because it will allow for them to check if it's a valid input to make a group for them or not.
        #It's checking the code if it's !=5 because it wants to make sure it's a valid user entry.
        if match or len(fields) != 5:
            continue

        # The purpose of the next 3 lines is so that it can split up the information that is being processed from the list.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # This split is being done because in the file it starts using the character "," for the groups they are in.
        groups = fields[4].split(',')

        # Let's you keep track and be able to see what accounts are being created for who
        print("==> Creating account for %s..." % (username))
        # Creates a new user and sets all the information for them. Disables the password since it hasnt been created yet.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #This helps create a folder or file in your home directory.
        #If uncommented the command won't run so the files or users won't be created.
	#Only prints if it's a dry-run which would be Y and actually runs the command if it isn't indicated by an "N"
        if answer.lower() == "y":
                print(cmd)
        if answer.lower() == "n":
        	os.system(cmd)

        # Allows for you to see the password that is set for the user.
        print("==> Setting the password for %s..." % (username))
        # This line creates the password for the user and reenables it so that they can use it to login to their account.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)


        #This helps create a folder or file in your home directory.
        #The first time you run the code...what should you do here?  If uncommented - what will the os.system(cmd) statemetn attempt to do?
        #If uncommented the command won't run so the files or users won't be created.
        if answer.lower() == "y":
                print(cmd)
        if answer.lower() == "n":
                os.system(cmd)


        for group in groups:
            #It will skip the group input since the character "-" will tell it that it doesn't have a group therefore it'll not assign the user to a group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                if answer.lower() == "y":
                     print(cmd)
                if answer.lower() == "n":
                     os.system(cmd)

if __name__ == '__main__':
    main()
