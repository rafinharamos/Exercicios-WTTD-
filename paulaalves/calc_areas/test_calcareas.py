import unittest
import calcareas


class TestAreaQuadrado(unittest.TestCase):
	"""
	teste da função areaquadrado()
	"""
	def test_areaquadrado_lado_2(self):
		result = calcareas.areaquadrado(2)
		expected = 4
		self.assertEqual(expected, result)

	def test_areaquadrado_lado_3(self):
		result = calcareas.areaquadrado(3)
		expected = 9
		self.assertEqual(expected, result)

	def test_areaquadrado_lado_10(self):
		result = calcareas.areaquadrado(10)
		expected = 100
		self.assertEqual(expected, result)

	def test_areaquadrado_lado_2_5(self):
		result = calcareas.areaquadrado(2.5)
		expected = 6.25
		self.assertEqual(expected, result)


class TestAreaTriangulo(unittest.TestCase):
	"""
	teste da função areatriangulo()
	"""
	def test_areatriangulo_base_2_altura_4(self):
		result = calcareas.areatriangulo(2, 4)
		expected = 4
		self.assertEqual(expected, result)

	def test_areatriangulo_base_3_altura_7(self):
		result = calcareas.areatriangulo(3, 7)
		expected = 10.5
		self.assertEqual(expected, result)

	def test_areatriangulo_base_10_altura_35(self):
		result = calcareas.areatriangulo(10, 35)
		expected = 175.0
		self.assertEqual(expected, result)

	def test_areatriangulo_base_5_6_altura_11_3(self):
		result = calcareas.areatriangulo(5.6, 11.3)
		expected = 31.64
		self.assertEqual(expected, result)


class TestAreaCirculo(unittest.TestCase):
	"""
	teste da função areacirculo()
	"""
	def test_areacirculo_raio_2(self):
		result = calcareas.areacirculo(2)
		expected = 12.566370614359172
		self.assertEqual(expected, result)

	def test_areacirculo_raio_11(self):
		result = calcareas.areacirculo(11)
		expected = 380.132711084365
		self.assertEqual(expected, result)

	def test_areacirculo_raio_234(self):
		result = calcareas.areacirculo(234)
		expected = 172021.0473399627
		self.assertEqual(expected, result)

	def test_areacirculo_raio_7_3(self):
		result = calcareas.areacirculo(7.3)
		expected = 167.41547250980008
		self.assertEqual(expected, result)


if __name__ == '__main__':
	unittest.main()
