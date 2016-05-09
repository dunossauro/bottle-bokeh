from bokeh.plotting import figure
from bokeh.charts import Bar
from bokeh.embed import file_html
from bokeh.resources import CDN
from bottle import Bottle, jinja2_view


app = Bottle()

# =========================== Start Bar
data = {
    'Palavras': [x for x in range(21)],
    'frequência': [x for x in range(21)]
}

bar = Bar(data, values='frequência', label='Palavras',
          title="Teste")

graph_bar = file_html(bar, CDN)

# =========================== End Bar

# =========================== Start Line
x = [1, 9, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(title="Exemplo Simples", x_axis_label='x', y_axis_label='y')
p.line(x, y, legend="Linha Azul", line_width=2)

graph_line = file_html(p, CDN)
# =========================== End Line

@app.route("/")
@jinja2_view('saida.html')
def grap():
    return dict(bokeh_line=graph_line,
                bokeh_bar=graph_bar,
                texto="Um exemplo simples integrando o Bokeh, Jinja2 e Bottle")

app.run()
