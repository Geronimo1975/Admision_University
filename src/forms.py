from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AdmissionForm(FlaskForm):
    name = StringField("Nume", validators=[DataRequired()])
    country = SelectField("Țară preferată", choices=[
        ("germania", "Germania"), ("franta", "Franța"), ("uk", "Marea Britanie"),
        ("italia", "Italia"), ("spania", "Spania")
    ], validators=[DataRequired()])
    budget = IntegerField("Buget (€)", validators=[DataRequired()])
    exams = StringField("Examene pregătite (ex: BMAT, UCAT, IMAT)")
    submit = SubmitField("Obține Recomandarea")
