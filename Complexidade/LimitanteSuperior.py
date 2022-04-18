# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
if __name__ == '__main__':
    # Data
    n = range(1, 2000);
    f = []
    g = []
    for value in n:
        f.append(value*1000)
        g.append(value * value)
    print(f)
    df = pd.DataFrame(
        {'n_values':n,
         'f_values': f,
         'g_values': g})

    # multiple line plots
    plt.plot('n_values', 'f_values', data=df, marker='',
             markerfacecolor='blue', markersize=12, color='skyblue',
             linewidth=2)
    plt.plot('n_values', 'g_values', data=df, marker='', color='olive', linewidth=2)

    # show legend
    plt.legend()

    # show graph
    plt.show()

