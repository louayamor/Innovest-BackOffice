# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Business(models.Model):
    owner = models.ForeignKey('User', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    description = models.TextField()
    revenue = models.DecimalField(max_digits=10, decimal_places=0)
    profit = models.DecimalField(max_digits=10, decimal_places=0)
    sector = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(db_comment='(DC2Type:datetime_immutable)')
    image_blob = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'business'


class Conversation(models.Model):
    sender = models.OneToOneField('User', models.DO_NOTHING)
    reciever = models.OneToOneField('User', models.DO_NOTHING, related_name='conversation_reciever_set', blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(db_comment='(DC2Type:datetime_immutable)')

    class Meta:
        managed = False
        db_table = 'conversation'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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
    id = models.BigAutoField(primary_key=True)
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

class Investment(models.Model):
    investor = models.ForeignKey('User', models.DO_NOTHING)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    comment = models.TextField()
    created_at = models.DateTimeField(db_comment='(DC2Type:datetime_immutable)')

    class Meta:
        managed = False
        db_table = 'investment'


class MessengerMessages(models.Model):
    id = models.BigAutoField(primary_key=True)
    body = models.TextField()
    headers = models.TextField()
    queue_name = models.CharField(max_length=190)
    created_at = models.DateTimeField(db_comment='(DC2Type:datetime_immutable)')
    available_at = models.DateTimeField(db_comment='(DC2Type:datetime_immutable)')
    delivered_at = models.DateTimeField(blank=True, null=True, db_comment='(DC2Type:datetime_immutable)')

    class Meta:
        managed = False
        db_table = 'messenger_messages'


class Sector(models.Model):
    sector_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sector'


class User(models.Model):
    email = models.CharField(unique=True, max_length=180)
    roles = models.JSONField(db_comment='(DC2Type:json)')
    password = models.CharField(max_length=255)
    is_active = models.IntegerField()
    username = models.CharField(max_length=255)
    is_verified = models.IntegerField()
    created_at = models.DateTimeField(db_comment='(DC2Type:datetime_immutable)')
    is_investor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class UserProfile(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profile'
