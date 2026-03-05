def calculate_balances(names, expenses):

    paid = {name: 0 for name in names}
    share = {name: 0 for name in names}

    for expense in expenses:

        payer = expense["payer"]
        amount = expense["amount"]
        participants = expense["participants"]

        paid[payer] += amount

        for person, value in participants.items():
            share[person] += value

    paid_list = [paid[name] for name in names]
    share_list = [share[name] for name in names]

    return paid_list, share_list