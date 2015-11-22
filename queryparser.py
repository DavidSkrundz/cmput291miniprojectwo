#p:stuff -- matches stuff in product title (pterms index)
#pprice -- can be used with > and < to match reviews with a product price matching the requirement
#rscore -- same as pprice (rscore index)
#rdate -- same as pprice with python datetime objects
#r:stuff -- matches stuff in rterms (rterms index)
#stuff -- matches stuff in pterms or rterms and returns the correct review numbers (rterms or pterms index)
import re

def askForQuery():
	while True:
		query = input("What is your database query? ($exit to quit): ")
		if query.lower() == '$exit':
			return
		query = re.sub("\\s+", " ", query)
		query = re.sub("\\s*>\\s*", ">", query)
		query = re.sub("\\s*<\\s*", "<", query)
		print(query)

		requirements = query.split(" ")
		runQuery(requirements)


def runQuery(requirements):

	pTerms = []
	rTerms = []
	genTerms = []

	rScore = []
	rDate = []
	pPrice = []

	for requirement in requirements:
		if requirement.startswith("pprice"):
			pPrice.append(requirement[6:])
		elif requirement.startswith("rscore"):
			rScore.append(requirement[6:])
		elif requirement.startswith("rdate"):
			rDate.append(requirement[5:])
		elif requirement.startswith("p:"):
			pTerms.append(requirement[2:])
		elif requirement.startswith("r:"):
			rTerms.append(requirement[2:])
		else:
			genTerms.append(requirement)

	if not pTerms and not rTerms and not genTerms and not rScore:
		print("Your query could not be run, please include an indexed requirement.")
	else:
		print(pTerms)
		print(rTerms)
		print(genTerms)
		print(rScore)
		print(rDate)
		print(pPrice)


if __name__ == '__main__':
	askForQuery()