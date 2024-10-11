from selenium_driverless import webdriver
import asyncio

async def main():
    # socks5 with credentials not supported due to https://bugs.chromium.org/p/chromium/issues/detail?id=1309413
    proxy = "http://14a51f7dce1cf:e041b7ba43@89.42.81.219:12323/"

    options = webdriver.ChromeOptions()
    # options.single_proxy = proxy

    async with webdriver.Chrome(options=options) as driver:

        # this will overwrite the proxy for ALL CONTEXTS
        await driver.set_single_proxy(proxy)

        await driver.get("https://browserleaks.com/webrtc")
        await driver.clear_proxy()  # clear proxy
        


asyncio.run(main())