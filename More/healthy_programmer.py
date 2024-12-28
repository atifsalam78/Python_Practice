from datetime import datetime
import time
alarm_set_water = int(input("Water minutes: "))
alarm_set_walk = int(input("Walk minutes: "))
alarm_set_eye = int(input("Eye minutes: "))

while True:
    set_alarm = datetime.now()
    showClock = "%s:%s:%s" % (set_alarm.hour, set_alarm.minute, set_alarm.second)
    print("\r", showClock, end="")
    time.sleep(1)
    if set_alarm.minute == alarm_set_water and set_alarm.second < 1:
        print("\n Water Time")
        water_msg = input("Water: \n")
        if water_msg == "drunk":
            print("Water Drunk")

    elif set_alarm.minute == alarm_set_walk and set_alarm.second < 1:
        print("\n Walk Time")
        water_msg = input("Walk: \n")
        if water_msg == "walk":
            print("Walked")

    elif set_alarm.minute == alarm_set_eye and set_alarm.second < 1:
        print("\n Eye Time")
        water_msg = input("Eye: \n")
        if water_msg == "yes":
            print("Eye Relaxed")
    if set_alarm.hour == 11 and set_alarm == 6:
        print("Good Bye see you ")
        break
