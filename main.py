from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
import random_name_generator
from time import sleep
import random_photo
import keyboard

proxy = "http://GKCyVlsgbSptcyhV:visPrxyBbs61_country-tr@geo.iproyal.com:12321/"
# proxy = "http://14a51f7dce1cf:e041b7ba43@89.42.81.219:12323/"

options = webdriver.ChromeOptions()
# with webdriver.Chrome(options=options) as driver:
driver = webdriver.Chrome(options=options)
driver.set_single_proxy(proxy)
driver.maximize_window()
driver.get("https://www.upwork.com/nx/signup/?dest=home", wait_load=True)
driver.sleep(0.5)

elem = driver.find_element(By.CSS_SELECTOR, "div[id=\"button-box-4\"]", timeout=10)
elem.click(move_to=True)

apply_button = driver.find_element(By.CSS_SELECTOR, "button[class=\"air3-btn air3-btn-primary air3-btn-block-sm\"]", timeout=10)
apply_button.click(move_to=True)

first_name, last_name = random_name_generator.generate("male")
print(f"First Name: {first_name}, Last Name: {last_name}")
first_name_input = driver.find_element(By.CSS_SELECTOR, "input[id=\"first-name-input\"]", timeout=10)
first_name_input.write(first_name)
last_name_input = driver.find_element(By.CSS_SELECTOR, "input[id=\"last-name-input\"]", timeout=10)
last_name_input.write(last_name)

email_address = ""
while True:
    try:
        with open("temp_email.txt", "r") as file:
            email_address = file.read()
    except:
        pass
    if email_address != "":
        break
    else:
        sleep(2)
email_input = driver.find_element(By.CSS_SELECTOR, "input[id=\"redesigned-input-email\"]", timeout=10)
email_input.write(email_address)

password_input = driver.find_element(By.CSS_SELECTOR, "input[id=\"password-input\"]", timeout=10)
password_input.write("1234qwer!@#$")

check_box = driver.find_elements(By.CSS_SELECTOR, "span[data-test=\"checkbox-input\"]")[1]
check_box.click(move_to=True)

submit_button = driver.find_element(By.CSS_SELECTOR, "button[id=\"button-submit-form\"]")
submit_button.click(move_to=True)

sleep(10)
verify_link = ""
while True:
    try:
        with open("verify_link.txt", "r") as file:
            verify_link = file.read()
    except:
        pass
    if verify_link != "":
        break
    else:
        sleep(2)
driver.get(verify_link)

while True:
    try:
        get_started_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa=\"get-started-btn\"]", timeout=10)
        get_started_button.click(move_to=True)
        break
    except:
        sleep(2)
        pass
sleep(5)
skip_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"skip-button\"]", timeout=10)
skip_button.click(move_to=True)
sleep(2)
skip_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"skip-button\"]", timeout=10)
skip_button.click(move_to=True)
sleep(2)
skip_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"skip-button\"]", timeout=10)
skip_button.click(move_to=True)

sleep(2)
resume_manual_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa=\"resume-fill-manually-btn\"]", timeout=10)
resume_manual_button.click(move_to=True)

sleep(2)
category_list = driver.find_element(By.CSS_SELECTOR, "li[class=\"air3-list-nav-item mb-3x\"]", timeout=10)
category_list.click(move_to=True)
sleep(2)
check_box = driver.find_element(By.CSS_SELECTOR, "label[class=\"air3-checkbox-label mb-2x\"]", timeout=10)
check_box.click(move_to=True)

next_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]", timeout=10)
next_button.click(move_to=True)

sleep(2)
skill_button = driver.find_element(By.CSS_SELECTOR, "div[class=\"air3-token air3-token-multi-select mr-2 mb-2\"]", timeout=10)
skill_button.click(move_to=True)

next_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]", timeout=10)
next_button.click(move_to=True)

sleep(2)
role_input = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby=\"title-label\"]", timeout=10)
role_input.write("Accounting")

next_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]", timeout=10)
next_button.click(move_to=True)

sleep(2)
skip_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"skip-button\"]", timeout=10)
skip_button.click(move_to=True)
sleep(2)
skip_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"skip-button\"]", timeout=10)
skip_button.click(move_to=True)
sleep(2)
#############LANGUAGE SETTING#####################
driver.find_element(By.CSS_SELECTOR, "div[class=\"air3-icon md air3-dropdown-icon\"]", timeout=10).click()

dropdown_menu = driver.find_element(By.CSS_SELECTOR, "ul[id=\"dropdown-menu\"]", timeout=10)
dropdown_menu.find_elements(By.TAG_NAME, "li")[3].click()

next_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]", timeout=10)
next_button.click(move_to=True)

sleep(2)
BIO = "I’m a developer experienced in building websites for small and medium-sized businesses. Whether you’re trying to win work, list your services, or create a new online store, I can help."
textarea = driver.find_element(By.TAG_NAME, "textarea", timeout=10)
textarea.write(BIO)

next_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]", timeout=10)
next_button.click(move_to=True)

sleep(2)
hourly_rate = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"data-test\"]", timeout=10)
hourly_rate.write("20")

next_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]", timeout=10)
next_button.click(move_to=True)

sleep(2)
upload_photo_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa=\"open-loader\"]", timeout=10)
upload_photo_button.click(move_to=True)

image_path = random_photo.get_random_photo()
image_input = driver.find_element(By.CSS_SELECTOR, "input[name=\"imageUpload\"]", timeout=10)
image_input.write(image_path)
sleep(3)
keyboard.write(image_path)
keyboard.press('tab')
keyboard.release('tab')
keyboard.press('enter')
keyboard.release('enter')
sleep(3)
attatch_photo_button = driver.find_element(By.CSS_SELECTOR, "button[data-qa=\"btn-save\"]", timeout=10)
attatch_photo_button.click(move_to=True)
sleep(10)

birth_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder=\"mm/dd/yyyy\"]", timeout=10)
birth_input.write("1998-03-03")
sleep(2)
country_select_button = driver.find_elements(By.CSS_SELECTOR, "div[class=\"air3-icon md air3-dropdown-icon\"]")[1]
country_select_button.click(move_to=True)
sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "span[class=\"air3-menu-item-text\"]")
print(len(countries))
for country in countries:
    if "canada" == country.text.lower():
        country.click()
        break

STREET_ADDRESS = ["130 rue Levy", "1573 Albert Street", "1712 No. 3 Road", "1465 9th Avenue", "2541 40th Street"]
CITY_NAME = ["Montreal", "Kitchener", "Richmond", "Hanover", "Calgary"]
PHONE_NUMBER = ["514-893-1337", "519-594-6242", "604-249-1676", "519-364-4817", "403-282-3010"]
ZIP_CODE = ["H3C 5K4", "N2L 3V2", "V6X 2B8", "N4N 2Z8", "T2M 0X4"]

street_address_input = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby=\"street-label\"]", timeout=10)
street_address_input.write(STREET_ADDRESS[0])
city_input = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby=\"city-label\"]", timeout=10)
city_input.write(CITY_NAME[0])
sleep(2)
city_menu = driver.find_element(By.CSS_SELECTOR, "ul[aria-labelledby=\"city-label\"]", timeout=10)
city_menu.find_element(By.TAG_NAME, "li").click()

zip_code_input = driver.find_element(By.CSS_SELECTOR, "input[aria-labelledby=\"postal-code-label\"]", timeout=10)
zip_code_input.write(ZIP_CODE[0])

phone_number_input = driver.find_element(By.CSS_SELECTOR, "input[data-ev-label=\"phone_number_input\"]", timeout=10)
phone_number_input.write(PHONE_NUMBER[0])

sleep(3)
next_button = driver.find_element(By.CSS_SELECTOR, "button[data-test=\"next-button\"]", timeout=10)
next_button.click(move_to=True)

sleep(1000)

