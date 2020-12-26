from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
from pyfiglet import figlet_format
import random

sleep(2)

print("\n\n")
print("\t\t INSTAGRAM BOT\n")
sleep(1)
print("Having Features like :-")
sleep(1)
print("\n -> Create new account (still having bugs)")
sleep(1)
print("\n -> Login")
sleep(1)
print("\n -> Story Viewer")
sleep(1)
print("\n -> DM's")
sleep(1)
print("\n -> Bomber")
sleep(1)
print("\n -> Increase Followers")
sleep(1)
print("\n -> Like, Comment")
sleep(1)
print("\n -> LogOut")
sleep(1)



DEVELOPER = "Nitesh Prajapat"
name = figlet_format(DEVELOPER)
print(f"\n\n\tDeveloped by \n\n{name}")
sleep(2)



chromedriver_path = 'C:/Users/Nitesh Prajapati/Downloads/chromedriver.exe' 
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.maximize_window()
driver.get("https://www.instagram.com")


Choice = int(pyautogui.prompt("1 for Login  2 for Sign up"))


def create_account():
    try:
        driver.get("https://www.instagram.com/accounts/emailsignup/")

        sleep(2)

        EMAIL_MOB = driver.find_element_by_css_selector("#react-root > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(4) > div > label > input")
        FULL_NAME = driver.find_element_by_css_selector("#react-root > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(5) > div > label > input")
        USER_NAME = driver.find_element_by_css_selector("#react-root > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(6) > div > label > input")
        PASS_WORD = driver.find_element_by_css_selector("#react-root > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(7) > div > label > input")


        sleep(2)

        _mob = pyautogui.prompt("Enter Email Address")
        _fullname = pyautogui.prompt("Enter Full Name")
        _username = pyautogui.prompt("Enter User name")
        _password = pyautogui.password("Enter Password")

        sleep(2)

        EMAIL_MOB.send_keys(_mob)
        FULL_NAME.send_keys(_fullname)
        USER_NAME.send_keys(_username)
        PASS_WORD.send_keys(_password)

        sleep(2)


        SIGN_UP_BTN = driver.find_element_by_css_selector("#react-root > section > main > div > div > div:nth-child(1) > div > form > div:nth-child(8) > div > button")
        SIGN_UP_BTN.submit()

        sleep(4)

        # MONTH = driver.find_element_by_css_selector("#react-root > section > main > div > div > div:nth-child(1) > div > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(1) > select")

        month = pyautogui.prompt("Enter month name (First letter should be Capital)")
        sleep(2)

        date = int(pyautogui.prompt("Enter your Birth Date"))
        sleep(2)

        year = int(pyautogui.prompt("Enter Birth Year "))
        sleep(2)



        MONTH = driver.find_element_by_css_selector(f'span[title="{month}"]')
        MONTH.click()

        sleep(4)

        DATE = driver.find_element_by_css_selector(f'span[title={date}]')
        DATE.click()

        sleep(4)

        YEAR = driver.find_element_by_css_selector(f'span[title={year}]')
        YEAR.click()

        sleep(4)

        NEXT_BUTTON = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button")
        NEXT_BUTTON.submit()

        sleep(2)

        confirmation_code = int(pyautogui.prompt("Enter confirmtion code received on your email address (DO IT AS FAST AS YOU CAN)"))

        sleep(30)


        CONFIRMATION_CODE = driver.find_element_by_name("email_confirmation_code")
        CONFIRMATION_CODE.send_keys(confirmation_code)


        NEXT_BUTTON_NEXT = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button")
        NEXT_BUTTON_NEXT.submit()


        TURN_OFF_NOTIFY = driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm")
        TURN_OFF_NOTIFY.click()


    except Exception as ex:
         print(f"Error is ==>>  {ex}")





def login():
    try:
        IG_username = pyautogui.prompt("Enter your Username")
        IG_password = pyautogui.password("Enter your Password")
        sleep(2)

        your_username = driver.find_element_by_name("username")
        your_password = driver.find_element_by_name("password")

        sleep(2)

        your_username.send_keys(IG_username)
        sleep(2)

        your_password.send_keys(IG_password)
        sleep(2)

        LOGIN_btn = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div") 
        LOGIN_btn.submit()
        sleep(5)

        # if not(IG_username == your_username.send_keys(IG_username) or IG_password == your_password.send_keys(IG_password) ):
        #     pyautogui.alert("Username or Password may be incorrect . Please try again!!")
        #     driver.close()
        #     exit()

        # else:
        #     pass

        
        Not_now = driver.find_element_by_xpath('//button[contains(text(), "Not Now")]')   # perfect 
        Not_now.click()

        sleep(5)

        Not_now_again = driver.find_element_by_xpath('//button[contains(text(), "Not Now")]')   # perfect
        Not_now_again.click()

        

        sleep(5)

        # ask for DM's or FOLLOWERS

        EXTRA_CHOICE = int(pyautogui.prompt("Enter 1 for Open Story  2 for Uploading Story  3  for DM's  4  for Increase Followers"))

        #===========================

        def OPEN_STORY():
            STRY = driver.find_element_by_class_name("OE3OK")
            STRY.click()

            sleep(2)

        #===========================

        def UPLOAD_STORY():
            try:
                ADD_btn = driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div/div/div/div[1]/button/div[2]/svg/path")
                ADD_btn.click()
                ADD_btn.send_keys("E:\DESKTOP 1\Thought.jpeg")

                ADD_TO_STRY_btn = driver.find_element_by_class_name("cQjQD")
                ADD_TO_STRY_btn.submit()


            except Exception as err:
                print(f"Error =>> {err}")


        #===========================

        def DM():
            try:

                USERS_TO_SEND_MSG = ['pythoncode.py' , 'dashing_vivek.08']

                sleep(2)

                driver.get("https://www.instagram.com/direct/new/")

                for i in USERS_TO_SEND_MSG:
                    TO = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input")
                    TO.send_keys(i)
                    sleep(4)

                    CHECK_BOX = driver.find_element_by_class_name("dCJp8 ")
                    CHECK_BOX.click()
                    sleep(4)


                    NEXT_BTN = driver.find_element_by_class_name("rIacr")
                    NEXT_BTN.click()
                    sleep(2)

                    MSG_BOX = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")

                    with open("msg.txt", "r") as msg_content :
                        for msges in msg_content:
                            MSG_BOX.send_keys( msges + Keys.ENTER)
                    


                WANT_TO_LOGOUT = pyautogui.prompt("Want to LOG OUT (y/n)")

                if WANT_TO_LOGOUT == "y" :
    
                    Log_out_img = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[5]/span/img")
                    Log_out_img.click()

                    Log_Out = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div")
                    Log_Out.click()
                    pyautogui.alert("You are Logged Out!!")

                    sleep(2)

                    driver.close()
                    exit()


                else:
                    pass

                

            except Exception as exr:
                print(f"Error is ==>> {exr}")


        # =====================



        # ======================

        def INCREASE_FOLLOWERS():

            try:
            
                hashtag_list = ["hacking"]  

                new_followed = []
                prev_user_list = []
                tag = -1
                followed = 0
                likes = 0 
                comments = 0

                for hashtag in hashtag_list:
                    tag += 1

                    driver.get("https://www.instagram.com/explore/tags/" + hashtag_list[tag] +"/")
                    sleep(2)

                    first_post = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]")
                    first_post.click()
                    sleep(2)

                    try:    
                        for i in range(0,100):
                            username = driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[1]/a ")
                            # username.click() 

                            if username not in prev_user_list:
                                if driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button").text == "Follow":
                                
                                    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button").click()

                                    new_followed.append(username)
                                    followed += 1

                                    like_btn = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
                                    like_btn.click()
                                    likes += 1

                                    sleep(10)

                                    comment_probability = random.randint(0,10)  # random no will generate

                                    if comment_probability >= 7:  # if number is greater or equals to 7 then like,share and comment process will run otherwise move to next post 

                                        comments += 1

                                        comment_btn = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button")
                                        comment_btn.click()
                                        comment_box = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")

                                        if comment_probability == 7:
                                            comment_box.send_keys("Nice!!")
                                            sleep(1)

                                        elif comment_probability == 8:
                                            comment_box.send_keys("Amazing!!")
                                            sleep(1)

                                        elif comment_probability == 9:
                                            comment_box.send_keys("Superb!!")
                                            sleep(1)

                                        else:
                                            comment_box.send_keys("MindBlowing!!!")
                                            sleep(1)

                                        comment_box.send_keys(Keys.ENTER)
                                        sleep(2)                          

                                        driver.find_element_by_link_text("Next").click()
                                        sleep(3)


                                    else:
                                        driver.find_element_by_link_text("Next").click()
                                        sleep(3)
                    
                    except:
                        continue

            
            except Exception as erorx:
                print(f"Error is ==>> {erorx}")


        # =================================================================== #

        if EXTRA_CHOICE == 1:
            OPEN_STORY()

        elif EXTRA_CHOICE == 2:
            UPLOAD_STORY()

        elif EXTRA_CHOICE == 3:
            DM()
    
        elif EXTRA_CHOICE == 4:
            INCREASE_FOLLOWERS()
        
        else:
            pass

    except Exception as e:
        print(f"Error is == >> {e}")



 
if __name__ == '__main__':
        
    if Choice == 1:
        login()

    elif Choice == 2:
        create_account()
    else:
        pass