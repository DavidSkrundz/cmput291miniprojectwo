import re
def rterms_Gen(stdinContents):
	stdinContents = stdinContents.replace("\\", "\\\\")
	stdinContents = stdinContents.replace("\"", "&quot;")

	reviewIndex = 0
	output = []
	tempwords = []

	for line in stdinContents.split("\n"):
		line = line.lower()
		if (re.match("^(product/productid: )", line)):
			output += tempwords
			tempwords = []
			reviewIndex += 1
			continue

		if(re.match("^(review/summary: )", line)):
			contents = re.finditer("[0-9a-z_]{3,}", line[15:])
			for item in contents:
				word = item.group(0)
				if not word in tempwords:
					tempwords.append(word + "," + str(reviewIndex))

		if(re.match("^(review/text: )", line)):
			contents = re.finditer("[0-9a-z_]{3,}", line[12:])
			for item in contents:
				word = item.group(0)
				if not word in tempwords:
					tempwords.append(word +"," + str(reviewIndex))

	output += tempwords

	out = open("rterms.txt", "w")
	for word in output:
		out.write(word + "\n")

if __name__ == '__main__':
	import sys
	contents = sys.stdin.read()
	rterms_Gen(contents)