import mysql.connector

mydb = mysql.connector.connect(
  host="198.244.148.241",
  user="gholipour",
  password="Wee%159159$125",

)

print(mydb)
mycursor= mydb.cursor()

mycursor.execute(""" SELECT user_agent, software , simple_sub_description_string FROM test.whatismybrowser_useragent where operating_system_name like "Windows 1%" or
                 operating_system_name like "Windows 8%" or
                 operating_system_name like "Linux %" limit 50000 """ )

myresult = mycursor.fetchall()

with open('user1.txt', 'w') as file:
    # Define a list of lines to write to the file
    # Use a for loop to iterate over the lines and write them to the file
    for line in myresult:
        file.write(str(line) +'\n')

print('Lines written to file successfully!')

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import random

# with open('./user.txt', 'r') as file:
#   lines = file.readlines()
#   random_line = random.choice(lines)

#             # Print the randomly chosen line
# print('Randomly chosen line:', random_line)

# def my_driver():
#     option = Options()
#     option.add_argument('--disable-infobars')
#     option.add_argument("start-maximized")
#     option.add_argument("--disable-extensions")
#     option.add_argument(f"--user-agent={random_line}")	
#     option.add_experimental_option("prefs", {
# 		"profile.default_content_setting_values.notifications": 1})
#     path = rf"./youtubeviewer\chromedriver.exe"
#     my_webdriver = webdriver.Chrome(executable_path=path ,options=option)
#     print('Driver connected')
#     return my_webdriver

# driver  = my_driver()
# driver.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
