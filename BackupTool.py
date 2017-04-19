#Creator: Cody Puskas
import sys
import time
import os
import shutil
import glob

date = (time.strftime("%m%d%y"))

#The user enters file path
while True:
    try:
        save_location = str(raw_input("Enter a file path to backup your data: "))
        save_location = save_location + "\\" + date
        break
    except ValueError:
        print "Invalid input"

#Creates folder if it doesn't exist
if not os.path.exists(save_location):
    os.makedirs(save_location)

print "Save location: " + save_location

#The user enters the database they want to save
while True:
    try:
        database = raw_input("Enter the database you want to save as a file path: ")
        print "Database being saved: " + database
        break
    except ValueError:
        print "Invalid input"

#Checks if database exists
if os.path.exists(database):
    print "Database exists"

#Checks for lock file in database
lock_file = glob.glob(database + "\*.lock")
if (len(lock_file) > 0):
    print("Lock file exist in database")
    sys.exit()

x = 1
final_location = save_location + "\\0" + str(x)
#Creates file when user backs up less than 9 times
while (x < 9):
    try:
        os.makedirs(final_location)
        break
    except WindowsError:
        x += 1
        final_location = save_location + "\\0" + str(x)
        
#Creates file when user backs up more than 9 times
while (x >= 9):
    try:
        os.makedirs(final_location)
        break
    except WindowsError:
        x += 1
        final_location = save_location + "\\" + str(x)

final_location = final_location + "\\" + os.path.basename(database)
shutil.copytree(database, final_location)

print(final_location)
print("Backup successful")
input()
