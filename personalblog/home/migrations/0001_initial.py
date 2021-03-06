# Generated by Django 3.2.2 on 2021-05-15 12:15

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_content', django_quill.fields.QuillField()),
                ('blog_image', models.ImageField(upload_to='home/static/images')),
                ('blog_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
