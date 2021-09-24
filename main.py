import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
USERNAME = "YOUR GMAIL"
PASSWORD = "YOUR PASSWORD"
PHONE = "YOUR NUMBER"

website = "https://www.linkedin.com/jobs/view/2703549089/"
# PATH WILL BE YOUR LOCATION ON YOUR PC
driver_path = "F:\Development\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get(website)
time.sleep(2)
# wait for the next page to load
sign_in_button_one = driver.find_element_by_xpath('/html/body/header/nav/div/a[2]')
sign_in_button_one.click()
time.sleep(2)
# wait for the next page to load
username = driver.find_element_by_id("username")
username.send_keys(USERNAME)
username.send_keys(Keys.ENTER)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
sign_in_button_two = driver.find_element_by_class_name(".btn__primary--large from__button--floating")
sign_in_button_two.click()
time.sleep(2)
# wait for the next page to load
all_listenings = driver.find_elements_by_css_selector(".jobs-apply-button--top-card")
for listing in all_listenings:
    print("called")
    listing.click()
    time.sleep()

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-apply-button")
        apply_button.click()
        time.sleep(2)

        # if phone number is not there then fill that
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
        # click next button
        next = driver.find_element_by_class_name("artdeco-button__text")
        next.click()
        # again next button
        next_two = driver.find_element_by_class_name("artdeco-button__text")
        next_two.click()
        # select option
        select_option = driver.find_element_by_class_name("fb-dropdown__select")
        select_option.click()
        profeciency = driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2703549089,33877602,multipleChoice)"]/option[4]')
        profeciency.click()
        select_yes = driver.find_element_by_xpath('//*[@id="ember170"]/div/form/div/div/div[2]/fieldset/div/div[1]/label/span')
        select_yes.click()
        select_yes_two = driver.find_element_by_xpath('//*[@id="ember170"]/div/form/div/div/div[3]/fieldset/div/div[1]/label/span')
        select_yes_two.click()
        select_yes_three = driver.find_element_by_class_name("fb-dropdown__select")
        select_yes_three.click()
        select_no = driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2703549089,33877770,multipleChoice)"]/option[3]')
        select_no.click()
        next_three = driver.find_element_by_xpath('//*[@id="ember180"]/span')
        next_three.click()
        select_yes_four = driver.find_element_by_xpath('//*[@id="ember170"]/div/form/div/div/div/fieldset/div/div[1]/label/span')
        select_yes_four.click()
        review = driver.find_element_by_xpath('//*[@id="ember183"]')
        review.click()
        submit_application = driver.find_element_by_xpath('//*[@id="ember194"]')
        submit_application.click()
    except:
        close_button = driver.find_element_by_xpath('//*[@id="ember214"]/li-icon/svg')
        close_button.click()

driver.quit()





















