import plotly.express as px
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
#fig.show()
fig.write_html("test1.html", include_plotlyjs='cdn')