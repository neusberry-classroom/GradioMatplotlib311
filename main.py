# import numpy as np
# import matplotlib.pyplot as plt
#
# xlist = []
# ylist = []
# for x in range(8):
#     xlist.append(x)
#     ylist.append(x * 3)
#
# x = np.array(xlist)
# y = np.array(ylist)
#
# plt.title("My First Mat Plot")
# plt.xlabel("Average count")
# plt.ylabel("Sales (Rs.)")
#
# plt.plot(x, y)
#
# plt.grid()
# plt.show()

# ################################################################################
import matplotlib.pyplot as plt
import numpy as np
import gradio as gr


def plot_forecast(final_year, companies, noise, show_legend, point_style):
    start_year = 2020
    x = np.arange(start_year, final_year + 1)
    year_count = x.shape[0]
    plt_format = ({"cross": "X", "line": "-", "circle": "o--"})[point_style]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i, company in enumerate(companies):
        series = np.arange(0, year_count, dtype=float)
        series = series**2 * (i + 1)
        series += np.random.rand(year_count) * noise
        ax.plot(x, series, plt_format)
    if show_legend:
        plt.legend(companies)
    return fig


demo = gr.Interface(
    plot_forecast,
    [
        gr.Radio([2025, 2030, 2035, 2040], label="Project to:"),
        gr.CheckboxGroup(["Google", "Microsoft", "Gradio"], label="Company Selection"),
        gr.Slider(1, 100, label="Noise Level"),
        gr.Checkbox(label="Show Legend"),
        gr.Dropdown(["cross", "line", "circle"], label="Style"),
    ],
    gr.Plot(label="forecast"),
)

if __name__ == "__main__":
    demo.launch(share=False)

# #############################################################################

# import gradio as gr
# from math import sqrt
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
#
# def outbreak(plot_type, r, month, countries, social_distancing):
#     months = ["January", "February", "March", "April", "May"]
#     m = months.index(month)
#     start_day = 30 * m
#     final_day = 30 * (m + 1)
#     x = np.arange(start_day, final_day + 1)
#     pop_count = {"USA": 350, "Canada": 40, "Mexico": 300, "UK": 120}
#     if social_distancing:
#         r = sqrt(r)
#     df = pd.DataFrame({"day": x})
#     for country in countries:
#         df[country] = x ** (r) * (pop_count[country] + 1)
#
#     if plot_type == "Matplotlib":
#         fig = plt.figure()
#         plt.plot(df["day"], df[countries].to_numpy())
#         plt.title("Outbreak in " + month)
#         plt.ylabel("Cases")
#         plt.xlabel("Days since Day 0")
#         plt.legend(countries)
#         return fig
#     else:
#         raise ValueError("A plot type must be selected")
#
#
# inputs = [
#     gr.Dropdown(["Matplotlib", "Plotly", "Altair"], label="Plot Type"),
#     gr.Slider(1, 4, 3.2, label="R"),
#     gr.Dropdown(["January", "February", "March", "April", "May"], label="Month"),
#     gr.CheckboxGroup(
#         ["USA", "Canada", "Mexico", "UK"], label="Countries", value=["USA", "Canada"]
#     ),
#     gr.Checkbox(label="Social Distancing?"),
# ]
# outputs = gr.Plot()
#
# demo = gr.Interface(
#     fn=outbreak,
#     inputs=inputs,
#     outputs=outputs,
#     examples=[
#         ["Matplotlib", 2, "March", ["Mexico", "UK"], True]
#     ],
#     cache_examples=True,
# )
#
# if __name__ == "__main__":
#     demo.launch(share=False)

# #################################################################################
# import gradio as gr
#
# def result(name, marks):
#     if marks >= 90:
#         return f"Dear {name}, you got {marks}, Result = Pass"
#     return f"Dear {name}, you got {marks}, Result = Fail. Workhard"
#
#
# demo = gr.Interface(fn=result, inputs=["text", "number"], outputs="label")
# demo.launch(share=False)