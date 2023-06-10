from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import SubmitField,PasswordField,StringField,BooleanField,TextAreaField
from wtforms.validators import data_required,Length,Email,EqualTo,ValidationError
from app.model import User
from flask_login import current_user
class RegistrationForm(FlaskForm):
    username=StringField('username',
                         validators=[data_required(),Length(min=2,max=20)])
    email=StringField('email',
                      validators=[data_required(),Email()])
    password=PasswordField('password',
                           validators=[data_required()])
    confirm_password=PasswordField('confirm_password',
                                   validators=[data_required(),EqualTo('password')])
    submit=SubmitField('Sign Up')
    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError ('Username is already taken,please choose another name')
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError ('email is already taken,please choose another email')
               
class LoginForm(FlaskForm):

    email=StringField('email',
                      validators=[data_required(),Email()])
    password=PasswordField('password',
                           validators=[data_required()])
    remember=BooleanField('Remember me')
    
    submit=SubmitField('Login')
class UpdationForm(FlaskForm):
    username=StringField('username',
                         validators=[data_required(),Length(min=2,max=20)])
    email=StringField('email',
                      validators=[data_required(),Email()])
    picture=FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])
    submit=SubmitField('Update')
    def validate_username(self,username):
        if username.data != current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError ('Username is already taken,please choose another name')
    def validate_email(self,email):
        if email.data != current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError ('Email  is already taken,please choose another name')
class PostForm(FlaskForm):
    title=StringField('Title',validators=[data_required()])
    content=TextAreaField('Content',validators=[data_required()])
    submit=SubmitField('Post')
    
    
                