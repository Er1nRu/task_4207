import datetime
def printObj(object):
    transfer = False
    if len(object[0][0]) > 2:
        transfer = True
    else:
        transfer = False
    print(len(object[0][0]))
    print((object[0][0]))
    # print(f"[{object[0][0][0].text} : {object[0][0][1].text}]")

    # for it in flight:
    #     print(it)
    #     print(f"[{object[0][0].text} : {object[0].text}] откуда [{object[0].text}] куда [{object[0].text}]")

# [самолёт : айди]
# откуда [] куда []
# [самолёт : айди]
# откуда [] куда []
# стоимость []
# 
# 
#             
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
    # data = {}
    # temp_data = {}
    # # print(flight[1][0][0])
    # for index in range(len(flight[0][0])):
    #     tempp_data = {}
    #     for atrr in flight[index][0][0]:
    #         print(atrr.tag)
    #         tempp_data[f'{atrr.tag}'] = atrr.text    
    #     temp_data['Flight'] = tempp_data

    # data['OnwardPricedItinerary'] = temp_data
    # data['ReturnPricedItinerary'] = flight[1]
    # data['Pricing'] = flight[2]
    # return data
    data = []  # Создаем список для хранения данных о рейсах
    
    for flight_item in flight:  # Перебираем элементы flight
        flight_data = {}
        
        # Обработка информации о рейсе (OnwardPricedItinerary)
        onward_data = {}
        for element in flight_item.iter():
            onward_data[element.tag] = element.text
        flight_data['OnwardPricedItinerary'] = onward_data

        # Обработка информации о ценах (Pricing)
        flight_data['Pricing'] = flight_item[0]  # Индекс 2 для Pricing
        
        data.append(flight_data)  # Добавляем данные о рейсе в список

    return data