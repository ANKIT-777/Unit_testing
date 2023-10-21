import csv
import matplotlib.pyplot as plt

class MatchStatistics:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.Matches = {}

    def process_data(self):
        with open(self.csv_file, newline='') as csvfile:
            Data = csv.DictReader(csvfile)
            for row in Data:
                year = row['season']
                if year not in self.Matches:
                    self.Matches[year] = 1
                else:
                    self.Matches[year] += 1

    def plot_data(self):
        x = list(self.Matches.keys())
        y = list(self.Matches.values())

        plt.bar(x, y)
        plt.xlabel('Year')
        plt.ylabel('Number of Matches')
        plt.title('Match Statistics Over the Years')
        plt.show()

def analyze_match_statistics(csv_file):
    match_stats = MatchStatistics(csv_file)
    match_stats.process_data()
    return match_stats.Matches

if __name__ == "__main__":
    csv_file = 'Unit_Test/Mock_Matches.csv'  # Replace with the actual file path
    match_data = analyze_match_statistics(csv_file)
    print(match_data)  # Print the data to see the results

# Now, run the script and check the printed output to see the match statistics.
