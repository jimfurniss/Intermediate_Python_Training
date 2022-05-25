from datetime import datetime
from csv import reader

# Pip install matplotlib (not if using replit.com)
from matplotlib.pyplot import subplots, show


def main():
    # Getting Static Data
    filename = "Little_Rock_Weather_2019.csv"

    with open(filename) as f:
        r = reader(f)

        # Grab (pop) the header row and remove it from the reader
        header_row = next(r)

        highs = []
        lows = []
        dates = []
        
        for row in r:
            # Getting a specific station: USW00003952
            if row[0] == "USW00003952":
                # Highs are in column 5
                high = int(row[5])
                highs.append(high)

                # Lows are in column 6
                low = int(row[6])
                lows.append(low)

                # Matplotlib.pyplot needs dates in a specific format
                date = datetime.strptime(row[2], "%Y-%m-%d")
                dates.append(date)

    # Setting up Graph
    graph = subplots()
    graph_figure = graph[0]
    graph_parts = graph[1]

    # Will plot 2 lines
    graph_parts.plot(dates, highs, c="red")
    graph_parts.plot(dates, lows, c="blue")

    # Labeling Graph
    graph_parts.set_title("Little Rock Daily Temps, 2019", fontsize=26)
    graph_parts.set_xlabel("Date", fontsize=18)
    graph_parts.set_ylabel("Temperature (\u00b0F)", fontsize=18)
    
    graph_figure.autofmt_xdate()

    # Show the graph
    show()
    
    # Save file
    # graph_figure.savefig("graph.png")


if __name__ == '__main__':
    main()