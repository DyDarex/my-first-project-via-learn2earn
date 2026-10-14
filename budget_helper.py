def budget_remaining(budget, food, transport, other_expenses):
    return budget - food - transport - other_expenses
    pass

def budget_message(name, remaining):
    return f"{name} has {remaining} remaining."
    pass

print(budget_remaining(1000, 200, 600, 100))  #normal case
# print(budget_remaining(1500, 0, 0))        #zero case
#print(budget_remaining(1000,800,500))       #over spend case

#remainings =3q) #for ada
#remaining = budget_remaining(1000,800,500)   #for tobi


#message= budget_message("Ada", remainings)
#result= budget_message("Tobi", remaining)

#print(message)
#print(result)
