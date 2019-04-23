
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest 

browser = webdriver.Chrome()
browser.get("localhost:5000")

def test_homepage():
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://localhost:5000/"
    assert "Shared Skies" in browser.title

def test_about():
    browser.get("localhost:5000/about")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://localhost:5000/about"
    assert "About" in browser.title

def test_contact():
    browser.get("localhost:5000/contact")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://localhost:5000/contact"
    assert "Contact" in browser.title

def test_button():
    browser.get("localhost:5000")
    CurrentUrl = browser.current_url
    assert CurrentUrl == "http://localhost:5000/"
    assert "Shared Skies" in browser.title
    Button = browser.find_element_by_class_name("btn-primary")
    Button.click()
    assert "Sign In" in browser.title
    
def test_login():
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
    time.sleep(10)
    browser.close()
    browser.quit()