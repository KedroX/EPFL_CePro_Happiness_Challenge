import pandas
import sys
import matplotlib.pyplot as plt


def top(file, col="GDP 2019", n=10):
    df = pandas.read_csv(file)

    # Keeps the n largest row by column col and sort them accordingly
    df2 = df.nlargest(n, col).reset_index(drop=True)

    print(f"\nTop {n} countries by {col} :")
    print(df2[['Country', col]])
    print("\n")


def bottom(file, col="GDP 2019", n=10):
    df = pandas.read_csv(file)

    # Keeps the n smallest row by column col and sort them accordingly
    df2 = df.nsmallest(n, col).reset_index(drop=True)

    print(f"\nBottom {n} countries by {col} :")
    print(df2[['Country', col]])
    print("\n")


def region_average(file, col="Score 2019"):
    df = pandas.read_csv(file)

    # Groups the data by Region and then calculates the mean of column col
    average_region = df.groupby("Region", as_index=False)[col].mean()

    # Renaming the column accordingly
    average_region = average_region.rename(columns={col: f"Average {col}"})

    print(f"Average {col} by Region:\n{average_region}\n")


def correlation(file, col1="GDP 2019", col2="Score 2019"):
    df = pandas.read_csv(file)

    df2 = df[col1].corr(df[col2])

    print(f"Correlation between {col1} and {col2}: \n{df2}\n")


def scatter(file, col1="GDP 2019", col2="Score 2019", output=""):
    # If no output is given creates default name
    if output == "":
        output = f"{col1}_{col2}_plot.png"

    df = pandas.read_csv(file)

    # Creation of the scatter plot
    plt.scatter(df[col1], df[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.title(f"Scatter plot of {col1} vs {col2}")
    plt.grid(True)

    # Save
    plt.savefig(output)
    print(f"Chart saved as {output}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide the parth to the CSV file as argument")
        print("Usage: python main.py <path>")
        sys.exit(1)

    file = sys.argv[1]

    region_average(file)
    top(file)
    bottom(file)
    correlation(file)
    scatter(file)