import mysql.connector
import datetime


#Function to select all the events
def select_all(conn):
    sql_select_query = "select * from data"
    cursor = conn.cursor()
    cursor.execute(sql_select_query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)     
    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Event = ", row[1])
        print("Person_name = ", row[2])
        print("Event_date  = ", row[3], "\n")

#Function to select the event by event name
def select_by_event_name(conn, event_name):
    sql_select_query = "select * from data where event_name = %s;"
    cursor = conn.cursor()
    cursor.execute(sql_select_query, (event_name,))
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)
    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Event = ", row[1])
        print("Person name  = ", row[2])
        print("Event_date  = ", row[3], "\n")



# Function to select the event by person_name
def select_by_person_name(conn, person_name):
    sql_select_query = "select * from data where person_name = %s;"
    cursor = conn.cursor()
    cursor.execute(sql_select_query, (person_name,))
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)
    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Event = ", row[1])
        print("Person name  = ", row[2])
        print("Event_date  = ", row[3], "\n")



#Function to insert the events
def insert_event(conn, event_id, event_name, person_name, event_date):
    sql_select_query = "Insert into data values (%d, \"%s\", \"%s\", \"%s\");" % (
    event_id, event_name, person_name, event_date)
    cursor = conn.cursor()
    cursor.execute(sql_select_query)
    conn.commit()
    print("Inserted successfully")


# Function to update the events
def update_event_name(conn, event_id, event_name):
    sql_select_query = "update data set event_name = \"%s\" where id = %d;" % (event_name, event_id)
    cursor = conn.cursor()
    cursor.execute(sql_select_query)
    conn.commit()
    print("Updated successfully")


#Function to delete events using event id
def delete_event(conn, event_id):
    sql_select_query = "delete from data where id = %d;" % event_id
    cursor = conn.cursor()
    cursor.execute(sql_select_query)
    conn.commit()
    print("Deleted successfully")


#Function to delete event using event name
def delete_event_by_name(conn, event_name):
    sql_select_query = "delete from data where event_name=%s"
    cursor = conn.cursor()
    cursor.execute(sql_select_query,(event_name,))
    conn.commit()
    print("Deleted successfully")


#Function to delete event using person name
def delete_event_by_person_name(conn, person_name):
    sql_select_query = "delete from data where person_name=%s"
    cursor = conn.cursor()
    cursor.execute(sql_select_query,(person_name,))
    conn.commit()
    print("Deleted successfully")


#Function to delete event using date
def delete_event_by_date(conn, event_date):
    sql_select_query = "delete from data where event_date=%s"
    cursor = conn.cursor()
    cursor.execute(sql_select_query,(event_date,))
    conn.commit()
    print("Deleted successfully")




connection = mysql.connector.connect(host='localhost', database='event', user='root', password='root123')
today = datetime.date.today()



#Menudriven program 
def mainmenu():
    print("     Welcome to Main Menu    ")      
    print("     1.Perform insertion     ")
    print("     2.Update the data      ")
    print("     3.Delete event by eventid     " )
    print("     4.Delete event by event name      ")
    print("     5.Delete event by date   ")
    print("     6.Delete event by person name  ")
    print("     7.To see all the events     ")
    print("     8.View the data by giving event name")
    print("     9.View the data by giving person name   ")
    print("     10.Exit                  ")

    mychoice = int(input("Enter your choice : "))

    if(mychoice==1):
        print("You are ready to perform insertion, please enter the values : ")
        event_id =int(input("Enter event id : "))
        event_name = input("Enter event name : ")
        person_name = input("Enter person name : ")
        event_date = input("Enter the event date : ")
        insert_event(connection,event_id,event_name,person_name,event_date)
        # select_all(connection)


    elif mychoice==2:
        print("You are ready to update the data, please enter the values : ")
        event_id= int(input("Enter event id: "))
        event_name= input("Enter event name : ")
        update_event_name(connection, event_id, event_name)
        # select_all(connection)



    elif mychoice==3:
        print("You are ready to perform deletion using event id, please enter the values : ")
        event_id =int(input("Enter event id : "))
        delete_event(connection, event_id)
        # select_all(connection)
    
    elif mychoice==4:
        print("You are ready to perform deletion using event name, please enter the values : ")
        event_name = input("Enter the event name :")
        delete_event_by_name(connection, event_name)
        # select_all(connection)

    elif mychoice==5:
        print("You are ready to perform deletion using event date, please enter the values : ")
        event_date= input("Enter date : ")
        delete_event_by_date(connection, event_date)
        # select_all(connection)

    elif mychoice==6:
        print("You are ready to perform deletion using person name, please insert the values : ")
        person_name=input("Enter person name : ")
        delete_event_by_person_name(connection, person_name)
        # select_all(connection)

    elif mychoice == 7:
        select_all(connection)


    elif mychoice==8:
         print("you are ready to view the data by giving the event name: ")
         event_name = input("enter event name : ")
         select_by_event_name(connection, event_name)


    elif mychoice==9:
        print("You are ready to view data by providing person name : ")
        person_name = input("enter person name : ")
        select_by_person_name(connection, person_name)


    elif mychoice==10:
        exit
    else:
        print("Enter  proper values from 1 to 10")


mainmenu()

