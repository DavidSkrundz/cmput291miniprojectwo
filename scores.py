import re
def scores_gen(contents):
	lines = contents.split("\n")
	scores = []
	for line in lines:
		line = line.lower()
		if re.match("review/score: .*", line):
			line = line[14:]
			for match in re.finditer("\d+\.\d+", line):
				score = match.group(0)
				if not score in scores:
					scores.append(score + "," + str(len(scores) + 1))
	out = open("scores.txt", "w")
	for score in scores:
		out.write(score + "\n")

if __name__ == "__main__":
	import sys
	contents = sys.stdin.read()
	scores_gen(contents)