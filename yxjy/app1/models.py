# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Account1(models.Model):
    gamearea = models.CharField(max_length=20)
    sex = models.CharField(max_length=5)
    profession = models.CharField(max_length=10)
    punish_record = models.CharField(max_length=20)
    qq_grade = models.CharField(max_length=20)
    qq_friends = models.CharField(max_length=20)
    safety_grade = models.CharField(max_length=10)
    publish_time = models.DateTimeField()
    price = models.FloatField()
    account_describe = models.CharField(max_length=200)
    account_number = models.IntegerField()
    account_photo = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    user = models.ForeignKey('User', models.DO_NOTHING)
    expiration_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'account1'


class Account2(models.Model):
    gamearea = models.CharField(max_length=20)
    sex = models.CharField(max_length=5)
    profession = models.CharField(max_length=20)
    punish_record = models.CharField(max_length=20)
    qq_grade = models.CharField(max_length=10)
    qq_friends = models.CharField(max_length=10)
    account_message = models.CharField(max_length=100)
    price = models.FloatField()
    publish_time = models.DateTimeField()
    expiration_time = models.DateTimeField()
    state = models.CharField(max_length=20)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account2'


class Credit(models.Model):
    credit = models.IntegerField()
    finishorder = models.IntegerField()
    cancelorder = models.IntegerField()
    okpercent = models.FloatField()
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'credit'


class Gold(models.Model):
    delivery = models.CharField(max_length=50)
    goodinfo = models.CharField(max_length=255)
    gamearea = models.CharField(max_length=100)
    goodsnum = models.IntegerField()
    unitprice = models.FloatField()
    price = models.FloatField()
    datetime = models.DateTimeField()
    productid = models.IntegerField()
    image = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gold'


class Goldorder(models.Model):
    num = models.IntegerField()
    reaparea = models.CharField(max_length=50)
    trading = models.CharField(max_length=20)
    picture = models.TextField(blank=True, null=True)
    tel = models.IntegerField()
    qq = models.IntegerField()
    payprice = models.FloatField()
    gold = models.ForeignKey(Gold, models.DO_NOTHING)
    ordernumber = models.ForeignKey('Order', models.DO_NOTHING, db_column='ordernumber')

    class Meta:
        managed = False
        db_table = 'goldorder'


class Materials(models.Model):
    delivery = models.CharField(max_length=50)
    goodinfo = models.CharField(max_length=255)
    gamearea = models.CharField(max_length=100)
    goodsnum = models.IntegerField()
    unitprice = models.FloatField()
    price = models.FloatField()
    datetime = models.DateTimeField()
    productid = models.IntegerField()
    image = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'materials'


class Materialsorder(models.Model):
    num = models.IntegerField()
    reaparea = models.CharField(max_length=50)
    rolename = models.CharField(max_length=20)
    tel = models.IntegerField()
    qq = models.IntegerField()
    payprice = models.FloatField()
    ordernumber = models.IntegerField()
    materials = models.ForeignKey(Materials, models.DO_NOTHING)
    order_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'materialsorder'


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


class Nav(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nav'


class Order(models.Model):
    ordernumber = models.IntegerField()
    ordertime = models.DateTimeField()
    price = models.FloatField()
    tel = models.IntegerField()
    clientserver = models.IntegerField()
    dealstate = models.CharField(max_length=20)
    number = models.IntegerField()
    buyorsell = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'order'


class Purchasemessage(models.Model):
    game_account = models.CharField(max_length=20)
    account_pwd = models.CharField(max_length=50)
    account2 = models.ForeignKey(Account2, models.DO_NOTHING)

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
    order_time = models.DateTimeField()
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
    order_tpye = models.IntegerField()

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
    order_tpye = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sellorder2'


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    qq = models.IntegerField()
    email = models.CharField(max_length=50)
    photo = models.CharField(max_length=100, blank=True, null=True)
    tel = models.IntegerField()
    permission = models.IntegerField(blank=True, null=True)
    pay_pwd = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    sign = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
