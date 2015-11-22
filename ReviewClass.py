class Review:
	productID = ""
	productTitle = ""
	productPrice = ""
	userID = ""
	profileName = ""
	helpfulness = ""
	score = 0
	secs = 0
	time = ""
	reviewSummary = ""
	reviewText = ""
	
	def __init__(data):
		data = data.replace("&quot;", "\"")
		data = data.replace("\\\\", "\\")
		data = data.split(",")
		(productID,
		productTitle,
		productPrice,
		userID,
		profileName,
		helpfulness,
		score,
		secs,
		reviewSummary,
		reviewText) = data
		time = datetime.datetime.fromtimestamp(secs)