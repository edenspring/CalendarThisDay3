from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from wtforms.validators import DataRequired, ValidationError 

validators = [DataRequired()]
class AppointmentForm(FlaskForm):
    name = StringField("Name", validators)
    start_date = DateField("Start date", validators)
    start_time = TimeField("Start time", validators)
    end_date = DateField("End date", validators)
    end_time = TimeField("End time", validators)
    description = TextAreaField("Description", validators)
    private = BooleanField("Private?")
    submit = SubmitField("Create an appointment")