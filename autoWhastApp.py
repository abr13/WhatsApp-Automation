from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

brwsr=webdriver.Chrome()

brwsr.maximize_window()
brwsr.get("https://web.whatsapp.com/")

print("Please scan the QR code in browser in 20 seconds to proceed, waiting...")
sleep(20)

active=0
while active==0:
    print("Enter the message: ")
    msg = input()
    print("Enter the no. of contacts/groups in total : ")
    n=int(input())
    print("Enter the contact/group names, separated by spaces : ")
    toWhom=[]
    for i in range(0,n):
        print("",i,": ")
        toWhom.append(input())

    for j in range(0,n):
        target = '"' + toWhom[j] + '"'

        brwsr.find_element_by_xpath('//*[@title='+target+']').click()
        sleep(1)
        message = brwsr.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
        message.send_keys(msg + Keys.RETURN)
        print("Sent to "+target)
    print("Do you want to continue? YES:'0'  NO:'1'")
    active=int(input())

