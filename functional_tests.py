from selenium import webdriver

browser = webdriver.Firefox()

# cool new online to-do app
browser.get('http://localhost:8000')

# title and headers mentions to-do list
assert 'To-Do' in browser.title
