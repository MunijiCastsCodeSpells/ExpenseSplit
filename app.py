from flask import Flask, render_template, request
from algorithm import settle_expenses_heap
from expenses import calculate_balances
from visualise import create_graph
import sqlite3
from database import init_db

app = Flask(__name__)
init_db()
@app.route("/", methods=["GET", "POST"])

def index():

    transactions = []
    error = None

    if request.method == "POST":

        try:

            names = request.form.get("names").split(",")
            names = [n.strip() for n in names]

            payers = request.form.getlist("payer")
            amounts = request.form.getlist("amount")
            categories = request.form.getlist("category")
            shares_raw = request.form.getlist("shares")

            expenses = []

            for i in range(len(payers)):

                if payers[i] == "" or amounts[i] == "" or shares_raw[i] == "":
                    continue

                payer = payers[i].strip()
                amount = float(amounts[i])
                category = categories[i]

                share_dict = {}

                pairs = shares_raw[i].split(",")

                for pair in pairs:

                    if ":" not in pair:
                        continue

                    name, value = pair.split(":")
                    share_dict[name.strip()] = float(value.strip())

                expenses.append({
                    "payer": payer,
                    "amount": amount,
                    "category": category,
                    "participants": share_dict
                })
                conn = sqlite3.connect("database.db")
                cursor = conn.cursor()

                cursor.execute(
                    "INSERT INTO expenses (payer, amount, category, shares) VALUES (?, ?, ?, ?)",
                    (payer, amount, category, shares_raw[i])
                )

                conn.commit()
                conn.close()

            paid, share = calculate_balances(names, expenses)

            transactions = settle_expenses_heap(names, paid, share)
            create_graph(transactions)

        except Exception as e:
            error = str(e)
    history = load_expenses()

    return render_template(
        "index.html",
        transactions=transactions,
        error=error,
        history = history
    )

def load_expenses():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT payer, amount, category, shares FROM expenses")

    rows = cursor.fetchall()

    conn.close()

    return rows
if __name__ == "__main__":
    app.run(debug=True)