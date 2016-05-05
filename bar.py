from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN
from bottle import Bottle, jinja2_view
from os import system
app = Bottle()


x = [1, 9, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="Exemplo Simples", x_axis_label='x', y_axis_label='y')
p.line(x, y, legend="Linha Azul", line_width=2)

graph = file_html(p, CDN)
#graph.replace('<title>Bokeh Application</title>', '')

@app.route("/")
@jinja2_view('saida.html')
def grap():
    return dict(bokeh=graph, texto="Um exemplo simples integrando o Bokeh, Jinja2 e Bottle")

app.run()
