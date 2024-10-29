from lxml import etree
import json
import datetime
from miniLib import printObj
from miniLib import FullInfo
from miniLib import PrintFlight
tree = etree.parse("./requests/RS_Via-3.xml")
root = tree.getroot()
print(f"root : {root}")



Flights = []
for child in root:
    Flights += child



#task 1
for flight in Flights:
    if flight[0][0][0][2].text == "DXB" and flight[1][0][0][2].text == "BKK":
        PrintFlight(flight)

#task 2

temp = []
for flight, currnetFlight in zip(Flights, Flights[1:]):
    flight_price = float(flight[-1][-1].text)
    currnetFlight_price = float(currnetFlight[-1][-1].text)
    if flight[0][0][0][2].text == "DXB" and flight[0][0][-1][3].text == "BKK":
        temp.append(flight)

max_flight = temp[0]  
min_flight = temp[0]  
for intem, utem in zip(temp, temp[1:]):
    intem_price = float(intem[-1][-1].text)
    utem_price = float(utem[-1][-1].text)
    if intem_price < utem_price:
        max_flight = utem
    if intem_price > utem_price:
        min_flight = utem

# PrintFlight(max_flight)
# PrintFlight(min_flight)

speed_flight = temp[0] 
slow_flight = temp[0] 

for intem in temp[1:]:  
    intem_departure_time = intem[0][0][0][4].text  
    intem_arrival_time = intem[1][0][0][4].text 

    speed_flight_departure_time = speed_flight[0][0][0][4].text  
    speed_flight_arrival_time = speed_flight[1][0][0][4].text  

    slow_flight_departure_time = slow_flight[0][0][0][4].text  
    slow_flight_arrival_time = slow_flight[1][0][0][4].text  

    if intem_departure_time < speed_flight_departure_time and intem_arrival_time < speed_flight_arrival_time:
        speed_flight = intem  

    if intem_departure_time > slow_flight_departure_time and intem_arrival_time > slow_flight_arrival_time:
        slow_flight = intem  

print(f"Самый быстрый рейс: {speed_flight[0][0][0][4].text} - {speed_flight[1][0][0][4].text}")
print(f"Самый медленный рейс: {slow_flight[0][0][0][4].text} - {slow_flight[1][0][0][4].text}")

for intem in temp[1:]:  
    intem_departure_time = intem[0][0][0][4].text  
    intem_arrival_time = intem[1][0][0][4].text 
    speed_flight_departure_time = speed_flight[0][0][0][4].text 
    speed_flight_arrival_time = speed_flight[1][0][0][4].text  

    slow_flight_departure_time = slow_flight[0][0][0][4].text  
    slow_flight_arrival_time = slow_flight[1][0][0][4].text 

    if intem_departure_time < speed_flight_departure_time and intem_arrival_time < speed_flight_arrival_time:
        speed_flight = intem  

    if intem_departure_time > slow_flight_departure_time and intem_arrival_time > slow_flight_arrival_time:
        slow_flight = intem 

with open('./results/max.json','w', encoding='utf-8') as f:
        max_flight_str = etree.tostring(max_flight).decode('utf-8')
        max_flight_dict = {}
        for element in max_flight.iter():
            max_flight_dict[element.tag] = element.text
        json.dump(max_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/min.json','w', encoding='utf-8') as f:
        min_flight_str = etree.tostring(min_flight).decode('utf-8')
        min_flight_dict = {}
        for element in min_flight.iter():
            min_flight_dict[element.tag] = element.text
        json.dump(min_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/speed.json','w', encoding='utf-8') as f:
        speed_flight_str = etree.tostring(speed_flight).decode('utf-8')
        speed_flight_dict = {}
        for element in speed_flight.iter():
            speed_flight_dict[element.tag] = element.text
        json.dump(speed_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/optium.json','w', encoding='utf-8') as f:
        speed_flight_str = etree.tostring(speed_flight).decode('utf-8')
        speed_flight_dict = {}
        for element in speed_flight.iter():
            speed_flight_dict[element.tag] = element.text
        json.dump(speed_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/slow.json','w', encoding='utf-8') as f:
        slow_flight_str = etree.tostring(slow_flight).decode('utf-8')
        slow_flight_dict = {}
        for element in slow_flight.iter():
            slow_flight_dict[element.tag] = element.text
        json.dump(slow_flight_dict, f, indent=4, ensure_ascii=False)

