from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('你的名字是什么?', validators=[DataRequired()])
    submit = SubmitField('提交')

class EditProfileForm(FlaskForm):   #普通用户权限
    name = StringField('真实姓名', validators=[Length(0, 64)])
    location = StringField('地点', validators=[Length(0, 64)])
    about_me = TextAreaField('简介')
    submit = SubmitField('提交')


class EditProfileAdminForm(FlaskForm):      #管理员权限
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('用户名', validators=[
        DataRequired(), Length(1, 64),
    ])
    #这里的注释是为了让用户名可以为中文
        # Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
        #        'Usernames must have only letters, numbers, dots or '
        #        'underscores')])
    confirmed = BooleanField('确认')
    role = SelectField('Role', coerce=int)
    name = StringField('真实姓名', validators=[Length(0, 64)])
    location = StringField('地点', validators=[Length(0, 64)])
    about_me = TextAreaField('简介')
    submit = SubmitField('提交')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PostForm(FlaskForm):
    body = TextAreaField("你要提交的文字？", validators=[DataRequired()])
    submit = SubmitField('提交')