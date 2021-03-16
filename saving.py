salary = 12000
interest = 0.05
total_month = 12
monthly_saving = 10

def interest_rate(salary, interest, total_month, monthly_saving):
    tot_sav = (salary*monthly_saving/100*total_month)
    amount_interest = tot_sav*interest
    yearly_amount = tot_sav+amount_interest
    return yearly_amount

print(interest_rate(12000,0.05, 12, 10))

 



