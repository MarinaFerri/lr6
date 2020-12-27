from flask import Flask, request, render_template, url_for, flash, redirect
from forms import LoginForm, RegisterForm
from jinja2 import Template, Environment, FileSystemLoader
app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
@app.route('/index')
def index():
	return render_template('articles.html', Articles = {
	"Надежно": "В World работают профессионалы с многолетним опытом, которым вы можете доверить свой долгожданный отдых. Наши специалисты подберут тур с учетом всех ваших пожеланий, оформят документы и порекомендуют, чем заняться в стране отдыха.",
	"Выгодно": "Среди предложений World множество акций, которые помогут сделать ваш отдых наиболее выгодным. Это и сезонные акции, например, «Раннее бронирование», «Бархатный сезон», и специальные предложения от отелей-партнеров.",
    "Отдых для всех": "Семьи с детьми всех возрастов, туристы старшего поколения, молодежные компании, влюбленные пары и одиночные путешественники – для всех категорий мы предложим качественный и интересный отдых.",
    "Большой выбор": "World предлагает туры на любой вкус: пляжные, экскурсионные, комбинированные, горнолыжные, корпоративные, элитные. Также в ассортименте представлены перелеты рейсами ведущих авиакомпаний мира."
})

@app.route('/sign_in', methods=['GET', 'POST'])
def login_form():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "user" and form.password.data == "password":
            flash("Вы успешно авторизованы")
            return redirect(url_for('index'))
        else:
            flash("Неверный логин или пароль")

    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register_form():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data == form.passwd_confirm.data:
            flash("Вы успешно зарегистрированы")
            return redirect(url_for('index'))
        else:
            flash("Пароли не совпадают")

    return render_template('register.html', title='Регистрация', form=form)

app.run(debug=True)
