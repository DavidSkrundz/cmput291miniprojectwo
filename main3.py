import os

from bsddb3 import db

if __name__ == "__main__":
	try:
		os.remove("rw.idx")
	except:
		pass
	try:
		os.remove("pt.idx")
	except:
		pass
	try:
		os.remove("rt.idx")
	except:
		pass
	try:
		os.remove("sc.idx")
	except:
		pass
	
	
	with open("sorted_reviews.txt", "r") as reviewsFile:
		rw = db.DB()
		rw.open("rw.idx", None, db.DB_HASH, db.DB_CREATE)
		for line in reviewsFile:
			line = line.split("\n")[0]
			parts = line.split(",", 1)
			index = parts[0]
			data = parts[1]
			rw.put(index.encode(), data.encode())
		rw.close()

	with open("sorted_pterms.txt", "r") as ptermFile:
		rw = db.DB()
		rw.set_flags(db.DB_DUP)
		rw.open("pt.idx", None, db.DB_BTREE, db.DB_CREATE)
		for line in ptermFile:
			line = line.split("\n")[0]
			parts = line.split(",", 1)
			index = parts[0]
			data = parts[1]
			rw.put(index.encode(), data.encode())
		rw.close()

	with open("sorted_rterms.txt", "r") as rtermFile:
		rw = db.DB()
		rw.set_flags(db.DB_DUP)
		rw.open("rt.idx", None, db.DB_BTREE, db.DB_CREATE)
		for line in rtermFile:
			line = line.split("\n")[0]
			parts = line.split(",", 1)
			index = parts[0]
			data = parts[1]
			rw.put(index.encode(), data.encode())
		rw.close()

	with open("sorted_scores.txt", "r") as scoresFile:
		rw = db.DB()
		rw.set_flags(db.DB_DUP)
		rw.open("sc.idx", None, db.DB_BTREE, db.DB_CREATE)
		for line in scoresFile:
			line = line.split("\n")[0]
			parts = line.split(",", 1)
			index = parts[0]
			data = parts[1]
			rw.put(index.encode(), data.encode())
		rw.close()