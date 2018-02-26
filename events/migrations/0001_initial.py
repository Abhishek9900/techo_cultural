# Generated by Django 2.0 on 2017-12-19 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusRepresantative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Institute', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=50)),
                ('EventDescription', models.CharField(max_length=1000)),
                ('eventCost', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('Event_Cat', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('PhoneNo', models.CharField(max_length=10)),
                ('Institute_Uni', models.CharField(max_length=100)),
                ('payment_to_be_paid', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('payment_paid', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('is_active', models.BooleanField(default=False)),
                ('secret_code', models.CharField(default=0, max_length=5)),
                ('events', models.ManyToManyField(blank=True, to='events.Events')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
