import sqlite3
from datetime import date, timedelta
import os

def connect():
    return sqlite3.connect('C:\\Users\\strat\\OneDrive\\Υπολογιστής\\Project Covid\\covid19.db')    #connect to database


def get_countries(n):                       #get countries
    if n==1:
        return connect().execute("SELECT Country FROM Cases").fetchall()
    elif n==2:
        return connect().execute("SELECT Country FROM Vaccinations").fetchall()


def get_col_num(table):                     #get number of dates
    cursor = connect().execute("SELECT * FROM " + table)
    n=0
    for i in cursor:                        #because cursor's style is: (...,(Null,Greece,0,0,0,0,0,0,....,34045,....),...)
        m = len(i)                          #we count the length of each tuple and save the max length (minus 2 beacuse the first two are State and Country)
        if m > n:
            n = m
    return n-2


def get_first_date(table):  #get first date from table
    cursor = connect().execute('select * from ' + table)
    names = list(map(lambda x: x[0], cursor.description))
    first_date = str(names[2])

    if table=='Vaccinations':
        first_date = first_date[1:].split('ymd')                                                    #}=>date decoding for datetime format
        first_date[0],first_date[1],first_date[2]=first_date[0],first_date[1],first_date[2]         #} 

    else:
        first_date = first_date[1:].split('mdy')                                                    #}=>date decoding for datetime format
        first_date[0],first_date[1],first_date[2]="20"+first_date[2],first_date[0],first_date[1]    #}

    return first_date


first = get_first_date('Cases')
cure = get_first_date('Vaccinations')

countries1=[]
countries2=[]
m=0
duplicate1={}
duplicate2={}

cases_dur=get_col_num('Cases')          #number of days in cases
deaths_dur=get_col_num('Deaths')        #number of days in deaths
vac_dur=get_col_num('Vaccinations')     #number of days in vaccinations
count=-1

for i in get_countries(1):              #get countries for table cases
    count += 1

    if i[0] not in countries1:
        countries1.append(i[0])         #list of countries
    
    if i[0] not in duplicate1:
        duplicate1[i[0]]=[count]        #if not in dictionary, add key and position number 
    else:
        duplicate1[i[0]].append(count)  #if in dictionary add it to the key's list

count=-1
    
for i in get_countries(2):              #get countries for table vaccinations
    count += 1

    if i[0] not in countries2:
        countries2.append(i[0])         #list of countries
    
    if i[0] not in duplicate2:
        duplicate2[i[0]]=[count]        #if not in dictionary, add key and position number
    else:
        duplicate2[i[0]].append(count)  #if in dictionary add it to the key's list


def country1(n = countries1):
    return n                            #return list of countries


def country2(n = countries1):
    n.insert(0,'None')
    return n                            #return list of countries with an added "None" at the start of the list


def dur():
    return cases_dur                    #return duration


def dates_between(val):
    
    sdate = date(int(first[0]),int(first[1]),int(first[2])) # first date
    edate = sdate + timedelta(days=val[1])   # end date
    sdate = date(int(first[0]),int(first[1]),int(first[2]))+timedelta(days=val[0]) #start date
    date_modified=sdate
    list=[sdate.strftime("%Y %m %d")] 

    while date_modified<edate-timedelta(days=1):        #if date modified is before end date-1
        date_modified+=timedelta(days=1)                #date = next date
        list.append(date_modified.strftime("%Y %m %d")) #and add it to list

    return list


def data(country,table,n,daily=False):
    date_data=[]
    date_total=[]
    if table == 'Vaccinations':
        duplicate=duplicate2
        countries=countries2
    else:
        duplicate=duplicate1
        countries=countries1
    
    if daily==True:     #daily values
        for i in n:
            if country not in countries:
                break
            i = i.split(' ')
            if table == 'Vaccinations':
                i='D'+i[0]+'ymd'+i[1]+'ymd'+i[2]        #date encoding based on the table
            else:                                       
                if i[1][0]=='0':                        #}
                    i[1]=i[1][1]                        #}
                if i[2][0]=='0':                        #}=>date encoding based on the table
                    i[2]=i[2][1]                        #}
                i='D'+i[1]+'mdy'+i[2]+'mdy'+i[0][2:]    #}
            try:
                cursor = connect().execute('select '+ i + ' from ' + table)
            except sqlite3.OperationalError:            #that happens if the date is before fist date of the table
                if table=='Vaccinations':
                    cursor=[]
                    for x in range(len(countries)):     #append as many (0,) as the length of countries
                        cursor.append((0,))
            li=[]
            for l in cursor:
                li.append(l[0])                         #clean up the cursor list
            date_sum=0
            for m in list(duplicate[str(country)]):     #list of indexi that Country is the selected country
                try:
                    date_sum += int(li[m])              #add that number that's in the place m in the list li
                except: pass
            if len(date_data)<=1:                       #because a previous number doesn't exist
                date_data.append(date_sum)              
            else:
                date_data.append(date_sum-int(date_total[-1]))  #append the difference between current date_sum and previous date_sum to get daily value
            date_total.append(date_sum)
        date_data.insert(0,0)           #}=>shift data one place to the right
        date_data.remove(date_data[-1]) #}

    else:           #total values
        for i in n:
            if country not in countries:
                break
            i = i.split(' ')
            if table == 'Vaccinations':
                i='D'+i[0]+'ymd'+i[1]+'ymd'+i[2]        #date encoding based on the table
            else:
                if i[1][0]=='0':                        #}
                    i[1]=i[1][1]                        #}
                if i[2][0]=='0':                        #}=>date encoding based on the table
                    i[2]=i[2][1]                        #}
                i='D'+i[1]+'mdy'+i[2]+'mdy'+i[0][2:]    #}
            try:
                cursor = connect().execute('select '+ i + ' from ' + table)
            except sqlite3.OperationalError:            #that happens if the date is before fist date of the table
                if table=='Vaccinations':
                    cursor=[]
                    for x in range(len(countries)):
                        cursor.append((0,))
            li=[] 
            for l in cursor:
                li.append(l[0])                         #cleans up the cursor list from the singular number tuples
            date_sum=0
            for m in list(duplicate[str(country)]):     #list of indexi that Country is the selected country
                try:
                    date_sum += int(li[m])              #add that number that's in the place m in the list li
                except: pass

            date_data.append(date_sum)                  #append data_sum to final list
            print(date_data)
        if table == 'Vaccinations':
            date_data.insert(0,0)           #}=>shift data one place to the right
            date_data=date_data[:-1]        #} 
            print(date_data)   
    return date_data
