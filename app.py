# -*- coding: utf-8 -*-
import os, datetime
import re
from unidecode import unidecode


from flask import Flask, request, render_template, redirect, abort

# import all of mongoengine
from mongoengine import *

# import data models
import models
import functions
import random

# for json needs
import json
from flask import jsonify

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
	return render_template("start.html")


@app.route("/question/<response>", methods=['GET','POST'])
def question(response):
	data = {'response':response}
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
		app.logger.debug( newQ.text )
		return redirect( '/admin' )
	else:
		q_form = models.QuestionForm(request.form)
		data = { 
				'list': categories,
				'form': q_form 
				}
	return render_template('add.html', **data)

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



	