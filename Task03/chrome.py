from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
chromedriver_path = 'C:\driver\chromedriver-win64\chromedriver.exe'
service = ChromeService(executable_path=chromedriver_path)
driver=webdriver.Chrome(service=service)

# Вход на сайт sdo.evolenta.ru
try:

    driver.get("https://sdo.evolenta.ru/login/index.php")
    driver.maximize_window()
except:
    print("Error")
else:
    print("Ok")


# Ввод логина и пароля
try:
    driver.find_element(By.ID, 'username').send_keys("d.bikmurzin")
    driver.find_element(By.ID, 'password').send_keys("********")# Пароль закрыт из-за конфиденциальности
    time.sleep(1)
    driver.find_element(By.ID, 'loginbtn').click()
    time.sleep(1)
except:
    print("Error")
else:
    print("Ok")

try:
    # Открытие меню пользователя
    driver.find_element(By.ID, 'usermenu').click()
    time.sleep(1)

    # Переход в раздел "События"
    driver.find_element(By.XPATH, '//*[@id="usermenu-dropdown"]/a[12]').click()
    time.sleep(1)

    # Создание нового события
    driver.find_element(By.CSS_SELECTOR, "button[data-action='new-event-button']").click()
    time.sleep(2)

    # Ввод названия события
    driver.find_element(By.ID, 'id_name').send_keys("Урок 1")
    time.sleep(2)

    # Сохранение нового события
    driver.find_element(By.CSS_SELECTOR, 'button[data-action="save"]').click()
    time.sleep(2)
except:
    print("Error")
else:
    print("Ok")

try:
# Удаление созданного события
    driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div[2]/section/div/div/div[1]/div/div[2]/div/div/div/div[1]/div[1]/a[1]/i')
    time.sleep(2)
except:
    print("Error")
else:
    print("Ok")

try:
    # Создание нового события
    driver.find_element(By.CSS_SELECTOR, "button[data-action='new-event-button']").click()
    time.sleep(2)

    # Сохранение нового события без названия
    driver.find_element(By.CSS_SELECTOR, 'button[data-action="save"]').click()
    time.sleep(2)


    # Закрытие окна создания события
    driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[1]/button/i').click()
    time.sleep(2)
except:
    print("Error")
else:
    print("Ok")

# Открытие меню пользователя
driver.find_element(By.ID, 'usermenu').click()
time.sleep(2)

# Нажатие кнопки выхода
driver.find_element(By.XPATH, '//*[@id="usermenu-dropdown"]/a[14]').click()
time.sleep(2)

# Нажатие кнопки входа
driver.find_element(By.XPATH, '/html/body/div[4]/div/header/div[1]/div/nav/div[2]/ul/li[6]/form/button').click()
time.sleep(2)
try:
    # Ввод неверного пароля
    driver.find_element(By.ID, 'username').send_keys("d.bikmurzin")
    driver.find_element(By.ID, 'password').send_keys("11111111")
    time.sleep(1)
    driver.find_element(By.ID, 'loginbtn').click()
    time.sleep(2)
except:
    print("Error")
else:
    print("Ok")
driver.quit()

input("Скрипт завершён")