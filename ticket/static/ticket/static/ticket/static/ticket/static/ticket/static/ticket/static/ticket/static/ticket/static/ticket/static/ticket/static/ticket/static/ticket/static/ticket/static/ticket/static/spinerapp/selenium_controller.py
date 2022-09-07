# import sys
# import os
# from pathlib import Path
# import time
#
# from spinerapp.multiple_accounts import  event, user_Credit_Or_Debit_Card_Numbers, card_Cvv_Numbers, \
#     card_Expiry_Months, card_Expiry_Years
#
# sys.path.append(Path(__file__).resolve().parent)
# from twocaptcha import TwoCaptcha
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
# event_name = ""
# number_of__seat = 0
# specific_seat = ''
# user_seat = ''
# user_area = ''
# users_list = []
# isCaptchaVisit = False
# user_Credit_Or_Debit_Card_Number = ''
# card_Cvv_Number = ''
# card_Expiry_Month = ''
# card_Expiry_Year = ''
#
#
# # input given by user
#
# def getUserInput():
#     global event_name
#     global number_of__seat
#     global specific_seat
#     global user_seat
#     global user_area
#     global users_list
#     global isCaptchaVisit
#     global user_Credit_Or_Debit_Card_Number
#     global card_Cvv_Number
#     global card_Expiry_Month
#     global card_Expiry_Year
#     # event_name = (input("enter the event name :- "))
#     event_name=event
#     number_of__seat = int(input("Please enter the number of seat you want :- "))
#     specific_seat = (input("Do You Want Specific Row and Seat Y/N :- "))
#     if specific_seat == 'Y':
#         dict = {'username': '', 'user_age': '', 'user_row': '', 'user_seat': ''}
#         if number_of__seat > 1:
#             user_seat = input("Please enter the specific seat with comma seprated eg 20,21,22 :- ")
#             users_list.clear()
#             for seat in range(len(user_seat.split(','))):
#                 dict = {'username': '', 'user_age': '', 'user_row': '', 'user_seat': ''}
#                 if seat == 0:
#                     dict['username'] = ''
#                     dict['user_age'] = ''
#                     dict['user_row'] = input(f"enter specific  row for {seat + 1} user :- ")
#                     dict['user_seat'] = dict['user_row'] + '/' + user_seat.split(',')[seat]
#                     users_list.append(dict)
#                 else:
#                     dict['username'] = input(f"please enter {seat + 1} username :- ")
#                     dict['user_age'] = input(f"please enter {seat + 1} user age :- ")
#                     dict['user_row'] = input(f"enter specific  row for {seat + 1} user :- ")
#                     dict['user_seat'] = dict['user_row'] + '/' + user_seat.split(',')[seat]
#                     users_list.append(dict)
#             print(users_list)
#         else:
#             user_seat = input("Please enter the specific seat :- ")
#             dict['username'] = ''
#             dict['user_age'] = ''
#             dict['user_row'] = input(f"enter specific  row :- ")
#             dict['user_seat'] = dict['user_row'] + '/' + user_seat
#             users_list.append(dict)
#         user_area = input("Please enter specific area eg N2401 :- ")
#         # user_area='N3408'
#         user_Credit_Or_Debit_Card_Number = input("enter the card number :- ")
#         card_Cvv_Number = input("enter the cvv number :- ")
#         card_Expiry_Month = input("enter the expire_month :- ")
#         card_Expiry_Year = input("enter the Expire_year :- ")
#     else:
#         # user_area = 'N3408'
#         # user_area = input("Please enter specific area eg N2401 :- ")
#         # user_Credit_Or_Debit_Card_Number = input("enter the card number :- ")
#         # user_Credit_Or_Debit_Card_Number='5355 2206 3239 8826'
#         user_Credit_Or_Debit_Card_Number=user_Credit_Or_Debit_Card_Numbers
#         card_Cvv_Number=card_Cvv_Numbers
#         card_Expiry_Month=card_Expiry_Months
#         card_Expiry_Year=card_Expiry_Years
#
# def initialize_chromebrowser(PATH, WEB_GUI=True):
#     """Function that will initialize all chromebrowser settings and launch a first page call"""
#     if 'darwin' in sys.platform:
#         CHROMEBROWSER_PATH = "C:\web_driver\chromedriver.exe"
#     elif 'win' in sys.platform:
#         CHROMEBROWSER_PATH = os.path.join(Path(PATH).resolve(), 'chromedriver.exe')
#     else:
#         CHROMEBROWSER_PATH = "C:\web_driver\chromedriver.exe"
#     # PROXY ="5.252.70.14:8458"
#     CHROME_OPTIONS = Options()
#     # CHROME_OPTIONS.add_argument('--proxy-server=%s' % PROXY)
#     CHROME_OPTIONS.add_argument('log-level=3')
#     CHROME_OPTIONS.add_argument('--window-size=1920,1080')
#     CHROME_OPTIONS.add_experimental_option('prefs', {'intl.accept_languages': 'en,en-US',
#                                                      'profile.default_content_settings.popups': 0})
#     if WEB_GUI:
#         pass
#     else:
#         CHROME_OPTIONS.add_argument(
#             '--headless')  # comment this line if you like to have the chromedriver run with a GUI
#     try:
#         browser = webdriver.Chrome(CHROMEBROWSER_PATH, chrome_options=CHROME_OPTIONS)
#     except:
#         a = input(
#             'Chromedriver is not compatible anymore with your current Chrome version. Download the new version at '
#             'https://chromedriver.chromium.org/downloads \nPress enter to quit.')
#         quit()
#     browser.get('https://login.manutd.com/sign-in')
#     return browser
# # page redirect to homepage
# def redirect_hometickets(browser):
#     time.sleep(4)
#     """Function that will initialize all chromebrowser settings and launch a first page call"""
#     browser.get('https://tickets.manutd.com/en-GB/categories/home-tickets')
#     # WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.ID, 'accept-btn'))).click()
#     return browser
#
#
#
# # user login page
# def log_in(browser, LOGIN, refresh=True):
#
#     """a function that will log into the site"""
#     if refresh:
#         #     browser.get('http://www.courtindex.com/login.aspx?ReturnUrl=%2farticle-search.aspx')
#         wait = WebDriverWait(browser, 15)
#         wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
#     try:
#         tryout = 0
#         while tryout < 20:
#             browser.find_element(By.ID, "Username").clear()
#             browser.find_element(By.ID, "Username").send_keys('tompalmer321@outlook.com')
#             browser.find_element(By.ID, "Password").clear()
#             browser.find_element(By.ID, "Password").send_keys('Euphoria123!')
#             browser.find_element(By.CLASS_NAME, "btn").click()
#             try:
#                 time.sleep(1)
#                 wait.until(EC.visibility_of_element_located((By.ID, 'multi-anchor')))
#                 tryout = 50
#             except:
#                 break
#         return True
#     except NoSuchElementException as e:
#         print(e)
#         return False
#
#
# # match name with match link
# def get_events(browser):
#     "That check_tickets function scrap the event_name, date, event_link "
#     time.sleep(10)
#     event_list = []
#     var = browser.find_elements(By.CLASS_NAME, "dataItem")
#     for i in var:
#         # print(i)
#         dict = {'date': '', 'event_name': '', 'event_hall': '', 'event_link': ''}
#         dict['date'] = i.find_element(By.CLASS_NAME, "itemsDateRange").text.replace('\n', ' ')
#         dict['event_name'] = i.find_element(By.CLASS_NAME, "name").text
#         dict['event_hall'] = i.find_element(By.ID, "eventhallname").text
#         dict['event_link'] = i.find_element(By.CSS_SELECTOR, ".itemsButtonsContainer a ").get_attribute(
#             "href") if i.find_element(By.CSS_SELECTOR, ".itemsButtonsContainer a ").get_attribute(
#             "style") != 'display: none;' else ''
#         dict['event_id'] = i.find_element(By.CSS_SELECTOR, ".itemsButtonsContainer a ").get_attribute("id")
#         event_list.append(dict)
#     return event_list
#
#
# def selectEvent(browser, eventList):
#     print(event_name)
#     for event in eventList:
#         if event['event_name'] == event_name and event['event_link'] != '':
#             browser.get(event['event_link'])
#             WebDriverWait(browser, 120).until(EC.element_to_be_clickable((By.ID, 'accept-btn'))).click()
#             break
#         elif event['event_link'] == '':
#             print('The event is not availble Pleas choose other one')
#             redirect_hometickets(browser)
#
#
# # event name or age and show the ticket
# def fetchAreaData(browser):
#     time.sleep(9)
#     wait = WebDriverWait(browser, 40)
#     # wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'area-info-container')))
#     if wait:
#         area_ids = browser.find_elements(By.CLASS_NAME, 'area-info-container')
#         # print(area_ids)
#         arr = []
#         result = []
#         for p in range(len(area_ids)):
#             if p == 0 or p == 1 or 'filtered' in str(area_ids[p].get_attribute('class')):
#                 pass
#             else:
#                 dict = {}
#                 dict['area-name'] = area_ids[p].find_element(By.CLASS_NAME, "name").text
#                 q = area_ids[p].find_element(By.CLASS_NAME, 'priceLevelImages')
#                 dict['price_range'] = q.find_element(By.CLASS_NAME, 'price-range').text
#                 dict['area-id'] = area_ids[p].get_attribute("data-areaid")
#                 # dict['adult_price']=q.find_element(By.CLASS_NAME, 'additionalPrices').text
#                 # result.append(dict)
#                 price = q.find_elements(By.CLASS_NAME, 'additionalPrices')
#                 for h in price:
#                     ages = h.find_elements(By.CLASS_NAME, 'name')
#                     prices = h.find_elements(By.CLASS_NAME, 'price')
#                     arr = []
#                     for pri in range(len(ages)):
#                         dict1 = {'age': '', 'price': ''}
#                         dict1['age'] = ages[pri].text
#                         dict1['price'] = prices[pri].text
#                         # dict.update(dict1)
#                         arr.append(dict1)
#                         # result.append(dict)
#                 dict['price'] = arr
#                 result.append(dict)
#         return result
#
# def selectArea(browser, areaList):
#     isAreaFound = False
#     eventLink = browser.execute_script('return window.location.href')
#     if specific_seat == 'N':
#         selectanyseat(browser)
#         return
#     else:
#         time.sleep(8)
#         for area in areaList:
#             if area['area-name'] == user_area:
#                 link = eventLink.replace('hallmap', '')
#                 areaLink = f"area={area['area-id']}&type=&sb2m=1"
#                 fullLink = link + areaLink
#                 isAreaFound = True
#                 browser.get(fullLink)
#
#                 break
#     if isAreaFound == False:
#         print("invalid area")
#         browser.get(eventLink)
#     selectSeat(browser)
#
#
# def selectanyseat(browser):
#     browser.execute_script("document.getElementsByClassName('areas-filter-panel__max-sum-input')[0].value=60")
#     total = browser.find_element(By.CSS_SELECTOR, "span[class='ui-button-icon ui-icon ui-icon-triangle-1-n']")
#     for i in range(0, number_of__seat):
#         total.click()
#     # browser.find_element_by_css_selector("span[class='ui-spinner areas-filter-panel__qty-wrapper ui-corner-all
#     # ui-widget ui-widget-content']").click()
#     browser.find_element(By.CLASS_NAME, 'areas-filter-panel__find-button').click()
#     print("seat not available")
#
#
#
# def proceedToPay(browser):
#     try:
#         time.sleep(11)
#         # browser.execute_script("document.getElementsByClassName('ui-button ui-corner-all ui-widget')[5].click()")
#         browser.execute_script(
#             "document.getElementsByClassName('ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close')[1].click()")
#
#         time.sleep(4)
#         browser.execute_script('document.getElementById("btnOrder").click()')
#     except:
#         time.sleep(4)
#         browser.execute_script('document.getElementById("btnOrder").click()')
#     time.sleep(4)
#     browser.execute_script('document.getElementById("btnSubmit").click()')
#     time.sleep(4)
#     browser.find_element(By.ID,"da6bdd56-dfc2-eb11-830a-b44d34921fe7")
#     try:
#         browser.find_element(By.ID,"da6bdd56-dfc2-eb11-830a-b44d34921fe7")
#         time.sleep(4)
#         browser.execute_script(
#             "document.getElementsByClassName('ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close')[1].click()")
#         # browser.execute_script("document.getElementsByClassName('ui-button ui-corner-all ui-widget')[5].click()")
#         time.sleep(4)
#         browser.find_element(By.ID,"fldpf_489_IsForFuturePayByCustomer").click()
#     except:
#         time.sleep(4)
#         browser.find_element(By.ID,"fldpf_489_IsForFuturePayByCustomer").click()
#     time.sleep(4)
#     browser.find_element(By.ID,"chkReadTerms").click()
#     time.sleep(4)
#     browser.find_element(By.ID,"btnOrder").click()
#     time.sleep(4)
#     add_Credit_Detail(browser)
#
# # check available seat and click on the seat
# def selectSeat(browser):
#     time.sleep(8)
#     wait = WebDriverWait(browser, 160)
#     wait.until(EC.visibility_of_element_located((By.ID, 'zoomContainer')))
#     id = browser.find_element(By.ID, "zoomContainer")
#     all_images = id.find_elements(By.CSS_SELECTOR, "img")
#     seats = []
#     for i in all_images:
#         if ('seat a' in i.get_attribute("class")):
#             print("hello")
#             if i.get_attribute('alt') in [sub['user_seat'] for sub in users_list]:
#                 seats.append(i)
#     if len(seats) == 0:
#         print("seat not available")
#         sys.exit()
#     clickSelectedSeats(browser, seats)
#
#
# def clickSelectedSeats(browser, seats):
#     gCapttchaInstance = browser.execute_script(
#         'return Object.entries(___grecaptcha_cfg.clients).map(([l,e])=>{const s={id:l,version:1e4<=l?"V3":"V2"},c=Object.entries(e).filter(([,e])=>e&&"object"==typeof e);c.forEach(([e,c])=>{var t=Object.entries(c).find(([,e])=>e&&"object"==typeof e&&"sitekey"in e&&"size"in e);"object"==typeof c&&c instanceof HTMLElement&&"DIV"===c.tagName&&(s.pageurl=c.baseURI);if(t){const[i,n]=t,a=(s.sitekey=n.sitekey,"V2"===s.version?"callback":"promise-callback");c=n[a];if(c){s.function=c;t=[l,e,i,a].map(e=>`["${e}"]`).join("");s.callback="___grecaptcha_cfg.clients"+t}else{s.callback=null;s.function=null}}});return s}); ')
#     if len(seats) > 1:
#         for seat in seats:
#             if checkCaptcha(browser, gCapttchaInstance):
#                 pass
#             else:
#                 seatId = seat.get_attribute('id')
#                 wait = WebDriverWait(browser, 200)
#                 wait.until(EC.element_to_be_clickable((By.ID, seatId))).click()
#         onProceed(browser)
#     else:
#         seats[0].click()
#         checkCaptcha(browser, gCapttchaInstance)
#         onProceed(browser)
#
#
# def checkCaptcha(browser, gCapttchaInstance):
#     frames = browser.find_elements(By.TAG_NAME, 'iframe')
#     for frame in frames:
#         if frame.get_attribute('aria-describedby') != None and frame.get_attribute('aria-describedby') != '':
#             isCaptchaVisit = True
#             solveCaptcha(browser, gCapttchaInstance)
#             time.sleep(9)
#             wait = WebDriverWait(browser, 100)
#             ActionChains(browser).move_by_offset(10, 10).click().perform()
#             time.sleep(2)
#             # browser.find_element(By.TAG_NAME, "html").click()
#             # browser.find_element(By.TAG_NAME, "body").click()
#             break
#         else:
#             isCaptchaVisit = False
#
#
# # solve the captcha
# def solveCaptcha(browser, gCapttchaInstance):
#     time.sleep(5)
#     print(gCapttchaInstance)
#     solver = TwoCaptcha('362cfde7052da1589a8efb5060438172')
#     data_sitekey = gCapttchaInstance[0]['sitekey']
#     try:
#         result = solver.recaptcha(
#             sitekey=data_sitekey,
#             url='https://tickets.manutd.com/demo/recaptcha-v2-invisible',
#             invisible=1
#         )
#         print(result['code'])
#         captha_results = result['code']
#         browser.execute_script(
#             """document.querySelector('[name="g-recaptcha-response"]').innerText='{}'""".format(captha_results))
#         print(gCapttchaInstance[0]['callback'])
#         browser.execute_script(f"{gCapttchaInstance[0]['callback']}('{captha_results}');")
#         browser.execute_script("document.getElementById('seat-key').click()")
#     except Exception as e:
#         sys.exit(e)
#     else:
#         print('result: ' + str(result))
# def onProceed(browser):
#     time.sleep(2)
#     browser.execute_script('document.getElementById("btnProceed").click()')
#     time.sleep(4)
#     browser.execute_script('onProceed();')
#     browser.execute_script('document.getElementById("btnSubmit").click()')
#     time.sleep(2)
#     browser.find_element(By.ID, "da6bdd56-dfc2-eb11-830a-b44d34921fe7")
#     time.sleep(5)
#     browser.execute_script("document.getElementsByClassName('ui-button ui-corner-all ui-widget ui-button-icon-only ui-dialog-titlebar-close')[1].click()")
#     # browser.execute_script("document.getElementsByClassName('ui-button ui-corner-all ui-widget')[3].click()")
#     time.sleep(5)
#     browser.find_element(By.ID, "fldpf_489_IsForFuturePayByCustomer").click()
#     # browser.execute_script("window.scrollBy(0,1000)","")
#     time.sleep(4)
#     browser.find_element(By.ID, "chkReadTerms").click()
#     time.sleep(5)
#     browser.find_element(By.ID, "btnOrder").click()
#     time.sleep(5)
#     add_Credit_Detail(browser)
#     print("program reached to proceed")
#
#
# def add_Credit_Detail(browser):
#     frames = browser.find_elements(By.TAG_NAME, 'iframe')
#     cardnumberFrame = ''
#
#     cvvFrame = ''
#     for frame in frames:
#         if "spreedly-number-frame" in frame.get_attribute('name'):
#             cardnumberFrame = frame
#         elif "spreedly-cvv-frame" in frame.get_attribute('name'):
#             cvvFrame = frame
#     browser.switch_to.frame(cardnumberFrame)
#     browser.find_element(By.ID, "card_number").send_keys(user_Credit_Or_Debit_Card_Number)
#
#     browser.switch_to.default_content()
#     browser.switch_to.frame(cvvFrame)
#     browser.find_element(By.ID, "cvv").send_keys(card_Cvv_Number)
#     browser.switch_to.default_content()
#     browser.find_element(By.ID, "month").clear()
#     browser.find_element(By.ID, "month").send_keys(card_Expiry_Month)
#     browser.find_element(By.ID, "year").clear()
#     browser.find_element(By.ID, "year").send_keys(card_Expiry_Year)
#     browser.execute_script("window.scrollBy(0,200)","")
#     time.sleep(5)
#     browser.find_element(By.CLASS_NAME, "sgs-form-button").click()
#     time.sleep(8)
#     browser.find_element(By.XPATH, "/html/body/main/div[5]/div/a").click()
#     time.sleep(3)
#     sys.exit()
