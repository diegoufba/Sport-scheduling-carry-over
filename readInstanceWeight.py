import xml.etree.ElementTree as ET

def getInstance(path):
    tree = ET.parse(path)
    root = tree.getroot()

    n = 0
    for team in root.iter('team'):
        n += 1
    
    weight = []
    for i in range (n):
        weight.append([0]*n)

    for COEWeight in root.iter('COEWeight'):
        i = int(COEWeight.attrib['team1'])
        j = int(COEWeight.attrib['team2'])
        w = int(COEWeight.attrib['weight'])
        weight[i][j] = w

    return weight,n