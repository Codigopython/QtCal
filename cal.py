#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Calculadora:
    def __init__(self):
        pass

    def total(self, elementos, operadores):
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

    def memoria(self, elementos, operadores):
        cadena = ""
        a = 0
        for i in elementos:
            if a >= len(operadores):
                cadena += str(i)
            else:
                cadena += str(i) + operadores[a]
            a += 1
        return cadena