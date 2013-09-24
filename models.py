# -*- coding: utf-8 -*-
from mongoengine import *

from flask.ext.mongoengine.wtf import model_form
from datetime import datetime


class Category(EmbeddedDocument):
	title = StringField(max_length=120, required=True)
	minValue = IntField(required=True)
	maxValue = IntField(required=True)
	currValue = DecimalField(force_string=True, precision=1)

# validation form
CategoryForm = model_form(Category)

class Candidate(Document):
	# basic info
	name = StringField(max_length=120, required=True)
	slug = StringField()
	tagline = StringField(required=True, verbose_name="What is your tagline?")
	photo = StringField()
	metrics = ListField(EmbeddedDocumentField(Category))
	timestamp = DateTimeField(default=datetime.now())

# validation form
CandidateForm = model_form(Candidate)