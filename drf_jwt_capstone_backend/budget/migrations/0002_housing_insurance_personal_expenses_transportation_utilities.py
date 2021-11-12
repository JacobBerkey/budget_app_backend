# Generated by Django 3.2.8 on 2021-11-09 17:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('water', models.DecimalField(decimal_places=2, max_digits=6)),
                ('electricity', models.DecimalField(decimal_places=2, max_digits=6)),
                ('hvac', models.DecimalField(decimal_places=2, max_digits=6)),
                ('gas', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sewage', models.DecimalField(decimal_places=2, max_digits=6)),
                ('internet', models.DecimalField(decimal_places=2, max_digits=6)),
                ('phone', models.DecimalField(decimal_places=2, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_payment', models.DecimalField(decimal_places=2, max_digits=6)),
                ('fuel', models.DecimalField(decimal_places=2, max_digits=6)),
                ('public_transportation', models.DecimalField(decimal_places=2, max_digits=6)),
                ('auto_maintenance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Personal_Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbies', models.DecimalField(decimal_places=2, max_digits=6)),
                ('clothes', models.DecimalField(decimal_places=2, max_digits=6)),
                ('streaming_services', models.DecimalField(decimal_places=2, max_digits=6)),
                ('subscriptions', models.DecimalField(decimal_places=2, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_insurance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('auto_insurance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('life_insurance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.DecimalField(decimal_places=2, max_digits=6)),
                ('mortgage', models.DecimalField(decimal_places=2, max_digits=6)),
                ('property_tax', models.DecimalField(decimal_places=2, max_digits=6)),
                ('hoa', models.DecimalField(decimal_places=2, max_digits=6)),
                ('maintenance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]