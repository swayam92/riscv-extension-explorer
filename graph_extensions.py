import json
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

with open("riscv-extensions-landscape/src/instr_dict.json", "r") as f:
    data = json.load(f)

graph = nx.Graph()

for instruction, info in data.items():

    extensions = info.get("extension", [])

    if len(extensions) > 1:

        for ext1, ext2 in combinations(extensions, 2):

            graph.add_edge(ext1, ext2)

print("Nodes:", graph.number_of_nodes())
print("Edges:", graph.number_of_edges())

plt.figure(figsize=(14, 10))

nx.draw(
    graph,
    with_labels=True,
    node_size=1200,
    font_size=8
)

plt.title("RISC-V Extension Relationship Graph")

plt.savefig("extension_graph.png")

plt.show()