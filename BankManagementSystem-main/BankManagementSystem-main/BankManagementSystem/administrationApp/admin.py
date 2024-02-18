from django.contrib import admin
from .models import customer, account, mn_accounts_customers,debit_cards, debit_card_usage, employee, bank_branch, Bank, department, loan, loan_payment, payment_source, loan_supporting_docs, address, credit_cards, credit_card_payment, credit_card_customers, loan_customer, card_info

# Register your models here. 
admin.site.register(customer) # done
admin.site.register(account) # done
admin.site.register(mn_accounts_customers) # done
admin.site.register(debit_cards) # done
admin.site.register(debit_card_usage) # done
admin.site.register(employee) # done
admin.site.register(bank_branch) # done
admin.site.register(Bank) # done
admin.site.register(department) # done
admin.site.register(loan) # done
admin.site.register(loan_payment) # done
admin.site.register(address) # done
admin.site.register(payment_source) # done
admin.site.register(loan_supporting_docs) # done
admin.site.register(credit_cards) # done
admin.site.register(credit_card_payment) # done
admin.site.register(credit_card_customers) # done
admin.site.register(loan_customer) # done
admin.site.register(card_info) # done