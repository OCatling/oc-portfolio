# Generated by Django 2.1.1 on 2018-11-30 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='isInvert',
            field=models.BooleanField(default=False),
        ),
    ]