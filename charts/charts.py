import matplotlib.pyplot as plt 

def generate_pie_chart(name_plot):
    labels = ['A', 'B', 'C']
    values = [200, 300, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig(name_plot)
    plt.close()