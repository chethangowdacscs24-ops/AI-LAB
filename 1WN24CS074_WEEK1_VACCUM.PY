def vaccum_cleaning_agent(loc,status):
    if status=="dirty":
         print("clean the room(pick the dust)")
    elif loc=="A":
        print("move right")
    elif loc=="B":
        print("move left")
loc =input("Enter current(room) location")
status = input("enter wheather the room is clean or dirty")
vaccum_cleaning_agent(loc,status) 