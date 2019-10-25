# PythonPleb
Im a pleb rying to learn some Python scripts 

print("hello world")
#Print visar utmatning till sin konsoll


name = input("please enter your name: ")
#Input gör att man frågar klienten om något. Eller får information om klienten

print("hello world")
()
print("did you see that blank line?")
print(blank line \nin the middle of sting")
#Att sätta en () mellan gör att det blir lättare att se samt att det skapar mellan rum mellan raderna. Att skriva \n gör att texten blir delad, så den ena stannar och den andra delan åker ner ett steg. 

#Ett av själen varför print är så bra är för att man kan använda det för "debugga". 

#För att datorn ska förstå att det är Python vi arbetar med så måste man spara filen man skapat med .py . Då kommer det även få färjer som gör det lättare att se om det är rätt eller inte. 


name = input("what is your name?")
print("hello")
print(name)
#Detta var mitt första skrip, "name" är variabelen och "input" är frågan. Detta gör att när jag kör skripted så kommer den fråga efter mitt namn som jag kan svara på. När jag gjort detta så kommer den att svar med hello. 
#Att skriva "cls" gör att man rensar teminalen. 

x = 1+1
y = x /0
print("Matte")
#Om man skriver en code som är felktig som så som ovan så kommer "debugga" att gå igång och säga till att det är fel: SyntaxError: "ZeroDivisionError: division by zero" då det inte går att dela med 0.
#Det står även vilken rad som det blev fel på: "line 2, in <module>"
#Ett annat tips är att om man skriver print och förklarar vad man gör efter varje code så är det lätt att se vad man håller på med. tex. print("adding numbers"),print("dividing numbers")

CTRL+K+C CTRL+K+U
#Dessa två är för att göra en text till en kommentar: CTRL+K+C eller till en code: CTRL+K+U

#Vad är en string?
#Det är något man lägger i en variabel, en variabel är en platshållare för code för "values". 
#Om man har två strings och till sätta ihop dessa så behöver man bara lägga till "+"tecknet. Exempel på detta är:
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
#Det vi gör här är att ändra på en sting, kom ihåg det jag skrev ovan, något amn lägger i en variabel. Man kan se vad jag vill ändra lätt om man kollar och svaret blir:
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
