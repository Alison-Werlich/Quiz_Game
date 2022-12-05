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
        MainWindow.setEnabled(True)
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QSize(1080, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_15 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Paginas = QStackedWidget(self.centralwidget)
        self.Paginas.setObjectName(u"Paginas")
        self.Paginas.setStyleSheet(u"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.153, x2:1, y2:0, stop:0 rgba(0, 92, 205, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"\n"
"\n"
"\n"
"")
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
        self.frame_6 = QFrame(self.Pagina_Inicial)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setStyleSheet(u"background-color:rgb(34, 60, 122,0);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.verticalLayout_12.addWidget(self.label)

        self.login_usuario = QLineEdit(self.frame_7)
        self.login_usuario.setObjectName(u"login_usuario")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.login_usuario.sizePolicy().hasHeightForWidth())
        self.login_usuario.setSizePolicy(sizePolicy3)
        self.login_usuario.setMaximumSize(QSize(16777215, 50))
        self.login_usuario.setFont(font)
        self.login_usuario.setStyleSheet(u"background-color: rgb(228, 231, 255);")

        self.verticalLayout_12.addWidget(self.login_usuario)

        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font)

        self.verticalLayout_12.addWidget(self.label_2)

        self.login_senha = QLineEdit(self.frame_7)
        self.login_senha.setObjectName(u"login_senha")
        sizePolicy3.setHeightForWidth(self.login_senha.sizePolicy().hasHeightForWidth())
        self.login_senha.setSizePolicy(sizePolicy3)
        self.login_senha.setMaximumSize(QSize(16777215, 50))
        self.login_senha.setFont(font)
        self.login_senha.setStyleSheet(u"background-color: rgb(228, 231, 255);")
        self.login_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_12.addWidget(self.login_senha)


        self.horizontalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy4)
        self.frame_8.setMaximumSize(QSize(200, 200))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer = QSpacerItem(5, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer)

        self.btn_login = QPushButton(self.frame_8)
        self.btn_login.setObjectName(u"btn_login")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy5)
        self.btn_login.setMaximumSize(QSize(250, 50))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_13.addWidget(self.btn_login)

        self.btn_novo_cadastro = QPushButton(self.frame_8)
        self.btn_novo_cadastro.setObjectName(u"btn_novo_cadastro")
        self.btn_novo_cadastro.setMaximumSize(QSize(250, 50))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_novo_cadastro.setFont(font2)
        self.btn_novo_cadastro.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_13.addWidget(self.btn_novo_cadastro)


        self.horizontalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_6)

        self.label_equipe = QLabel(self.Pagina_Inicial)
        self.label_equipe.setObjectName(u"label_equipe")
        sizePolicy.setHeightForWidth(self.label_equipe.sizePolicy().hasHeightForWidth())
        self.label_equipe.setSizePolicy(sizePolicy)
        self.label_equipe.setMaximumSize(QSize(520, 220))
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

        self.verticalSpacer_2 = QSpacerItem(10, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMaximumSize(QSize(16777215, 50))
        self.frame_13.setStyleSheet(u"border:nome")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_nome_logado = QLabel(self.frame_13)
        self.label_nome_logado.setObjectName(u"label_nome_logado")
        self.label_nome_logado.setFont(font)
        self.label_nome_logado.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.label_nome_logado)

        self.pushButton = QPushButton(self.frame_13)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_10.addWidget(self.pushButton)


        self.verticalLayout_3.addWidget(self.frame_13)


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
        self.label_regras.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_regras)

        self.btn_voltar = QPushButton(self.frame_5)
        self.btn_voltar.setObjectName(u"btn_voltar")
        self.btn_voltar.setMinimumSize(QSize(250, 50))
        self.btn_voltar.setMaximumSize(QSize(250, 50))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.btn_voltar.setFont(font3)
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
        self.Pagina_Cadastro = QWidget()
        self.Pagina_Cadastro.setObjectName(u"Pagina_Cadastro")
        self.verticalLayout_14 = QVBoxLayout(self.Pagina_Cadastro)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_3 = QLabel(self.Pagina_Cadastro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")

        self.verticalLayout_14.addWidget(self.label_3)

        self.frame_9 = QFrame(self.Pagina_Cadastro)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Cadastro_Nome = QLineEdit(self.frame_9)
        self.Cadastro_Nome.setObjectName(u"Cadastro_Nome")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Cadastro_Nome.sizePolicy().hasHeightForWidth())
        self.Cadastro_Nome.setSizePolicy(sizePolicy6)
        self.Cadastro_Nome.setMaximumSize(QSize(16777215, 50))
        self.Cadastro_Nome.setFont(font2)
        self.Cadastro_Nome.setStyleSheet(u"\n"
"QLineEdit{\n"
"\n"
"	\n"
"	background-color: rgb(229, 229, 229);\n"
"	color: rgb(0,0,0);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}")
        self.Cadastro_Nome.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.Cadastro_Nome)

        self.Cadastro_Sobrenome = QLineEdit(self.frame_9)
        self.Cadastro_Sobrenome.setObjectName(u"Cadastro_Sobrenome")
        self.Cadastro_Sobrenome.setMaximumSize(QSize(16777215, 50))
        self.Cadastro_Sobrenome.setFont(font2)
        self.Cadastro_Sobrenome.setStyleSheet(u"QLineEdit{\n"
"\n"
"	\n"
"	background-color: rgb(229, 229, 229);\n"
"	color: rgb(0,0,0);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}")

        self.horizontalLayout_6.addWidget(self.Cadastro_Sobrenome)


        self.verticalLayout_14.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.Pagina_Cadastro)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Cadastro_Login = QLineEdit(self.frame_10)
        self.Cadastro_Login.setObjectName(u"Cadastro_Login")
        self.Cadastro_Login.setMaximumSize(QSize(16777215, 50))
        self.Cadastro_Login.setFont(font2)
        self.Cadastro_Login.setStyleSheet(u"QLineEdit{\n"
"\n"
"	\n"
"	background-color: rgb(229, 229, 229);\n"
"	color: rgb(0,0,0);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}")

        self.horizontalLayout_7.addWidget(self.Cadastro_Login)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_14.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.Pagina_Cadastro)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Cadastro_Senha_1 = QLineEdit(self.frame_11)
        self.Cadastro_Senha_1.setObjectName(u"Cadastro_Senha_1")
        self.Cadastro_Senha_1.setMaximumSize(QSize(16777215, 50))
        self.Cadastro_Senha_1.setFont(font2)
        self.Cadastro_Senha_1.setStyleSheet(u"QLineEdit{\n"
"\n"
"	\n"
"	background-color: rgb(229, 229, 229);\n"
"	color: rgb(0,0,0);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}")
        self.Cadastro_Senha_1.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.Cadastro_Senha_1)

        self.Cadastro_Senha_2 = QLineEdit(self.frame_11)
        self.Cadastro_Senha_2.setObjectName(u"Cadastro_Senha_2")
        self.Cadastro_Senha_2.setMaximumSize(QSize(16777215, 50))
        self.Cadastro_Senha_2.setFont(font2)
        self.Cadastro_Senha_2.setStyleSheet(u"QLineEdit{\n"
"\n"
"	\n"
"	background-color: rgb(229, 229, 229);\n"
"	color: rgb(0,0,0);\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"	border-color: black\n"
"}")
        self.Cadastro_Senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.Cadastro_Senha_2)


        self.verticalLayout_14.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.Pagina_Cadastro)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_cadastrar = QPushButton(self.frame_12)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMaximumSize(QSize(250, 50))
        self.btn_cadastrar.setFont(font2)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_9.addWidget(self.btn_cadastrar)

        self.btn_cadastro_voltar = QPushButton(self.frame_12)
        self.btn_cadastro_voltar.setObjectName(u"btn_cadastro_voltar")
        self.btn_cadastro_voltar.setMaximumSize(QSize(250, 50))
        self.btn_cadastro_voltar.setFont(font2)
        self.btn_cadastro_voltar.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_9.addWidget(self.btn_cadastro_voltar)


        self.verticalLayout_14.addWidget(self.frame_12)

        self.Paginas.addWidget(self.Pagina_Cadastro)
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
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_pergunta.sizePolicy().hasHeightForWidth())
        self.label_pergunta.setSizePolicy(sizePolicy7)
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
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_n_pergunta.sizePolicy().hasHeightForWidth())
        self.label_n_pergunta.setSizePolicy(sizePolicy8)
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
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.resposta_1.setFont(font4)
        self.resposta_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Imagem/Imagens/images-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resposta_1.setIcon(icon)

        self.verticalLayout_6.addWidget(self.resposta_1)

        self.resposta_2 = QCommandLinkButton(self.frame_3)
        self.resposta_2.setObjectName(u"resposta_2")
        self.resposta_2.setFont(font4)
        self.resposta_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.resposta_2.setIcon(icon)

        self.verticalLayout_6.addWidget(self.resposta_2)

        self.resposta_3 = QCommandLinkButton(self.frame_3)
        self.resposta_3.setObjectName(u"resposta_3")
        self.resposta_3.setEnabled(True)
        self.resposta_3.setFont(font4)
        self.resposta_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.resposta_3.setIcon(icon)

        self.verticalLayout_6.addWidget(self.resposta_3)

        self.resposta_4 = QCommandLinkButton(self.frame_3)
        self.resposta_4.setObjectName(u"resposta_4")
        self.resposta_4.setFont(font4)
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
        self.btn_novo_jogo.setFont(font3)
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
        self.btn_voltar_2.setFont(font3)
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
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_11 = QHBoxLayout(self.page)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(20)
        self.label_4.setFont(font5)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255, 0);\n"
"text-align: center;\n"
"display: flex;\n"
"justify-content: center;\n"
"align-items: center;")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.BTN_voltarmenu = QPushButton(self.page)
        self.BTN_voltarmenu.setObjectName(u"BTN_voltarmenu")
        self.BTN_voltarmenu.setMaximumSize(QSize(251, 50))
        self.BTN_voltarmenu.setFont(font)
        self.BTN_voltarmenu.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_11.addWidget(self.BTN_voltarmenu)

        self.Paginas.addWidget(self.page)

        self.verticalLayout_15.addWidget(self.Paginas)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Cadastro_Senha_1, self.btn_novo_jogo)
        QWidget.setTabOrder(self.btn_novo_jogo, self.btn_cadastro_voltar)
        QWidget.setTabOrder(self.btn_cadastro_voltar, self.Cadastro_Nome)
        QWidget.setTabOrder(self.Cadastro_Nome, self.Cadastro_Sobrenome)
        QWidget.setTabOrder(self.Cadastro_Sobrenome, self.Cadastro_Login)
        QWidget.setTabOrder(self.Cadastro_Login, self.Cadastro_Senha_2)
        QWidget.setTabOrder(self.Cadastro_Senha_2, self.btn_voltar_2)
        QWidget.setTabOrder(self.btn_voltar_2, self.btn_cadastrar)
        QWidget.setTabOrder(self.btn_cadastrar, self.resposta_3)
        QWidget.setTabOrder(self.resposta_3, self.resposta_4)
        QWidget.setTabOrder(self.resposta_4, self.btn_sair)
        QWidget.setTabOrder(self.btn_sair, self.btn_voltar)
        QWidget.setTabOrder(self.btn_voltar, self.btn_regras)
        QWidget.setTabOrder(self.btn_regras, self.resposta_1)
        QWidget.setTabOrder(self.resposta_1, self.resposta_2)
        QWidget.setTabOrder(self.resposta_2, self.btn_jogar)
        QWidget.setTabOrder(self.btn_jogar, self.login_usuario)
        QWidget.setTabOrder(self.login_usuario, self.login_senha)
        QWidget.setTabOrder(self.login_senha, self.btn_login)
        QWidget.setTabOrder(self.btn_login, self.btn_novo_cadastro)

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.login_usuario.setInputMask("")
        self.login_usuario.setText("")
        self.login_usuario.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.login_senha.setText("")
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_novo_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_equipe.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">EQUIPE DE DESENVOLVIMENTO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ALISON PEDRO WERLICH</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">DOUGLAS DOS SANTOS COSTA DE ARAUJO</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">KAYKY WILIAM DA COSTA FERREIRA</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">THA\u00cdS GON\u00c7ALVES VITALINO DE SOUZA</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">MATHEUS DIAS DA SILVA PAULA</span></p></body></html>", None))
        self.label_logo_inicio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/Imagem/Imagens/Unigranrio_com_logo-removebg-preview.png\"/></p></body></html>", None))
        self.label_inicio.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">QUIZ LOADING PYTHON</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">SEJA MUITO BEM VINDO!!! </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">TESTE SEUS CONHECIMENTOS NESTE QUIZ DE </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">CONHECIMENTOS GERAIS QUE REPLICA PERGUNTAS</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">DE VESTIBULARES E CONCURSOS PUBLICOS, E AO </span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">FINAL TENHA UM HISTORICO DE TEMAS COM MENOS</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">ACERTOS PARA PODER FOCAR SEUS ESTUDOS.</span></p><p align=\"center\"><span style=\" font-size:12pt; "
                        "font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">BOA SORTE!!!</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.btn_jogar.setText(QCoreApplication.translate("MainWindow", u"JOGAR", None))
        self.btn_regras.setText(QCoreApplication.translate("MainWindow", u"REGRAS", None))
        self.btn_sair.setText(QCoreApplication.translate("MainWindow", u"SAIR", None))
        self.label_nome_logado.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
        self.label_regras.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; text-decoration: underline;\">REGRAS E INFORMA\u00c7\u00d5ES</span></p><p align=\"center\"><br/></p><p><span style=\" font-size:16pt;\">Quiz Loading Python se trata de um game no modelo quiz com o objetivo de auxiliar no estudo para vestibulares e concursos.</span></p><p><span style=\" font-size:16pt;\">Ao todo s\u00e3o 30 perguntas divididas em cinco disciplinas (Portugu\u00eas, Matem\u00e1tica, Geografia, Hist\u00f3ria e Ci\u00eancias) sendo seis perguntas de cada mat\u00e9ria por rodada.</span></p><p><span style=\" font-size:16pt;\">O jogo simula uma prova de vestibular ou concurso, onde todas as perguntas s\u00e3o de vestibulares e concursos passados.</span></p><p><span style=\" font-size:16pt;\">Ao final da partida o jogador ter\u00e1 um relat\u00f3rio contendo a quantidade de erros total e uma nota baseado na quantidade de acertos, tamb\u00e9m ser\u00e1 gerado um relat\u00f3rio detalhado por mat\u00e9ria mostrando a qu"
                        "antidade de erros em cada mat\u00e9ria, sendo um \u00f3timo auxilio para saber onde o jogador tem maior dificuldade podendo assim focar melhor seus estudos.</span></p><p><br/></p><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Regra 01</span><span style=\" font-size:16pt;\"> - O jogador n\u00e3o poder\u00e1 fechar o programa ap\u00f3s iniciar a partida, pois o progresso n\u00e3o ser\u00e1 salvo;</span></p><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Regra 02</span><span style=\" font-size:16pt;\"> - Para avan\u00e7ar para a pr\u00f3xima pergunta, \u00e9 necess\u00e1rio responder a anterior;</span></p><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Regra 03</span><span style=\" font-size:16pt;\"> - Para jogar \u00e9 necess\u00e1rio realizar o cadastro, e logar com sua conta;</span></p><p align=\"center\"><br/><br/><span style=\" font-size:16pt;\">Boa Sorte!</span><br/></p><p align=\"justify\"><br/></p><p align="
                        "\"justify\"><br/></p></body></html>", None))
        self.btn_voltar.setText(QCoreApplication.translate("MainWindow", u"VOLTAR AO MENU", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt;\">Cadastro de Usu\u00e1rio </span></p></body></html>", None))
        self.Cadastro_Nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Digite Seu Primeiro Nome", None))
        self.Cadastro_Sobrenome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Digite seu Sobrenome", None))
        self.Cadastro_Login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Digite Seu Login", None))
        self.Cadastro_Senha_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Digite Sua Senha", None))
        self.Cadastro_Senha_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   Repita Sua Senha", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_cadastro_voltar.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        self.label_pergunta.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">CLIQUE EM NOVO JOGO PARA INICIAR</span></p></body></html>", None))
        self.label_logo_jogo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/Imagem/Imagens/Unigranrio_icone.png\"/></p></body></html>", None))
        self.label_n_pergunta.setText("")
        self.resposta_1.setText("")
        self.resposta_2.setText("")
        self.resposta_3.setText("")
        self.resposta_4.setText("")
        self.btn_novo_jogo.setText(QCoreApplication.translate("MainWindow", u"NOVO JOGO", None))
        self.btn_voltar_2.setText(QCoreApplication.translate("MainWindow", u"VOLTAR AO MENU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.BTN_voltarmenu.setText(QCoreApplication.translate("MainWindow", u"Voltar Menu", None))
    # retranslateUi

