import pyautogui
import time
import random
import pyperclip

person = "윤대호이"
personList = person.split(", ")
massage = "happynewyear!"

pyautogui.click(666, 1068) #click friend
pyautogui.click(945, 1068) #click search

for i in range(len(personList)):
    time_wait = random.uniform(2, 4)
    print(f"{personList[i]} 에게 메세지를 보낸당")

    pyperclip.copy(personList[i]) #보낼사람 입력
    pyautogui.hotkey("ctrl", "v")    
    pyautogui.keyDown("down")#한칸 밑으로

    pyautogui.keyDown("enter") #첫번째 사람 창열기
    pyperclip.copy(massage) #내용입력
    pyautogui.hotkey("ctrl", "v")     
    time.sleep(time_wait)

    pyautogui.keyDown("enter") #보내기
    pyautogui.keyDown("esc") #창닫기
    time.sleep(1)

    print(f"{personList[i]} 메세지 전송 완료 ", time_wait)
    pyautogui.click(760, 1119, clicks=2)
    pyautogui.keyDown("delete")
print("모두에게 메세지 전송 완료")



