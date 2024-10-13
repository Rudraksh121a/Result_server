from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import requests
import os
import pandas as pd
import re
from io import StringIO
from selenium.webdriver.common.keys import Keys
from ocr import get_text_captcha



def scrap(enrollment:str,sem:str)->dict:
        

        
        if len(enrollment)==12:
            try:



                if int(sem) > 8:
                    return "enter valid sem"



                chrome_options = Options()
                chrome_options.add_argument("--headless")  
                chrome_options.add_argument("--disable-gpu") 
                chrome_options.add_argument("--no-sandbox")  

                web = webdriver.Chrome(options=chrome_options)
                # web = webdriver.Chrome()
                web.get('http://result.rgpv.ac.in/Result/ProgramSelect.aspx')
                radio_button=web.find_element(By.ID,'radlstProgram_1')
                radio_button.click()
                sleep(1)

                nexturl=web.current_url

                


                web.get(nexturl)
                time.sleep(1)
                
                


                roll_number = enrollment
                name_field = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_txtrollno"]')
                name_field.send_keys(roll_number)
                check_sem=(int(sem)-1)
                str(check_sem)
                sem_dropdown = Select(web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_drpSemester"]'))
                sem_dropdown.select_by_index(check_sem)

                captcha_img=web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_pnlCaptcha"]/table/tbody/tr[1]/td/div/img')
                time.sleep(1)
                captcha_link=captcha_img.get_attribute("src")
               


                result_captcha=get_text_captcha(captcha_link)
                
               
         
            
                captcha_field = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_TextBox1"]')
                captcha_field.send_keys(result_captcha)

                
               
      


                submit_button = web.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_btnviewresult"]')
                submit_button.click()
                time.sleep(2)
                try:

                    if web.switch_to.alert:
                        if web.switch_to.alert.text=="Result for this Enrollment No. not Found":
                            return "Result not found"
                        return "try again"
                        
                except Exception as e:
               
                    sgpa = web.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblSGPA").text
              
                    
                            
                    cgpa = web.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblcgpa").text
                        
                    result = web.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblResultNewGrading").text
                        
                    name = web.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblNameGrading").text
                    enroll = web.find_element(By.ID, "ctl00_ContentPlaceHolder1_lblRollNoGrading").text

                    data_dict_1 = {
                        
                            "Name": name,
                            "Enrollment Number": enroll
                        }

                    table=web.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_pnlGrading"]/table/tbody/tr[3]').text

                    data_io = StringIO(table)

                    df = pd.read_csv(data_io, delim_whitespace=True)

                    Subject_list = df['Subject'] + " " + df['Total'].astype(str)

                    Subject_list = Subject_list.tolist()

                    grade = df['Credit.1'].tolist()


                    data_dict_2 = {}


                    for i in range(len(Subject_list)):
                        data_dict_2[Subject_list[i]] = grade[i]
                        
                    data_dict_3={
                        "SGPA": sgpa,
                        "CGPA": cgpa,
                        "Result": result
                      }

    
                    return data_dict_1,data_dict_2,data_dict_3
                        
                        
                
            except Exception as e:
                return "try again"
            
        else: return "invalid enrollment"

def main():
    print(scrap("0403AL221026","4"))

if __name__=="__main__":
    main()