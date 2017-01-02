# email_grades
A python script I made to make it easier to email grades and individualized comments to students in one of my chem 102 lab classes.  It probably won't be applicable to you, but who knows?

@author: JonMeyers
http://orcid.org/0000-0002-6698-3420
Written for Python 3

This script was written to make much simpler the process of giving individualized student feedback within a short time of completing the grading.

Please note: this program doesn't have a nice user interface because I didn't need it and therefore didn't want to spend the time making it.


How does it work?

First, understand that I regularly emailed grades out for two different types of assignments: pre-lab assignments and in-lab asssignments (or lab participation points).  Thus, the code includes hard-code formatting for both types of assignments.  Obviously, you would have to change the hardcoding to fit your needs.

I kept my assignment records in one large excel workbook.  As I graded, I would write down individual comments in an Excel cell so that I didn't have to hand-write a lot of feedback.  Plus, this way, I could email them the feedback so they got the feedback before they handed in their next assignment.


When grading was finished, I copied most of the columns from that workbook into a temporary CSV file.  This is key to making this python program work.  The format is shown in the included CSV file.

-->Cell A1 is the assignment (pre-lab or in-lab).  This tells the code which formatting to use.

-->Cells C1 to K1 are the total point values available for each section of the rubric.  The total points available is 25.  The rubric is hard-coded in the python script.

-->Cell L1 is a comment that will be given to the entire class

-->Cell A2 is the student's first name

-->Cell B2 is the student's onyen (Only Name You'll Ever Need at UNC.  At other institutions, you can just use the students 365 user name).  This is how the program sends them an individual email.

-->Cells C2 to K2 are the points earned by the student for each section of the rubric.

-->Cell L2 is a comment that will only be given to the associated student.


Once the CSV is saved and ready, I opened the __main__.py file.

-->Make sure to enter the correct email settings

-->Change the subject of the email and the text you want to start the email with.  I also did a different valediction in each email.  I think it made the emails a bit more personal.

-->Save the file


Now the program is ready to run.  Open the command prompt, find the email_grades directory, and run the command:

python __main__.py

and the program should run.

-->It first shows you the preface to the email so you can make sure it was correct.  Confirm it's correct.

-->Now the program will go through each student listed in the CSV file and create an individualized email for them that includes the rubric breakdown, their points out of the possible points, and their total score.  It also gives them the average and maximum score in the class (I think that's great motivation).  It adds the comments to the entire class and to them personally.

-->The program will first send YOU the first email produced (the student at the top of the list) so you can confirm that the email looks correct.  If you say y, the program will proceed to send everyone their emails.

-->This generally takes less than a minute for a class of 20 students.  What a time saver!  And helpful to the students.

-->The program will then close.


And that's it!  Next time you need to email grades and feedback, copy your new grades to the temporary grades.csv file and follow the same procedure as explained above.



I know this code and the documentation is not perfect.  It wasn't really meant to be shared, but I thought I would share it anyway.

If you have any questions/comments, contact me by using my ORCID above!
