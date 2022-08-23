from django.http import HttpResponse

# -*- coding: utf-8 -*-
"""
Created on May 31, 2020 10:14am
Email: er.gautamkadian@gmail.com

@author: Gautam Kadian

"""

# import general modules
import os
import datetime
# import pandas as pd
# import dateparser

# import custom modules
from spinerapp import selenium_controller

#############################################
# 1: Initialize settings                     #
#############################################
PATH = os.path.abspath(os.path.dirname(__file__))
web_gui = True
litigation_cases = []
credentials = {
    'USERNAME': 'camcrystalmanc@gmail.com',
    'PASSWORD': ' United1!'
}

# searchType : Muncipal Suits,  Real Estate Transfers


export_folder = "D:/Personal/Documents/New folder/"

# for filters in filter_list:
output_folder = export_folder
page_count = 0
records_count = []
month_list = {}
#############################################
# 2: Code begin for the COURT INDEX                   #
#############################################
# Start time, when the process starts
start_time = datetime.datetime.now()

# Initialize browser
print("Starting the execution of Ticket purchasing")
selenium_controller.getUserInput()
browser = selenium_controller.initialize_chromebrowser(PATH, web_gui)
# selenium_controller.downloadFile()

# login into the court indexbrowser
login_bool = selenium_controller.log_in(browser, credentials, False)
if login_bool:
    selenium_controller.redirect_hometickets(browser)
    eventLists = selenium_controller.get_events(browser)
    selenium_controller.selectEvent(browser, eventLists)
    areaList = selenium_controller.fetchAreaData(browser)
    selenium_controller.selectArea(browser, areaList)
    selenium_controller.proceedToPay(browser)
    # selenium_controller.click_ticket(browser)
    # selenium_controller.check_avail(browser)
input('\n\nAll ready. Press enter twice to quit.\nAny questions or remarks: kadianwebserivc@automate.it')
