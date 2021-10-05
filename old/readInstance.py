import xml.etree.ElementTree as ET
import json

class Carryover:
    def __init__(self):
        self.objective = None
        self.format = []
        self.teams = []
        self.timeSlots = []
        self.weights = []

def getInstance(path):
    carryover = Carryover()
    tree = ET.parse(path + '.xml')
    root = tree.getroot()

    carryover.objective = root.find('./ObjectiveFunction/Objective').text

    for format in root.iter('Format'):
        numberRoundRobin = format.find('numberRoundRobin').text
        compactness = format.find('compactness').text
        carryover.format.append({**format.attrib,'numberRoundRobin':numberRoundRobin,'compactness':compactness})

    for team in root.iter('team'):
        carryover.teams.append(team.attrib)

    for slot in root.iter('slot'):
        carryover.timeSlots.append(slot.attrib)

    for COEWeight in root.iter('COEWeight'):
        carryover.weights.append(COEWeight.attrib)

    with open(path + '.json','w') as file:
        json.dump(carryover.__dict__,file,indent=4)
    
    return carryover