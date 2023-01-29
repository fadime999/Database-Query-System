#2019510045 FADİME KAPLAN
import pandas as pd 
from blist import sorteddict
import json

#Reading csv file.
# making data frame from txt file 
df = pd.read_csv('students.csv', sep=';', names= ['id','name','lastname','email','grade'])
id=sorteddict(df.id)
name=sorteddict(df.name)
lastname=sorteddict(df.lastname)
email=sorteddict(df.email)
grade=sorteddict(df.grade)

length_dic=len(name)
numberlistt=list()
while True:
   command=input("Please enter your command line : ")
   if(command.startswith("exit") or command.startswith("Exit") or command.startswith("EXIT") ):   
      break
   if(command.startswith("SELECT")):   
     command=command.split(" ")
     column_name=command[1].split(",")
     temp=1
     select_name=sorteddict({0: 'name'})
     select_lastname=sorteddict({0: 'lastname'})
     select_email=sorteddict({0: 'email'})
     select_id=sorteddict({0: 'id'})
     select_grade=sorteddict({0: 'grade'})
     for i in range(0,len(column_name)):
         copy_name=name.copy()
         copy_lastname=lastname.copy()
         copy_email=email.copy()
         copy_id=id.copy()
         copy_grade=grade.copy()   
         temp=1
         if(len(command)==11 ):
            if(command[5]=="grade" or command[5]=="id"):
                if(command[5]=="grade" or command[5]=="id"):
                      if(command[5]=="grade" ):
                          copy_number=grade.copy() 
                      elif(command[5]=="id"):
                           copy_number=id.copy()
                      number=int(command[7])   
            for x in name:
              if(command[6]=="<="):  
                if(int(copy_number.values()[temp]) <= number):                                          
                   if(column_name[len(column_name)-1-i]=="name"):
                        select_name[temp]=copy_name.values()[temp]
                   elif(column_name[len(column_name)-1-i]=="lastname"):
                        select_lastname[temp]=copy_lastname.values()[temp]
                   elif(column_name[len(column_name)-1-i]=="email"):
                       select_email[temp]=copy_email.values()[temp]
              elif(command[6]==">="):
                 if(int(copy_number.values()[temp]) >= number):  
                    if(column_name[len(column_name)-1-i]=="name"):
                        select_name[temp]=copy_name.values()[temp]
                    elif(column_name[len(column_name)-1-i]=="lastname"):
                        select_lastname[temp]=copy_lastname.values()[temp]
                    elif(column_name[len(column_name)-1-i]=="email"):
                       select_email[temp]=copy_email.values()[temp]
              elif(command[6]==">" or command[6]=="!<"):
                 if(int(copy_number.values()[temp]) > number):  
                     if(column_name[len(column_name)-1-i]=="name"):
                        select_name[temp]=copy_name.values()[temp]
                     elif(column_name[len(column_name)-1-i]=="lastname"): 
                        select_lastname[temp]=copy_lastname.values()[temp]
                     elif(column_name[len(column_name)-1-i]=="email"):
                       select_email[temp]=copy_email.values()[temp]
              elif(command[6]=="<" or command[6]=="!>"):
                   if(int(copy_number.values()[temp]) < number):  
                     if(column_name[len(column_name)-1-i]=="name"):
                        select_name[temp]=copy_name.values()[temp]
                     elif(column_name[len(column_name)-1-i]=="lastname"):
                        select_lastname[temp]=copy_lastname.values()[temp]
                     elif(column_name[len(column_name)-1-i]=="email"):
                       select_email[temp]=copy_email.values()[temp]
              elif(command[6]=="="):
                 if(int(copy_number.values()[temp]) == number):  
                    if(column_name[len(column_name)-1-i]=="name"):
                        select_name[temp]=copy_name.values()[temp]
                    elif(column_name[len(column_name)-1-i]=="lastname"):
                        select_lastname[temp]=copy_lastname.values()[temp]
                    elif(column_name[len(column_name)-1-i]=="email"):
                       select_email[temp]=copy_email.values()[temp]
              elif(command[6]=="!="):    
                if(int(copy_number.values()[temp]) != number):  
                   if(column_name[len(column_name)-1-i]=="name"):
                        select_name[temp]=copy_name.values()[temp]
                   elif(column_name[len(column_name)-1-i]=="lastname"):
                        select_lastname[temp]=copy_lastname.values()[temp]
                   elif(column_name[len(column_name)-1-i]=="email"):
                       select_email[temp]=copy_email.values()[temp]
              temp=temp+1 
              if(temp==len(copy_name)):
                   break

         if(len(command)==15):
           if(command[8].lower()=="and"):   
              if(column_name[len(column_name)-1-i]=="name" or column_name[len(column_name)-1-i]=="lastname" or column_name[len(column_name)-1-i]=="email" or column_name[len(column_name)-1-i]=="grade" or column_name[len(column_name)-1-i]=="id"):
                if(command[9]=="name" or command[5]=="name" or command[9]=="lastname" or command[5]=="lastname"):
                   if(command[6]=="=" or command[10]=="=" or command[6]=="=" or command[10]=="="):
                      if(command[6]=="="):
                          selected=command[7]
                      elif(len(command)!=11):
                         selected=command[11]
                for x in name:                  
                     if(command[9]=="name" or command[5]=="name" or command[9]=="lastname" or command[5]=="lastname" or command[9]=="email" or command[5]=="email" or column_name[len(column_name)-1-i]=="grade" or column_name[len(column_name)-1-i]=="id"):
                        if(selected[1:len(selected)-1]==copy_name.values()[temp] or selected[1:len(selected)-1]==copy_lastname.values()[temp] or selected[1:len(selected)-1]==copy_email.values()[temp]):   
                          if(command[5]=="grade" or command[9]=="grade" or command[5]=="id" or command[9]=="id"):
                            if(command[5]=="grade" or command[5]=="id"):
                                if(command[5]=="grade" ):
                                   copy_number=grade.copy() 
                                elif(command[5]=="id"):
                                    copy_number=id.copy()
                                number=int(command[7])
                            else:
                                if(command[9]=="grade" ):
                                   copy_number=grade.copy() 
                                elif(command[9]=="id"):
                                    copy_number=id.copy()
                                number=int(command[11])
                            if(command[6]=="<=" or command[10]=="<="):  
                                if(int(copy_number.values()[temp]) <= number):                                          
                                    if(column_name[len(column_name)-1-i]=="name"):
                                        select_name[temp]=copy_name.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="lastname"): 
                                        select_lastname[temp]=copy_lastname.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="email"):
                                        select_email[temp]=copy_email.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="grade"):
                                        select_grade[temp]=copy_grade.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="id"):
                                        select_id[temp]=copy_id.values()[temp]                                        
                            elif(command[6]==">=" or command[10]==">="):
                                if(int(copy_number.values()[temp]) >= number):  
                                    if(column_name[len(column_name)-1-i]=="name"):
                                        select_name[temp]=copy_name.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="lastname"): 
                                        select_lastname[temp]=copy_lastname.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="email"):
                                        select_email[temp]=copy_email.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="grade"):
                                        select_grade[temp]=copy_grade.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="id"):
                                        select_id[temp]=copy_id.values()[temp]                                        
                            elif(command[6]==">" or command[10]=="!<" or command[10]==">" or command[6]=="!<" ):
                                if(int(copy_number.values()[temp]) > number):  
                                    if(column_name[len(column_name)-1-i]=="name"):
                                        select_name[temp]=copy_name.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="lastname"): 
                                        select_lastname[temp]=copy_lastname.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="email"):
                                        select_email[temp]=copy_email.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="grade"):
                                        select_grade[temp]=copy_grade.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="id"):
                                        select_id[temp]=copy_id.values()[temp]
                            elif(command[6]=="<" or command[10]=="!>" or command[10]==">" or command[6]=="!<"):
                                  if(int(copy_number.values()[temp]) < number):  
                                    if(column_name[len(column_name)-1-i]=="name"):
                                        select_name[temp]=copy_name.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="lastname"): 
                                        select_lastname[temp]=copy_lastname.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="email"):
                                        select_email[temp]=copy_email.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="grade"):
                                        select_grade[temp]=copy_grade.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="id"):
                                        select_id[temp]=copy_id.values()[temp]                                        
                            elif(command[6]=="=" or command[10]=="="):
                                if(int(copy_number.values()[temp]) == number):  
                                    if(column_name[len(column_name)-1-i]=="name"):
                                        select_name[temp]=copy_name.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="lastname"): 
                                        select_lastname[temp]=copy_lastname.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="email"):
                                        select_email[temp]=copy_email.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="grade"):
                                        select_grade[temp]=copy_grade.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="id"):
                                        select_id[temp]=copy_id.values()[temp]                                        
                            elif(command[6]=="!=" or command[10]=="="):    
                                if(int(copy_number.values()[temp]) != number):  
                                    if(column_name[len(column_name)-1-i]=="name"):
                                        select_name[temp]=copy_name.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="lastname"): 
                                        select_lastname[temp]=copy_lastname.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="email"):
                                        select_email[temp]=copy_email.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="grade"):
                                        select_grade[temp]=copy_grade.values()[temp]
                                    elif(column_name[len(column_name)-1-i]=="id"):
                                        select_id[temp]=copy_id.values()[temp]                                       
                     temp=temp+1
                     if(temp==len(copy_email)):
                         break

     if(column_name[len(column_name)-1-i]=="id"):
         if(command[9]!="id" and command[5]!="id"):
             select_id=id.copy()
         elif(command[9]=="id" or command[5]=="id"):
             copy_number=id.copy()
             if(command[9]=="id"):
                id_number=int(command[11])
             else:
                id_number=int(command[7]) 
             for x in name:          
                if(command[6]=="<=" or command[10]=="<="):  
                   if(int(copy_number.values()[temp]) <= id_number):                                          
                    select_id[temp]=copy_id.values()[temp]
                elif(command[6]==">=" or command[10]==">="):
                   if(int(copy_number.values()[temp]) >=id_number):  
                    select_id[temp]=copy_id.values()[temp]              
                elif(command[6]==">" or command[10]=="!<" or command[10]==">" or command[6]=="!<" ):
                    if(int(copy_number.values()[temp]) > id_number):  
                        select_id[temp]=copy_id.values()[temp]              
                elif(command[6]=="<" or command[10]=="!>" or command[10]==">" or command[6]=="!<"):
                  if(int(copy_number.values()[temp]) < id_number):  
                    select_id[temp]=copy_id.values()[temp]              
                elif(command[6]=="=" or command[10]=="="):
                  if(int(copy_number.values()[temp]) == id_number):  
                    select_id[temp]=copy_id.values()[temp]           
                elif(command[6]=="!=" or command[10]=="="):    
                   if(int(copy_number.values()[temp]) != id_number):  
                     select_id[temp]=copy_id.values()[temp]              
                temp=temp+1
                if(temp==len(copy_id)):
                   break
                      
     elif(column_name[len(column_name)-1-i]=="grade"):
         if(command[9]!="grade" and command[5]!="grade"):
             select_id=grade.copy()
         elif(command[9]=="grade" or command[5]=="grade"):
             copy_number=grade.copy()
             if(command[9]=="grade"):
                grade_number=int(command[11])
             else:
                grade_number=int(command[7]) 
             for x in name:          
                if(command[6]=="<=" or command[10]=="<="):  
                   if(int(copy_number.values()[temp]) <=grade_number):                                          
                    select_grade[temp]=copy_grade.values()[temp]
                elif(command[6]==">=" or command[10]==">="):
                   if(int(copy_number.values()[temp]) >=grade_number):  
                    select_grade[temp]=copy_grade.values()[temp]              
                elif(command[6]==">" or command[10]=="!<" or command[10]==">" or command[6]=="!<" ):
                    if(int(copy_number.values()[temp]) >grade_number):  
                        select_grade[temp]=copy_grade.values()[temp]              
                elif(command[6]=="<" or command[10]=="!>" or command[10]==">" or command[6]=="!<"):
                  if(int(copy_number.values()[temp]) < grade_number):  
                    select_grade[temp]=copy_grade.values()[temp]              
                elif(command[6]=="=" or command[10]=="="):
                  if(int(copy_number.values()[temp]) == grade_number):  
                    select_grade[temp]=copy_grade.values()[temp]           
                elif(command[6]=="!=" or command[10]=="="):    
                   if(int(copy_number.values()[temp]) != grade_number):  
                     select_grade[temp]=copy_grade.values()[temp]              
                temp=temp+1
                if(temp==len(copy_grade)):
                   break
       
     print(select_name.values())                      
     print(select_lastname.values())
     print(select_email.values())
     print(select_id.values())
     print(select_grade.values())     
     if(command[9]=="ASC"):
         select_name=sorted(select_name.items())
         select_lastname=sorted(select_lastname.items())
         select_email=sorted(select_email.items())
         select_id=sorted(select_id.items())
         select_grade=sorted(select_grade.items())
     elif(command[9]=="DSC"):
         select_name=sorted(select_name.items(),reverse=True)
         select_lastname=sorted(select_lastname.items(),reverse=True)
         select_email=sorted(select_email.items(),reverse=True)
         select_id=sorted(select_id.items(),reverse=True)
         select_grade=sorted(select_grade.items(),reverse=True)
   elif(command.startswith("INSERT")):
        new_student=command[command.index("(")+1:command.index(")") ]
        data=new_student.split(",") 
        id[0]=data[0]
        name[0]=data[1]
        lastname[0]=data[2]
        email[0]=data[3]
        grade[0]=data[4]
   
   elif(command.startswith("DELETE")):
       command=command.split(" ")      
       #name or lastname or email 
       if(command[4]=="name" or command[8]=="name"):
           copy=name.copy()
       elif(command[4]=="lastname" or command[8]=="lastname"):
               copy=lastname.copy()
       elif(command[4]=="email" or command[8]=="email"):
          copy=email.copy()
          pass
       if(len(command)==11):
         if(command[7].lower()=="and"): 
            count=0   
            if(command[5]=="=" or command[9]=="="):
                if(command[5]=="="):
                    delete=command[6]
                else:
                    delete=command[10]
                for x in copy:
                    if(delete[1:len(delete)-1]==copy.values()[count]):
                        if(command[8]=="grade" or command[4]=="grade" or command[8]=="id" or command[4]=="id"):
                            if(command[8]=="grade" or command[8]=="id"):
                                if(command[8]=="grade" ):
                                   copy_number=grade.copy() 
                                elif(command[8]=="id"):
                                    copy_number=id.copy()
                                number2=int(command[10])
                            else:
                                if(command[4]=="grade" ):
                                   copy_number=grade.copy() 
                                elif(command[4]=="id"):
                                    copy_number=id.copy()
                                number2=int(command[6])
                            if(command[9]=="<=" or command[5]=="<="):  
                                    if(int(copy_number.values()[count]) <= number2):  
                                        del[id[count]]
                                        del[name[count]]
                                        del[lastname[count]]
                                        del[email[count]]
                                        del[grade[count]]
                                        numberlistt.append(count) 
                            elif(command[9]==">=" or command[5]==">="):
                                    if(int(copy_number.values()[count]) >= number2):  
                                        del[id[count]]
                                        del[name[count]]
                                        del[lastname[count]]
                                        del[email[count]]
                                        del[grade[count]]
                                        numberlistt.append(count) 
                            elif(command[9]==">" or command[9]=="!<" or command[5]==">" or command[5]=="!<" ):
                                    if(int(copy_number.values()[count]) > number2):  
                                            del[id[count]]
                                            del[name[count]]
                                            del[lastname[count]]
                                            del[email[count]]
                                            del[grade[count]]
                                            numberlistt.append(count) 
                            elif(command[9]=="<" or command[9]=="!>" or command[5]==">" or command[5]=="!<"):
                                        if(int(copy_number.values()[count]) < number2):  
                                            del[id[count]]
                                            del[name[count]]
                                            del[lastname[count]]
                                            del[email[count]]
                                            del[grade[count]]
                                            numberlistt.append(count) 
                            elif(command[9]=="=" or command[5]=="="):
                                       if(int(copy_number.values()[count]) == number2):  
                                           del[id[count]]
                                           del[name[count]]
                                           del[lastname[count]]
                                           del[email[count]]
                                           del[grade[count]]
                                           numberlistt.append(count) 
                            elif(command[9]=="!=" or command[5]=="="):    
                                       if(int(copy_number.values()[count]) != number2):  
                                           del[id[count]]
                                           del[name[count]]
                                           del[lastname[count]]
                                           del[email[count]]
                                           del[grade[count]]
                                           numberlistt.append(count) 
                    count=count+1  
                    if(count==len(copy)):
                        break             
            else: #for "!="
                count=1
                not_delete_name=command[6]
                for x in copy:           
                    if(count==len(copy)):
                        break 
                    if(not_delete_name[1:len(not_delete_name)-1]!=copy.values()[count]): 
                        del[id[count]]
                        del[name[count]]
                        del[lastname[count]]
                        del[email[count]]
                        del[grade[count]]               
                    count=count+1                            
         elif(command[7].lower()=="or"):
             count=0   
             numberlist=list()
             if(command[5]=="="):
                if(command[5]=="=" or command[9]=="="):
                    delete=command[6]
                else:
                    delete=command[10]
                number_count=0
                for x in copy:
                   if(delete[1:len(delete)-1]==copy.values()[count]):                
                      del[id[count]]
                      del[name[count]]
                      del[lastname[count]]
                      del[email[count]]
                      del[grade[count]]
                      numberlist.append(count)                  
                   count=count+1   
                   if(count==len(copy)):
                      break
             else:
                    not_delete_name=command[6]
                    for x in copy:
                        if(not_delete_name[1:len(not_delete_name)-1]!=copy.values()[count]): 
                            del[id[count]]
                            del[name[count]]
                            del[lastname[count]]
                            del[email[count]]
                            del[grade[count]]
                            numberlist.append(count)  
                        count=count+1  
                        if(count==len(copy)):
                            break

             if(command[8]=="grade" or command[4]=="grade" or command[8]=="id" or command[4]=="id"):
                       if(command[8]=="grade" or command[8]=="id"):
                           if(command[8]=="grade" ):
                              copy_number=grade.copy() 
                           elif(command[8]=="id"):
                                copy_number=id.copy()
                           number3=int(command[10])
                       else:
                            if(command[8]=="grade" ):
                               copy_number=grade.copy() 
                            elif(command[8]=="id"):
                                copy_number=id.copy()
                            number3=int(command[6])                         
                    
             count2=0
             for x in copy: 
                       count2=count2+1
                       for i in range(0,len(numberlist)):       
                          if(numberlist[i]==count2):
                             count2=count2+1
                             break
                       for i in range(0,len(numberlistt)):       
                          if(numberlistt[i]==count2):
                             count2=count2+1
                             break
                       if(count2==len(copy_number)):
                           break            
                       if(command[9]=="<="):                      
                           if(int(copy_number.values()[count2]) <= number3):   
                                  del[id[count2]]
                                  del[name[count2]] 
                                  del[lastname[count2]]
                                  del[email[count2]]
                                  del[grade[count2]]
                       elif(command[9]==">="):
                            if(int(copy_number.values()[count2]) >= number3):  
                                  del[id[count2]]
                                  del[name[count2]]
                                  del[lastname[count2]]
                                  del[email[count2]]
                                  del[grade[count2]]
                       elif(command[9]==">" or command[9]=="!<"):
                            if(int(copy_number.values()[count2]) > number3):  
                                  del[id[count2]]
                                  del[name[count2]]
                                  del[lastname[count2]]
                                  del[email[count2]]
                                  del[grade[count2]]
                       elif(command[9]=="<" or command[9]=="!>"):
                            if(int(copy_number.values()[count]) < number3):  
                                  del[id[count2]]
                                  del[name[count2]]
                                  del[lastname[count2]]
                                  del[email[count2]]
                                  del[grade[count2]]
                       elif(command[9]=="="):
                            if(int(copy_number.values()[count]) == number3):  
                                  del[id[count2]]
                                  del[name[count2]]
                                  del[lastname[count2]]
                                  del[email[count2]]
                                  del[grade[count2]]
                       elif(command[9]=="!="):    
                            if(int(copy_number.values()[count]) != number3):  
                                  del[id[count2]]
                                  del[name[count2]]
                                  del[lastname[count2]]
                                  del[email[count2]]
                                  del[grade[count2]]  
                                  
#conversion from sorttedictden to dictionary construction
dict_students=dict()
for i in range(0,len(name)):
    dict_students.update({
    i: {
        'id':id.values()[i],
        'name': name.values()[i],
        'lastname': lastname.values()[i],
        'email':email.values()[i],
        'grade':grade.values()[i]
    }
   })

#writing data to a json file
with open('students.json', 'w') as json_file:
  json.dump(dict_students, json_file, indent = 4, ensure_ascii=False)
