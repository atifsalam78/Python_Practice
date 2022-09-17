from datetime import datetime
import time
import pytz
user_name = input("Your good name please: ")
while True:
    try:
        alarm_set_water = int(input(f"{user_name} set minutes for today's water break(1-59): "))
        if alarm_set_water not in range(1, 60):
            raise ValueError
            
        alarm_set_walk = int(input(f"{user_name} set minutes for today's physical activity(1-59): "))
        if alarm_set_walk not in range(1, 60):
            raise ValueError
            
        alarm_set_eye = int(input(f"{user_name} set minutes for today's eye relaxing activity(1-59): "))
        if alarm_set_eye not in range(1, 60):
            raise ValueError
        break
    except ValueError:
        print("Only numbers with in range 1-59")


def activity():
    pkt_khi = pytz.timezone("Asia/Karachi")
    fmt = "%d-%m-%Y %H:%M:%S %Z%z"
    now = datetime.now(pkt_khi)
    with open("activity.txt", "a") as log_file:
        log_file.write(f"{user_name} {msg_print} on {now.strftime(fmt)} \n")
        log_file.write("*************************************************\n")


def sound_activity(act_sound):
    import time
    from pygame import mixer
    mixer.init()
    mixer.music.load(act_sound)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)


def user_input():
    import string
    global msg_print
    msg = ""
    while msg.strip(f"{string.punctuation} {string.digits}") != "done":
        msg = input("""Write "done" :""")


while True:
    now = datetime.now()
    showClock = "%s:%s:%s" % (now.hour, now.minute, now.second)
    print("\r", showClock, end="")
    time.sleep(1)

    if now.minute == alarm_set_water and now.second < 1:
        print("\nWater Time \n")
        act_sound = "water.mp3"
        sound_activity(act_sound)
        user_input()
        msg_print = "Drunk Water"
        print(msg_print)
        activity()

    elif now.minute == alarm_set_walk and now.second < 1:
        print("\nPhysical Time")
        act_sound = "physical.mp3"
        sound_activity(act_sound)
        user_input()
        msg_print = "Walked"
        print(msg_print)
        activity()

    elif now.minute == alarm_set_eye and now.second < 1:
        print("\nEye Time")
        act_sound = "eyes.mp3"
        sound_activity(act_sound)
        user_input()
        msg_print = "Relaxed Eyes"
        print(msg_print)
        activity()

    # if now.hour == 17 and now.minute == 30:
    #     print("Thanks for your contribution")
    # with open("activity.txt") as log_file:
    #     for lines in log_file.readlines():
    #         print(lines, end="")
    # break



