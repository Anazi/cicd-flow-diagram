# Importing required libraries again due to the execution state reset
import matplotlib.pyplot as plt
import networkx as nx

# Create a new directed graph for the extended flow involving Docker and Helm
G_extended = nx.DiGraph()

# Add nodes with their descriptions for the extended flow
nodes_extended = {
    'CodeWrite': 'Write Code',
    'CodeCommit': 'Code Commit\n(GitLab)',
    'MavenBuild': 'Build with Maven\n(Spring Boot)',
    'ArtifactStorage': 'Artifact Storage\n(Artifactory)',
    'Dockerize': 'Dockerize',
    'DockerRegistry': 'Docker Registry\n(Docker Hub, Private Registry, etc.)',
    'HelmPackage': 'Helm Package',
    'HelmK8s': 'Deploy to K8s\n(Helm)',
    'K8sMaster': 'K8s Master Node',
    'K8sWorker': 'K8s Worker Nodes'
}
G_extended.add_nodes_from(nodes_extended.keys())

# Add edges to indicate the extended flow
edges_extended = [
    ('CodeWrite', 'CodeCommit'),
    ('CodeCommit', 'MavenBuild'),
    ('MavenBuild', 'ArtifactStorage'),
    ('ArtifactStorage', 'Dockerize'),
    ('Dockerize', 'DockerRegistry'),
    ('DockerRegistry', 'HelmPackage'),
    ('HelmPackage', 'HelmK8s'),
    ('HelmK8s', 'K8sMaster'),
    ('K8sMaster', 'K8sWorker')
]
G_extended.add_edges_from(edges_extended)

# Draw the extended graph
plt.figure(figsize=(14, 10))
pos_extended = nx.spring_layout(G_extended, seed=42)  # positions for all nodes
nx.draw(G_extended, pos_extended, with_labels=False, arrows=True, node_color='skyblue', node_size=3000, font_size=18, font_color='black', font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G_extended, 'weight')
nx.draw_networkx_edge_labels(G_extended, pos_extended, edge_labels=labels)
nx.draw_networkx_labels(G_extended, pos_extended, nodes_extended, font_size=10)

# Show UML-style notes for Docker and Helm details
docker_helm_notes = {
    'Dockerize': 'Build Docker Image\nwith JAR file.',
    'DockerRegistry': 'Push Image to Docker Registry.',
    'HelmPackage': 'Package app & image\nin Helm chart.',
    'HelmK8s': 'GitLab CI/CD triggers\nHelm CLI.',
    'K8sMaster': 'Helm talks to K8s API\nServer on Master Node.',
    'K8sWorker': 'Worker Nodes pull\nDocker images from\nRegistry and run Pods.'
}

for node, (x, y) in pos_extended.items():
    if node in docker_helm_notes:
        plt.text(x, y - 0.15, docker_helm_notes[node], fontsize=10, ha='center')

# Show the diagram
plt.title('Complete CI/CD Flow with Code, Maven, Artifactory, Docker, Helm, and Kubernetes')
plt.show()
