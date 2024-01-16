import json

def add_event(day, time, startTime, endTime, eventName):
    with open('cally.json') as schedule_file:
        schedule = json.load(schedule_file)
    #Check if schedule is empty
    if len(schedule[day]) == 0:
        schedule[day].append({"time": time, "startTime": startTime, "endTime": endTime, "eventName": eventName})
        with open('cally.json', 'w') as schedule_file:
            schedule_file.write("")
        with open('cally.json', "a") as schedule_file:
            json.dump(schedule, schedule_file)
        print("Event has been added to your calendar")
    
    #if schedule is not empty
    else:
        isHandled = False
        #Check for double-booking
        for event in schedule[day]:
            if (event["startTime"] == startTime) or (event["endTime"] == endTime) or (startTime > event["startTime"] and startTime < event["endTime"]) or (event["startTime"] > startTime and event["startTime"] < endTime):
               
                print("It seems that you have double-booked your schedule")
                print("You already have a "+event["eventName"]+" at "+event["time"])
                decision = input("Do you still want to add this event? ").upper()
                if decision == "NO":
                    isHandled = True
                    print("Event has not been added to your calendar")
                    break
                else:
                    isHandled = True
                
                    for index in range(schedule[day].index(event), len(schedule[day])):
                        if index == len(schedule[day])-1:
                            if schedule[day][index]["startTime"] > startTime:
                                schedule[day].insert(index, {"time": time, "startTime": startTime, "endTime": endTime, "eventName": eventName})
                            else:
                                schedule[day].insert(index+1, {"time": time, "startTime": startTime, "endTime": endTime, "eventName": eventName})
                            
                        elif schedule[day][index]["startTime"] < startTime and startTime < schedule[day][index+1]["startTime"]:
                            schedule[day].insert(index+1, {"time": time, "startTime": startTime, "endTime": endTime, "eventName": eventName})
                            break
                        elif startTime < schedule[day][index]["startTime"]:
                            if index == 0:
                                schedule[day].insert(0, {"time": time, "startTime": startTime, "endTime": endTime, "eventName": eventName})
                                break
                            elif startTime > schedule[day][index-1]["endTime"]:
                                schedule[day].insert(index, {"time": time, "startTime": startTime, "endTime": endTime, "eventName": eventName})
                                break
                    break
                    
        #Add event in appropriate chronic order if there is no schedule conflict
        if isHandled == False:
            for event in schedule[day]:
                if startTime < event["startTime"]:
                    insert_index = schedule[day].index(event) 
                    break
                elif event == schedule[day][-1]:
                    insert_index = len(schedule[day])
            
            schedule[day].insert(insert_index, {"time": time, "startTime": startTime, "endTime": endTime, "eventName": eventName})

        with open('cally.json', 'w') as schedule_file:
            schedule_file.write("")
        with open('cally.json', "a") as schedule_file:
            json.dump(schedule, schedule_file)
        print("Event has been added to your calendar")
  
def delete_event(day, time, eventName):
    
    with open('cally.json') as schedule_file:
        schedule = json.load(schedule_file)
    isHandled = False
    for event in schedule[day]:
        if event['time'] == time and event['eventName'] == eventName:
            isHandled = True
            schedule[day].remove(event)
            break
    if isHandled:
        with open('cally.json', 'w') as schedule_file:
            schedule_file.write("")
        with open('cally.json', "a") as schedule_file:
            json.dump(schedule, schedule_file)
        print("Event has been removed from your calendar")
    else:
        print("Error! Please double check your event details. Make sure you input the correct event name and time")

def edit_event(originalDay, originalTime, originalEventName, newDay, newTime, startTime, endTime, newEventName):
    with open('cally.json') as schedule_file:
        schedule = json.load(schedule_file)
    error = True
    for e in schedule[originalDay]:
        if e["eventName"] == originalEventName and e["time"] == originalTime:
            error = False
    if error:
        print("Error! Event does not exist. Please double check your event details. Make sure you input the correct event name and time")
        
    else:
    
        if len(schedule[newDay]) == 0:
            #remove original event
            
            for deletedEvent in schedule[originalDay]:
                if deletedEvent["time"] == originalTime and deletedEvent["eventName"] == originalEventName:
                    schedule[originalDay].remove(deletedEvent)
                    break
        
            schedule[newDay].append({"time": newTime, "startTime": startTime, "endTime": endTime, "eventName": newEventName})
            with open('cally.json', 'w') as schedule_file:
                schedule_file.write("")
            with open('cally.json', "a") as schedule_file:
                json.dump(schedule, schedule_file)
            print("Event has been edited successfully")
        
        #if schedule is not empty
        else:
            isHandled = False
            #Check for double-booking
            for event in schedule[newDay]:
                if (event["startTime"] == startTime) or (event["endTime"] == endTime) or (startTime > event["startTime"] and startTime < event["endTime"]) or (event["startTime"] > startTime and event["startTime"] < endTime):
                
                    print("It seems that you have double-booked your schedule")
                    print("You already have a "+event["eventName"]+" at "+event["time"])
                    decision = input("Do you still want to add this event? ").upper()
                    if decision == "NO":
                        isHandled = True
                        print("Event has not been edited")
                        break
                    else:
                        isHandled = True
                        #remove original event
                        
                        for deletedEvent in schedule[originalDay]:
                            
                            if deletedEvent["time"] == originalTime and deletedEvent["eventName"] == originalEventName:
                                schedule[originalDay].remove(deletedEvent)
                                break
                       

                        for index in range(schedule[newDay].index(event), len(schedule[newDay])):
                            if index == len(schedule[newDay])-1:
                                if schedule[newDay][index]["startTime"] > startTime:
                                    schedule[newDay].insert(index, {"time": time, "startTime": startTime, "endTime": endTime, "eventName": newEventName})
                                else:    
                                    schedule[newDay].insert(index+1, {"time": newTime, "startTime": startTime, "endTime": endTime, "eventName": newEventName})
                                
                            elif schedule[newDay][index]["startTime"] < startTime and startTime < schedule[newDay][index+1]["startTime"]:
                                schedule[newDay].insert(index+1, {"time": newTime, "startTime": startTime, "endTime": endTime, "eventName": newEventName})
                                break
                            elif startTime < schedule[newDay][index]["startTime"]:
                                if index == 0:
                                    schedule[newDay].insert(0, {"time": newTime, "startTime": startTime, "endTime": endTime, "eventName": newEventName})
                                    break
                                elif startTime > schedule[newDay][index-1]["startTime"]:
                                    schedule[newDay].insert(index, {"time": newTime, "startTime": startTime, "endTime": endTime, "eventName": newEventName})
                                    break
                        print("Event has been edited successfully")
                        break
                        
            #Add event in appropriate chronic order if there is no schedule conflict
            if isHandled == False:
                #remove original event
                for event in schedule[originalDay]:
                            if event["time"] == originalTime and event["eventName"] == originalEventName:
                                schedule[originalDay].remove(event)
                                break
                for event in schedule[newDay]:
                    if startTime < event["startTime"]:
                        insert_index = schedule[newDay].index(event) 
                        break
                    elif event == schedule[newDay][-1]:
                        insert_index = len(schedule[newDay])
                
                schedule[newDay].insert(insert_index, {"time": newTime, "startTime": startTime, "endTime": endTime, "eventName": newEventName})
                print("Event has been edited successfully")

            with open('cally.json', 'w') as schedule_file:
                    schedule_file.write("")
            with open('cally.json', "a") as schedule_file:
                    json.dump(schedule, schedule_file)
    
def show_calendar(choice):
    with open('cally.json') as schedule_file:
            schedule = json.load(schedule_file)
    
    if choice != "THE WHOLE WEEK":
        print(choice)
        print("----------------------------------")
        if len(schedule[choice]) == 0:
                print("Avaialble all day")
                print("\n")
        else:
            for event in schedule[choice]:
                    print("Event: " + event["eventName"])
                    print("Time: " + event["time"])
                    print("\n")
    else:
        for day in daysInTheWeek:
            show_calendar(day)

def clear_calendar(choice, period):
    with open('cally.json') as schedule_file:
            schedule = json.load(schedule_file)
        
    if choice != "THE WHOLE WEEK":
        if period == "THE WHOLE DAY":
            schedule[choice] = []
        else:

            if len(schedule[choice]) > 0:
                isHandled = False
                for event in schedule[choice]:
                   
                    if event["startTime"] >= 1200:
                        isHandled = True
                        if period == "MORNING":
                            schedule[choice] = schedule[choice][schedule[choice].index(event):]
                        else:
                            schedule[choice] = schedule[choice][:schedule[choice].index(event)]
                        break
                if not isHandled and period == "MORNING":
                    schedule[choice] = []


        with open('cally.json', 'w') as schedule_file:
            schedule_file.write("")
        with open('cally.json', "a") as schedule_file:
            json.dump(schedule, schedule_file)
    else:
        for day in daysInTheWeek:
            clear_calendar(day, period)

def show_availability(choice):
    availability = []
    with open('cally.json') as schedule_file:
            schedule = json.load(schedule_file)
    if choice != "THE WHOLE WEEK":
        if not schedule[choice]:
            availability.append("Available all day")
        else:
            isHandled = False
            startTimeList = []
            endTimeList = []
            for event in schedule[choice]:
                startTimeList.append(event["startTime"])
                endTimeList.append(event["endTime"])
            availability.append("12:00am to "+time_converter_to_string(startTimeList[0]))
            index_endTime = 0
            index_startTime = 0
            while index_endTime < len(endTimeList):
                freeTimeStart = endTimeList[index_endTime]
                freeTimeEnd = startTimeList[index_startTime]
                while freeTimeStart >= freeTimeEnd:
                    index_startTime += 1
                    if index_startTime == len(startTimeList):
                        freeTimeStart = max(endTimeList)
                        freeTimeEnd = 2359
                        isHandled = True
                        break
                    else:
                        freeTimeEnd = startTimeList[index_startTime]
                availability.append(time_converter_to_string(freeTimeStart)+" to "+time_converter_to_string(freeTimeEnd))
                if isHandled:
                    break
                else:
                    index_endTime = startTimeList.index(freeTimeEnd)
        availability.append("")
        print("YOUR AVAILABILITIES ON "+choice+" ARE:")
        for timeslot in availability: 
            print(timeslot)
    else:
        for day in daysInTheWeek:
            show_availability(day)

def time_converter_to_string(time):
    if time < 1200:
        tail = "am"
        if time < 60:
            if time < 10:
                time = "12:0"+str(time)+tail
            else:
                time = "12:"+str(time)+tail
        else:
            time = str(time)[:-2]+":"+str(time)[-2:]+tail
    else:
        tail = "pm"
        time = time-1200
        if time == 0:
            time = 1200
        elif time > 0 :
            if time < 10:
                time = int("120"+str(time))
            elif time < 60:
                time = int("12"+str(time))
        time = str(time)[:-2]+":"+str(time)[-2:]+tail
    
    return time
        
def time_converter_to_int(time):
    for i in range(len(time)):
            if time[i] == "a":
              
                time = time[:i]
                if ("12" in time):
                    time = "00"+time[2:]
                   
                if len(time) == 1 or len(time) == 2:
                    
                    time = int(time+"00")
                else:
                    time = int(time)
                break

            elif time[i] == "p":
                time = time[:i]
                if time == "12":
                    time = "0"
                if len(time) == 1 or len(time) == 2:
                    time = int(str(int(time)+12)+"00")
                else:
                    time = int(str(int(time[0:len(time)-2])+12)+time[len(time)-2:])
            
                break
   
    return time

def has_number(time):
    return any(char.isdigit() for char in time)
    


def has_tail(time):
    return "m" in time and ("a" in time or "p" in time)
        
def get_time_input():
    time = input("Please note that end time cannot be earlier than start time. Specify start time and end time like this example format: 9am to 10am. Time of event? ")
    while "to" not in time:
        time = input("Please include \"to\" between start time and end time in your input. Time of event? ")
    timeList = time.split('to')
    startTime = timeList[0].strip().replace(" ","")
    endTime = timeList[1].strip().replace(" ","")
    if has_number(startTime) and has_number(endTime) and has_tail(startTime) and has_tail(endTime) and time_converter_to_int(startTime) < time_converter_to_int(endTime):
        startTime = time_converter_to_int(startTime)
        endTime = time_converter_to_int(endTime)
        time = time_converter_to_string(startTime)+" to "+time_converter_to_string(endTime)
        return [time, startTime, endTime]
    else:
        get_time_input()


    

daysInTheWeek = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print("Hi, I'm Cally, the only Secreatary you need for your calendar")
running = True
while running:
    request = input("Please enter your request: ").upper().strip()

    if "CLOSE" in request:
        running = False

    elif "ADD" in request and "EVENT" in request:
        day = input("On which day? ").upper()
        while day not in daysInTheWeek:
            day = input("Could you please tell me the day of the event again? ").upper()
        time = get_time_input()
        
        eventName = input("Name of event? ")    
        print("Adding that event to your calendar...")
        add_event(day, time[0], time[1], time[2], eventName)

    elif "DELETE" in request and "EVENT" in request:
        day = input("On which day? ").upper()
        while day not in daysInTheWeek:
            day = input("Could you please tell me the day of the event again? ").upper()
        time = get_time_input()
        
        eventName = input("Name of event? ")
        print("Removing that event from your calendar...")
        delete_event(day, time[0], eventName)

    elif "EDIT" in request and "EVENT" in request:
        originalEventName = input("Original name of event? ")
        print("Original time of event?")
        originalTime = get_time_input()
        originalDay = input("Original day of event? ").upper()
        while originalDay not in daysInTheWeek:
            originalDay = input("Could you please tell me the day of the event again? ").upper()
        
        newEventName = input("Is the name of the new event same as the original? (Press \"y\" or \"n\") ").lower()
        while newEventName != "y" and newEventName != "n":
            newEventName = input("Is the name of the new event same as the original? (Press \"y\" or \"n\") ").lower()
        if newEventName == "y":
            newEventName = originalEventName
        else:
            newEventName = input("Name of new event? ")

        newTime = input("Is the time of the new event the same as the original? (Press \"y\" or \"n\") ").lower()
        while newTime != "y" and newTime != "n":
            newTime = input("Is the time of the new event the same as the original? (Press \"y\" or \"n\") ").lower()
        if newTime == "y":
            newTime = originalTime
        else:
            newTime = get_time_input()
        
        newDay = input("Is the day of the new event the same as the original? (Press \"y\" or \"n\") ").lower()
        while newDay != "y" and newDay != "n":
            newDay = input("Is the day of the new event the same as the original? (Press \"y\" or \"n\") ").lower()
        if newDay == "y":
            newDay = originalDay
        else:
            newDay = input("Day of the new event? ").upper()
            while newDay not in daysInTheWeek:
                newDay = input("Could you please tell me the day of the event again? ").upper()
        print("Editing the event...")
        edit_event(originalDay, originalTime[0], originalEventName, newDay, newTime[0], newTime[1], newTime[2], newEventName)

    elif "SHOW" in request and "CALENDAR" in request:
        choice = input("Please specify a day or say the whole week: ").upper()
        while choice not in daysInTheWeek and choice != "THE WHOLE WEEK":
                choice = input("Could you please tell me the day of the event again? ").upper()
        show_calendar(choice)
    
    elif "CLEAR" in request and "CALENDAR" in request:
        choice = input("Please specify a day or say the whole week: ").upper()
        while choice not in daysInTheWeek and choice != "THE WHOLE WEEK":
                choice = input("Could you please tell me the day of the event again? ").upper()
        period = input("Do you want to clear your schedule for the morning or the afternoon or the whole day? ").upper()
        while period != "MORNING" and period != "AFTERNOON" and period != "THE WHOLE DAY":
                period = input("Please say one of the three following: \"MORNING\" or \"AFTERNOON\" or \"THE WHOLE DAY\" ").upper()
        clear_calendar(choice, period)
        print("Your calendar has been updated successfully")
    
    elif "SHOW" in request and "AVAILABILITY" in request:
        choice = input("Please specify a day or say the whole week: ").upper()
        show_availability(choice)

    
    else:
        print("I'm sorry, I don't recognize that command. Please try the following commands:")
        print("ADD EVENT")
        print("EDIT EVENT")
        print("DELETE EVENT")
        print("SHOW CALENDAR")
        print("CLEAR CALENDAR")
        print("SHOW AVAILABILITY")




