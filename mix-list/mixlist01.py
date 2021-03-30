#!/usr/bin/env python3

# create a list containing three items
my_list = [ "192.168.0.5", 5060, "UP" ]

# display the first item in the list
print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
print("The last item in the list (state): " + my_list[2] )

new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#print out new list
print(new_list[5], new_list[4],new_list[3],new_list[2],new_list[2],new_list[0])

# Make a new directory in which we can store this project, /home/student/mycode/mix-list/

# student@beachhead:~$ mkdir -p /home/student/mycode/mix-list/

# Move into the ~/mycode/ directory.

 #student@beachhead:~$ cd ~/mycode/

# Great! Let's write a python script.

# student@beachhead:~/mycode$ vim mix-list/mixlist01.py

# Begin with a shebang line that will let your program run in Python 3. Copy the line below into the top line of your program.


#!/usr/bin/env python3
# Now create a list. In practice, we might read data in from an excel file, or an email. Lists are made with square brackets. The line below should be your second line.


# my_list = [ "192.168.0.5", 5060, "UP" ]
# Now let's write a line of code to return the IP address from out list. Notice that the first item in the list, is indexed as zero. Lists always begin at zero!


# print("The first item in the list (IP): " + my_list[0] )
# Now return the port 5060. The problem is 5060 is an integer, not a string. Strings are surrounded with quotes. We may not combine unlike data types within Python. So, below is the solution. We can force an integer value to be a string with the str() function.


# print("The second item in the list (port): " + str(my_list[1]) )
# Now return the last item in the list, this is a string value "UP".


# print("The last item in the list (state): " + my_list[2] )
# Put comments on the code you've written so far. Use previous lab examples as a guide. Remember, comments begin with # and always be descriptive

# At this time, your code should look something like the following:


#!/usr/bin/env python3

# create a list containing three items
# my_list = [ "192.168.0.5", 5060, "UP" ]

# display the first item in the list
# print("The first item in the list (IP): " + my_list[0] )

# display the second item in the list
# print("The second item in the list (port): " + str(my_list[1]) )

# display the third item in the list
# print("The last item in the list (state): " + my_list[2] )
# Save and exit with ESC and then :wq

# Run your script with Python 3.

# student@beachhead:~/mycode$ python3 mix-list/mixlist01.py

# The program should run. If it did not, then once again open your script, and find the bug.

