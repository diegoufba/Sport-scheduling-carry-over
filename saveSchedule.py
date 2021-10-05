import xml.etree.ElementTree as ET

def save_solution(schedule):
    tree = ET.ElementTree(ET.fromstring('<Solution></Solution>'))
    root = tree.getroot()

    games = ET.SubElement(root,'Games')

    solution = []

    n = len(schedule)

    for t in range(n):
        for r in range(n-1):
            away = schedule[t][r]
            if away > t:
                game = {
                    'home': str(t),
                    'away' : str(away),
                    'slot' : str(r),
                }
                solution.append(game)


    for jogo in solution:
        game = ET.SubElement(games,'ScheduledMatch',jogo)
    tree.write('Solution.xml')
