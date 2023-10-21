import csv
import matplotlib.pyplot as plt

class MatchesWonByTeam:
    def __init__(self):
        self.matches_won = {}

    def read_data(self, file_path):
        with open(file_path) as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                winner = row['winner']
                season = row['season']
                self.update_matches_won(winner, season)

    def update_matches_won(self, team, season):
        if team not in self.matches_won:
            self.matches_won[team] = {}

        if season not in self.matches_won[team]:
            self.matches_won[team][season] = 0

        self.matches_won[team][season] += 1

    def plot_stacked_bar_chart(self):
        teams = list(self.matches_won.keys())
        seasons = list(set(season for season_dict in self.matches_won.values() for season in season_dict.keys()))

        fig, ax = plt.subplots(figsize=(12, 6))

        bottom = [0] * len(teams)

        for season in seasons:
            matches_won_by_season = [self.matches_won[team].get(season, 0) for team in teams]

            ax.bar(teams, matches_won_by_season, label=season, bottom=bottom)
            bottom = [sum(x) for x in zip(bottom, matches_won_by_season)]

        ax.set_ylabel('Number of Matches Won')
        ax.set_xlabel('Teams')
        ax.set_title('Matches Won by IPL Teams Over the Years')
        plt.xticks(rotation=45, ha='right')
        ax.legend(title='Seasons', loc='upper left', bbox_to_anchor=(1, 0))

        plt.show()

def analyze_matches_won_by_team(file_path):
    matches_won_by_team = MatchesWonByTeam()
    matches_won_by_team.read_data(file_path)
    return matches_won_by_team.matches_won

if __name__ == "__main__":
    csv_file = 'Unit_Test/Mock_Matches.csv'  # Replace with the actual file path
    match_data = analyze_matches_won_by_team(csv_file)
    print(analyze_matches_won_by_team(csv_file))