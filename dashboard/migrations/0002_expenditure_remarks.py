# Generated by Django 3.2.6 on 2021-08-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenditure',
            name='Remarks',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
