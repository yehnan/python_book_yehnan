
def getbits(x, p, n):
	return (x >> (p+1-n)) & ~(~0b0 << n)

print(bin(getbits(0b10101010, 4, 3)))
print(bin(getbits(0b11110101, 5, 4)))

