#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Calculadora basica escrita solo para mostar como crear una Gui sencilla con
#PyQt, @Harrinsoft - harrinsoft@gmail.com
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic


def total(elementos, operadores):
    y = 0
    for i in operadores:
        if i == "+" and y == 0:
            subtotal = elementos[y] + elementos[y + 1]
        elif i == "+" and y != 0:
            subtotal += elementos[y + 1]
        elif i == "-" and y == 0:
            subtotal = elementos[y] - elementos[y + 1]
        elif i == "-" and y != 0:
            subtotal -= elementos[y + 1]
        elif i == "*" and y == 0:
            subtotal = elementos[y] * elementos[y + 1]
        elif i == "*" and y != 0:
            subtotal *= elementos[y + 1]
        elif i == "/" and y == 0:
            if elementos[y + 1] != 0:
                subtotal = elementos[y] / elementos[y + 1]
            else:
                return "division por 0"
        elif i == "/" and y != 0:
            if elementos[y + 1] != 0:
                subtotal /= elementos[y + 1]
            else:
                return "division por 0"
        y += 1
    return subtotal


def memoria(elementos, operadores):
    cadena = ""
    a = 0
    for i in elementos:
        if a >= len(operadores):
            cadena += str(i)
        else:
            cadena += str(i) + operadores[a]
        a += 1
    return cadena

path = str(sys.path[0])
form_QtCalWindow = uic.loadUiType(path + "/ui/QtCal.ui")[0]


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
        with open("styles.css") as f:
            self.setStyleSheet(f.read())

    def addn(self):
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
                x = total(self.lista_numeros, self.lista_op)
                self.display_ql.setText(str(x))
                self.registro_ql.setText(memoria(self.lista_numeros,
                                                 self.lista_op))
                self.lista_op.append(operacion)
                self.primer_caracter = True
        elif operacion == "R2":
            #if self.totalizo:
            #    self.lista_numeros.append(float(self.display_ql.text()))
            #ejemplo de un QMessageBox
            QMessageBox.information(self, 'Informacion:', 'no implementado '
                                                          'lo sentimos.')
        elif operacion == "=":
            self.lista_numeros.append(float(self.display_ql.text()))
            x = total(self.lista_numeros, self.lista_op)
            self.display_ql.setText(str(x))
            self.registro_ql.setText(memoria(self.lista_numeros,
                                             self.lista_op))
            self.clear(False)
            self.totalizo = True
        elif operacion == "CE":
            self.clear(True)


app = QApplication(sys.argv)
ventana = QtCalWin()
ventana.show()
app.exec_()