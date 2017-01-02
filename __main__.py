# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:38:50 2016

@author: JonMeyers
http://orcid.org/0000-0002-6698-3420
Please see the readme file for instructions.
"""

import handle_csv as csv		#code to read the csv into a nice list
from sys import exit
from email365 import send_mail		#code to utilize Office365
from format_html import format_message	#code that makes a nice HTML email message


#IMPORTANT!  Email settings are listed here.  No, it's not good practice to keep passwords inside code.  I'd like to learn the better way sometime.
my_email='jkm@unc.edu'
students_email_domain='@ad.unc.edu'
three60_user='jkm@ad.unc.edu'
three60_pass='jd04*3jklM'


def main():


    #user settings to be changed for each email
    subject="Pre-lab grades for exp 13"					#subject of the email

    #The email will start with the first name of the student (e.g. Matthew,) obtained from the CVS file
    forward="""Your last pre-lab grades!"""				#the text before the grade breakdown (a friendly message).  If you want multiple lines, simply hit ENTER.  The code will be converted to HTML later.

    #then the grade breakdown

    #Then the closing
    valediction="Enthusiastically"					#choose how to close your email
    name="Jon"								#your name
    signature="<br/><br/><p>"+valediction+",</p><br/><p>"+name+"</p>"	#signature (written in HTML)



    #have user verify the message at the beginning of the email is correct.  If it's not, give user a chance to escape
    print ("\n\n\n",forward)    
    fwd=input("\n\nIs this the forward you wish to send?  And did you check the subject line?  Enter y for yes.\nResponse: ")
    if fwd!='y':
        print("\n\nI am exiting so you can change the forward message.")
        exit()
        
        
    #load the grades from the directory of this program.
    grades=csv.get_csv('grades.csv')
    col_start_grades=2 #the column index where the actual grades begin (remember column A is 0, column B is 1, etc.)

    max_score=grades.pop(0) #the top line should be the maximum scores possible.  Remove this from the grades and save it elsewhere
    task=max_score.pop(0) #The top left cell should contain the task to be done (in-lab or pre-lab)
    max_score.pop(0) #Get rid of one more blank cell (what was once row 1 column B)
    #at this point, the max_score should only be the maximum scores possible, and one cell for comments to the entire class of students.
    



    #stop if there are no grades to go through.
    if len(grades)==0:
        print("\n\nI am exiting because there were no students to send grades to.")
        exit()
        
        
    
    
    #get max and avg grades for student reference
    max_avg=[grades[i][col_start_grades:len(grades[i])-1] for i in range(len(grades))] #the grades still have name, onyen, and comments.  However, this line gets just the numerical data.
    for a in range(len(max_avg)): #go through all the numerical data entries (this is by student)
        for b in range(len(max_avg[a])): #go through each grade for each student
            max_avg[a][b]=eval(max_avg[a][b]) #change the grade from a string format to an integer format.
        max_avg[a]=sum(max_avg[a]) #get the maximum overall grade from all the students
    max_avg=[max(max_avg),sum(max_avg)/len(max_avg)] #set the max_avg variable as [highest_grade, average_grade]
    
    

    #if you are working with a grade sheet for in-labs
    if task=='in-lab':
        
        if len(grades[0])!=8: #make sure that we have the correct number of columns (only a rough data verification)
            print("\n\nI am exiting because there aren't the exact number of columns")
            exit()


    #if you are working with a grade sheet for pre-labs
    elif task=='pre-lab':
        
        if len(grades[0])!=12: #make sure that we have the correct number of columns (only a rough data verification)
            print("\n\nI am exiting because there aren't the exact number of columns")
            exit()        
        
        
    else: #if no task was listed in the top-left cell of the grade sheet
        
        print("\n\nI am exiting because you didn't tell me the task")
        exit()
        
        
        
    #now start with the real work by going through each student's grades
    for student in range(len(grades)):    
        
        #print(grades[student])
        name=grades[student].pop(0) #get name
        #print (type(name),name)
        onyen=grades[student].pop(0) #get onyen
        #print (grades[student])
        #print ("onyen is",onyen)
        
        p_forward=name+",\n\n"+forward 		#make the stuff you say at the beginning of your email more personal by starting with their name.
        #print(p_forward)
        
        #formulate the message HTML
        message=format_message(task,max_score,grades[student],p_forward,max_avg,signature)
        
        
        #a nice test feature.  Send the first student's email to your email so you can check to make sure it looks right before you send each student their email.
        if student==0: #on the first student
            send_email(my_email,subject,message)
            
            #give user a chance to approve the email            
            test=input("Did your test look as it should? (y/n)\nResponse: ")
            
            if test!='y':
                print("\n\nI'm exiting because you said the test failed.")            
                exit()
        
        
        #if the test was successful, send out all the emails!
        send_email(onyen+students_email_domain,subject,message) 	#sends the email to the student based on their onyen.
        
        print("Email sent to ",name)	#print confirmation
    
    
def send_email(to_whom,subject,message):
    """Sends an HTML message to a recipient."""
    
    try:
        send_mail(my_email,to_whom,subject,message,username=three60_user,password=three60_pass,html=True)
    except:
        print ("I had a problem emailing",to_whom)
    
    
if __name__=='__main__':
    main()