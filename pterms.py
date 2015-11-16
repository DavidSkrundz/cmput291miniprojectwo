import re
def pterms_gen(contents):
	lines = contents.split("\n")
	words = []
	reviewIndex = 0
	for line in lines:
		line = line.lower()
		if re.match("product/title: .*", line):
			line = line[15:]
			tempWords = []
			reviewIndex += 1
			for match in re.finditer("[0-9a-z_]{3,}", line):
				word = match.group(0)
				if not word in tempWords:
					tempWords.append(word + "," + str(reviewIndex))
			words += tempWords
	out = open("pterms.txt", "w")
	for word in words:
		out.write(word + "\n")

if __name__ == "__main__":
	import sys
	contents = sys.stdin.read()
	pterms_gen(contents)