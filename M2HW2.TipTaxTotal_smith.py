
# CTI-110 
 # M2HW2 - Tip Tax Total 
 # Smithg0481
 # 09/11/2017
 
#ask the cost of food
foodCost= int(input ('What is food cost? ') )
#(Assume 18% tip and 7% sales tax.)
tipAmount=0.18 * foodCost
print('The Tip is', format(tipAmount,'.2f'))
saleTax=0.07 * foodCost
print('The tax is', format(saleTax,'.2f'))
#what is total cost
totalCost= foodCost + (tipAmount + saleTax)
print ('Total cost ', format(totalCost, '.2f'))
