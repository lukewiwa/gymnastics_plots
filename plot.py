import numpy as np
import pandas as pd
import toyplot
import toyplot.html
from pathlib import Path

def load_csv(csv):
    with open(csv, 'r') as f:
        dataframe = pd.read_csv(f)
    return dataframe

def plot(app_name, data):
    matrix = pd.crosstab(
        data[data.app==app_name].value,
        data.eg,
    )
    domain_min = matrix.values.min()
    domain_max = matrix.values.max()
    tlocator=toyplot.locator.Explicit(labels=list(matrix))
    llocator=toyplot.locator.Explicit(labels=list(matrix.index))
    width = 500
    height = 600
    label = app_name
    tlabel = "Element Group"
    llabel = "Value"
    colormap = toyplot.color.brewer.map(
        "Greens",
        reverse=True,
        domain_min=domain_min,
        domain_max=domain_max,
    )
    app_canvas, app_table = toyplot.matrix(
        (matrix, colormap),
        tlocator=tlocator,
        llocator=llocator,
        width=width,
        height=height,
        label=label,
        tlabel=tlabel,
        llabel=llabel,
    )
    app_table.body.grid.hlines[[0,-1],...] = "single"
    app_table.body.grid.vlines[...,[0,-1]] = "single"
    plot_name = "{}.html".format(app_name)
    plot_dir = str(Path('.', 'plots', plot_name))
    toyplot.html.render(
        app_canvas,
        plot_dir,
    )

def render_plots(app_names, data):
    for app_name in app_names:
        plot(app_name, data)

cop = load_csv('code_of_points_MAG_2020.csv')
apps = cop.app.unique()

render_plots(apps, cop)   
