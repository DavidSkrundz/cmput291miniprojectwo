if __name__ == "__main__":
	import sys
	contents = sys.stdin.read()

	from pterms import pterms_gen
	from rterms import rterms_Gen
	from reviews import reviewsgen
	from scores import scores_gen

	pterms_gen(contents)
	rterms_Gen(contents)
	reviewsgen(contents)
	scores_gen(contents)