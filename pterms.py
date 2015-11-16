import re
def pterms_gen(contents):
	lines = contents.split("\n")
	reviewIndex = 0
	out = open("pterms.txt", "w")
	for line in lines:
		line = line.lower()
		if re.match("product/title: .*", line):
			line = line[15:]
			words = []
			reviewIndex += 1
			for match in re.finditer("[0-9a-z_]{3,}", line):
				word = match.group(0)
				if not word in words:
					words.append(word + "," + str(reviewIndex))
					out.write(word + "," + str(reviewIndex) + "\n")

if __name__ == "__main__":
	import sys
	contents = sys.stdin.read()
	pterms_gen(contents)