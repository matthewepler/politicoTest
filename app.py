# -*- coding: utf-8 -*-
import os, datetime
import re
from unidecode import unidecode


from flask import Flask, request, render_template, redirect, abort

# import all of mongoengine
from mongoengine import *

# import data models
import models
from otherFunctions import *
import random

# # for json needs
# import json
# from flask import jsonify

import requests

app = Flask(__name__)  
app.config['CSRF_ENABLED'] = False
app.secret_key = os.environ.get('SECRET_KEY')

# --------- Database Connection ----------------------------------------------------
# MongoDB connection to MongoLab's database
connect('mydata', host=os.environ.get('MONGOLAB_URI'))
app.logger.debug("Connecting to MongoLabs")


# --------- Routes -----------------------------------------------------------------
@app.route("/", methods=['GET'])
def index():
	initEverything()
	app.logger.debug( "database cleared and refilled")

	#create new mayor
	models.Candidate.objects.delete()
	newCan = models.Candidate()
	newCan.name = "Mayor"
	categories = models.Category.objects()
	for c in categories:
		ranNum = random.randint(2,5)
		newCan.currScores[c.title] = ranNum
	newCan.save()
	metrics = {}
	metrics = sorted(newCan.currScores, key=lambda key: newCan.currScores[key])
	questions = models.Question.objects(category=metrics[0])
	ranNum = random.randint(0, len(questions))
	question = questions[ranNum]
	
	data = {
			'currScores' : newCan.currScores,
			'question'   : question
			}

	return render_template("start.html", **data)


@app.route("/question/<response>/<qText>", methods=['GET','POST'])
def question(response, qText):
	qText = qText + "?"
	if response == '0':
		#reset everything
		mayor = models.Candidate.objects.get()
		categories = models.Category.objects()

		#evaluate the current scores
		metrics = {}
		metrics = sorted(mayor.currScores, key=lambda key: mayor.currScores[key])

		#pick a question from the category with the lowest score
		questions = models.Question.objects(category=metrics[0])
		ranNum = random.randint(0, len(questions))
		question = questions[ranNum]

		data = {
				'currScores' : mayor.currScores,
				'question'   : question
				}

		return render_template("question.html", **data)

	elif response == '1': #Yes
		mayor = models.Candidate.objects.get()
		app.logger.debug( qText )
		prevQuestion = models.Question.objects.get(text=qText)

		# save the currScores into prevScores before altering them
		mayor.prevScores = mayor.currScores

		# qet the yesValues for the previous question
		prevQYesValues = prevQuestion.yesValues

		# add them to the currScores 
		counter = 0
		for i in mayor.currScores.keys():
			pScore = mayor.currScores[i]
			app.logger.debug( pScore )
			nScore = prevQYesValues[counter]
			app.logger.debug( nScore )
			adjScore = pScore + nScore
			app.logger.debug( adjScore )
			mayor.currScores[i] = adjScore
			app.logger.debug( mayor.currScores[i] )
			counter = counter + 1

		# prevMetrics = sorted(prevMetrics, key=lambda key: prevMetrics[key])
		# questions = models.Question.objects(category=prevMetrics[0])
		# if len(questions) > 1:
		# 	ranNum = random.randint(0, len(questions))
		# 	question = questions[ranNum]
		# 	models.Question.objects.get(text=question.text).delete()
		# else:
		# 	question = questions[0]

		data = {
				'currScores' : mayor.currScores,
				'question'   : question
				}
		render_template("question.html", **data)

	elif response == '2': #No
		data = {}

	return render_template("question.html", **data)

@app.route("/admin", methods=['GET', 'POST'])
def admin():
	questions = models.Question.objects().order_by('+category')
	if questions:
		data = {'list':questions}
	return render_template('admin.html', **data)

@app.route("/add", methods=['GET', 'POST'])
def updateAdmin():
	categories = models.Category.objects()
	if request.method == "POST":
		newQ = models.Question()
		newQ.category = request.form.get('category-list')
		newQ.text = request.form.get('text')
		for c in categories:
			newQ.relations.append(c.title)
			yesValueName = c.title + "-yes"
			noValueName = c.title + "-no"
			newQ.yesValues.append(request.form.get(yesValueName))
			newQ.noValues.append(request.form.get(noValueName))
		newQ.yesResponse = request.form.get("yResponse")
		newQ.noResponse = request.form.get("nResponse")
		newQ.save()
		return redirect( '/admin' )
	else:
		q_form = models.QuestionForm(request.form)
		data = { 
				'list': categories,
				'form': q_form 
				}
	return render_template('add.html', **data)

@app.route("/edit/<question>", methods=['GET', 'POST'])
def edit(question):
	categories = models.Category.objects()
	question = question + "?"
	editQ = models.Question.objects.get(text=question)
	app.logger.debug( editQ.yesResponse )
	if editQ and request.method == "GET":
		data ={
				"editQ": editQ,
				"list" : categories
				}
		return render_template("edit.html", **data)
	else:
		editQ.category = request.form.get('category-list')
		editQ.text = request.form.get('text')
		for c in categories:
			editQ.relations.append(c.title)
			yesValueName = c.title + "-yes"
			noValueName = c.title + "-no"
			editQ.yesValues.append(request.form.get(yesValueName))
			editQ.noValues.append(request.form.get(noValueName))
		editQ.yesResponse = request.form.get("yResponse")
		editQ.noResponse = request.form.get("nResponse")
		editQ.save()
		return redirect("/admin")

# --------- Helper Functions -------------------------------------------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# slugify the title 
# via http://flask.pocoo.org/snippets/5/
_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')
def slugify(text, delim=u'-'):
	"""Generates an ASCII-only slug."""
	result = []
	for word in _punct_re.split(text.lower()):
		result.extend(unidecode(word).split())
	return unicode(delim.join(result))

# --------- Server On ---------------------------------------------------------------
# start the webserver
if __name__ == "__main__":
	app.debug = True
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	