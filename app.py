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

defaultCategories = ["Reputation", "Pole_Position", "Cash", "Media"]

# --------- Routes -----------------------------------------------------------------
@app.route("/", methods=['GET'])
def index():
	form = models.CandidateForm(request.form)
	data = {'form' : form}
	return render_template("start.html", **data)


@app.route("/phaseone", methods=['POST'])
def phase_one():
	newCan = models.Candidate()
	newCan.name = request.form.get('name')
	newCan.slogan = request.form.get('slogan')

	# set default categories
	for i in defaultCategories:
		newCat = models.Category()
		newCat.title = i
		newCat.minValue = 0
		newCat.maxValue = 10
		newCan.metrics.append( newCat )

	newCan.save()
	app.logger.debug( newCan.name + ' campaign created.')
	app.logger.debug( defaultCategories )

	return render_template("phaseone.html")


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



	