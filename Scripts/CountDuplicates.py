import sys

def main(argv):
	input_file = argv[0]
	file = open(input_file, "r")

	arr = file.readlines()
	arr = [line.lower() for line in arr]
	pairs = {i:arr.count(i) for i in arr}

	for k,v in pairs.items():
		if v >= 2:
			print(k.rstrip('\n').capitalize() + " " + str(v))

	print("Total Count: " + str(len(pairs.items())) )

if __name__ == "__main__":
	main(sys.argv[1:])
	pass