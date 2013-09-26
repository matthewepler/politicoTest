import models

def initEverything():
	#clear database - will not work for more than one user
	models.Question.objects.delete()
	models.Category.objects.delete()
	models.Candidate.objects.delete()

	#create default categories the long way
	titles = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	for t in titles:
		newCat = models.Category()
		newCat.title = t
		newCat.save()

#create default Questions the long way
	q1 = models.Question()
	q1.text = "Should you add a new stadium?"
	q1.category = "Tax"
	q1.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q1.yesValues = [ 2, -2, -2, -3, -2, 3 ]
	q1.noValues =  [ 0, 2, -3, 3, 2, 0]
	q1.yesResponse = "You just created 2,000 jobs! Also, expect some good return on tourism when you open the stadium. Of course, you might want to invest in some infrastructure for all that new traffic. Oh, and some folks are angry with the higher taxes you'll be enforcing to pay for this."
	q1.noResponse = "Probably smart to save that money. You might lose out on some tourism and added seasonal income, but now you can focus on your aging infrastructure and maybe do something nice for the kids in school!"
	q1.save()

	q2 = models.Question()
	q2.text = "The roads need fixing. Should you do it this year?"
	q2.category = "Tax"
	q2.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q2.yesValues = [ 2, 0, 0, 0, -1, 1 ]
	q2.noValues =  [ 0, 0, 0, 0, 0, -1]
	q2.yesResponse = "Good idea. You created 1,000 new jobs. Bit of a tax hike, though. Maybe you could justify it by allocating some of it for something else?"
	q2.noResponse = "It can wait. Those tour buses can take a few bumps, right?"
	q2.save()

	q3 = models.Question()
	q3.text = "Big business is pressuring you to lower taxes. Should you listen to them?"
	q3.category = "Tax"
	q3.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q3.yesValues = [ -2, -1, -1, -2, 1, 1 ]
	q3.noValues =  [ -1, 0, -1, -1, 0, 1 ]
	q3.yesResponse = "Good idea. You created 1,000 new jobs. Bit of a tax hike, though. Maybe you could justify it by allocating some of it for something else?"
	q3.noResponse = "They are your biggest campaign contributors. You can do more in the long run, even though this will make some people angry in the short run."
	q3.save()

	q4 = models.Question()
	q4.text = "Start a new charter school program?"
	q4.category = "Education"
	q4.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q4.yesValues = [ -2, 3, 0, 2, 3, 0 ]
	q4.noValues =  [ 0, -2, 0, 0, 0, 0 ]
	q4.yesResponse = "Good idea. Jobs for teachers and staff while saving taxes. They can also sponser community programs."
	q4.noResponse = "You have your reasons. But the public school system isn't making any progress on standardized tests."
	q4.save()

	q5 = models.Question()
	q5.text = "Reward teachers based on standardized testing?"
	q5.category = "Education"
	q5.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q5.yesValues = [ 0, -3, 0, -2, 0, 0 ]
	q5.noValues =  [ 0, 1, 0, 2, 0, 0 ]
	q5.yesResponse = "Oops, that backfired. Turns out they don't do so well as a whole. Teachers are frustrated and leaving. Let's hope tourist season is good, maybe some of them will want to stay."
	q5.noResponse = "Testing testers isn't the answer. Maybe funding more community programs when you have the chance will increase motivation for families to help their kids in school."
	q5.save()

	q6 = models.Question()
	q6.text = "Sponsor an after school program for kids with single parents?"
	q6.category = "Education"
	q6.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q6.yesValues = [ -1, 1, -1, -2, -1, 0 ]
	q6.noValues =  [ 1, 0, 1, 0, -1, 1, 0 ]
	q6.yesResponse = "Good news! The government has a funding program that will keep you from raising taxes. Smart move."
	q6.noResponse = "You could have created a few jobs, but at least you're saving the money for something else."
	q6.save()

	q7 = models.Question()
	q7.text = "The river is on the edge of being declared a superfund site. Pay to clean it up?"
	q7.category = "Public Health"
	q7.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q7.yesValues = [ 2, 0, 3, 0, 0, 0 ]
	q7.noValues =  [ -1, 0, -2, 0, 0, 0 ]
	q7.yesResponse = "Here's to public health! It's expensive, but at least a few jobs will be available. Might lose some of your infrastructure resources to cut costs, though."
	q7.noResponse = "Tell them you're applying for federal funds. It'll hold them off. It's not a superfund site yet..."
	q7.save()

	q8 = models.Question()
	q8.text = "Sponsor a city-wide marathon and an excercise campaign?"
	q8.category = "Public Health"
	q8.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q8.yesValues = [ 1, 1, 2, 0, 0, 2 ]
	q8.noValues =  [ -1, 0, 0, 0, 0, 0 ]
	q8.yesResponse = "It all goes swimmingly. That slight tax bump was offset by tourism money!"
	q8.noResponse = "Why strain a city that's already strained? Kids will learn to love apples...right?"
	q8.save()

	q9 = models.Question()
	q9.text = "Start a recycling program?"
	q9.category = "Public Health"
	q9.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q9.yesValues = [ 2, 0, 2, 0, -2, 0 ]
	q9.noValues =  [ -1, 0, -1, 0, 0, 0 ]
	q9.yesResponse = "People are willing to pay for a cleaner city. And more jobs! Let's hope Big Business doesn't start hollering about the tax hike."
	q9.noResponse = "You can use what you save with this decision on more pressing issues. But that landfill ain't getting any smaller, and it's right next to the river..."
	q9.save()

	q10 = models.Question()
	q10.text = "Start a Maker Faire?"
	q10.category = "Community Arts"
	q10.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q10.yesValues = [ 1, -2, 0, 2, 0, 1 ]
	q10.noValues =  [ 0, 0, 0, 0, 0, -1 ]
	q10.yesResponse = "Great idea! You can bundle your community art funding here and invite all the organizations to participate! Might put a strain on your transit infrastructure, though."
	q10.noResponse = "Meh. Who needs a bunch of 3D printers and flame-throwing robots? You've got bigger things on your mind."
	q10.save()

	q11 = models.Question()
	q11.text = "Build a state-of-the-art community arts center downtown?"
	q11.category = "Community Arts"
	q11.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q11.yesValues = [ 1, 0, 0, 2, -2, -1 ]
	q11.noValues =  [ 0, 0, 0, -1, -1, 0 ]
	q11.yesResponse = "A good move, but you'll have to improve your bus lines if you want everyone to have access. You get a few jobs out of this deal and the Nutcracker brings in folks from 5 counties!"
	q11.noResponse = "Probably best to focus on the neighborhood programs. Last thing you need is a strained transit system."
	q11.save()

	q12 = models.Question()
	q12.text = "Sponsor after-school program for aspiring entrepreneurs?"
	q12.category = "Community Arts"
	q12.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q12.yesValues = [ 1, 0, 0, 3, 0, 0 ]
	q12.noValues =  [ 0, 0, 0, -1, 1, 0 ]
	q12.yesResponse = "Could lead to good things. Worth the investment and you're getting great press."
	q12.noResponse = "It isn't proven to help in the long run. You need something more engaging for everyone, not just kids. Maybe a big event...like a Maker Faire... "
	q12.save()

	q13 = models.Question()
	q13.text = "The Unions say the river cleanup will make the ports less accessible and are threatening to strike. Do you put off the cleanup?"
	q13.category = "Unemployment"
	q13.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q13.yesValues = [ 0, 0, -2, 0, 0, -2 ]
	q13.noValues  = [ 0, 0, 2, 0, 0, 1 ]
	q13.yesResponse = "Dang. This is a loose-loose. You need that port and jobs are important in this economy. The river will have to wait. Let's hope it doesn't reach superfund status"
	q13.noResponse = "Public Health is important. You're taking care of tens-of-thousands in the long-run while angering just a few thousand in the short term. You can't please everyone. You might have to create some jobs to appease the Unions, though."
	q13.save()

	q14 = models.Question()
	q14.text = "Should you privatize the city's energy?"
	q14.category = "Unemployment"
	q14.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q14.yesValues = [ 1, 0, -1, 0, -2, 1 ]
	q14.noValues =  [ -2, 0, -1, 0, -1, 0 ]
	q14.yesResponse = "You're a tough negotiator and it pays off. You get more jobs, an updated infrastructure, and they're building a large park to offset their environmental impact. Let's hope you didn't put them too close to the river..."
	q14.noResponse = "Probably a safe bet. But your infrastructure hasn't been maintained well and your main subway line just went down. Looks like taxes will have to go up again."
	q14.save()

	q15 = models.Question()
	q15.text = "Should you open a high-security prison on the edge of town?"
	q15.category = "Unemployment"
	q15.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q15.yesValues = [ -1, 0, 0, 0, -2, -2 ]
	q15.noValues =  [ 0, 0, 0, 0, 2, 0 ]
	q15.yesResponse = "You just created thousands of jobs! The road repairs will have to wait and tourism will drop off, but hopefully the profit from the prison with help from federal funds should cover that...eventually."
	q15.noResponse = "You're right. You can find better jobs without risking tourism and diverting funds from your aging infrastructure."
	q15.save()

	q16 = models.Question()
	q16.text = "Make a bid to be the host city for 2018 Super Bowl?"
	q16.category = "Tourism"
	q16.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q16.yesValues = [ 1, 0, 0, 0, -2, 3 ]
	q16.noValues  = [ 0, 0, 0, 0, 0, 0 ]
	q16.yesResponse = "You can't buy publicity like this...only you did because you had to spend some money shining up your public sites for the review committee. Let's hope you get it."
	q16.noResponse = "Risk nothing, gain nothing. In politics, that isn't a bad thing."
	q16.save()

	q17 = models.Question()
	q17.text = "Build a Convention Center?"
	q17.category = "Tourism"
	q17.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q17.yesValues = [ 1, 0, 0, 0, -1, 2 ]
	q17.noValues  = [ 0, 0, 0, 0, 0, 0 ]
	q17.yesResponse = "Makes sense. More jobs, tourism, and a better infrastructure. Worth the tax hike."
	q17.noResponse = "OK. Maybe build invest somewhere else?"
	q17.save()

	q18 = models.Question()
	q18.text = "Build a modern art museum?"
	q18.category = "Tourism"
	q18.relations = [ "Tax", "Education", "Public Health", "Community Arts", "Unemployment", "Tourism"]
	q18.yesValues = [ 0, 0, 0, 0, 0, 2 ]
	q18.noValues  = [ 0, 0, 0, 0, 0, 0 ]
	q18.yesResponse = "Temporary jobs and a slight bump in tourism is never a bad thing. Doesn't seem like the locals care as much about art as they do that river cleanup, though."
	q18.noResponse = "Could have livened things up, but you have more presseing issues that need attending to."
	q18.save()
