import numpy as np
import toyplot
import toyplot.html
from scipy.optimize import curve_fit

x_axis = np.linspace(0, 3)
salto = np.array([0, 1, 2])
hspring = np.array([2.0, 2.8, 5.6])

linear_m, linear_b = np.polyfit(salto, hspring, 1)
linear_fit = linear_m * x_axis + linear_b

def func(x, a, b ,c):
    return a*np.exp(-b*x) + c

popt, pcov = curve_fit(func, salto, hspring)
a, b, c = popt
exp_fit = func(x_axis, a, b, c)


canvas = toyplot.Canvas(width=400, height=400)
axes = canvas.cartesian(
    label="Vault Extrapolations",
    xlabel="Rotations",
    ylabel="Value",
)
mark1 = axes.scatterplot(
    salto,
    hspring,
    color="red",
    size=8,
)
mark2 = axes.plot(x_axis, linear_fit)
mark3 = axes.plot(x_axis, exp_fit)
canvas.legend([
    ("Value", mark1),
    ("Linear Fit", mark2),
    ("Exponential Fit", mark3),
    ],
    corner=("top-left", 60, 80, 80),
    )

toyplot.html.render(
    canvas,
    "vault_plot.html",
    )
