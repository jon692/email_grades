# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:23:38 2016

@author: JonMeyers
http://orcid.org/0000-0002-6698-3420
Please see the readme file for instructions.
"""

#Pre-lab and participation points (in-lab) rubric breakdown
pre_titles=['title','I. Goal','II. Calc/Analysis','III. Measurements','IV. Observations','I. Safety Info','II. Disposal','I. Org & Clarity','II. Refs/Citation']
pp_titles=['I. Safety','II. Lab Citizenship','III. Independence','I. Notebook/Raw Data','II. Raw Data Curation']

def format_message(which,max_score,grade,forward,max_avg,signature):
    """Creates the HTML for your email."""    
    

    msg=[] #initialize the list that will contain all the components to this HTML email.  It will become a string later.
    
    
    #start the HTML head    
    msg.append("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    td {
        padding: 5px;
    }
    th {
        padding: 5px;
        text-align: center
    }
    </style>
    </head>""")
    
    
    #start the HTML body
    msg.append("<body>")
    
    
    
    #Write the first paragraph
    msg.append("<p>")
    msg.append(forward.replace("\n","</p><p>")) #if you have multiple paragraphs in the beginning part to your email, format the HTML correctly.
    msg.append("</p>")    
    


    #Create the table and the header row
    msg.append("""
    <table style="width:100%">
    
    <tr>
    <th>Rubric Item</th>
    <th>Score</th>
    </tr>""")
    
    
    
    #start creating the individualized table    
    if which=='pre-lab': 				#hardcoded format for pre-lab rubric tables
        col_comments=9					#columns of numeric grades before the column of comments
        

	#assignment overview row
        msg.append("""
        <tr>
        <td bgcolor='#A4A4A4'><b>Pre-lab Assignment</b></td>
        <td bgcolor='#A4A4A4' style="text-align: center"><b>""")
        
        #print (grade)
        #print (max_score)    
        
        msg.append(str(sum(eval(g) for g in grade[0:9]))+"/"+str(sum(eval(s) for s in max_score[0:9])))   #grade/possible grade
        
        msg.append("""
        </b></td>
        </tr>""")
        

	#Rubric item section A
        msg.append("""
        <tr>
        <td bgcolor='#D8D8D8' style="text-indent: 1em"><b>A. Title, Date, etc.</b></td>
        <td bgcolor='#D8D8D8' style='text-align: center'><b>""")
        
        #print (grade)
        #print (max_score)    
        
        msg.append(str(sum(eval(g) for g in grade[0:1]))+"/"+str(sum(eval(s) for s in max_score[0:1])))   #grade/possible grade
        
        msg.append("""
        </b></td>
        </tr>""")
        
        
	#Rubric item section B    
        msg.append("""
        <tr>
        <td bgcolor='#D8D8D8' style="text-indent: 1em"><b>B. Purpose and Intro</b></td>
        <td bgcolor='#D8D8D8' style='text-align: center'><b>""")
        
        #print (grade)
        #print (max_score)    
        
        msg.append(str(sum(eval(g) for g in grade[1:5]))+"/"+str(sum(eval(s) for s in max_score[1:5])))   #grade/possible grade
        
        msg.append("""
        </b></td>
        </tr>""")    
        
        
        
	#Rubric item section B subparts I, II, III, IV    
        for thing in [1,2,3,4]:
            msg.append("""
            <tr>
            <td style="text-indent: 2em">""")
            msg.append(str(pre_titles[thing]))
            msg.append("""
            </b></td>
            <td style='text-align: center'>""")
             
            
            msg.append(str(grade[thing])+"/"+str(max_score[thing]))   #grade/possible grade
            
            msg.append("""
            </td>
            </tr>
            """)
            
    

	#Rubric item section C
        msg.append("""<tr>
        <td bgcolor='#D8D8D8' style="text-indent: 1em"><b>C. Experimental</b></td>
        <td bgcolor='#D8D8D8' style='text-align: center'><b>""")
        
        #print (grade)
        #print (max_score)    
        
        msg.append(str(sum(eval(g) for g in grade[5:7]))+"/"+str(sum(eval(s) for s in max_score[5:7])))   #grade/possible grade
        
        msg.append("""
        </b></td>
        </tr>""")
    

	#Rubric item section C subparts I and II    
        for thing in [5,6]:
            msg.append("""
            <tr>
            <td style="text-indent: 2em">""")
            msg.append(str(pre_titles[thing]))
            msg.append("""
            </b></td>
            <td style='text-align: center'>""")
             
            
            msg.append(str(grade[thing])+"/"+str(max_score[thing]))   #grade/possible grade
            
            msg.append("""
            </td>
            </tr>
            """)
    

	#Rubric item section D
        msg.append("""
        <tr>
        <td bgcolor='#D8D8D8' style="text-indent: 1em"><b>D. Mechanics</b></td>
        <td bgcolor='#D8D8D8' style='text-align: center'><b>""")
        
        #print (grade)
        #print (max_score)    
        
        msg.append(str(sum(eval(g) for g in grade[7:9]))+"/"+str(sum(eval(s) for s in max_score[7:9])))   #grade/possible grade
        
        msg.append("""
        </b></td>
        </tr>""")    
        
        
        
	#Rubric item section D subparts I and II        
        for thing in [7,8]:
            msg.append("""
            <tr>
            <td style="text-indent: 2em">""")
            msg.append(str(pre_titles[thing]))
            msg.append("""
            </b></td>
            <td style='text-align: center'>""")
             
            
            msg.append(str(grade[thing])+"/"+str(max_score[thing]))   #grade/possible grade
            
            msg.append("""
            </td>
            </tr>
            """)
    
    
    
    
        msg.append("""        
        
        </table>""")
        
    elif which=='in-lab':				#hardcoded format for pre-lab rubric tables
        col_comments=5					#columns of numeric grades before the column of comments
        

	#assignment overview row
        msg.append("""        
        <tr>
        <td bgcolor='#A4A4A4'><b>In-lab Assignment</b></td>
        <td bgcolor='#A4A4A4' style="text-align: center"><b>""")
        
        #print (grade)
        #print (max_score)    
        
        msg.append(str(sum(eval(g) for g in grade[0:5]))+"/"+str(sum(eval(s) for s in max_score[0:5])))   #grade/possible grade
        

	#Rubric item section A
        msg.append("""
        </b></td>
        </tr>
        <tr>
        <td bgcolor='#D8D8D8' style="text-indent: 1em"><b>A. Lab Performance</b></td>
        <td bgcolor='#D8D8D8' style='text-align: center'><b>""")
        
        #print (grade)
        #print (max_score)    
        
        msg.append(str(sum(eval(g) for g in grade[0:3]))+"/"+str(sum(eval(s) for s in max_score[0:3])))   #grade/possible grade
        


	#Rubric item section A subparts I, II, III
        msg.append("""
        </b></td>
        </tr>""")
    
        for thing in [0,1,2]:
            msg.append("""
            <tr>
            <td style="text-indent: 2em">""")
            msg.append(str(pp_titles[thing]))
            msg.append("""
            </b></td>
            <td style='text-align: center'>""")
             
            
            msg.append(str(grade[thing])+"/"+str(max_score[thing]))   #grade/possible grade
            
            msg.append("""
            </td>
            </tr>
            """)
            
    
	#Rubric item section B    
        msg.append("""<tr>
        <td bgcolor='#D8D8D8' style="text-indent: 1em"><b>B. Experimental Info</b></td>
        <td bgcolor='#D8D8D8' style='text-align: center'><b>""")
        
        #print (grade)
        #print (max_score)    
        
        msg.append(str(sum(eval(g) for g in grade[3:5]))+"/"+str(sum(eval(s) for s in max_score[3:5])))   #grade/possible grade
        
        msg.append("""
        </b></td>
        </tr>""")
    

	#Rubric item section B subparts I and II        
        for thing in [3,4]:
            msg.append("""
            <tr>
            <td style="text-indent: 2em">""")
            msg.append(str(pp_titles[thing]))
            msg.append("""
            </b></td>
            <td style='text-align: center'>""")
             
            
            msg.append(str(grade[thing])+"/"+str(max_score[thing]))   #grade/possible grade
            
            msg.append("""
            </td>
            </tr>
            """)
    
        msg.append("""        
        
        </table>""")   #Finish off the table     
    
    
    #add an average/max score section so students can compare their score to their peers (my kind of motivation).
    msg.append("<p style='text-align: right'>Average Score: ")
    msg.append(str(round(max_avg[1]*2.)/2))	#Avg score
    msg.append("<br/>Highest Score: ")
    msg.append(str(round(max_avg[0]*2.)/2))	#Max score
    msg.append("</p>")



    #add comments

    if max_score[col_comments]!='': #I have comments for the whole class    
        msg.append("<p>Notes for entire section: ")
        msg.append(max_score[col_comments])
        msg.append("</p>")
    
    if grade[col_comments]!='': #I have comments for this student
        msg.append("<p>Notes for you: ")
        msg.append(grade[col_comments])
        msg.append("</p>")
    

    #add signature
    msg.append(signature)    
    
    
    #finish off HTML
    msg.append("""
    </body>
    </html>""")
    
    #print (msg)
    
    return ''.join(msg)



