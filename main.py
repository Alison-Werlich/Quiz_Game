
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

        self.btn_iniciar.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Menu))
        self.btn_jogar.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Jogo))
        self.btn_regras.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Regras))
        self.btn_voltar.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Menu))
        self.btn_voltar_2.clicked.connect(lambda: self.Paginas.setCurrentWidget(self.Pagina_Menu))

        self.btn_sair.clicked.connect(lambda:sys.exit())

        self.btn_novo_jogo.clicked.connect(lambda: self.iniciar_game())
        ###################################################################


    def iniciar_game(self):

        self.num_perguntas = 0
        db = Data_base()
        self.perguntas_portugues = db.criar_lista_perguntas('portugues')
        self.perguntas_matematica = db.criar_lista_perguntas('matematica')
        self.perguntas_ciencias = db.criar_lista_perguntas('ciencias')
        self.perguntas_historia = db.criar_lista_perguntas('historia')
        self.perguntas_geofrafia = db.criar_lista_perguntas('geografia')

        self.escolha_perguntas()


    def escolha_perguntas(self):

        if self.num_perguntas < 7:
            pergunta = self.perguntas_portugues[randint(0, len(self.perguntas_portugues) - 1)]
            self.perguntas_portugues.remove(pergunta)

        elif self.num_perguntas < 13:
            pass
        elif self.num_perguntas < 19:
            pass
        elif self.num_perguntas < 25:
            pass
        elif self.num_perguntas <=30:
            pass
        else:
            pass

        self.label_pergunta.setText(pergunta[1])
        self.resposta_1.setText(pergunta[2])
        self.resposta_2.setText(pergunta[3])
        self.resposta_3.setText(pergunta[4])
        self.resposta_4.setText(pergunta[5])

        self.resposta_certa = pergunta[6]

        self.num_perguntas += 1


if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec_()



