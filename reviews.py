def reviewsgen(contents):
	outfile = open("reviews.txt", "w")
	
	reviews = contents.split("\n\n")
	if reviews[-1] == "":
		reviews = reviews[:-1]
		
	reviewno = 1;
	for review in reviews:
		outfile.write(str(reviewno) + ",")
		
		lines = review.split("\n")
		for line in lines:
			vals = line.split(": ", 1)
			quotes = "title" in vals[0] \
				or "profileName" in vals[0] \
				or "summary" in vals[0] \
				or "text" in vals[0]
			
			value = vals[1]
			value = value.replace("\"", "&quot;")
			value = value.replace("\\","\\\\")
			value = value.replace(",", "&com;")
			if quotes:
				outfile.write("\"")
				
			outfile.write(value)
			
			if quotes:
				outfile.write("\"")
				
			if "text" not in vals[0]:
				outfile.write(",")
		
		outfile.write("\n")
		reviewno += 1
		
	outfile.close()
	
if __name__ == "__main__":
	import sys
	contents = sys.stdin.read()
	reviewsgen(contents)