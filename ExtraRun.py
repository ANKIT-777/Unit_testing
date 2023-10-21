import csv
import matplotlib.pyplot as plt

class ExtraRunsAnalysis:
    def __init__(self, file_path):
        self.file_path = file_path
        self.extra_runs = {}

    def analyze_extra_runs(self):
        with open(self.file_path) as csvfile:
            dataset = csv.DictReader(csvfile)
            for row in dataset:
                if 577 <= int(row['match_id']) <= 636:
                    self.update_extra_runs(row)

    def update_extra_runs(self, row):
        bowling_team = row['bowling_team']
        extra_runs = int(row['extra_runs'])

        if bowling_team not in self.extra_runs:
            self.extra_runs[bowling_team] = 0

        self.extra_runs[bowling_team] += extra_runs

    def plot_extra_runs(self):
        x = list(self.extra_runs.values())
        y = list(self.extra_runs.keys())

        plt.plot(y, x, marker='o')
        plt.xticks(rotation=45)
        plt.show()

def analyze_extra_runs_data(file_path):
    extra_runs_analysis = ExtraRunsAnalysis(file_path)
    extra_runs_analysis.analyze_extra_runs()
    return extra_runs_analysis.extra_runs

if __name__ == '__main__':
    file_path = 'IPL/deliveries.csv'  # Update with the correct file path
    extra_runs_data = analyze_extra_runs_data(file_path)
    print(extra_runs_data)  # Print the data to see the results
