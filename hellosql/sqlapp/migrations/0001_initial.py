# Generated by Django 3.0.8 on 2020-07-30 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.SmallIntegerField(choices=[(0, '女'), (1, '男'), (2, '保密')])),
                ('tel', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=64)),
                ('birthday', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pub_date', models.DateField()),
                ('authors', models.ManyToManyField(to='sqlapp.Author')),
                ('publish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sqlapp.Publish')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='au_detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sqlapp.AuthorDetail'),
        ),
    ]