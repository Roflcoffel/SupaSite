import sys, getopt

## Gets the complement a number
def complement(num, comp):
	return comp-num

def main(argv):
	comp = 6 ## Default Value

	try:
		comp = int(argv[1])
	except:
		pass

	try:
		input_file = argv[0]
		file = open(input_file, "r")

		arr = []
		for line in file.readlines():
			if line == "\n":
				print(str(sum(arr)))
				arr = []
				continue

			arr.append(complement(int(line), comp))
	except:
		print("Usage: SumRank.py <file> <complement>")
		pass

if __name__ == "__main__":
	main(sys.argv[1:])
	pass