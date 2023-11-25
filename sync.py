from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from datetime import datetime
from selenium_driverless.types.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# can place a bet
# can scrape odds
# can get balance
# can refresh
# can get race time
# can login - YES


class XPath:
    LOGIN_BUTTON = "//div[@class='hm-MainHeaderRHSLoggedOutWide_Login ']"
    USER_NAME_INPUT = "//input[@class='lms-StandardLogin_Username ']"
    PASSWORD_INPUT = "//input[@class='lms-StandardLogin_Password ']"
    LOGIN_MODAL = "//div[@class='lms-StandardLogin_Container ']"
    MODAL_LOGIN_BUTTON = "//div[@class='lms-LoginButton_Text ']"
    RUNNER = "//*[@class='srm-ParticipantHorseRacingFixed gl-Market_General-cn1 ']"


class ClassName:
    RUNNER_NAME_CLASS = "srm-ParticipantDetailsRacingFixed_RunnerName "
    BACK_ODD = "srm-ParticipantHorseRacingOddsFixed_Odds"
    STAKE_INPUT = "bsf-StakeBox_StakeInput "
    BET_BUTTON = "bsf-StakeBox_StakeInput "
    RACE_START_TIME = "sah-MarketEventHeaderInfoAus_Item "


def get_horse_odds(driver) -> dict[str, float]:
    driver.refresh()
    wait = WebDriverWait(driver, 10)  # 10 seconds timeout

    horse_odds = {}
    # horses = driver.find_elements(By.XPATH, XPath.RUNNER)
    horses = wait.until(EC.presence_of_all_elements_located((By.XPATH, XPath.RUNNER)))

    try:
        for h in horses:
            children = h.children

            if len(children) > 0:
                name_element = findWebElementByClassName(
                    children, ClassName.RUNNER_NAME_CLASS
                )
                back_odd_element = findWebElementByClassName(
                    children, ClassName.BACK_ODD
                )
                horse_odds[name_element.text] = float(back_odd_element.text)

    except Exception as e:
        print(f"Exception thrown: {e}")

    return horse_odds


def findWebElementByClassName(
    web_elements: [WebElement], class_name: str
) -> WebElement:
    for web_element in web_elements:
        if web_element.get_property("className") == class_name:
            return web_element


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.bet365.com.au/#/AC/B2/C101/D20231125/E20928239/F147093069/P12/")
driver.sleep(0.5)

while True:
    data = get_horse_odds(driver)
    time = datetime.now()
    print(time, data)
