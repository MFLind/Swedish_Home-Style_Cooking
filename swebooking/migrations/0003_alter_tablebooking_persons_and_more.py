# Generated by Django 4.1.6 on 2023-03-02 08:47

from django.db import migrations, models
import swebooking.models


class Migration(migrations.Migration):

    dependencies = [
        ('swebooking', '0002_alter_tablebooking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablebooking',
            name='persons',
            field=models.PositiveIntegerField(validators=[swebooking.models.validate_persons]),
        ),
        migrations.AlterField(
            model_name='tablebooking',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, validators=[swebooking.models.validate_datetime]),
        ),
    ]
