# Currency Calculator
# INS:
#  * EUR/USD amount of money  100USD, 60EUR
# OUT:
#  * euquivalent in MDL

k_eur_2_mdl = 20.00
k_usd_2_mdl = 18.00


str_amount = input("Enter money amount (USD/EUR): ")



amount   = int( str_amount[:-3] )
currency = str_amount[-3:] 

amount_mdl = amount * k_usd_2_mdl

print(amount, currency, " => ", amount_mdl, "MDL")
  