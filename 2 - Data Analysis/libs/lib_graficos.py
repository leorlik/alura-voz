import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_hist(df: pd.DataFrame, column: str, title: str, bins: int = 0):

    fig = plt.figure(figsize=(10, 6))

    column = df.dropna(subset=[column])[column]

    if(not bins):
        bin_edges = np.histogram_bin_edges(column)
    else:
        bin_edges = np.histogram_bin_edges(column, bins=bins)
    
    ax = column.hist(bins=bin_edges, edgecolor='black')

    plt.xticks(bin_edges)
    plt.title(title)
    plt.ticklabel_format(style='plain', axis='x')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    return fig


def create_categorical_bar_chart(df: pd.DataFrame, column: str, title: str, rotate: bool = False, numerical: bool = False,
                                 pctg: bool = False):
    
    fig, ax = plt.subplots(figsize=(10, 6))

    counts = df[column].dropna().value_counts()

    if(numerical):
        counts.index = counts.index.astype(int)
        counts = counts.sort_index()

    ax = counts.plot(kind='bar', edgecolor='black')

    ax.set_title(title)
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')

    for rect in ax.patches:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2
        space = 1
        label = "{:.2f}".format(y_value) if pctg else str(y_value)
        ax.annotate(label, (x_value, y_value), textcoords="offset points",  ha='center', va = 'bottom')

    if(rotate):
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
    else:
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

    return fig

def get_pie_chart(df: pd.DataFrame, column: str, title: str):

    fig = plt.subplots(figsize=(10, 6))

    counts = df[column].dropna().value_counts().sort_index()

    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)
    
    plt.pie(counts, labels=counts.index, autopct=lambda pct: func(pct, len(df[~df[column].isna()])))

    total = sum(counts)
    plt.text(0 , 0, f'Total: {total}', fontsize=12, ha='center')

    plt.title(title)

    return fig
    
def get_scatter_plot(df: pd.DataFrame, x: str, y: str, title: str):

    fig = plt.figure(figsize=(10, 6))

    ax = sns.scatterplot(x = x, y = y, data = df)

    plt.title(title)

    return fig

def get_heatmap(df: pd.DataFrame, title: str, col_x: str, col_y: str, x_label: str, y_label: str):

    fig = plt.figure(figsize=(10, 6))
    cross_tab = pd.crosstab(df[col_x], df[col_y])

    ax = sns.heatmap(cross_tab, annot=True, fmt='d', cmap='coolwarm')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    return fig

def get_box_plot(df: pd.DataFrame, x: str, y: str, title: str):

    fig = plt.figure(figsize=(10, 6))

    ax = sns.boxplot(x = x, y = y, data = df)

    plt.title(title)

    return fig