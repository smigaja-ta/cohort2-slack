from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///cohort.db")

app = Flask(__name__)

Base = automap_base()
Base.prepare(engine, reflect=True)

Students = Base.classes.students
session = Session(engine)


@app.route('/')
def welcome():
    return(
    '''
    Welcome to the T/TH Cohort Slack API!
    Available Routes:
    ''')

