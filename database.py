
import sqlite3


class Data_base():

    def __init__(self, name = 'banco_dados.db') -> None:
        self.name = name
        self.connection = name


    def criar_lista_perguntas(self, materia):

        try:
            self.connection = sqlite3.connect(self.name)
            cursor = self.connection.cursor()
            cursor.execute(f"SELECT * FROM Perguntas WHERE materia = '{materia}'")
            perguntas = cursor.fetchall()
            self.connection.close()
            return perguntas

        except AttributeError:
            print('Falha na conecção com banco de dados.')


    def inserir_usuario(self, nome, sobrenome, login, senha):

        try:
            self.connection = sqlite3.connect(self.name)
            cursor = self.connection.cursor()
            cursor.execute("""
            
                INSERT INTO Usuarios(nome, sobrenome, login, senha) VALUES(?,?,?,?)
                    
                """, (nome, sobrenome, login, senha))

            self.connection.commit()
            self.connection.close()

        except AttributeError:
            print('Falha na conecção com banco de dados.')


    def checar_login(self, login, senha):

        try:
            self.connection = sqlite3.connect(self.name)
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM Usuarios;
                
                """)

            for linha in cursor.fetchall():
                if linha[3].upper() == login.upper() and linha[4] == senha:
                    return True
                else:
                    continue

            self.connection.close()

            return False


        except AttributeError:
            print('Falha na conecção com banco de dados.')


    def login_existente(self, login):

        try:
            self.connection = sqlite3.connect(self.name)
            cursor = self.connection.cursor()
            cursor.execute("""

                SELECT * FROM Usuarios;
                
                """)

            for linha in cursor.fetchall():
                if linha[3].upper() == login.upper():
                    return True

            self.connection.close()

            return False

        except AttributeError:
            print('Falha na conecção com banco de dados.')



