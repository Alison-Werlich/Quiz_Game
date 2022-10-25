# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Interface_Grafica.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import Imagem_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QSize(1080, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Paginas = QStackedWidget(self.centralwidget)
        self.Paginas.setObjectName(u"Paginas")
        self.Paginas.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.153, x2:1, y2:0, stop:0 rgba(0, 92, 205, 255), stop:1 rgba(255, 255, 255, 255))")
        self.Pagina_Inicial = QWidget()
        self.Pagina_Inicial.setObjectName(u"Pagina_Inicial")
        self.Pagina_Inicial.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.Pagina_Inicial)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_titulo = QLabel(self.Pagina_Inicial)
        self.label_titulo.setObjectName(u"label_titulo")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_titulo.sizePolicy().hasHeightForWidth())
        self.label_titulo.setSizePolicy(sizePolicy)
        self.label_titulo.setMaximumSize(QSize(16777215, 16777215))
        self.label_titulo.setLayoutDirection(Qt.LeftToRight)
        self.label_titulo.setStyleSheet(u"background-color: rgb(255, 255, 255,0);")
        self.label_titulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_titulo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_iniciar = QPushButton(self.Pagina_Inicial)
        self.btn_iniciar.setObjectName(u"btn_iniciar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_iniciar.sizePolicy().hasHeightForWidth())
        self.btn_iniciar.setSizePolicy(sizePolicy1)
        self.btn_iniciar.setMaximumSize(QSize(250, 50))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.btn_iniciar.setFont(font)
        self.btn_iniciar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_iniciar.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color:rgb(34, 60, 122);\n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(34, 60, 122);\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_iniciar)

        self.Espaco = QSpacerItem(70, 1, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.Espaco)

        self.label_equipe = QLabel(self.Pagina_Inicial)
        self.label_equipe.setObjectName(u"label_equipe")
        sizePolicy.setHeightForWidth(self.label_equipe.sizePolicy().hasHeightForWidth())
        self.label_equipe.setSizePolicy(sizePolicy)
        self.label_equipe.setMaximumSize(QSize(420, 220))
        self.label_equipe.setStyleSheet(u"QLabel{\n"
"\n"
"	background-color: rgba(240, 240, 240, 0);\n"
"	color: rgb(52, 51, 153);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.label_equipe)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.Paginas.addWidget(self.Pagina_Inicial)
        self.Pagina_Menu = QWidget()
        self.Pagina_Menu.setObjectName(u"Pagina_Menu")
        self.verticalLayout_5 = QVBoxLayout(self.Pagina_Menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_logo_inicio = QLabel(self.Pagina_Menu)
        self.label_logo_inicio.setObjectName(u"label_logo_inicio")
        self.label_logo_inicio.setMaximumSize(QSize(16777215, 250))
        self.label_logo_inicio.setStyleSheet(u"background-color: rgb(0,0,0,0)")

        self.verticalLayout_5.addWidget(self.label_logo_inicio)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_inicio = QLabel(self.Pagina_Menu)
        self.label_inicio.setObjectName(u"label_inicio")
        self.label_inicio.setMaximumSize(QSize(16777215, 16777215))
        self.label_inicio.setStyleSheet(u"background-color:rgb(34, 60, 122,0);\n"
"border: 2px solid;\n"
"border-radius:5px;\n"
"border-color: black\n"
"")

        self.horizontalLayout_2.addWidget(self.label_inicio)

        self.frame = QFrame(self.Pagina_Menu)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color:rgb(34, 60, 122,0);\n"
"border: 2px solid;\n"
"border-radius:5px;\n"
"border-color: black\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_jogar = QPushButton(self.frame)
        self.btn_jogar.setObjectName(u"btn_jogar")
        sizePolicy.setHeightForWidth(self.btn_jogar.sizePolicy().hasHeightForWidth())
        self.btn_jogar.setSizePolicy(sizePolicy)
        self.btn_jogar.setMinimumSize(QSize(250, 50))
        self.btn_jogar.setMaximumSize(QSize(250, 50))
        self.btn_jogar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_jogar.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color:rgb(34, 60, 122);\n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(34, 60, 122);\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_jogar, 0, Qt.AlignHCenter)

        self.btn_regras = QPushButton(self.frame)
        self.btn_regras.setObjectName(u"btn_regras")
        sizePolicy.setHeightForWidth(self.btn_regras.sizePolicy().hasHeightForWidth())
        self.btn_regras.setSizePolicy(sizePolicy)
        self.btn_regras.setMinimumSize(QSize(250, 50))
        self.btn_regras.setMaximumSize(QSize(250, 50))
        self.btn_regras.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_regras.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color:rgb(34, 60, 122);\n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(34, 60, 122);\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_regras, 0, Qt.AlignHCenter)

        self.btn_sair = QPushButton(self.frame)
        self.btn_sair.setObjectName(u"btn_sair")
        sizePolicy.setHeightForWidth(self.btn_sair.sizePolicy().hasHeightForWidth())
        self.btn_sair.setSizePolicy(sizePolicy)
        self.btn_sair.setMinimumSize(QSize(250, 50))
        self.btn_sair.setMaximumSize(QSize(250, 50))
        self.btn_sair.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color:rgb(34, 60, 122);\n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(34, 60, 122);\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_sair, 0, Qt.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.Paginas.addWidget(self.Pagina_Menu)
        self.Pagina_Regras = QWidget()
        self.Pagina_Regras.setObjectName(u"Pagina_Regras")
        self.verticalLayout_10 = QVBoxLayout(self.Pagina_Regras)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_5 = QFrame(self.Pagina_Regras)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: none")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_regras = QLabel(self.frame_5)
        self.label_regras.setObjectName(u"label_regras")

        self.verticalLayout_9.addWidget(self.label_regras)

        self.btn_voltar = QPushButton(self.frame_5)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setMinimumSize(QSize(250, 50))
        self.btn_voltar.setMaximumSize(QSize(250, 50))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_voltar.setFont(font1)
        self.btn_voltar.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color:rgb(34, 60, 122);\n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(34, 60, 122);\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.btn_voltar, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.Paginas.addWidget(self.Pagina_Regras)
        self.Pagina_Jogo = QWidget()
        self.Pagina_Jogo.setObjectName(u"Pagina_Jogo")
        self.verticalLayout_7 = QVBoxLayout(self.Pagina_Jogo)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.Pagina_Jogo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 280))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255,0);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_pergunta = QLabel(self.frame_2)
        self.label_pergunta.setObjectName(u"label_pergunta")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_pergunta.sizePolicy().hasHeightForWidth())
        self.label_pergunta.setSizePolicy(sizePolicy2)
        self.label_pergunta.setMaximumSize(QSize(16777215, 16777215))
        self.label_pergunta.setStyleSheet(u"	background-color:rgb(34, 60, 122);\n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"\n"
"\n"
"")
        self.label_pergunta.setAlignment(Qt.AlignCenter)
        self.label_pergunta.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_pergunta)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_logo_jogo = QLabel(self.frame_2)
        self.label_logo_jogo.setObjectName(u"label_logo_jogo")
        self.label_logo_jogo.setMaximumSize(QSize(200, 200))
        self.label_logo_jogo.setStyleSheet(u"background-color: rgb(255, 255, 255,0);")

        self.verticalLayout_8.addWidget(self.label_logo_jogo, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_n_pergunta = QLabel(self.frame_2)
        self.label_n_pergunta.setObjectName(u"label_n_pergunta")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_n_pergunta.sizePolicy().hasHeightForWidth())
        self.label_n_pergunta.setSizePolicy(sizePolicy3)
        self.label_n_pergunta.setMinimumSize(QSize(250, 50))
        self.label_n_pergunta.setMaximumSize(QSize(250, 50))
        self.label_n_pergunta.setStyleSheet(u"	background-color:rgb(34, 60, 122);\n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black;\n"
"	font: 14px\n"
"\n"
"\n"
"")

        self.verticalLayout_8.addWidget(self.label_n_pergunta, 0, Qt.AlignRight)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.Pagina_Jogo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QCommandLinkButton{\n"
"\n"
"	background-color:rgb(34, 60, 122);\n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}\n"
"\n"
"QCommandLinkButton:hover{\n"
"\n"
"	color: rgb(34, 60, 122);\n"
"	background-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: none\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.resposta_1 = QCommandLinkButton(self.frame_3)
        self.resposta_1.setObjectName(u"resposta_1")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.resposta_1.setFont(font2)
        self.resposta_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Imagem/Imagens/images-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resposta_1.setIcon(icon)

        self.verticalLayout_6.addWidget(self.resposta_1)

        self.resposta_2 = QCommandLinkButton(self.frame_3)
        self.resposta_2.setObjectName(u"resposta_2")
        self.resposta_2.setFont(font2)
        self.resposta_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.resposta_2.setIcon(icon)

        self.verticalLayout_6.addWidget(self.resposta_2)

        self.resposta_3 = QCommandLinkButton(self.frame_3)
        self.resposta_3.setObjectName(u"resposta_3")
        self.resposta_3.setEnabled(True)
        self.resposta_3.setFont(font2)
        self.resposta_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.resposta_3.setIcon(icon)

        self.verticalLayout_6.addWidget(self.resposta_3)

        self.resposta_4 = QCommandLinkButton(self.frame_3)
        self.resposta_4.setObjectName(u"resposta_4")
        self.resposta_4.setFont(font2)
        self.resposta_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.resposta_4.setIcon(icon)

        self.verticalLayout_6.addWidget(self.resposta_4)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.Pagina_Jogo)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255,0);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_novo_jogo = QPushButton(self.frame_4)
        self.btn_novo_jogo.setObjectName(u"btn_novo_jogo")
        self.btn_novo_jogo.setMinimumSize(QSize(250, 50))
        self.btn_novo_jogo.setMaximumSize(QSize(250, 16777215))
        self.btn_novo_jogo.setFont(font1)
        self.btn_novo_jogo.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color:rgb(34, 60, 122);\n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(34, 60, 122);\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_novo_jogo)

        self.btn_voltar_2 = QPushButton(self.frame_4)
        self.btn_voltar_2.setObjectName(u"btn_voltar_2")
        self.btn_voltar_2.setMinimumSize(QSize(250, 50))
        self.btn_voltar_2.setMaximumSize(QSize(250, 16777215))
        self.btn_voltar_2.setFont(font1)
        self.btn_voltar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar_2.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color:rgb(34, 60, 122);\n"
"	color: rgb(255,255,255);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	color: rgb(34, 60, 122);\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btn_voltar_2)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.Paginas.addWidget(self.Pagina_Jogo)

        self.verticalLayout_4.addWidget(self.Paginas)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Paginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/Imagem/Imagens/Unigranrio_inicio.png\" /></p></body></html>", None))
        self.btn_iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar ", None))
        self.label_equipe.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">EQUIPE DE DESENVOLVIMENTO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ALISON PEDRO WERLICH</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">DOUGLAS DOS SANTOS COSTA DE ARAUJO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">KAYKY WILIAM DA COSTA FERREIRA</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">THA\u00cdS GON\u00c7ALVES VITALINO DE SOUZA</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">MATHEUS DIAS DA SILVA PAULA</span></p></body></html>", None))
        self.label_logo_inicio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/Imagem/Imagens/Unigranrio_com_logo-removebg-preview.png\"/></p></body></html>", None))
        self.label_inicio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">QUIZ LOADING PYTHON</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">SEJA MUITO BEM VINDO!!! </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">TESTE SEUS CONHECIMENTOS NESTE QUIZ DE </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">CONHECIMENTOS GERAIS QUE REPLICA PERGUNTAS</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">DE VESTIBULARES E CONCURSOS PUBLICOS, E AO </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">FINAL TENHA UM HISTORICO DE TEMAS COM MENOS</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">ACERTOS PARA PODER FOCAR SEUS ESTUDOS.</span></p><p align=\"center\"><span style=\" font-size:12pt; "
                        "font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">BOA SORTE!!!</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.btn_jogar.setText(QCoreApplication.translate("MainWindow", u"JOGAR", None))
        self.btn_regras.setText(QCoreApplication.translate("MainWindow", u"REGRAS", None))
        self.btn_sair.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        self.label_regras.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline;\">REGRAS E INFORMA\u00c7\u00d5ES</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:12pt;\">REGRAS</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.btn_voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR AO MENU", None))
        self.label_pergunta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">CLIQUE EM NOVO JOGO PARA INICIAR</span></p></body></html>", None))
        self.label_logo_jogo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Imagem/Imagens/Unigranrio_icone.png\"/></p></body></html>", None))
        self.label_n_pergunta.setText("")
        self.resposta_1.setText("")
        self.resposta_2.setText("")
        self.resposta_3.setText("")
        self.resposta_4.setText("")
        self.btn_novo_jogo.setText(QCoreApplication.translate("MainWindow", u"NOVO JOGO", None))
        self.btn_voltar_2.setText(QCoreApplication.translate("MainWindow", u"VOLTAR AO MENU", None))
    # retranslateUi

