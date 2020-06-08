import random
from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    values = int(input('Valores a graficar: '))
    x_val = list(range(values))
    y_val = [random.randint(0, 99) for i in range(values)]

    output_file = 'Graficado_Simple.html'
    fig = figure()
    fig.line(x_val, y_val, line_width=2)
    show(fig)

    print(x_val)
    print(y_val)