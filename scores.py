import re
def scores_gen(contents):
	lines = contents.split("\n")
	reviewNumber = 0
	out = open("scores.txt", "w")
	for line in lines:
		line = line.lower()
		if re.match("review/score: .*", line):
			reviewNumber += 1
			line = line[14:]
			for match in re.finditer("\d+\.\d+", line):
				out.write(match.group(0) + "," + str(reviewNumber) + "\n")

if __name__ == "__main__":
	import sys
	contents = sys.stdin.read()
	scores_gen(contents)