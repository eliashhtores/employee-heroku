# Generated by Django 3.2.9 on 2021-12-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0010_alter_person_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]