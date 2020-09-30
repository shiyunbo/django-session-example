# Generated by Django 3.1.1 on 2020-09-25 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvitationCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.UUIDField(verbose_name='邀请码')),
                ('expire', models.DateTimeField(verbose_name='过期时间')),
            ],
        ),
    ]
