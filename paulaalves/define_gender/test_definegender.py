import unittest
import definegender


class TestGenderFinder(unittest.TestCase):
	"""
	teste para a função genderfinder()
	"""

	def test_gender_finder_if_name_is_paula(self):
		result = definegender.genderfinder('paula')
		expected = 'female'
		self.assertEqual(expected, result)


	def test_gender_finder_if_name_is_leandro(self):
		result = definegender.genderfinder('leandro')
		expected = 'male'
		self.assertEqual(expected, result)


	def test_gender_finder_if_name_is_nei(self):
		result = definegender.genderfinder('nei')
		expected = 'male'
		self.assertEqual(expected, result)


	def test_gender_finder_if_name_is_capa_de_chuva(self):
		result = definegender.genderfinder('capadechuva')
		expected = 'not a name.'
		self.assertEqual(expected, result)


if __name__ == '__main__':
	unittest.main()
