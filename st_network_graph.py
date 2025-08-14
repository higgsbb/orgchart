from pyvis.network import Network
import streamlit as st

net = Network(height="750px", width="100%", directed=True)

# Example org data
employees = [
    {"id": "CEO", "title": "Chief Executive Officer", "manager": None},
    {"id": "CTO", "title": "Chief Technology Officer", "manager": "CEO"},
    {"id": "Team1", "title": "Team Members:\n- Alice\n- Bob\n- Charlie", "manager": "CTO", "is_team": True},
    {"id": "Eng1", "title": "Engineer 1", "manager": "Team1"},
    {"id": "Eng2", "title": "Engineer 2", "manager": "Team1"},
]

# Add nodes
for emp in employees:
    if emp.get("is_team"):
        # Big box for team
        net.add_node(
            emp["id"],
            label=emp["title"],
            shape="box",
            color={"background": "#FFF8DC", "border": "#DEB887"},
            font={"size": 14, "align": "left"},
            widthConstraint={"minimum": 200, "maximum": 300}
        )
    else:
        net.add_node(
            emp["id"],
            label=f"{emp['id']}\n{emp['title']}",
            shape="box"
        )

# Add edges
for emp in employees:
    if emp["manager"]:
        net.add_edge(emp["manager"], emp["id"])

# Top-down layout
net.set_options("""
{
  "layout": {
    "hierarchical": {
      "direction": "UD",
      "sortMethod": "directed",
      "levelSeparation": 150,
      "nodeSpacing": 200
    }
  },
  "physics": {
    "hierarchicalRepulsion": {
      "nodeDistance": 200
    }
  }
}
""")

# Show in Streamlit
net.save_graph("org_chart.html")
html_file = open("org_chart.html", 'r', encoding='utf-8').read()
st.components.v1.html(html_file, height=800)
