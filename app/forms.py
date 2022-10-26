from flask_wtf import FlaskForm
from wtforms import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime, timedelta 

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

    def validate_end_date(form, field):
        start = datetime.combine(form.start_date.data, form.start_time.data)
        end = datetime.combine(field.data, form.end_time.data)
        if start >= end:
            msg = "End date/time must come after start date/time"
            raise ValidationError(msg)
        if form.start_date.data != form.end_date.data:
            msg = "End date must be the same as start date"
            raise ValidationError(msg)
