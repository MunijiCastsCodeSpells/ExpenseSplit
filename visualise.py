import networkx as nx
import matplotlib.pyplot as plt


def create_graph(transactions):

    G = nx.DiGraph()

    for t in transactions:

        parts = t.split()

        debtor = parts[0]
        creditor = parts[2]
        amount = float(parts[3].replace("₹",""))

        G.add_edge(debtor, creditor, weight=amount)

    pos = nx.spring_layout(G)

    labels = nx.get_edge_attributes(G, 'weight')

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="lightblue",
        node_size=3000,
        font_size=10
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=labels
    )

    plt.title("Expense Settlement Graph")

    plt.savefig("static/graph.png")

    plt.clf()