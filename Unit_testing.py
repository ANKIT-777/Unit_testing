import unittest
from Bowlers import analyze_bowlers_economy
from Mathces import analyze_match_statistics
from Winners import analyze_matches_won_by_team
from ExtraRun import analyze_extra_runs_data

class IPl_datset_unitTesting(unittest.TestCase):

    def test_analyze_bowlers_economy(self):
        file_path = 'IPL/deliveries.csv'  # Replace with the actual file path
        top_bowlers, top_economy = analyze_bowlers_economy(file_path)

        expected_top_bowlers = ['LH Ferguson', 'GJ Maxwell', 'Harbhajan Singh', 'S Nadeem', 'Washington Sundar', 'P Negi', 'Avesh Khan', 'R Tewatia', 'Mohammad Nabi', 'NB Singh']
        expected_top_economy = [4.390243902439025, 5.363636363636363, 5.604395604395605, 6.0, 6.08433734939759, 6.258278145695364, 6.538461538461538, 6.545012165450121, 6.596858638743455, 6.713286713286713]

        self.assertEqual(top_bowlers, expected_top_bowlers)
        self.assertEqual(top_economy, expected_top_economy)
        
    def test_analyze_match_statistics(self):
        csv_file = 'Unit_Test/Mock_Matches.csv'  
        expected_data = {'2017': 4, '2013': 6, '2015': 5}
        
        actual_data = analyze_match_statistics(csv_file)
        self.assertEqual(actual_data, expected_data)
        
    def test_analyze_matches_won_by_team(self):
        csv_file = 'Unit_Test/Mock_Matches.csv'  # Replace with the actual file path
        expected_data = {
            'Sunrisers Hyderabad': {'2017': 1, '2013': 1},
            'Rising Pune Supergiant': {'2017': 1},
            'Kolkata Knight Riders': {'2017': 1, '2015': 1},
            'Kings XI Punjab': {'2017': 1},
            'Mumbai Indians': {'2013': 1},
            'Chennai Super Kings': {'2013': 2, '2015': 1},
            'Delhi Daredevils': {'2013': 1, '2015': 2},
            'Royal Challengers Bangalore': {'2013': 1},
            'Rajasthan Royals': {'2015': 1}
        }

        actual_data = analyze_matches_won_by_team(csv_file) 
        self.assertEqual(actual_data, expected_data)
        
    def test_analyze_extra_runs_data(self):
        csv_file = 'IPL/deliveries.csv'  # Replace with the actual file path
        expected_data = {
            'Rising Pune Supergiants': 108,
            'Mumbai Indians': 102,
            'Kolkata Knight Riders': 122,
            'Delhi Daredevils': 106,
            'Gujarat Lions': 98,
            'Kings XI Punjab': 100,
            'Sunrisers Hyderabad': 107,
            'Royal Challengers Bangalore': 156
        }
        
        
        actual_data = analyze_extra_runs_data(csv_file)
        
        self.assertEqual(actual_data, expected_data)    
if __name__ == '__main__':
    unittest.main()
