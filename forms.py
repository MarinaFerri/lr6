from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, AnyOf
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField("Ваш логин:", validators=[DataRequired(), Length(max=32)])
    password = PasswordField("Пароль:", validators=[DataRequired(), Length(min=4, max=32)])
    submit = SubmitField("Войти")
    remember = BooleanField("Запомнить", default=False)


class RegisterForm(FlaskForm):
    username = StringField("Придумайте логин:", validators=[DataRequired(), Length(max=32)])
    password = PasswordField("Пароль:", validators=[DataRequired(), Length(min=4, max=32)])
    passwd_confirm = PasswordField("Повторите пароль:", validators=[DataRequired(), Length(min=4, max=32)])
    submit = SubmitField("Зарегистрироваться")
