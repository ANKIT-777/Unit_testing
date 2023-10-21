import csv
import matplotlib.pyplot as plt

def analyze_bowlers_economy(file_path):
    bowlers_data = {}
    bowlers_overs = {}

    with open(file_path, newline='') as csvfile:
        dataset = csv.DictReader(csvfile)

        for row in dataset:
            if 1 <= int(row['match_id']) <= 59:
                bowler = row['bowler']
                total_runs = int(row['total_runs'])
                if bowler not in bowlers_data:
                    bowlers_data[bowler] = total_runs
                    bowlers_overs[bowler] = 1
                else:
                    bowlers_data[bowler] += total_runs
                    bowlers_overs[bowler] += 1

    for bowler in bowlers_overs:
        total_deliveries = bowlers_overs[bowler]
        overs = total_deliveries // 6
        balls = total_deliveries % 6
        overs += balls / 10
        bowlers_overs[bowler] = overs

    Economy = {}

    for bowler in bowlers_data:
        if bowler in bowlers_overs:
            econ = float(bowlers_data[bowler] / bowlers_overs[bowler])
            Economy[bowler] = econ

    sorted_bowlers = dict(sorted(Economy.items(), key=lambda item: item[1]))

    top_N = 10
    top_bowlers = list(sorted_bowlers.keys())[:top_N][::-1]
    top_economy = list(sorted_bowlers.values())[:top_N]

    return top_bowlers, top_economy

if __name__ == "__main__":
    file_path = r'/Users/ankitsharma/Desktop/Python/IPL/deliveries.csv'
    top_bowlers, top_economy = analyze_bowlers_economy(file_path)
    print(top_bowlers)
    print(top_economy)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.barh(top_bowlers, top_economy, color='skyblue')
    plt.xlabel('Economy Rate')
    plt.ylabel('Bowler')
    plt.title('Top 10 Bowlers by Economy Rate')
    plt.gca().invert_yaxis()

    for i, v in enumerate(top_economy):
        plt.text(v, i, f'{v:.1f}', color='black', va='center')

    plt.show()
