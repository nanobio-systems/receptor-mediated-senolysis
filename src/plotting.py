import matplotlib.pyplot as plt

def plot_single(
    x, y, xlabel, ylabel, title, label=None
):
    plt.figure(figsize=(8,5))

    plt.plot(x, y, label=label)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    if label is not None:
                plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show

def plot_comp(
    x1, y1, label1, x2, y2, label2, xlabel, ylabel, title
):
    plt.figure(figsize=(8,5))
    plt.plot(x1, y1, label=label1)
    plt.plot(x2, y2, label=label2)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend
    plt.grid(True)
    plt.tight_layout()
    plt.show()
