from datetime import datetime
from selenium_driverless import webdriver
from selenium_driverless.types.by import By
from selenium_driverless.types.webelement import WebElement
import asyncio

# import inspect module
import inspect


class XPath:
    LOGIN_BUTTON = "//div[@class='hm-MainHeaderRHSLoggedOutWide_Login ']"
    USER_NAME_INPUT = "//input[@class='lms-StandardLogin_Username ']"
    PASSWORD_INPUT = "//input[@class='lms-StandardLogin_Password ']"
    LOGIN_MODAL = "//div[@class='lms-StandardLogin_Container ']"
    MODAL_LOGIN_BUTTON = "//div[@class='lms-LoginButton ']"
    RUNNER = "//*[@class='srm-ParticipantHorseRacingFixed gl-Market_General-cn1 ']"


class ClassName:
    RUNNER_NAME_CLASS = "srm-ParticipantDetailsRacingFixed_RunnerName "
    BACK_ODD = "srm-ParticipantHorseRacingOddsFixed_Odds"
    STAKE_INPUT = "bsf-StakeBox_StakeInput "
    BET_BUTTON = "bsf-StakeBox_StakeInput "
    RACE_TIME_CLASS = "sah-MarketEventHeaderInfoAus_Item "


async def get_horse_odds(driver) -> dict[str, float]:
    await driver.refresh()

    await driver.sleep(2)

    horse_odds = {}
    horses = await driver.find_elements(By.XPATH, XPath.RUNNER)

    try:
        for h in horses:
            children = await h.children

            if len(children) > 0:
                name_element = await findWebElementByClassName(
                    children, ClassName.RUNNER_NAME_CLASS
                )
                back_odd_element = await findWebElementByClassName(
                    children, ClassName.BACK_ODD
                )
                horse_odds[await name_element.text] = float(await back_odd_element.text)

    except Exception as e:
        print(f"Exception thrown: {e}")

    return horse_odds


async def findWebElementByClassName(
    web_elements: [WebElement], class_name: str
) -> WebElement:
    for web_element in web_elements:
        if await web_element.get_property("className") == class_name:
            return web_element


async def main():
    options = webdriver.ChromeOptions()
    async with webdriver.Chrome(options=options) as driver:
        await driver.get(
            "https://www.bet365.com.au/#/AC/B2/C101/D20231125/E20928239/F147093069/P12/"
        )
        await driver.sleep(0.5)

        while True:
            data = await get_horse_odds(driver)
            time = datetime.now()
            print(time, data)

        # login = await driver.find_element(By.XPATH, XPath.LOGIN_BUTTON)

        # await login.click()

        # username = await driver.find_element(By.XPATH, XPath.USER_NAME_INPUT)
        # await username.write("xcisis")

        # password = await driver.find_element(By.XPATH, XPath.PASSWORD_INPUT)

        # await password.write("Lighthollow1")

        # login_button = await driver.find_element(By.XPATH, XPath.MODAL_LOGIN_BUTTON)

        # # For some reason a double click works but a single click doesn't? Applies to clickable elements on modal
        # await login_button.click()
        # await login_button.click()

        # await driver.sleep(20)
        # horse_racing = await driver.search_elements(
        #     "/html/body/div[1]/div/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div[5]/div[2]"
        # )
        # horse_racing[0].click()

        # await driver.sleep(5)
        # race1 = await driver.search_elements(
        #     "/html/body/div[1]/div/div[4]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[4]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div"
        # )
        # print(race1)
        # race1[0].click()


asyncio.run(main())
