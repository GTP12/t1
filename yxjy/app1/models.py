# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account1(models.Model):
    gamearea = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    profession = models.CharField(max_length=10, blank=True, null=True)
    punish_record = models.CharField(max_length=20, blank=True, null=True)
    qq_grade = models.CharField(max_length=20, blank=True, null=True)
    qq_friends = models.CharField(max_length=20, blank=True, null=True)
    safety_grade = models.CharField(max_length=10, blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    account_describe = models.CharField(max_length=200, blank=True, null=True)
    account_number = models.BigIntegerField(blank=True, null=True)
    account_photo = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)
    gameareaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account1'


class Account2(models.Model):
    gamearea = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=5, blank=True, null=True)
    profession = models.CharField(max_length=20, blank=True, null=True)
    punish_record = models.CharField(max_length=20, blank=True, null=True)
    qq_grade = models.CharField(max_length=10, blank=True, null=True)
    qq_friends = models.CharField(max_length=10, blank=True, null=True)
    account_message = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    publish_time = models.DateTimeField(blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    gameareaid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account2'


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
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
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


class Credit(models.Model):
    credit = models.IntegerField()
    finishorder = models.IntegerField()
    cancelorder = models.IntegerField()
    okpercent = models.FloatField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'credit'


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


class Gold(models.Model):
    dealtype = models.CharField(max_length=10)
    delivery = models.CharField(max_length=50)
    goodinfo = models.CharField(max_length=255)
    gamearea = models.CharField(max_length=100)
    gameareaid = models.IntegerField()
    goodsnum = models.IntegerField()
    unitprice = models.FloatField()
    price = models.FloatField()
    datetime = models.DateTimeField(blank=True, null=True)
    productid = models.BigIntegerField()
    image = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gold'
        unique_together = (('id', 'dealtype'),)


class Goldorder(models.Model):
    num = models.IntegerField()
    reaparea = models.CharField(max_length=50)
    trading = models.CharField(max_length=20)
    tel = models.BigIntegerField()
    qq = models.IntegerField()
    payprice = models.FloatField()
    gold = models.ForeignKey(Gold, models.DO_NOTHING)
    ordernumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'goldorder'


class Goldorder1(models.Model):
    gold = models.ForeignKey(Gold, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    order_time = models.DateTimeField(blank=True, null=True)
    order_state = models.IntegerField()
    total_price = models.FloatField()
    order_num = models.IntegerField()
    order_tpye = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'goldorder1'


class Goldorder2(models.Model):
    gold = models.ForeignKey(Gold, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    order_time = models.DateTimeField(blank=True, null=True)
    order_state = models.IntegerField()
    total_price = models.FloatField()
    order_num = models.BigIntegerField()
    order_tpye = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'goldorder2'


class Goldtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    gameareaid = models.IntegerField()
    areaname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'goldtypes'


class Materials(models.Model):
    dealtype = models.CharField(max_length=20)
    delivery = models.CharField(max_length=50)
    meaterialsname = models.CharField(max_length=50)
    meaterialsid = models.IntegerField()
    goodinfo = models.CharField(max_length=255)
    gamearea = models.CharField(max_length=100)
    gameareaid = models.IntegerField()
    goodsnum = models.IntegerField()
    price = models.FloatField()
    datetime = models.DateTimeField(blank=True, null=True)
    productid = models.BigIntegerField()
    image = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'materials'


class Materialsorder(models.Model):
    num = models.IntegerField()
    reaparea = models.CharField(max_length=50)
    rolename = models.CharField(max_length=20)
    tel = models.BigIntegerField()
    qq = models.IntegerField()
    payprice = models.FloatField()
    ordernumber = models.BigIntegerField()
    materials = models.ForeignKey(Materials, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'materialsorder'
        unique_together = (('id', 'ordernumber'),)


class Materialsorder1(models.Model):
    materials = models.ForeignKey(Materials, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    order_time = models.DateTimeField(blank=True, null=True)
    order_state = models.IntegerField()
    total_price = models.FloatField()
    order_num = models.IntegerField()
    order_tpye = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'materialsorder1'


class Materialsorder2(models.Model):
    materials = models.ForeignKey(Materials, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    order_time = models.DateTimeField(blank=True, null=True)
    order_state = models.IntegerField()
    total_price = models.FloatField()
    order_num = models.BigIntegerField()
    order_tpye = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'materialsorder2'


class Materialtypes(models.Model):
    id = models.IntegerField(primary_key=True)
    materialsid = models.IntegerField()
    materialsname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'materialtypes'


class Moneymanage(models.Model):
    dealprice = models.FloatField()
    dealstate = models.CharField(max_length=20)
    number = models.IntegerField()
    mymoney = models.IntegerField()
    finishtime = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'moneymanage'
        unique_together = (('user', 'number', 'finishtime'),)


class Nav(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nav'


class Order(models.Model):
    ordernumber = models.IntegerField()
    ordertime = models.DateTimeField(blank=True, null=True)
    price = models.FloatField()
    tel = models.IntegerField()
    clientserver = models.IntegerField()
    dealstate = models.CharField(max_length=20)
    number = models.IntegerField()
    buyorsell = models.CharField(max_length=11, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order'


class Purchasemessage(models.Model):
    game_account = models.CharField(max_length=20)
    account_pwd = models.CharField(max_length=50)
    account2 = models.ForeignKey(Account2, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'purchasemessage'


class Purchaseorder1(models.Model):
    account2 = models.ForeignKey(Account2, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    order_time = models.DateTimeField()
    order_state = models.IntegerField()
    total_price = models.FloatField()
    order_num = models.IntegerField()
    order_tpye = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'purchaseorder1'


class Purchaseorder2(models.Model):
    account2 = models.ForeignKey(Account2, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    order_time = models.DateTimeField(blank=True, null=True)
    order_state = models.IntegerField()
    total_price = models.FloatField()
    order_num = models.IntegerField()
    order_tpye = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'purchaseorder2'


class Sellorder1(models.Model):
    account1 = models.ForeignKey(Account1, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    order_time = models.DateTimeField()
    order_state = models.IntegerField()
    total_price = models.FloatField()
    order_num = models.IntegerField()
    order_tpye = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sellorder1'


class Sellorder2(models.Model):
    account1 = models.ForeignKey(Account1, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    order_time = models.DateTimeField()
    order_state = models.IntegerField()
    total_price = models.FloatField()
    order_num = models.IntegerField()
    order_tpye = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'sellorder2'


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    qq = models.IntegerField()
    email = models.CharField(max_length=50)
    photo = models.CharField(max_length=100, blank=True, null=True)
    tel = models.BigIntegerField()
    permission = models.BigIntegerField(blank=True, null=True)
    pay_pwd = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    sign = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('username', 'tel'),)
