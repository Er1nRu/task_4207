from lxml import etree
import json
import datetime
from miniLib import printObj
from miniLib import FullInfo
from miniLib import file1Edit
from miniLib import file2Edit
from miniLib import PrintFlight

#file 1
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

with open('./results/RS_Via-3_max.json','w', encoding='utf-8') as f:
        max_flight_str = etree.tostring(max_flight).decode('utf-8')
        max_flight_dict = {}
        for element in max_flight.iter():
            max_flight_dict[element.tag] = str(element.text).strip()
        file1Edit(max_flight_dict)
        json.dump(max_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/RS_Via-3_min.json','w', encoding='utf-8') as f:
        min_flight_str = etree.tostring(min_flight).decode('utf-8')
        min_flight_dict = {}
        for element in min_flight.iter():
            min_flight_dict[element.tag] = str(element.text).strip()
        file1Edit(min_flight_dict)
        json.dump(min_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/RS_Via-3_speed.json','w', encoding='utf-8') as f:
        speed_flight_str = etree.tostring(speed_flight).decode('utf-8')
        speed_flight_dict = {}
        for element in speed_flight.iter():
            speed_flight_dict[element.tag] = str(element.text).strip()
        file1Edit(speed_flight_dict)
        json.dump(speed_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/RS_Via-3_optium.json','w', encoding='utf-8') as f:
        speed_flight_str = etree.tostring(speed_flight).decode('utf-8')
        speed_flight_dict = {}
        for element in speed_flight.iter():
            speed_flight_dict[element.tag] = str(element.text).strip()
        file1Edit(speed_flight_dict)

        json.dump(speed_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/RS_Via-3_slow.json','w', encoding='utf-8') as f:
        slow_flight_str = etree.tostring(slow_flight).decode('utf-8')
        slow_flight_dict = {}
        for element in slow_flight.iter():
            slow_flight_dict[element.tag] = str(element.text).strip()
        file1Edit(slow_flight_dict)
        json.dump(slow_flight_dict, f, indent=4, ensure_ascii=False)


tree = etree.parse("./requests/RS_ViaOW.xml")
root = tree.getroot()
print(f"root : {root}")

flights = []
for item in root[1]:
    flights.append(item)
print(*flights[0], sep="\n")

#task 1
for flight in flights:
    if flight[0][0][0][2].text == "DXB" and flight[0][0][-1][3].text == "BKK":
        # print(flight[0][0][-1][2].text)
        PrintFlight(flight)

#task 2

max_flight2 = flights[0]  
min_flight2 = flights[0]  
for intem, utem in zip(flights, flights[1:]):
    intem_price = float(intem[-1][2].text)
    utem_price = float(utem[-1][2].text)
    if intem_price < utem_price:
        max_flight2 = utem
    if intem_price > utem_price:
        min_flight2 = utem
print("Дорогой")
PrintFlight(max_flight2)
print("Дешёвый")
PrintFlight(min_flight2)

speed_flight2 = flights[0] 
slow_flight2 = flights[0] 

for intem in flights[1:]:  
    intem_departure_time = intem[0][0][0][4].text  
    intem_arrival_time = intem[0][0][-1][5].text 

    speed_flight_departure_time = speed_flight2[0][0][0][4].text  
    speed_flight_arrival_time = speed_flight2[0][0][-1][5].text  

    slow_flight_departure_time = slow_flight2[0][0][0][4].text  
    slow_flight_arrival_time = slow_flight2[0][0][-1][5].text  

    if intem_departure_time < speed_flight_departure_time and intem_arrival_time < speed_flight_arrival_time:
        speed_flight2 = intem  

    if intem_departure_time > slow_flight_departure_time and intem_arrival_time > slow_flight_arrival_time:
        slow_flight2 = intem  

print(f"Самый быстрый рейс:")
PrintFlight(speed_flight2)
print(f"Самый медленный рейс:")
PrintFlight(slow_flight2)

with open('./results/RS_ViaOW_max.json','w', encoding='utf-8') as f:
        max_flight_str = etree.tostring(max_flight2).decode('utf-8')
        max_flight_dict = {}
        for element in max_flight2.iter():
            max_flight_dict[element.tag] = str(element.text).strip()
        max_flight_dict['ServiceCharges'] = max_flight2[-1][2].text
        file2Edit(max_flight_dict)
        json.dump(max_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/RS_ViaOW_min.json','w', encoding='utf-8') as f:
        min_flight_str = etree.tostring(min_flight2).decode('utf-8')
        min_flight_dict = {}
        for element in min_flight2.iter():
            min_flight_dict[element.tag] = str(element.text).strip()
        min_flight_dict['ServiceCharges'] = min_flight2[-1][2].text
        file2Edit(min_flight_dict)
        json.dump(min_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/RS_ViaOW_speed.json','w', encoding='utf-8') as f:
        speed_flight_str = etree.tostring(speed_flight2).decode('utf-8')
        speed_flight_dict = {}
        for element in speed_flight2.iter():
            speed_flight_dict[element.tag] = str(element.text).strip()
        speed_flight_dict['ServiceCharges'] = speed_flight2[-1][2].text
        file2Edit(speed_flight_dict)
        json.dump(speed_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/RS_ViaOW_optium.json','w', encoding='utf-8') as f:
        speed_flight_str = etree.tostring(speed_flight2).decode('utf-8')
        speed_flight_dict = {}
        for element in speed_flight2.iter():
            speed_flight_dict[element.tag] = str(element.text).strip()
        speed_flight_dict['ServiceCharges'] = speed_flight2[-1][2].text
        file2Edit(speed_flight_dict)
        json.dump(speed_flight_dict, f, indent=4, ensure_ascii=False)

with open('./results/RS_ViaOW_slow.json','w', encoding='utf-8') as f:
        slow_flight_str = etree.tostring(slow_flight2).decode('utf-8')
        slow_flight_dict = {}
        for element in slow_flight2.iter():
            slow_flight_dict[element.tag] = str(element.text).strip()
        slow_flight_dict['ServiceCharges'] = slow_flight2[-1][2].text
        file2Edit(slow_flight_dict)
        json.dump(slow_flight_dict, f, indent=4, ensure_ascii=False)