class Review:
	productID = ""
	productTitle = ""
	productPrice = ""
	userID = ""
	profileName = ""
	helpfulness = ""
	score = 0
	time = 0
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
		time,
		reviewSummary,
		reviewText) = data