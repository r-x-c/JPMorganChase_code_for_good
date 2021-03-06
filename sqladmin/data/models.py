from __future__ import unicode_literals

from django.db import models


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class AnswerT(models.Model):
    answer_id = models.AutoField(primary_key=True)
    question = models.ForeignKey('QuestionT', models.DO_NOTHING, blank=True, null=True)
    answer = models.CharField(max_length=64, blank=True, null=True)
    gpa_effect = models.FloatField(blank=True, null=True)
    discipline_effect = models.FloatField(blank=True, null=True)
    balance_effect = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer_t'

    def __str__(self):  # __unicode__ on Python 2
        return ("Question_ID: {} Answer: {} Effects: [GPA {}] [Balance {}] [Discipline {}]".format(self.question,
                                                                                                   self.answer,
                                                                                                   self.gpa_effect,
                                                                                                   self.balance_effect,
                                                                                                   self.discipline_effect))


class AnsweredQuestionsT(models.Model):
    user = models.ForeignKey('UserT', models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey('QuestionT', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answered_questions_t'



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HeroT(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    hero_id = models.AutoField(primary_key=True)
    race = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hero_t'

    def __str__(self):  # __unicode__ on Python 2
        return ("{}, {}".format(self.name, self.age))



class QuestionT(models.Model):
    question_id = models.AutoField(primary_key=True)
    q_text = models.CharField(max_length=256, blank=True, null=True)
    hero = models.ForeignKey(HeroT, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_t'

    def __str__(self):  # __unicode__ on Python 2
        return ("Hero {} asks {}".format(self.hero, self.q_text))



class UserT(models.Model):
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    race = models.CharField(max_length=32, blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)
    discipline = models.FloatField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    user_id = models.AutoField(primary_key=True)
    hero = models.ForeignKey(HeroT, models.DO_NOTHING)
    location = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_t'

    def __str__(self):  # __unicode__ on Python 2
        return ("Age {} {} from {} [GPA {} Discipline {} Balance {}]".format(self.age, self.gender, self.location,
                                                                             self.gpa, self.discipline, self.balance))

