import networkx as nx
import matplotlib.pyplot as plt

# Input data
total_applications = int(input("Enter the total number of applications: "))
no_response = int(input("Enter the number of applications with no response: "))
rejections = int(input("Enter the number of rejections: "))
interviews = int(input("Enter the number of interviews: "))
job_offers = int(input("Enter the number of job offers: "))

# Create a directed graph
G = nx.DiGraph()

# Add nodes with labels
G.add_node("Total Applications", count=total_applications)
G.add_node("No Response", count=no_response)
G.add_node("Rejections", count=rejections)
G.add_node("Interviews", count=interviews)
G.add_node("Job Offers", count=job_offers)

# Add edges with weights
G.add_edges_from([
    ("Total Applications", "No Response", {'weight': no_response}),
    ("Total Applications", "Rejections", {'weight': rejections}),
    ("Total Applications", "Interviews", {'weight': interviews}),
    ("Interviews", "Job Offers", {'weight': job_offers})
])

# Positioning the nodes
pos = nx.spring_layout(G)

# Drawing nodes and labels
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)

# Drawing edge labels
edge_labels = {(u, v): f"{d['weight']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.title("Job Application Flow Chart")
plt.show()
