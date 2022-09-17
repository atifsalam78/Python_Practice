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
    act_now = datetime.now(pkt_khi)
    with open("activity.txt", "a") as log_file:
        log_file.write(f"{user_name} {msg_print} on {act_now.strftime(fmt)} \n")


def sound_activity(sound_file):
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    from pygame import mixer
    mixer.init()
    mixer.music.load(sound_file)
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)


def user_input():
    import string
    msg = ""
    while msg.strip(f"{string.punctuation} {string.digits}") != "done":
        msg = input(f"""Write "done" if you had :""")


while True:
    now = datetime.now()
    showClock = "%s:%s:%s" % (now.hour, now.minute, now.second)
    print("\r", showClock, end="")
    time.sleep(1)

    if now.minute == alarm_set_water and now.second < 1:
        print("\nWater Time")
        act_sound = "water.mp3"
        sound_activity(act_sound)
        user_input()
        msg_print = "drunk water"
        print(f"Great you {msg_print}")
        activity()

    elif now.minute == alarm_set_walk and now.second < 1:
        print("\nPhysical Time")
        act_sound = "physical.mp3"
        sound_activity(act_sound)
        user_input()
        msg_print = "walked"
        print(f"Great you {msg_print}")
        activity()

    elif now.minute == alarm_set_eye and now.second < 1:
        print("\nEye Time")
        act_sound = "eyes.mp3"
        sound_activity(act_sound)
        user_input()
        msg_print = "eyes are relaxed"
        print(f"Great your {msg_print}")
        activity()

    if now.hour == 17:
        print("Thanks for your contribution")
        break
