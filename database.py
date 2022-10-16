
import sqlite3


class Data_base():

    def __init__(self, name = 'banco_dados.db') -> None:
        self.name = name
        self.connection = name


    def criar_lista_perguntas(self, materia):

        self.connection = sqlite3.connect(self.name)

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Perguntas WHERE materia = '{materia}'")
            perguntas = cursor.fetchall()
            self.connection.close()
            return perguntas
        except Exception as e:
            print(e)
            return e




