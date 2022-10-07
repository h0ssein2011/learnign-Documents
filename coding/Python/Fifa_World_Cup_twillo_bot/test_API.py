urls = {'group': 'http://worldcup.sfg.io/teams/group_results',
        'country': 'http://worldcup.sfg.io/matches/country?fifa_code=',
        'today': 'http://worldcup.sfg.io/matches/today',
        'tomorrow': 'http://worldcup.sfg.io/matches/tomorrow',
        'all_games':'http://worldcup.sfg.io/matches'
}

countries = ['KOR', 'PAN', 'MEX', 'ENG', 'COL', 'JPN', 'POL', 'SEN',
            'RUS', 'EGY', 'POR', 'MAR', 'URU', 'KSA', 'IRN', 'ESP',
            'DEN', 'AUS', 'FRA', 'PER', 'ARG', 'CRO', 'BRA', 'CRC',
            'NGA', 'ISL', 'SRB', 'SUI', 'BEL', 'TUN', 'GER', 'SWE']

import requests
# ...
html = requests.get(urls['all_games']).json()
for match in html:
     print(match['home_team_country'], 'vs',
        match['away_team_country'], 'at',
        match['datetime'])