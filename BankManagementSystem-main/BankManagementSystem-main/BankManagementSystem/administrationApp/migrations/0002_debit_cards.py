# Generated by Django 4.1.3 on 2022-11-02 20:28

import administrationApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrationApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='debit_cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.CharField(help_text='Debit Card number', max_length=100)),
                ('type_of_card', models.CharField(choices=[('Visa', 'Visa'), ('Master Card', 'Master Card')], default='Visa', help_text='Choose right type of card', max_length=100)),
                ('issued_date', models.DateTimeField()),
                ('expire_date', models.DateTimeField()),
                ('ccv', models.IntegerField(default=administrationApp.models.ccv_generator)),
                ('card_holder_print_name', models.CharField(help_text='Enter Card Holders Printable name', max_length=25)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrationApp.account')),
            ],
            options={
                'verbose_name': 'Debit Cards',
                'verbose_name_plural': 'Debit Cards',
            },
        ),
    ]