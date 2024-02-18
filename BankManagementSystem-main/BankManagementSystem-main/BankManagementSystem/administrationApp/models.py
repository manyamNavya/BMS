from django.db import models
from django.contrib.auth.models import User
import random
import ccard

# choices
role_choices = (
    ('Primary', 'Primary'),
    ('Secondary', 'Secondary')
)

# Create your models here.
us_states = (
    ('CA', 'CA'),
    ('AZ', 'AZ'),
    ('TX', 'TX'),
)
class address(models.Model):

    first_line = models.CharField(max_length=100, help_text="Enter Street name")
    second_line = models.CharField(max_length=10, null=True, blank=True, help_text="Enter unit/appt number")
    city_name = models.CharField(max_length=100)
    state = models.CharField(max_length=10, choices=us_states)
    zipcode = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Address"

    def __str__(self):
        return "{} {}".format(self.first_line, self.second_line)
    pass

class customer(models.Model):

    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Choose customer online profile")
    display_name = models.CharField(max_length=100, null=False, blank=False, help_text="Enter customer display name")
    customer_role = models.CharField(max_length=100, null=True, blank=True, choices=role_choices,default="Primary",help_text="Choose Right Customer Role")
    phone_number= models.CharField(max_length=100, null=False, blank=False, help_text="Enter Phone number with country code, Ex: +1-111-222-3333")
    address = models.ForeignKey(address,on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name="Customers"
        verbose_name_plural="Customers"
    
    def __str__(self):
        return self.display_name

# >>> format(110, '05d')
# '00110'
# >>> 'Formatted String : {0:05d}'.format(12)
# 'Formatted String : 00012'


def customer_account_no_generator():

    obj = account.objects.last()
    prefix = "BMSBANK"
    if obj is None:
        return '{}{}'.format(prefix, "0000001")
    else:
        new_number = '{0:07d}'.format(int(obj.account_number.split('BMSBANK')[1]) + 1)
        return '{}{}'.format(prefix, new_number)

account_choices = (
    ('Savings Account', 'Savings Account'),
    ('Checking Account', 'Checking Account'),
)
class account(models.Model):

    account_number = models.CharField(max_length=100, primary_key=True, default=customer_account_no_generator)
    account_type = models.CharField(max_length=100, choices=account_choices, default="Savings Account", help_text="Choose right type of the account")
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    opening_balance=models.FloatField(default=0.00)

    class Meta:
        verbose_name="Accounts"
        verbose_name_plural="Accounts"
    
    def __str__(self):
        return self.account_number

class Bank(models.Model):

    name = models.CharField(max_length=100, help_text="Enter bank name")
    legal_name = models.CharField(max_length=100)
    established_date = models.DateField()
    customer_care_number = models.CharField(max_length=100, null=False, blank=False, help_text="Enter Phone number with country code, Ex: +1-111-222-3333")
    description = models.CharField(max_length=250)
    address = models.ForeignKey(address, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name="Bank"
        verbose_name_plural="Bank"
    
    def __str__(self):
        return self.name

class bank_branch(models.Model):

    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=25)
    address = models.ForeignKey(address,on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name="Bank Branch"
        verbose_name_plural="Bank Branch"
    
    def __str__(self):
        return self.name

class department(models.Model):

    branch = models.ForeignKey(bank_branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    department_code = models.CharField(max_length=25)

    class Meta:
        verbose_name="Department"
        verbose_name_plural="Department"
    
    def __str__(self):
        return self.name

def employee_id_generator():

    obj = employee.objects.last()
    prefix = "BMSEMP"
    if obj is None:
        return '{}{}'.format(prefix, '00001')
    else:
        new_number = '{0:05d}'.format(int(obj.employeeId.split(prefix)[1]) + 1)
        return '{}{}'.format(prefix, new_number)

class employee(models.Model):

    department=models.ForeignKey(department, on_delete=models.CASCADE)
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    employeeId = models.CharField(max_length=100, default=employee_id_generator)
    employee_title = models.CharField(max_length=100)
    employee_designation = models.CharField(max_length=100)
    employee_start_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    office_contact_number=models.CharField(max_length=100, null=False, blank=False, help_text="Enter Phone number with country code, Ex: +1-111-222-3333")
    address = models.ForeignKey(address,on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name="Employee"
        verbose_name_plural="Employees"
    
    def __str__(self):
        return self.employeeId

class mn_accounts_customers(models.Model):

    account_number = models.ForeignKey(account, on_delete=models.CASCADE)
    customer_info = models.ForeignKey(customer, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Accounts Customers"
        verbose_name_plural="Accounts Customers"
        unique_together = ['account_number', 'customer_info']
    
    def __str__(self):
        return "{} - {}".format(self.account_number, self.customer_info)

debit_card_types = (
    ('Visa', 'Visa'),
    ('Master Card', 'Master Card'),
)

def card_number_generator():

    return ccard.visa()

def ccv_generator():
    return random.randint(100, 999)

class debit_cards(models.Model):

    account = models.ForeignKey(account, on_delete=models.CASCADE)
    card_num=models.CharField(max_length=100, default=card_number_generator, help_text="Debit Card number")
    type_of_card=models.CharField(max_length=100, choices=debit_card_types, default="Visa" ,help_text="Choose right type of card")
    issued_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    ccv = models.IntegerField(null=False, blank=False, default=ccv_generator)
    card_holder_print_name = models.CharField(max_length=25, null=False, blank=False, help_text="Enter Card Holders Printable name")
    
    class Meta:
        verbose_name="Debit Cards"
        verbose_name_plural="Debit Cards"
    
    def __str__(self):
        return self.card_num

card_usage_status = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
)

class debit_card_usage(models.Model):

    debit_card = models.ForeignKey(debit_cards, on_delete=models.CASCADE)
    spent_amount=models.FloatField()
    date_time=models.DateTimeField(auto_now_add=True)
    merchant = models.CharField(max_length=100, null=True, blank=True, help_text="Where this money has been spent?")
    status_of_spent = models.CharField(max_length=100, choices=card_usage_status, default="Pending",help_text="Current status of transaction")
    
    class Meta:
        verbose_name="Debit Card Usage"
        verbose_name_plural="Debit Card Usage"
    
    def __str__(self):
        return '{} - Amount - {} spent at {} is {}'.format(self.debit_card, self.spent_amount, self.merchant, self.status_of_spent)

loan_types = (
    ('Personal Loan', 'Personal Loan'),
    ('Auto Loan', 'Auto Loan'),
    ('Mortgage Loan', 'Mortgage Loan'),
    ('Education Loan', 'Education Loan'),
)

def loan_number_generator():

    obj = loan.objects.last()
    prefix = "BMSLOAN"
    if obj is None:
        return '{}{}'.format(prefix, '00001')
    else:
        new_number = '{0:05d}'.format(int(obj.loanId.split(prefix)[1]) + 1)
        return '{}{}'.format(prefix, new_number)


class loan(models.Model):

    loanId = models.CharField(max_length=100, null=False, unique=True, blank=False, default=loan_number_generator,help_text="Loan application number")
    loan_type = models.CharField(max_length=100, choices=loan_types)
    requesting_amount = models.FloatField()
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_date = models.DateTimeField(auto_now_add=True)
    current_status = models.CharField(max_length=100, choices=card_usage_status, default="Pending")
    status_changed_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Loan"
        verbose_name_plural="Loans"
    
    def __str__(self):
        return self.loanId


class loan_customer(models.Model):
    
    loan_info = models.ForeignKey(loan, on_delete=models.CASCADE)
    customer_info = models.ForeignKey(customer, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Loan Customers"
        verbose_name_plural="Loan Customers"
        unique_together = ['loan_info', 'customer_info']
    
    def __str__(self):
        return "{} - {}".format(self.loan_info, self.customer_info)


class card_info(models.Model):

    card_number = models.CharField(max_length=100, null=False, blank=False)
    card_holder_name = models.CharField(max_length=100)
    ccv=models.CharField(max_length=4)

    class Meta:
        verbose_name = "Card Info"
        verbose_name_plural = "Card Info"
    
    def __str__(self):
        return self.card_number


class payment_source(models.Model):

    type_of_card = models.CharField(max_length=100, help_text="Choose right type of card")
    nick_name = models.CharField(max_length=100, help_text="Nick Name for Payment source")
    account_holder_name = models.CharField(max_length=100)
    card_info = models.ForeignKey(card_info, on_delete=models.CASCADE)
    billing_address = models.ForeignKey(address,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Payment Source"
        verbose_name_plural="Payment Source"
    
    def __str__(self):
        return self.nick_name

class loan_payment(models.Model):

    loan = models.ForeignKey(loan, on_delete=models.CASCADE)
    payment_source = models.ForeignKey(payment_source, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=card_usage_status, default="Pending")
    DueTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Loan Payments"
        verbose_name_plural="Loan Payments"
    
    def __str__(self):
        return 'Ammount: {} received for Loan account: {}'.format(self.amount, self.loan)

class loan_supporting_docs(models.Model):

    pass

class credit_cards(models.Model):

    card_num=models.CharField(max_length=100, help_text="Debit Card number")
    type_of_card=models.CharField(max_length=100, choices=debit_card_types, default="Visa" ,help_text="Choose right type of card")
    issued_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    ccv = models.IntegerField(null=False, blank=False, default=ccv_generator)
    card_holder_print_name = models.CharField(max_length=25, null=False, blank=False, help_text="Enter Card Holders Printable name")
    usage_limit = models.FloatField()

    class Meta:
        verbose_name="Credit Cards"
        verbose_name_plural="Credit Cards"
    
    def __str__(self):
        return self.card_num


class credit_card_customers(models.Model):

    credit_card = models.ForeignKey(credit_cards, on_delete=models.CASCADE)
    customer_info = models.ForeignKey(customer, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Credit Card Customers"
        verbose_name_plural="Credit Card Customers"
        unique_together = ['credit_card', 'customer_info']
    
    def __str__(self):
        return "{} - {}".format(self.credit_card, self.customer_info)


class credit_card_payment(models.Model):

    credit_card = models.ForeignKey(loan, on_delete=models.CASCADE)
    payment_source = models.ForeignKey(payment_source, on_delete=models.CASCADE)
    amount = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=card_usage_status, default="Pending")
    DueTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Loan Payments"
        verbose_name_plural="Loan Payments"
    
    def __str__(self):
        return 'Ammount: {} received for Credit Card account: {}'.format(self.amount, self.loan)