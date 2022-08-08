import webbrowser, time
import pyautogui as pag
import schedule

def meeting_join():
    url = "https://meet.google.com/izx-goag-dxy?authuser=1"

    webbrowser.open(url)

    time.sleep(10)

    pag.hotkey('command','d')
    # time.sleep(3)
    pag.hotkey('command','e')

    time.sleep(3)

    for i in range(6):
        pag.press('tab')

    time.sleep(2)
    pag.press('enter')

    print('Press (Ctrl+c) to exit the program ')
    time.sleep(2)

def comment(name,regNo,classSec):
    # time.sleep(1)
    # pag.moveTo(3585, 323)
    # pag.click()
    # time.sleep(1)

    # for i in range(5):
    #     pag.press('tab')
    for i in range(2):
        pag.press('tab')
    pag.press('enter')

    time.sleep(3)

    pag.write(name, interval=0.1)
    time.sleep(0.5)
    pag.hotkey('shift','enter')
    pag.write(regNo, interval=0.1)
    time.sleep(0.5)
    pag.hotkey('shift','enter')
    pag.write(classSec, interval=0.1)
    pag.press('enter')

def mainFunc():
    meeting_join()
    # print('start timer')
    # time.sleep(1)
    # print('timer endresna1s')
    name = "Vannes"
    regNo = "12a6 / 28"
    classSec = "hadir"
    comment(name,regNo,classSec)
    time.sleep(5)
    pag.hotkey('command','w')
    print('Meeting ended')

mainFunc()

# if __name__ == "main":
# #     # Schedule it to the time given
#     meet_join_time = "02:46"
#     schedule.every().day.at("%s"%meet_join_time).do(mainFunc)
#     print("Scheduling meeting at ",meet_join_time)
# # mainFunc()

#     while True: 
#     # Check whether any scheduled task is pending to run or not
#         schedule.run_pending() 
#         time.sleep(1)