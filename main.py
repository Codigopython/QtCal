#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Calculadora basica escrita solo para mostar como crear una Gui sencilla con
#PyQt, @Harrinsoft - harrinsoft@gmail.com
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
from cal import Calculadora

path = str(sys.path[0])
form_QtCalWindow = uic.loadUiType(path + "/ui/QtCal.ui")[0]
path_HojaEstilo = path + "/ui/styles.qss"
calc = Calculadora()


class QtCalWin(QMainWindow, form_QtCalWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        #se conectan las señales de los botones con las funciones
        for i in [self.pb_1, self.pb_2, self.pb_3, self.pb_4,
                  self.pb_5, self.pb_6, self.pb_7, self.pb_8,
                  self.pb_9, self.pb_p, self.pb_0]:
            self.connect(i, SIGNAL("clicked()"), self.addn)

        for i in [self.suma_pb, self.resta_pb, self.multiplicar_pb,
                  self.dividir_pb, self.raiz_pb, self.igual_pb,
                  self.clear_pb]:
            self.connect(i, SIGNAL("clicked()"), self.op)

        self.lista_numeros = []
        self.lista_op = []
        self.primer_caracter = True
        #self.totalizo = False

        #se carga la hoja de estilo de la aplicacion
        self.setObjectName("WindowMain")
        with open(path_HojaEstilo) as f:
            self.setStyleSheet(f.read())

    def addn(self):
        if self.sender().objectName()[-1:] == "p":
            n = "."
        else:
            n = self.sender().objectName()[-1:]
        if self.display_ql.text() == "0" or self.display_ql.text() == "" or \
                self.primer_caracter:
            self.display_ql.setText(str(n))
            self.primer_caracter = False
        else:
            self.display_ql.setText(self.display_ql.text() + str(n))

    def clear(self, opcion):
        while len(self.lista_op):
            self.lista_op.pop(0)
        while len(self.lista_numeros):
            self.lista_numeros.pop(0)
        if opcion:
            self.display_ql.setText("0")
            self.registro_ql.setText("0")

    def op(self):
        operacion = self.sender().text()

        if operacion == "+" or operacion == "-" or operacion == "*" or \
                        operacion == "/":
            if not len(self.lista_numeros):
                self.lista_numeros.append(float(self.display_ql.text()))
                self.registro_ql.setText(self.display_ql.text())
                self.display_ql.setText("0")
                self.lista_op.append(operacion)
            elif len(self.lista_op):
                self.lista_numeros.append(float(self.display_ql.text()))
                x = calc.total(self.lista_numeros, self.lista_op)
                self.display_ql.setText(str(x))
                self.registro_ql.setText(calc.memoria(self.lista_numeros,
                                                      self.lista_op))
                self.lista_op.append(operacion)
                self.primer_caracter = True
        elif operacion == "R2":
            #if self.totalizo:
            #    self.lista_numeros.append(float(self.display_ql.text()))

            QMessageBox.information(self, 'Informacion:', 'no implementado '
                                                          'lo sentimos.')
        elif operacion == "=":
            self.lista_numeros.append(float(self.display_ql.text()))
            x = calc.total(self.lista_numeros, self.lista_op)
            self.display_ql.setText(str(x))
            self.registro_ql.setText(calc.memoria(self.lista_numeros,
                                                  self.lista_op))
            self.clear(False)
            #self.totalizo = True
        elif operacion == "CE":
            self.clear(True)


app = QApplication(sys.argv)
ventana = QtCalWin()
ventana.show()
app.exec_()