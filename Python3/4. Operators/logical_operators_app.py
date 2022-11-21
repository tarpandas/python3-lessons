has_high_income = True
has_good_credit = True
is_legal = True
if has_high_income and has_good_credit and is_legal:
    print("Eligible for loan.")
elif has_high_income or has_good_credit and is_legal:
    print("Talk to the manager.")
elif not is_legal:
    print("Ineligible due to legal reasons.")
else:
    print("Not eligible for loan.")

'''
and: both
or: at least one is true
not: inverse
'''