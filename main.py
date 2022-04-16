import traceback
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

id = input("아이디 입력 : ")
password = input("패스워드 입력 :")

driver = webdriver.Chrome("./chromedriver")
url = "https://www.melon.com/"
driver.get(url)

# 메인 페이지
main_login_button = driver.find_element_by_xpath('//*[@id="gnbLoginDiv"]/div/button')
main_login_button.click()

melon_login_button = driver.find_element_by_xpath(
    '//*[@id="conts_section"]/div/div/div[3]/button'
)
melon_login_button.click()

# 로그인 페이지
driver.find_element_by_xpath('//*[@id="id"]').send_keys(id)
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

# 마크업 구조 맞추기 위해 임의의 텍스트 검색
driver.find_element_by_xpath('//*[@id="top_search"]').send_keys("test")
driver.find_element_by_xpath('//*[@id="gnb"]/fieldset/button[2]').click()

# Playlist 로드
file = open("playlist.txt", mode="rt", encoding="utf-8")
plist = file.readlines()
file.close()

for p in plist:
    try:
        driver.switch_to.window(driver.window_handles[0])

        p = p.split("\n")[0]

        # playlist 검색
        search_input = driver.find_element_by_id("top_search")
        search_button = driver.find_element_by_xpath(
            '//*[@id="header_wrap"]/div[2]/fieldset/button[2]/span'
        )

        search_input.clear()
        search_input.send_keys(p)
        search_button.click()

        open_add_playlist_button = driver.find_element_by_xpath(
            '//*[@id="frm_songList"]/div/table/tbody/tr[1]/td[3]/div/div/button[2]/span'
        )
        open_add_playlist_button.click()

        # playlist 추가 팝업 대기
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))
        driver.switch_to.window(driver.window_handles[2])

        tmp = driver.window_handles[2]

        first_playlist_cell = driver.find_element_by_xpath(
            '//*[@id="plylstList"]/div/table/tbody/tr/td[1]/div/div/span'
        )
        first_playlist_cell.click()

        add_paylist_button = driver.find_element_by_xpath(
            '//*[@id="plylstList"]/div/table/tbody/tr/td[1]/div/span/button/span/span'
        )
        add_paylist_button.click()

        try:
            alert = Alert(driver)
            alert_text = alert.text
            alert.accept()
            driver.close()
            print(alert_text)
        except NoAlertPresentException:
            while True:
                if len(driver.window_handles) > 2:
                    if tmp != driver.window_handles[2]:
                        break

            WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(3))
            driver.switch_to.window(driver.window_handles[2])
            driver.find_element_by_xpath("/html/body/div/div/div[2]/button").click()

    except NoSuchElementException:
        print("Error: " + p)
        traceback.print_exc()
        continue
    except IndexError:
        print("Error: " + p)
        traceback.print_exc()
        continue


driver.close()
