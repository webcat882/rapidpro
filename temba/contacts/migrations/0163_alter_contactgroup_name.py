# Generated by Django 4.0.3 on 2022-04-18 19:28

from django.db import migrations, models

import temba.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0162_alter_contactfield_field_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactgroup",
            name="name",
            field=models.CharField(max_length=64, validators=[temba.utils.fields.validate_name]),
        ),
    ]
