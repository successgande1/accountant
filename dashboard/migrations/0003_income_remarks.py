# Generated by Django 3.2.6 on 2021-08-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_expenditure_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='income',
            name='Remarks',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
