"""
Calcular areas da seguintes figuras geométricas planas:
1. Quadrado = lado * lado
2. Triângulo = (base * altura) / 2
3. Círculo = pi * (r ^ r)
Testes:
1 . Testar se o argumento é numérico - a fazer
2 . Testes de cada funcão:
	* areaquadrado()
	* areatriangulo()
	* areacirculo()
"""
import math

def areaquadrado(lado):
	area = lado * lado
	return area


def areatriangulo(base, altura):
	area = (base * altura) / 2
	return area


def areacirculo(raio):
	area = math.pi * (raio * raio)
	return area
