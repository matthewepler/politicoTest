def initMetrics():
	# set default categories
	categories = ["Reputation", "Pole_Position", "Cash", "Media"]
	for i in categories:
		newCat = models.Category()
		newCat.title = i
		newCat.minValue = 0
		newCat.maxValue = 10
		newCat.save()
		app.logger.debug( newCat.title + ' created')