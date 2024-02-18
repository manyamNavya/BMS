# BankManagementSystem
 
issues:
	
fix: Bank account number: nvalid literal for int() with base 10: 'BMSBANK0000001' --> done
fix: Card number --> done
fix: Employee ID --> done
fix: loan number ID -> done
fix: loan supporting documents --> required internet

how to run?

to install dependecies
pip3 install -r requirements.text

to create tables
python3 manage.py makemigrations
python3 manage.py migrate

to run application
python3 manage.py runserver
