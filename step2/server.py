import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


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


def get_db_connection():
    try:
        return psycopg2.connect(
            host=host,
            port=port,
            dbname=db_name,
            user=user,
            password=password
        )
    except Exception as e:
        print(f"Errore di connessione al database: {e}")
        return None




@app.route('/compagnia' , methods=["GET"])
def getCompagnia():
    cursor = connection.cursor()
    cursor.execute("SELECT c.nome , c.annoFondaz FROM Compagnia as c")
    compagnie = cursor.fetchall()
    return jsonify (compagnie)




@app.route('/voliMagic'  , methods = ["GET"])
def getVoliMagic():
    cursor2 = connection.cursor()
    cursor2.execute("SELECT v.codice , v.comp , v.durataminuti FROM Volo as v WHERE v.comp = 'MagicFly' ")
    voliMagic = cursor2.fetchall()
    return voliMagic

@app.route('/voliInPartenza' , methods = ["GET"])
def getVoliInPartenza():
    cursor3 = connection.cursor()
    cursor3.execute("SELECT v.codice , v.comp FROM Volo as v  JOIN ArrPart ap ON ap.codice = v.codice ORDER BY v.comp ASC")
    voliInPartenza = cursor3.fetchall()
    return voliInPartenza

@app.route('/tabelle/<table_name>', methods=["GET"])
def getTabelleMultiple(table_name):
    try:
        query = f"SELECT * FROM {table_name}"
        connection = get_db_connection()
        if not connection:
            return jsonify({"error": "Connessione al database fallita"}), 500
        
        cursor = connection.cursor()
        cursor.execute(query)
        tabellaScelta = cursor.fetchall()
        cursor.close()
        connection.close()
        
        return jsonify(tabellaScelta)
    except Exception as e:
        return jsonify({"error": f"Errore: {str(e)}"}), 400



if __name__ == '__main__':
    app.run(debug=True, port=8080)














