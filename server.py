import psycopg2
import flask
import dbclient
import myjson


host = "localhost"
port = "5432"
db_name = "Cielo"
user = 'postgres'
password = "postgres"


#Connessione al database 

try:
    connection = psycopg2.connect(
        host = host,
        port = port,
        dbname = db_name,
        user = user,
        password = password
    )

    print("Connessione al database avvenuta con successo")

except Exception as e :
    print(f"Errore di connessione al database : {e}")






flag : bool = True # Variabile di flag inizalizzata a True per accedere al ciclo. All'operatore 5 la variabile si setta a false per terminare il ciclo



while flag :


    print("Scegliere un operazione da 1 a 5 :")
    print("Premere 1 per vedere tutte le compagnie dei voli")
    print("Premere 2 per vedere tutti i voli con nominativo 'MagicFly' ")
    print("Premere 3  per vedere tutti voli in partenza")
    print("Premere 4 per scegliere cosa vedere inserendo il nome di una tabella fra : 'Volo' , 'Compagnia' , 'Aeroporto'")
    print("Premere 5 per uscire")
    

    scelta = int(input())  # Scelta dell'utente


    if scelta == 1 :
        cursor1 = connection.cursor()
        cursor1.execute("SELECT c.nome , c.annoFondaz FROM Compagnia as c")
        rows = cursor1.fetchall()
        for row in rows :
            print(f"Compagnae : {row}")
    
    if scelta == 2 : 
        cursor2 = connection.cursor()
        cursor2.execute("SELECT v.codice , v.comp , v.durataminuti FROM Volo as v WHERE v.comp = 'MagicFly' ")
        rows2 = cursor2.fetchall()
        for row in rows2 :
            print(f"Volo con nominativo MagicFly : {row}")

    if scelta == 3 :
        cursor3 = connection.cursor()
        cursor3.execute("SELECT v.codice , v.comp FROM Volo as v  JOIN ArrPart ap ON ap.codice = v.codice ORDER BY v.comp ASC")
        rows3 = cursor3.fetchall()
        for row in rows3 :
            print (f"Voli in partenza : {row}")


    if scelta == 4:
        try :
            sceltaTabella = input("Inserire la tabella desiderata : ")
            query = f"Select * From {sceltaTabella}"
            cursor4 = connection.cursor()
            cursor4.execute(query)
            rows4 = cursor4.fetchall()
            for row in rows4 :
                    if sceltaTabella == "Volo":
                        print(f"Volo {row}")
                    elif sceltaTabella == "Compagnia" :
                        print(f"Compagnia {row}")
                    elif sceltaTabella == "Aeroporto":
                        print(f"Aeroporto : {row}")       
        except :
            print(f"La tabella inserita non esiste per favore inserire le tabelle scritte")

    if scelta == 5 :
        print("Grazie e arrivederci")
        flag = False














