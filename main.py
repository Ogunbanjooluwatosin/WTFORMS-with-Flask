from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(max=8)])
    submit = SubmitField('Log In')


app = Flask(__name__)
app.secret_key = 'ogunbanjotosin'
bootstrap = Bootstrap5(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['Get', 'Post'])
def login():
    form_login = LoginForm()
    if form_login.validate_on_submit():
        if form_login.email.data == 'admin@gmail.com' and form_login.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form_login)


if __name__ == "__main__":
    app.run(debug=True)
