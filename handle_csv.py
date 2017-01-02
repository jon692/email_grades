# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:39:02 2016

@author: JonMeyers
http://orcid.org/0000-0002-6698-3420
Please see the readme file for instructions.
"""


def get_csv(filename):
    """read a csv file and put it into a nicely formatted list.  This function allows you to retain commas written inside quotes in the CSV."""

    import re	#should be included in stock python
    

    #read CSV into python
    infile=open(filename,'r') #load file
    lines=infile.readlines() #save all file contents to variable
    infile.close() #close file
    

#    print "DB get_csv lines are:\n",lines
    
    
    #scan the lines to make this a well-formatted list.  Also, keep in mind that there may be commas inside double quotes - we want to save these.
    for i in range(len(lines)):
        #get rid of the new line characters at the end of every csv row
        if lines[i].find('\n',len(lines[i])):
            lines[i]=lines[i][:len(lines[i])-1]

        
        #to be honest, I'm not quite sure how this works.  I had to look up how to use the re module.
        lines[i]=re.sub(r',(?=[^"]*"(?:[^"]*"[^"]*")*[^"]*$)', "&SAVE&", lines[i])  #Replace commas inside " " with &SAVE& symbol (to preserve them)
#        print "after re.sub",lines[i]
        
        #now the commas are protected, so let's split the lines into a list.
        lines[i]=lines[i].split(',')
        
        #now we need to go back and fix the comma situation.
        for j in range(len(lines[i])):
            lines[i][j]='' if lines[i][j]=='""' else lines[i][j] #if the cell is just "", then remove it
            lines[i][j]=lines[i][j].replace('&SAVE&',",")  #change &SAVE& symbols back to commas
            
            #Now for some reason wherever I had double quotes, I now have double double quotes.  Save those and get rid of the double quotes at the beginning and end           
            lines[i][j]=lines[i][j].replace('""','&SAVE&')
            lines[i][j]=lines[i][j].replace('"','')   #remove double quotes (these held together the groups that have commas in them)
            lines[i][j]=lines[i][j].replace('&SAVE&','"') #put back the quotes that I want.
            
    #print ("\nDB",__name__,"lines are:",lines)
            
    return lines
    
    
if __name__=='__main__':
    get_csv('grades.csv')
