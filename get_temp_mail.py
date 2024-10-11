from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options
from time import sleep

def scroll_down(count):
    screen_size = driver.get_window_size()
    print(screen_size)
    start_x = screen_size['width'] / 2
    start_y = screen_size['height'] * 0.8
    end_x = screen_size['width'] / 2
    end_y = screen_size['height'] * 0.2
    for _ in range(count):
        driver.swipe(start_x, start_y, end_x, end_y, 500)

def scroll_up(count):
    screen_size = driver.get_window_size()
    print(screen_size)
    start_x = screen_size['width'] / 2
    start_y = screen_size['height'] * 0.2
    end_x = screen_size['width'] / 2
    end_y = screen_size['height'] * 0.8
    for _ in range(count):
        driver.swipe(start_x, start_y, end_x, end_y, 500)

udid = "emulator-5554"
appium_port = "4723"

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName=udid,
    udid=udid,
    appPackage='com.android.chrome',
    appActivity='com.google.android.apps.chrome.Main',
    # language='en',
    # locale='US',
    noReset=True,
    newCommandTimeout=3000,
)

appium_server_url = f'http://localhost:{appium_port}'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)
driver.implicitly_wait(5)

url = 'https://temp-mail.org'
driver.get(url)

try:
    cf_checkbox = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.CheckBox')
    cf_checkbox.click()
except:
    pass

while True:
    email_field = driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText')
    email = email_field.text
    print(email)
    if "temp-mail.org" not in email.lower() and "loading" not in email.lower():
        with open("temp_email.txt", "w") as file:
            file.write(email)
        break
    sleep(3)

scroll_down(2)
sleep(2)
while True:
    try:
        upwork_notification = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Upwork Notifications donotreply@upwork.com Verify your email address')
        upwork_notification.click()
        sleep(3)
        scroll_down(3)
        sleep(3)
        verify_email = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Verify Email"]')
        bounds = verify_email.get_attribute('bounds')
        result = [list(map(int, pair.split(','))) for pair in bounds.strip('][').split('][')]
        x = (result[1][0] - result[0][0]) / 2 + result[0][0]
        y = (result[1][1] - result[0][1]) / 2 + result[0][1]
        print(x, y)
        driver.execute_script('mobile: longClickGesture', {'x': x, 'y': y, 'duration': 1000})
        sleep(3)
        copy_link_address = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Copy link address"]')
        copy_link_address.click()
        verify_link = driver.get_clipboard_text()
        print(verify_link)
        with open("verify_link.txt", "w") as file:
            file.write(verify_link)
        break
    except:
        sleep(5)
        pass

scroll_up(1)

delete_button = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Delete"]')
delete_button.click()



