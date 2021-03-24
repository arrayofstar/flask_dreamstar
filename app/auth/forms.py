from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):     #登陆表单
    email = StringField('账号（邮箱）', validators=[DataRequired(), Length(1, 64),
                                             Email()])     #这里要求了数据的提交格式必须是邮箱
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('保持我的登陆状态')
    submit = SubmitField('登陆')


class RegistrationForm(FlaskForm):      #注册表单
    email = StringField('Email（电子邮箱）', validators=[DataRequired(), Length(1, 64),Email()])
    username = StringField('Username（用户名）', validators=[
        DataRequired(), Length(1, 64)])
        # ，Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
        #        '用户名必须以字母为开头并且只包含字母、数字、下划线和点号')])
    password = PasswordField('Password（密码）', validators=[
        DataRequired(), EqualTo('password2', message='密码必须和前面一致')])
    password2 = PasswordField('Confirm password（再次确认密码）', validators=[DataRequired()])
    submit = SubmitField('Register（完成注册）')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('邮箱已经被注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经被使用')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password（旧密码）', validators=[DataRequired()])
    password = PasswordField('New password（新密码）', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm new password（确认新密码）',
                              validators=[DataRequired()])
    submit = SubmitField('Update Password（确认修改密码）')

class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password（重置密码）')

class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password（重置密码）')
