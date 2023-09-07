import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes with their descriptions
nodes = {
    'CodeCommit': 'Code Commit (GitLab)',
    'MavenBuild': 'Build with Maven\n(Spring Boot)',
    'ArtifactStorage': 'Artifact Storage\n(Artifactory)',
    'Dockerize': 'Dockerize',
    'HelmPackage': 'Helm Package',
    'HelmK8s': 'Deploy to K8s\n(Helm)',
    'K8sMaster': 'K8s Master Node',
    'K8sWorker': 'K8s Worker Nodes'
}
G.add_nodes_from(nodes.keys())

# Add edges to indicate the flow
edges = [
    ('CodeCommit', 'MavenBuild'),
    ('MavenBuild', 'ArtifactStorage'),
    ('ArtifactStorage', 'Dockerize'),
    ('Dockerize', 'HelmPackage'),
    ('HelmPackage', 'HelmK8s'),
    ('HelmK8s', 'K8sMaster'),
    ('K8sMaster', 'K8sWorker')
]
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # positions for all nodes
nx.draw(G, pos, with_labels=False, arrows=True, node_color='skyblue', node_size=3000, font_size=18, font_color='black', font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
nx.draw_networkx_labels(G, pos, nodes, font_size=10)

# Show UML-style notes for Kubernetes details
k8s_notes = {
    'HelmK8s': 'GitLab CI/CD triggers\nHelm CLI',
    'K8sMaster': 'Helm talks to K8s API\nServer on Master Node',
    'K8sWorker': 'Worker Nodes pull\nDocker images from\nArtifactory and run Pods'
}

for node, (x, y) in pos.items():
    if node in k8s_notes:
        plt.text(x, y - 0.15, k8s_notes[node], fontsize=10, ha='center')

# Show the diagram
plt.title('CI/CD Flow with Maven, Spring Boot, Artifactory, Docker, Helm, and Kubernetes')
plt.show()
