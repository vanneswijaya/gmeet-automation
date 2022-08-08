import webbrowser, time
import pyautogui as pag
import schedule
from datetime import datetime
import random



def meeting_join():
    # url = "https://meet.google.com/ikg-yjww-qwj?authuser=1"
    # url = "https://meet.google.com/lookup/bhgesmhrjl?authuser=1"
    url = "https://meet.google.com/vmq-oihd-qvq"

    webbrowser.open(url)

    time.sleep(8)

    pag.hotkey('ctrl','d')
    time.sleep(5)
    pag.hotkey('ctrl','e')

    time.sleep(5)

    for i in range(2):
        pag.press('tab')
        time.sleep(2)

    time.sleep(2)
    pag.press('enter')

    # print("Session has started and will continue for %s mi            
    # nutes"%meeting_time)
    print('Press (Ctrl+c) to exit the program ')
    time.sleep(5)

def comment(name,regNo,classSec):
    # time.sleep(1)
    # pag.moveTo(3585, 323)
    # pag.click()
    # time.sleep(1)

    # for i in range(5):
    #     pag.press('tab')
    for i in range(2):
        pag.press('tab')
        time.sleep(2)
    pag.press('enter')

    time.sleep(1)

    pag.write(name, interval=0.1)
    time.sleep(0.5)
    pag.hotkey('shift','enter')
    pag.write(regNo, interval=0.1)
    time.sleep(0.5)
    pag.hotkey('shift','enter')
    pag.write(classSec, interval=0.1)
    pag.press('enter')
    time.sleep(1)
    # pag.press('print')

def get_time():
    time = 57
    # time += random.randint(0,25)
    return f'00:{time}'


# Where the wizards work
def mainFunc():
    meeting_join()
    # print('start timer')
    # time.sleep(1)
    # print('timer endresna1s')
    name = "Vannes Wijaya"
    regNo = "12a6 / 28"
    classSec = "hadir"
    comment(name,regNo,classSec)
    screenshot()
    time.sleep(10)
    pag.hotkey('ctrl','w')
    print('Meeting ended')

def screenshot():
    print('scrc')
    im1 = pag.screenshot()
    now = datetime.now()
    filename = (now.strftime("%Y-%m-%d-%H-%M-%S"))
    im1.save(f"~\Documents\screenshots\{filename}.png")
    print(f"Images saved at -> ~\Documents\screenshots\{filename}.png")
    


if __name__ == "__main__":
    # mainFunc()
    
    meet_join_time = get_time()
    schedule.every().day.at("%s"%meet_join_time).do(mainFunc)
    print("Scheduling meeting at ",meet_join_time)

    while True: 
    # Check whether any scheduled task is pending to run or not
        schedule.run_pending() 
        time.sleep(1) 
