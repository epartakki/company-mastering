import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the CSV file
@st.cache
def load_data():
    data = pd.read_csv('output.csv')
    return data

def create_hierarchy(data):
    G = nx.DiGraph()

    # Iterate through the rows and add edges to the graph
    for index, row in data.iterrows():
        source = row['parent'] if row['level'] != 'global' else None
        target = row['branch']
        G.add_edge(source, target)

    return G

def main():
    st.title("Hierarchy Visualization App")

    data = load_data()
    G = create_hierarchy(data)

    pos = nx.spring_layout(G, seed=42)  # Positions for all nodes

    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, font_size=10, font_color='black', node_color='skyblue', ax=ax)
    st.pyplot(fig)

if __name__ == '__main__':
    main()
