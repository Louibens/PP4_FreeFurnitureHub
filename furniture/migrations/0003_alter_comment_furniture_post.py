# Generated by Django 3.2.20 on 2023-08-05 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('furniture', '0002_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='furniture_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='furniture.furniture'),
        ),
    ]