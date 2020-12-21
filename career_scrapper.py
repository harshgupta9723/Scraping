import os
import selenium
from selenium import webdriver
import time
import io
import bs4 as bs
import requests
import csv
import json
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import ElementClickInterceptedException

start_time=time.time()
driver = webdriver.Chrome(ChromeDriverManager().install())

#Specify Search URL
search_url = 'https://www.google.com/search?sxsrf=ALeKk00gwrM0rgs9ak8BrV8TP4OE_lHTNA%3A1608576867382&source=hp&ei=Y-_gX52HFcG9rQHox4q4Dg&q=courses+after+10th+class&oq=courses+after+10&gs_lcp=CgZwc3ktYWIQAxgCMggIABCxAxDJAzICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoHCCMQ6gIQJzoECCMQJzoFCAAQkQI6CAgAELEDEIMBOgUIABCxAzoLCC4QsQMQxwEQowI6BAguEEM6BwgAELEDEEM6BAgAEEM6CggAELEDEIMBEEM6BwguELEDEEM6BwgAEBQQhwI6CAgAEMkDEJECOgcIIxDJAxAnOgoIABCxAxDJAxBDOgUIABDJA1CWlgNYldUDYOfmA2gFcAB4AIAB7wGIAZcWkgEGMC4xOC4ymAEAoAEBqgEHZ3dzLXdperABCg&sclient=psy-ab'

#get request
driver.get(search_url)
