# Generated by Django 3.1.4 on 2021-01-26 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Warszawa', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='konferencja', max_length=100)),
                ('info', models.TextField(blank=True)),
                ('date', models.CharField(default='1 stycznia', max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('photo', models.ImageField(default='default.jpg', upload_to='images/')),
                ('schedule', models.FileField(default='default.pdf', upload_to='schedule/')),
                ('accepted', models.BooleanField(default=False)),
                ('localization', models.ForeignKey(default='Warszawa', on_delete=django.db.models.deletion.CASCADE, to='content.city')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.organizer')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Ogólna', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.event')),
                ('owner', models.ManyToManyField(blank=True, related_name='tickets', to='users.NormalUser')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(default='Ogólna', on_delete=django.db.models.deletion.CASCADE, to='content.type'),
        ),
    ]
