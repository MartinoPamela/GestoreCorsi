import mysql.connector
from mysql.connector import errorcode


class DBConnect:
    """Class that is used to create and manage a pool of connections to the database.
    It implements a class method that works as a factory for lending the connections from the pool"""
    # we keep the pool of connections as a class attribute, not an instance attribute
    _cnxpool = None
    # attributo che tiene traccia delle connessioni, manca il self perché noi abbiamo una risorsa, che è la connessione,
    # e non vogliamo creare tante istanze ognuna con il suo pool di connessioni a questa risorsa, perché altrimenti ogni
    # istanza cercherebbe di gestire la stessa risorsa e non èquello che vogliamo, perché vogliamo un unico
    # gestore di risorsa, quest'approccio è chiamato singleton, ovvero ho una classe di cui esiste un sola istanza,
    # oppure nessuna istanza e ho solo dei parametri di classe, questa è una variabile condivisa nella classe

    def __init__(self):
        raise RuntimeError('Do not create an instance, use the class method get_connection()!')

    @classmethod  # è un decoratore, un metodo di classe,
    # quindi non riceve self ma cls, può acedere agli attributi di classe
    def get_connection(cls, pool_name="my_pool", pool_size=3) -> mysql.connector.pooling.PooledMySQLConnection:
        """Factory method for lending connections from the pool. It also initializes the pool
        if it does not exist
        :param pool_name: name of the pool
        :param pool_size: number of connections in the pool
        :return: mysql.connector.connection"""
        # cls._cnxpool è la variabile classe in cui viene messa la connessione
        if cls._cnxpool is None: # principio di lazy initialization
            try:
                cls._cnxpool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_name=pool_name,
                    pool_size=pool_size,
                    option_files='./database/connector.cnf'
                )
                return cls._cnxpool.get_connection()
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                    return None
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                    return None
                else:
                    print(err)
                    return None
        else:
            return cls._cnxpool.get_connection()
