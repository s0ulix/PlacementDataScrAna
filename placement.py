from selenium import webdriver
import time
import pandas as pd


user="Enter your username here"
pwd="Enter your password here"

driver = webdriver.Chrome('C:\\webdriver\\chromedriver.exe')
driver.get('https://ums.lpu.in/Placements/')
username = driver.find_element_by_name("txtUserName")
username.clear()
username.send_keys(user)
password = driver.find_element_by_name("txtPassword")
password.clear()
password.send_keys(pwd)
driver.find_element_by_name("Button1").click()
driver.get('https://ums.lpu.in/Placements/frmPlacementDriveRegistration.aspx')
cmp=[]
gen=[]
deg=[]
ele=[]
ctc=[]
def fun(var1,var2):
    try:

        for i in range(var1,var2):
            print(i)
            try:
                driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gdvPlacement"]/tbody/tr[52]/td/table/tbody/tr/td['+str(i)+']/a').click()
            except:
                pass
            for j in range(2,52):
                print(i,j)
                a=driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_gdvPlacement"]/tbody/tr['+str(j)+']/td[5]')
                if('CSE/IT' in a.text):
                    driver.find_element_by_id("ctl00_ContentPlaceHolder1_gdvPlacement_ctl"+str("{:02d}".format(j))+"_hypJobProfile").click()
                    time.sleep(2)
                    driver.switch_to.window(driver.window_handles[1])
                    cmp.append(driver.find_element_by_xpath('//*[@id="tblEmailData"]/table[1]/tbody/tr[4]/td[2]').text)
                    deg.append(driver.find_element_by_xpath('//*[@id="tblEmailData"]/table[1]/tbody/tr[6]/td/table/tbody/tr[2]/td[2]').text)
                    ele.append(driver.find_element_by_xpath('//*[@id="tblEmailData"]/table[1]/tbody/tr[6]/td/table/tbody/tr[2]/td[3]').text)
                    ctc.append(driver.find_element_by_xpath('//*[@id="tblEmailData"]/table[1]/tbody/tr[6]/td/table/tbody/tr[2]/td[4]').text)
                    try:
                        gen.append(driver.find_element_by_xpath('//*[@id="tblEmailData"]/table[1]/tbody/tr[13]/td[2]').text)
                    except:
                        pass
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

        print('done')
    except:
        print('some error occured')
fun(1,12)
fun(3,13)
fun(3,13)
fun(3,13)
df=pd.DataFrame(list(zip(cmp,deg,ele,ctc )),columns =['Company', 'Designation','Eligibility','CTC'])
df.to_csv('placement3.csv')

