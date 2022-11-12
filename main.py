
from PySide2.QtWidgets import *
from ui_interface_grafica import Ui_MainWindow
import sys
import sqlite3
from database import Data_base
from random import randint


class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Quiz Loading Python')

        ###################################################################
        # Conexão entre as paginas e botoes

        self.btn_login.clicked.connect(lambda: self.login())
        self.btn_novo_cadastro.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Cadastro))
        self.btn_jogar.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Jogo))
        self.btn_cadastro_voltar.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Inicial))
        self.btn_regras.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Regras))
        self.btn_voltar.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Menu))
        self.btn_voltar_2.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Menu))
        self.btn_cadastrar.clicked.connect(lambda: self.novo_cadastro_usuario())


        self.btn_sair.clicked.connect(lambda:sys.exit())

        self.btn_novo_jogo.clicked.connect(lambda: self.iniciar_game())


        self.resposta_1.clicked.connect(lambda: self.confirmar_resposta("1"))
        self.resposta_2.clicked.connect(lambda: self.confirmar_resposta("2"))
        self.resposta_3.clicked.connect(lambda: self.confirmar_resposta("3"))
        self.resposta_4.clicked.connect(lambda: self.confirmar_resposta("4"))

        ###################################################################


    def login(self):

        login = self.login_usuario.text()
        senha = self.login_senha.text()

        db = Data_base()

        resp = db.checar_login(login, senha)

        if resp == True:
            self.Paginas.setCurrentWidget(self.Pagina_Menu)
            self.usuario_logado = login

        else:
            msg = QMessageBox()
            msg.setWindowTitle('Loading Python Quiz')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Login ou senha invalido!')
            msg.exec_()


    def novo_cadastro_usuario(self):

        nome = self.Cadastro_Nome.text()
        sobrenome = self.Cadastro_Sobrenome.text()
        login = self.Cadastro_Login.text()
        senha1 = self.Cadastro_Senha_1.text()
        senha2 = self.Cadastro_Senha_2.text()
        db = Data_base()

        if nome == '' or sobrenome == '' or login == '' or senha1 == '':
            msg = QMessageBox()
            msg.setWindowTitle('Loading Python Quiz')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Todos os campos devem ser preenchidos.')
            msg.exec_()

        elif senha1 != senha2:
            msg = QMessageBox()
            msg.setWindowTitle('Loading Python Quiz')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('As senhas devem ser iguais.')
            msg.exec_()
            self.Cadastro_Senha_1.setText('')
            self.Cadastro_Senha_2.setText('')

        elif db.login_existente(login) == True:
            msg = QMessageBox()
            msg.setWindowTitle('Loading Python Quiz')
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Login já existente, tente novamente.')
            msg.exec_()
            self.Cadastro_Login.setText('')

        else:
            db = Data_base()
            db.inserir_usuario(nome, sobrenome, login, senha1)

            msg = QMessageBox()
            msg.setWindowTitle('Loading Python Quiz')
            msg.setText('Cadastrado com sucesso')
            msg.exec_()

            self.Paginas.setCurrentWidget(self.Pagina_Inicial)


    def iniciar_game(self):

        self.erros = []
        self.num_perguntas = 0
        db = Data_base()
        self.perguntas_portugues = db.criar_lista_perguntas('portugues')
        self.perguntas_matematica = db.criar_lista_perguntas('matematica')
        self.perguntas_ciencia = db.criar_lista_perguntas('ciencia')
        self.perguntas_historia = db.criar_lista_perguntas('historia')
        self.perguntas_geofrafia = db.criar_lista_perguntas('geografia')

        self.escolha_perguntas()


    def escolha_perguntas(self):


        self.num_perguntas += 1
        if self.num_perguntas <= 30:
            self.label_n_pergunta.setText(f'     Pergunta {self.num_perguntas} de 30')


        if self.num_perguntas < 7:
            self.pergunta = self.perguntas_portugues[randint(0, len(self.perguntas_portugues) - 1)]
            self.perguntas_portugues.remove(self.pergunta)
        elif self.num_perguntas < 13:
            self.pergunta = self.perguntas_matematica[randint(0, len(self.perguntas_matematica) - 1)]
            self.perguntas_matematica.remove(self.pergunta)
        elif self.num_perguntas < 19:
            self.pergunta = self.perguntas_ciencia[randint(0, len(self.perguntas_ciencia) - 1)]
            self.perguntas_ciencia.remove(self.pergunta)
        elif self.num_perguntas < 25:
            self.pergunta = self.perguntas_historia[randint(0, len(self.perguntas_historia) - 1)]
            self.perguntas_historia.remove(self.pergunta)
        elif self.num_perguntas <=30:
            self.pergunta = self.perguntas_geofrafia[randint(0, len(self.perguntas_geofrafia) - 1)]
            self.perguntas_geofrafia.remove(self.pergunta)
        else:
            self.fim_jogo()

        self.label_pergunta.setText(self.pergunta[1])
        self.label_pergunta.setStyleSheet(u"""
            background-color:rgb(34, 60, 122);
	        color: rgb(255,255,255);
	        font: 14pt;
	        border: 2px solid;
	        border-radius: 15px;
	        border-color: black""")
        self.label_pergunta.setWordWrap(True)

        self.resposta_1.setText(self.pergunta[2])
        self.resposta_2.setText(self.pergunta[3])
        self.resposta_3.setText(self.pergunta[4])
        self.resposta_4.setText(self.pergunta[5])

        self.resposta_certa = self.pergunta[6]


    def confirmar_resposta(self, s):

        if self.num_perguntas > 0 and self.num_perguntas <= 30:

            msg = QMessageBox()
            msg.setWindowTitle('Loading Python Quiz')
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setText('Confirma resposta selecionada?')
            resp = msg.exec_()

            if resp == QMessageBox.Yes:

                if s == self.resposta_certa:     # se resposta certa

                    if s == "1":
                        r_correta = self.resposta_1
                    elif s == "2":
                        r_correta = self.resposta_2
                    elif s == "3":
                        r_correta = self.resposta_3
                    elif s == "4":
                        r_correta = self.resposta_4

                    r_correta.setStyleSheet(u"""
                                    QCommandLinkButton{
                                        background-color:rgb(0, 200, 0);
                                        color: rgb(0,0,0);
                                        border: 2px solid;
                                        border-radius: 15px;
                                        border-color: black
                                    }""")

                    msg = QMessageBox()
                    msg.setWindowTitle('Loading Python Quiz')
                    msg.setText('Resposta Certa!')
                    msg.exec_()

                else:                            #  se resposta errrada

                    self.erros.append(self.pergunta[7])

                    if self.resposta_certa == "1":
                        r_correta = self.resposta_1
                    elif self.resposta_certa == "2":
                        r_correta = self.resposta_2
                    elif self.resposta_certa == "3":
                        r_correta = self.resposta_3
                    elif self.resposta_certa == "4":
                        r_correta = self.resposta_4

                    r_correta.setStyleSheet(u"""
                                    QCommandLinkButton{
                                        background-color:rgb(250, 0, 0);
                                        color: rgb(0,0,0);
                                        border: 2px solid;
                                        border-radius: 15px;
                                        border-color: black
                                    }""")

                    msg = QMessageBox()
                    msg.setWindowTitle('Loading Python Quiz')
                    msg.setText('Resposta Errada!')
                    msg.exec_()

                self.formatar_respostas()
                self.escolha_perguntas()


    def formatar_respostas(self):

        lista = [self.resposta_1, self.resposta_2, self.resposta_3, self.resposta_4]

        for item in lista:
            item.setStyleSheet(u"""
                                    QCommandLinkButton{
                                        background-color:rgb(34, 60, 122);
                                        color: rgb(255,255,255);
                                        border: 2px solid;
                                        border-radius: 15px;
                                        border-color: black
                                    }
                                    QCommandLinkButton:hover{
                                        color: rgb(34, 60, 122);
                                        background-color: rgb(0,0,0);
                                    }""")


    def fim_jogo(self):

        if matematica in self.erros:
            erros_matematica = self.erros.count(matematica)
        else:
            erros_matematica = 0
        if portugues in self.erros:
            erros_portugues = self.erros.count(portugues)
        else:
            erros_portugues = 0
        if historia in self.erros:
            erros_historia = self.erros.count(historia)
        else:
            erros_historia = 0
        if geografia in self.erros:
            erros_geografia = self.erros.count(geografia)
        else:
            erros_geografia = 0
        if ciencia in self.erros:
            erros_ciencia = self.erros.count(ciencia)
        else:
            erros_ciencia = 0




if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()



