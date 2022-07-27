from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, length, EqualTo
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired(), length(min=5, max=35)])
    name = StringField("Name: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired(), length(min=6, max=35),
                                                       EqualTo('confirm_password', message="Passwords must match.")])
    confirm_password = PasswordField("Confirm Password: ", validators=[DataRequired(), length(min=6, max=35)])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email: ", validators=[DataRequired(), length(min=5, max=35)])
    password = PasswordField("Password: ", validators=[DataRequired(), length(min=6, max=35)])
    submit = SubmitField("Log In")

class CommentForm(FlaskForm):
    text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Post Comment")