# Generated by Django 4.1.7 on 2023-04-08 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matéria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descrição', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descrição', models.TextField()),
                ('matéria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dash.matéria')),
            ],
        ),
    ]
