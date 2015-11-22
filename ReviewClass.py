import datetime

class Review:
	def __init__(self, data):
		data = data.replace("&quot;", "\"")
		data = data.replace("\\\\", "\\")
		data = data.split(",")
		for i in range(0, len(data)):
			data[i] = data[i].replace("&com;", ",")
		(self.productID,
		self.productTitle,
		self.productPrice,
		self.userID,
		self.profileName,
		self.helpfulness,
		self.score,
		self.secs,
		self.reviewSummary,
		self.reviewText) = data
		self.time = datetime.datetime.fromtimestamp(int(self.secs))
	def __str__(self):
		return \
"""Product ID: {}
Title: {}
Price: {}
User ID: {}
Profile Name: {}
Helpfulness: {}
Score: {}
Date Reviewed: {}
Summary: {}
Review: {}
	""".format(self.productID,
			   self.productTitle,
			   self.productPrice,
			   self.userID,
			   self.profileName,
			   self.helpfulness,
			   self.score,
			   self.time,
			   self.reviewSummary,
			   self.reviewText)
	def validatedate(self, dates):
		for date in dates:
			if date[0] == ">":
				vals = date[1:].split("/")
				dt = datetime.datetime(int(vals[0]), int(vals[1]), int(vals[2]))
				if not self.time > dt:
					return False
			else:
				vals = date[1:].split("/")
				dt = datetime.datetime(int(vals[0]), int(vals[1]), int(vals[2]))
				if not self.time < dt:
					return False
		return True
	def validateprice(self, prices):
		try:
			float(self.productPrice)
		except:
			return True
		for price in prices:
			if price[0] == "<":
				if float(price[1:]) <= float(self.productPrice):
					return False
			else:
				if float(price[1:]) >= float(self.productPrice):
					return False
		return True