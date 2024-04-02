from pprint import pprint

def transactions_for(inv_id, transaction_lst):
    return [item for item in transaction_lst
            if item["id"] == inv_id]

# Works but a bit unwieldy to read

# def is_item_available(inv_id, transaction_lst):
#     item_total = sum([transaction['quantity'] if transaction['movement'] == 'in'
#                       else -transaction['quantity']
#                       for transaction
#                       in transactions_for(inv_id, transaction_lst)])
#     print(item_total)
#     return item_total > 0

def is_item_available(item, transactions):
    relevant_transactions = transactions_for(item, transactions)
    quantity = 0

    for transaction in relevant_transactions:
        if transaction['movement'] == 'in':
            quantity += transaction['quantity']
        else:
            quantity -= transaction['quantity']
    
    return quantity > 0

transactions = [ {"id": 101, "movement": 'in',  "quantity":  5},
                 {"id": 105, "movement": 'in',  "quantity": 10},
                 {"id": 102, "movement": 'out', "quantity": 17},
                 {"id": 101, "movement": 'in',  "quantity": 12},
                 {"id": 103, "movement": 'out', "quantity": 20},
                 {"id": 102, "movement": 'out', "quantity": 15},
                 {"id": 105, "movement": 'in',  "quantity": 25},
                 {"id": 101, "movement": 'out', "quantity": 18},
                 {"id": 102, "movement": 'in',  "quantity": 22},
                 {"id": 103, "movement": 'out', "quantity": 15}]

# pprint(transactions_for(101, transactions))
# prints
# [ {"id": 101, "movement": "in",  "quantity":  5},
#   {"id": 101, "movement": "in",  "quantity": 12},
#   {"id": 101, "movement": "out", "quantity": 18} ]

print(is_item_available(101, transactions))  # False
print(is_item_available(103, transactions))  # False
print(is_item_available(105, transactions))  # True