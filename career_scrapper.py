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


def get_query_list(path):

    '''
        input: path of text file containing search queries
        output: list of search queries
    '''
    query_file = open(path, "r")
    test_list = query_file.readlines()
    query_list = [x.strip() for x in test_list]
    query_file.close()

    return query_list

def get_search_query(query_list):

    query = query_list[0]
    words = query.split(' ')
    search_string = '+'.join([word for word in words])

    #Specify Search URL
    search_url = 'https://www.google.com/search?channel=fs&client=ubuntu&q={}'
    search_query = search_url.format(search_string)

    return search_query


def get_results(search_query):

    start_time=time.time()
    driver = webdriver.Chrome(ChromeDriverManager().install())

    #get request
    driver.get(search_query)
    time.sleep(2)

    results = driver.find_elements_by_class_name('RqBzHd')

    print(results)


def main():

    file_name = 'search_queries.txt'
    search_query_list = get_query_list(file_name)
    search_query_string = get_search_query(search_query_list)
    get_results(search_query_string)

if __name__ == "__main__":
    main()
    


