#also runs the queueue
#also asks for the kiwi

#p:stuff -- matches stuff in product title (pterms index)
#pprice -- can be used with > and < to match reviews with a product price matching the requirement
#rscore -- same as pprice (rscore index)
#rdate -- same as pprice with python datetime objects
#r:stuff -- matches stuff in rterms (rterms index)
#stuff -- matches stuff in pterms or rterms and returns the correct review numbers (rterms or pterms index)
import re

from ReviewClass import Review

from bsddb3 import db

def askForQuery():
	while True:
		#ask for queries in a loop
		query = input("What is your database query? ($exit to quit): ")
		if query.lower() == '$exit':
			return
		#deal with greaters and lessers
		query = re.sub("\\s+", " ", query)
		query = re.sub("\\s*>\\s*", ">", query)
		query = re.sub("\\s*<\\s*", "<", query)
#		print(query)

		requirements = query.split(" ")
		#run the query
		runQuery(requirements)


def runQuery(requirements):

	pTerms = []
	rTerms = []
	genTerms = []

	rScore = []
	rDate = []
	pPrice = []
	#Create the lists of requirements
	for requirement in requirements:
		if requirement.startswith("pprice"):
			pPrice.append(requirement[6:])
		elif requirement.startswith("rscore"):
			rScore.append(requirement[6:])
		elif requirement.startswith("rdate"):
			rDate.append(requirement[5:])
		elif requirement.startswith("p:"):
			pTerms.append(requirement[2:].lower())
		elif requirement.startswith("r:"):
			rTerms.append(requirement[2:].lower())
		else:
			genTerms.append(requirement.lower())


#Make sure we have at least one indexed column
	if not pTerms and not rTerms and not genTerms and not rScore:
		print("Your query could not be run, please include an indexed requirement.")
		return


	allSets = []
	if genTerms:
		allSets.append(getGenTerms(genTerms))
	if rTerms:
		allSets.append(getIndices("rt.idx", rTerms))
	if pTerms:
		allSets.append(getIndices("pt.idx", pTerms))
	if rScore:
		allSets.append(getScoreIndices(rScore))
#Create the set of reviews which are valid to all terms
	allThings = allSets[0]
	for set in allSets:
		allThings = allThings & set

# TODO PRINT THINGS
	database = db.DB()
	database.open("rw.idx")
	for id in allThings:
		review = Review(database.get(id.encode()).decode())
		if review.validatedate(rDate) and review.validateprice(pPrice):
			print(review)
	database.close()

#Eldritch fucking magic
def getGenTerms(terms):
	indices = set()
	for term in terms:
		list = getIndices("rt.idx", [term]) | getIndices("pt.idx", [term])
		if indices:
			indices = indices & list
		else:
			indices = list
	return indices

def getIndices(dbName, terms):
	database = db.DB()
	database.open(dbName)
	cur = database.cursor()
	
	indices = set()
	for term in terms:
		list = []
		if term[-1] == "%":
			current = cur.get(term.encode(), db.DB_SET)
			while current:
				if current[0].decode().startswith(term):
					list.append(current[1].decode())
				else:
					break
				current = cur.get(term.encode(), db.DB_NEXT)
			if indices:
				indices = indices & set(list)
			else:
				indices = set(list)
		else:
			current = cur.get(term.encode(), db.DB_SET)
			while current:
				if current[0].decode() == term:
					list.append(current[1].decode())
				else:
					break
				current = cur.get(term.encode(), db.DB_NEXT)
			if indices:
				indices = indices & set(list)
			else:
				indices = set(list)

	cur.close()
	database.close()

	return indices

def getScoreIndices(terms):
	indices = set()
	for term in terms:
		list = _getScoreIndices(term)
		if indices:
			indices = indices & list
		else:
			indices = list
	return indices

def _getScoreIndices(term):
	database = db.DB()
	database.open("sc.idx")
	cur = database.cursor()
	
	indices = set()
	if term[0] == ">":
		current = cur.get(b'', db.DB_LAST)
		while current:
			if (float(current[0].decode())) > float(term[1:]):
				indices.add(current[1].decode())
			else:
				break
			current = cur.get(b'', db.DB_PREV)
	else:
		current = cur.get(b'', db.DB_FIRST)
		while current:
			if (float(current[0].decode())) < float(term[1:]):
				indices.add(current[1].decode())
			else:
				break
			current = cur.get(b'', db.DB_NEXT)

	cur.close()
	database.close()
	
	return indices

if __name__ == '__main__':
	askForQuery()