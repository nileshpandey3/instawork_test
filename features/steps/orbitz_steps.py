import datetime
import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from features.steps.orbitz_data import home_url, home_page_title

driver = webdriver.Chrome('/Users/nileshpandey/PycharmProjects/friendbuy_test/chromedriver')


# @when("I click on start sharing")
# def start_sharing(context):
#     start_sharing_btn = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, sharing_btn)))
#     start_sharing_btn.click()

# - Visit www.orbitz.com website.
# - Select Flights
# - Select “Roundtrip”.
# - Enter “Leaving from” : San Francisco and “Going to”: New York.
# - Select “Departing” date to be 2 weeks from today and “Returning” date to be 3 weeks from today.
# - Click on Search.
# - Assert that the search results are rendered correctly (Ex: Departure/Arrival location and dates match the input data).
# - Select “Nonstop” flights.
# - Select the most expensive flight from the list.
# - Click on “Select” and then click on “Select this fare” to book.
# - Assert the flight details & price on the flight review page.


@given("I am on orbitz homepage")
def got_to_homepage(context):
    driver.get(home_url)
    driver.maximize_window()
    get_home_page_title = driver.title
    assert get_home_page_title == home_page_title


@when("I click on flight selection option")
def select_flight_option(context):
    flight_tab = driver.find_element_by_xpath('//*[@aria-controls="wizard-flight-pwa"]')
    flight_tab.is_displayed()
    flight_tab.click()


@when("I select roundtrip option")
def select_roundtrip(context):
    roundtrip = driver.find_element_by_xpath('//*[@aria-controls="wizard-flight-tab-roundtrip"]')
    roundtrip.click()


@when("Enter source location")
def leaving_from(context):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Leaving from"]'))).send_keys("San Francisco")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//li[1]//button[1]'))).click()


@when("Enter destination location")
def going_to(context):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="Going to"]'))).send_keys("London")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@data-stid="location-field-leg1-destination-result-item-button"]'))).click()


@when("I Pick a date range and search for flights")
def pick_date(context):
    today_date = datetime.date.today()
    context.two_weeks = today_date + datetime.timedelta(weeks=2)
    context.three_weeks = today_date + datetime.timedelta(weeks=3)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@data-stid="open-date-picker"]'))).click()
    driver.find_element_by_xpath(f"//h2[normalize-space()='June 2021']").is_displayed()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, f"//button[@aria-label='Jun {context.two_weeks.day}, 2021 selected, current check in date.']"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, f"//button[@aria-label='Jun {context.three_weeks.day}, 2021']"))).click()
    driver.find_element_by_xpath("//body/div[@id='app']/div[@id='app-layer-manager']/div[@id='app-layer-base']/div[contains(@class,'uitk-grid')]/div[@class='uitk-cell Storefront-Homepage']/div[@role='main']/div[@class='StorefrontWizardRegionCOMET comet-homepage-module']/div[@class='cometRegion']/figure[@class='uitk-image cometBackgroundImageFigure']/div[@class='uitk-layout-grid uitk-layout-grid-columns-small-2 uitk-layout-grid-columns-large-12 wizardCard all-t-padding-six all-x-padding-six SimpleContainer']/div[@class='uitk-card-aloha uitk-card-aloha-roundcorner-all uitk-layout-grid-item all-cell-1-1 all-b-padding-six uitk-layout-grid-item-columnspan-small-2 uitk-layout-grid-item-columnspan-large-12']/div[@class='uitk-tabs-container']/div[@class='uitk-tabs-content']/div[@id='wizard-flight-pwa']/div[@class='wizardOverHeroImage all-x-padding-six']/form[@id='wizard-flight-pwa-1']/div[@class='uitk-tabs-container']/div[@class='uitk-tabs-content']/div[@id='wizard-flight-tab-roundtrip']/div[@class='uitk-layout-grid uitk-layout-grid-gap-three uitk-layout-grid-columns-small-4 uitk-layout-grid-columns-medium-6 uitk-layout-grid-columns-large-12 uitk-spacing uitk-spacing-padding-block-three']/div[@class='uitk-layout-grid-item uitk-layout-grid-item-columnspan-small-4 uitk-layout-grid-item-columnspan-medium-6 uitk-layout-grid-item-columnspan-large-4']/div[@class='Dates']/div[contains(@class,'uitk-flex uitk-flex-row uitk-flex-gap-three uitk-flex-item uitk-date-fields uitk-flex-grow-1')]/div[@class='uitk-flex-item uitk-flex-basis-zero uitk-flex-grow-1 uitk-date-field-wrapper']/div[@class='uitk-date-picker-menu uitk-menu uitk-menu-mounted']/div[@class='uitk-date-picker-menu-container uitk-date-picker-menu-container-double uitk-menu-container uitk-menu-open uitk-menu-pos-left uitk-menu-container-autoposition uitk-menu-container-text-nowrap']/div[@class='uitk-date-picker date-picker-menu']/div[@class='uitk-flex uitk-date-picker-menu-footer']/button[@type='button']/span[1]").click()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="Search"]'))).click()


@then("I validate the search results")
def validate_results(context):
    assert WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@value="San Francisco, CA, United States of America (SFO)"]')))
    assert WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@value="London, England, UK (LON)"]')))
    assert WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, f'//*[@value="6/{context.two_weeks.day}/2021"]')))
    assert WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, f'//*[@value="6/{context.three_weeks.day}/2021"]')))


