from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PredictForm(FlaskForm):
    stockTicker = SelectField('Stock Ticker', choices=[("Snap", "Snapchat"), ("TWTR", "Twitter"), ("VZ", "Verizon"), ("DB", "Deutsche Bank"), ("XOM", "Exxon Mobil")])
    daysToPredict = SelectField('Days', choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")])
    submit = SubmitField("Submit")