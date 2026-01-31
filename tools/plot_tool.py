import matplotlib.pyplot as plt

def plot_histogram(df, column):
    plt.figure()
    df[column].hist()
    plt.title(column)
    plt.savefig(f"data/uploads/{column}.png")
