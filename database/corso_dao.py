import mysql.connector
from database.DB_connect import DBConnect
from model.corso import Corso


class CorsoDao:

    @staticmethod
    def get_matricole_corso(codins):
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore connessione")
            return None
        else:
            result = set()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT i.matricola
                    FROM iscritticorsi.iscrizione i 
                    WHERE i.codins = %s"""
            cursor.execute(query, (codins,))
            for row in cursor:
                result.add(row["matricola"])
    # questo set di matricole andrà ad essere inserito dal modello, lo va a mettere dentro il corso, corso.matricole
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_all_corsi():  # questa funzione legge tutti i corsi
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.*
                    FROM corso c"""
            cursor.execute(query)
            for row in cursor:
                result.append(Corso(row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod  # questo decoratore mi dice che posso eseguire questo metodo senza avere un'istanza di corso dao
    # ma direttamente dalla classe
    def get_corsi_periodo(pd):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return result
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.*
            FROM corso c
            WHERE c.pd = %s"""
            cursor.execute(query, (pd,))
            for row in cursor:
                result.append(Corso(row["codins"],
                                    row["crediti"],
                                    row["nome"],
                                    row["pd"]))
            cursor.close()
            cnx.close()
            return result

    @staticmethod
    def get_numero_studenti_periodo(pd):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Errore connessione")
            return result
        else:
            cursor = cnx.cursor()
            query = """SELECT COUNT(DISTINCT i.matricola)
                    FROM iscritticorsi.corso c, iscritticorsi.iscrizione i  
                    WHERE c.pd = %s AND c.codins  = i.codins """
            cursor.execute(query, (pd,))
            result = 0  # lo inizializzo a 0 così ho sempre un valore di ritorno
            if cursor.with_rows:  # è una funzione che mi dovrebbe dire se c'è un risultato
                result = cursor.fetchone()[0]
            print(result)
            cursor.close()
            cnx.close()
            return result


