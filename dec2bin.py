# Python program to convert decimal to binary


p=35462379996539444573


# Function to convert Decimal number
# to Binary number
def decimalToBinary(n):
	return bin(n).replace("0b", "")

# Driver code
if __name__ == '__main__':
	print(decimalToBinary(p))

