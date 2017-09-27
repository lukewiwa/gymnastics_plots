import numpy as np
import toyplot
import toyplot.html
from scipy.optimize import curve_fit
import json


class Linear:
    x_axis = np.linspace(0, 3)

    def func(self, x, m, b):
        return m*x + b

    def __init__(self, x_values, y_values):
        self.x, self.y = x_values, y_values
        popt, self.pcov = curve_fit(self.func, x_values, y_values)
        self.m, self.b = popt
        self.equation = self.m * self.x_axis + self.b

    def standard_error(self):
        variance = np.diagonal(self.pcov)
        std_error = np.sqrt(variance)
        return std_error

class Exponential:
    x_axis = np.linspace(0, 3)

    def func(self, x, a, b):
        return a*np.exp(-b*x) + 1.679

    def __init__(self, x_values, y_values):
        self.x, self.y = x_values, y_values
        popt, self.pcov = curve_fit(self.func, x_values, y_values)
        self.a, self.b = popt
        self.equation = self.func(self.x_axis, self.a, self.b)
    
    def standard_error(self):
        variance = np.diagonal(self.pcov)
        std_error = np.sqrt(variance)
        return std_error


class Plot:
    x_axis = np.linspace(0, 3)

    def __init__(self, x_values, y_values):
        self.x, self.y = x_values, y_values
        self.linear = Linear(x_values, y_values)
        self.exponential = Exponential(x_values, y_values)

    def plot(self):
        canvas = toyplot.Canvas(width=400, height=400)
        axes = canvas.cartesian(
            label="Vault Extrapolations",
            xlabel="Rotations",
            ylabel="Value",
        )
        mark1 = axes.scatterplot(
            self.x,
            self.y,
            color="red",
            size=8,
        )
        mark2 = axes.plot(self.x_axis, self.linear.equation)
        mark3 = axes.plot(self.x_axis, self.exponential.equation)
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

salto = np.array([0, 1, 2])
hspring = np.array([2.0, 2.8, 5.6])

if __name__ == "__main__":
    plot = Plot(salto, hspring)
    plot.plot()