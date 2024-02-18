# Generated by Django 4.1.3 on 2022-11-03 18:02

import administrationApp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrationApp', '0007_loan_loan_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_line', models.CharField(help_text='Enter Street name', max_length=100)),
                ('second_line', models.CharField(blank=True, help_text='Enter unit/appt number', max_length=10, null=True)),
                ('city_name', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('CA', 'CA'), ('AZ', 'AZ'), ('TX', 'TX')], max_length=10)),
                ('zipcode', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='card_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=100)),
                ('card_holder_name', models.CharField(max_length=100)),
                ('ccv', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Card Info',
                'verbose_name_plural': 'Card Info',
            },
        ),
        migrations.CreateModel(
            name='credit_cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_num', models.CharField(help_text='Debit Card number', max_length=100)),
                ('type_of_card', models.CharField(choices=[('Visa', 'Visa'), ('Master Card', 'Master Card')], default='Visa', help_text='Choose right type of card', max_length=100)),
                ('issued_date', models.DateTimeField()),
                ('expire_date', models.DateTimeField()),
                ('ccv', models.IntegerField(default=administrationApp.models.ccv_generator)),
                ('card_holder_print_name', models.CharField(help_text='Enter Card Holders Printable name', max_length=25)),
                ('usage_limit', models.FloatField()),
            ],
            options={
                'verbose_name': 'Credit Cards',
                'verbose_name_plural': 'Credit Cards',
            },
        ),
        migrations.CreateModel(
            name='loan_supporting_docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='payment_source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_card', models.CharField(help_text='Choose right type of card', max_length=100)),
                ('nick_name', models.CharField(help_text='Nick Name for Payment source', max_length=100)),
                ('account_holder_name', models.CharField(max_length=100)),
                ('billing_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrationApp.address')),
                ('card_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrationApp.card_info')),
            ],
            options={
                'verbose_name': 'Payment Source',
                'verbose_name_plural': 'Payment Source',
            },
        ),
        migrations.CreateModel(
            name='credit_card_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=100)),
                ('DueTime', models.DateTimeField(auto_now_add=True)),
                ('credit_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrationApp.loan')),
                ('payment_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrationApp.payment_source')),
            ],
            options={
                'verbose_name': 'Loan Payments',
                'verbose_name_plural': 'Loan Payments',
            },
        ),
        migrations.AddField(
            model_name='loan_payment',
            name='payment_source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administrationApp.payment_source'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='loan_customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('customer_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrationApp.customer')),
                ('loan_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrationApp.loan')),
            ],
            options={
                'verbose_name': 'Loan Customers',
                'verbose_name_plural': 'Loan Customers',
                'unique_together': {('loan_info', 'customer_info')},
            },
        ),
        migrations.CreateModel(
            name='credit_card_customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('credit_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrationApp.credit_cards')),
                ('customer_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrationApp.customer')),
            ],
            options={
                'verbose_name': 'Credit Card Customers',
                'verbose_name_plural': 'Credit Card Customers',
                'unique_together': {('credit_card', 'customer_info')},
            },
        ),
    ]
