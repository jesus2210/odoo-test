#!/usr/bin/python
import unittest
import math


def calculaDiscriminante(a, b, c):
    discriminante=float((b**2)-(4*a*c))
    return discriminante

def calculaRaiz(discriminante):
    resultado=float(discriminante**0.5)
    return resultado

def calculaResultado1(a, raiz, b):
    resultado1=float((-b+raiz)/(2*a))
    return resultado1

def calculaResultado2(a, raiz, b):
    resultado2=float((-b-raiz)/(2*a))
    return resultado2


def main():
    print 'ingrese 3 valores enteros'
    a=int(input('valor a: '))
    b=int(input('valor b: '))
    c=int(input('valor c: '))
    discriminante=calculaDiscriminante(a, b, c)
    
    print 'Discriminante: '+str(discriminante)
    
    if (discriminante < 0):
        print 'La raiz es imaginaria'
    elif (discriminante == 0):
        print 'La raiz no puede ser cero'
    else:
        raiz = calculaRaiz(discriminante)
        print 'Raiz '+str(raiz)
        resultado1=float(calculaResultado1(a, raiz, b))
        resultado2=float(calculaResultado2(a, raiz, b))
        print 'Resultado 1: ' + str(resultado1)
        print 'Resultado 2: ' +  str(resultado2)
        

        
# Pruebas Unitarias

class TestUM(unittest.TestCase):
    def test_caso1_2_6_4(self):
        self.assertEqual(4,calculaDiscriminante(2, 6, 4))
    def test_caso2_2_6_4(self):
        self.assertNotEqual(1,calculaDiscriminante(2, 6, 4))
    def test_caso_raiz(self):
        self.assertEqual(2,calculaRaiz(4))
    def test_caso1_resultado1(self):
        self.assertEqual(-1, calculaResultado1(2,2,6))


if __name__ == '__main__':
    #unittest.main()
    main()

