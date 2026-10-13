def budget_remaining(budget, food, transport):
    return budget - food - transport
    pass

def budget_message(name, remaining):
    return f"{name} has {remaining} remaining."
    pass

remainings = budget_remaining(2000, 900, 600)
message= budget_message("Ada", remainings)
print(message)
