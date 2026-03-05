import heapq

def settle_expenses_heap(names, paid, share):

    if abs(sum(paid) - sum(share)) > 0.01:
        raise ValueError("Total paid must equal total share")

    balance = [paid[i] - share[i] for i in range(len(names))]

    creditors = []
    debtors = []

    for i, b in enumerate(balance):

        if b > 0:
            heapq.heappush(creditors, (-b, names[i]))  

        elif b < 0:
            heapq.heappush(debtors, (b, names[i]))     

    transactions = []

    while creditors and debtors:

        credit, creditor = heapq.heappop(creditors)
        debit, debtor = heapq.heappop(debtors)

        credit = -credit
        debit = -debit

        amount = min(credit, debit)

        transactions.append(
            f"{debtor} pays {creditor} ₹{amount:.2f}"
        )

        credit -= amount
        debit -= amount

        if credit > 0:
            heapq.heappush(creditors, (-credit, creditor))

        if debit > 0:
            heapq.heappush(debtors, (-debit, debtor))

    return transactions