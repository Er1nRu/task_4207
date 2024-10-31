import datetime
def printObj(object):
    transfer = False
    if len(object[0][0]) > 2:
        transfer = True
    else:
        transfer = False
    print(len(object[0][0]))
    print((object[0][0]))
        
def PrintFlight(flights):
    transfer = False
    localFlighgt = flights[0][0]
    if len(localFlighgt) >= 2:
        transfer = True
    else:
        transfer = False
    # print(transfer)
    for index in range(len(localFlighgt)):
        dateFrom = datetime.datetime.strptime(localFlighgt[index][4].text,'%Y-%m-%dT%H%M')
        dateTo = datetime.datetime.strptime(localFlighgt[index][5].text, '%Y-%m-%dT%H%M')
        datetime.datetime.strftime(dateFrom,'%d %B %Y года, %H:%M')
        datetime.datetime.strftime(dateTo,'%d %B %Y года, %H:%M')
        print(f"[{localFlighgt[index][0].text} : {localFlighgt[index][1].text}]\nОткуда [{localFlighgt[index][2].text}|{dateFrom}] Куда [{localFlighgt[index][3].text}|{dateTo}]\nСтоимость [{flights[-1][-1].text}]")
    print(f"Пересадка [{transfer}]")
    print()

def FullInfo(flight):
    data = [] 
    
    for flight_item in flight:  
        flight_data = {}
        
        onward_data = {}
        for element in flight_item.iter():
            onward_data[element.tag] = element.text
        flight_data['OnwardPricedItinerary'] = onward_data
        flight_data['Pricing'] = flight_item[0]
        del data['Flights']
        data.append(flight_data)  
    return data
    
def file1Edit(list):
    list.pop('Flights')
    list.pop('OnwardPricedItinerary')
    list.pop('Flight')
    list.pop('ReturnPricedItinerary')
    list.pop('Pricing')