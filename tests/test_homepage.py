
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest 

browser = webdriver.Chrome()
browser.get("http://www.sharedskies.us")

def test_homepage():
    #Tests that default homepage is up
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://www.sharedskies.us/"
    assert "Shared Skies" in browser.title

def test_about():
    #Test the about page
    browser.get("http://www.sharedskies.us/about")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://www.sharedskies.us/about"
    assert "About" in browser.title

def test_contact():
    #Test the contact page
    browser.get("http://www.sharedskies.us/contact")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://www.sharedskies.us/contact"
    assert "Contact" in browser.title

def test_button():
    #Test the Login button
    browser.get("http://www.sharedskies.us/")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://www.sharedskies.us/"
    assert "Shared Skies" in browser.title
    Button = browser.find_element_by_class_name("btn-primary")
    Button.click()
    assert "Sign In" in browser.title
    
def test_login():
    #tests auth0 login
    time.sleep(3)
    Email = browser.find_element(By.CSS_SELECTOR, 'input[name^="email"]')
    Password = browser.find_element_by_css_selector('input[name="password"]')
    Email.clear
    Password.clear
    Email.send_keys("eaglelandcalendar@gmail.com")
    time.sleep(1)
    Password.send_keys("SharedSkies2019")
    time.sleep(1)
    Submit = browser.find_element_by_class_name("auth0-lock-submit")
    Submit.click()
    time.sleep(2)
    assert "2019" in browser.page_source
    assert "Sign In" not in browser.title

def test_calendar_nav_buttons():
    #Tests the calendar nav buttons (day, week, prev, next)
    time.sleep(1)
    Day = browser.find_element_by_class_name("fc-timeGridDay-button")
    Day.click()
    time.sleep(1)
    Week = browser.find_element_by_class_name("fc-timeGridWeek-button")
    Week.click()
    time.sleep(1)
    Prev = browser.find_element_by_class_name("fc-prev-button")
    Prev.click()
    time.sleep(1)     
    Next = browser.find_element_by_class_name("fc-next-button")
    Next.click()
        
    
def test_friends():
    #tests friend buttons
    Searchbar = browser.find_element_by_id("add-friend")
    Searchbar.clear
    Searchbar.send_keys("lukerinehart79@gmail.com")
    time.sleep(1)
    Add = browser.find_element_by_xpath("/html/body/div/div/div/div[3]/div[1]/button")
    Add.click()
    #Find Friend List
    #Friend-List = browser.find_element_by_id("friend-list")

    #exits the browser
    time.sleep(10)
    browser.close()
    browser.quit()