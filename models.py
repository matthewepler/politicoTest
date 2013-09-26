# -*- coding: utf-8 -*-
from mongoengine import *

from flask.ext.mongoengine.wtf import model_form
from datetime import datetime
import logging

class Question(Document):
	text = StringField(required=True)
	category = StringField(required=True)
	relations = ListField(StringField())
	yesValues = ListField(IntField())
	noValues = ListField(IntField())
	yesResponse = StringField()
	noResponse = StringField()

QuestionForm = model_form(Question)


class Category(Document):
	title = StringField(max_length=120, required=True)
	currValue = DecimalField(force_string=True, precision=1)

CategoryForm = model_form(Category)


class Candidate(Document):
	name = StringField()
	categories = ListField(StringField())
	prevScores = DictField()
	currScores = DictField()
	timestamp = DateTimeField(default=datetime.now())

# validation form
CandidateForm = model_form(Candidate)
