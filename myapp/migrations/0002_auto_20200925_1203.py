# Generated by Django 3.1.1 on 2020-09-25 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcode',
            name='code',
            field=models.CharField(max_length=10, unique=True, verbose_name='邀请码'),
        ),
    ]