
class Calculator:
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def add(self):
		answer = self.num1 + self.num2
		return answer

	def subtract(self):
		return self.num1 - self.num2

	def multiply(self):
		return self.num1 * self.num2

	def divide(self):
		return self.num1 / self.num2

	def exponent(self):
		return self.num1 ** self.num2


class Compute(Calculator):
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def radical(self):
		return Calculator(self.num1, (1 / self.num2)).exponent()


# Sample
if __name__ == '__main__':
	data1 = Calculator(3, 2)
	exp = data1.exponent()
	print(exp)

	data2 = Compute(25, 2)
	square = data2.radical()
	print(square)
