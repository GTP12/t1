# Generated by Django 2.0.6 on 2019-01-24 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gamearea', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=5)),
                ('profession', models.CharField(max_length=10)),
                ('punish_record', models.CharField(max_length=20)),
                ('qq_grade', models.CharField(max_length=20)),
                ('qq_friends', models.CharField(max_length=20)),
                ('safety_grade', models.CharField(max_length=10)),
                ('publish_time', models.DateTimeField()),
                ('price', models.FloatField()),
                ('account_describe', models.CharField(max_length=200)),
                ('account_number', models.IntegerField()),
                ('account_photo', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Account_deal',
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.IntegerField()),
                ('finishorder', models.IntegerField()),
                ('cancelorder', models.IntegerField()),
                ('okpercent', models.FloatField()),
            ],
            options={
                'db_table': 'credit',
            },
        ),
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.CharField(max_length=50)),
                ('goodinfo', models.CharField(max_length=255)),
                ('gamearea', models.CharField(max_length=100)),
                ('goodsnum', models.IntegerField()),
                ('unitprice', models.FloatField()),
                ('price', models.FloatField()),
                ('datetime', models.DateTimeField()),
                ('productid', models.IntegerField()),
                ('image', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'gold',
            },
        ),
        migrations.CreateModel(
            name='Goldorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('reaparea', models.CharField(max_length=50)),
                ('trading', models.CharField(max_length=20)),
                ('picture', models.TextField(blank=True, null=True)),
                ('tel', models.IntegerField()),
                ('qq', models.IntegerField()),
                ('payprice', models.FloatField()),
                ('gold', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app1.Gold')),
            ],
            options={
                'db_table': 'goldorder',
            },
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.CharField(max_length=50)),
                ('goodinfo', models.CharField(max_length=255)),
                ('gamearea', models.CharField(max_length=100)),
                ('goodsnum', models.IntegerField()),
                ('unitprice', models.FloatField()),
                ('price', models.FloatField()),
                ('datetime', models.DateTimeField()),
                ('productid', models.IntegerField()),
                ('image', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'materials',
            },
        ),
        migrations.CreateModel(
            name='Materialsorder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('reaparea', models.CharField(max_length=50)),
                ('rolename', models.CharField(max_length=20)),
                ('tel', models.IntegerField()),
                ('qq', models.IntegerField()),
                ('payprice', models.FloatField()),
                ('ordernumber', models.IntegerField()),
                ('order_id', models.IntegerField()),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Materials')),
            ],
            options={
                'db_table': 'materialsorder',
            },
        ),
        migrations.CreateModel(
            name='Moneymanage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealprice', models.FloatField()),
                ('dealstate', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('mymoney', models.IntegerField()),
                ('finishtime', models.DateTimeField()),
            ],
            options={
                'db_table': 'moneymanage',
            },
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'nav',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordernumber', models.IntegerField()),
                ('ordertime', models.DateTimeField()),
                ('price', models.FloatField()),
                ('tel', models.IntegerField()),
                ('clientserver', models.IntegerField()),
                ('dealstate', models.CharField(max_length=20)),
                ('number', models.IntegerField()),
                ('buyorsell', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('qq', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('photo', models.CharField(blank=True, max_length=100, null=True)),
                ('tel', models.IntegerField()),
                ('permission', models.IntegerField(blank=True, null=True)),
                ('pay_pwd', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('sign', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User'),
        ),
        migrations.AddField(
            model_name='moneymanage',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User'),
        ),
        migrations.AddField(
            model_name='materials',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User'),
        ),
        migrations.AddField(
            model_name='goldorder',
            name='ordernumber',
            field=models.ForeignKey(db_column='ordernumber', on_delete=django.db.models.deletion.CASCADE, to='app1.Order'),
        ),
        migrations.AddField(
            model_name='gold',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User'),
        ),
        migrations.AddField(
            model_name='credit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.User'),
        ),
    ]
