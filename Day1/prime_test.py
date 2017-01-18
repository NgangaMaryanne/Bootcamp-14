import unittest
from prime_generator import gen_prime

class Prime_Generator_test(unittest.TestCase):
	def test_generates_primes(self):
		self.assertEqual(gen_prime(7), [2,3,5,7])

	def test_Raises_error_for_input_zero(self):
		with self.assertRaises(ValueError):gen_prime(0)

	def test_Raises_error_for_negative_input(self):
		with self.assertRaises(ValueError):gen_prime(-1)

	def test_Raises_error_for_dict_input(self):
		with self.assertRaises(TypeError):gen_prime({})

	def test_generates_one_prime_for_input_2(self):
		self.assertEqual(gen_prime(2), [2])

	def test_Raises_error_for_float_input(self):
		with self.assertRaises(TypeError):gen_prime(4.5)

	def test_Raises_error_for_list_input(self):
		with self.assertRaises(TypeError):gen_prime([2])

	def test_raises_error_for_no_input(self):
		with self.assertRaises (TypeError):gen_prime(None)
	def test_input_is_number(self):
		self.assertIsInstance(gen_prime(9), list)

	def test_Raises_error_for_basstring_input(self):
		with self.assertRaises(TypeError):gen_prime("hello")






if __name__=='__main__':
	unittest.main()