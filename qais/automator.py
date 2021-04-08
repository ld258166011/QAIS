import os
import time
import ctypes
import xpinyin
import platform
import pyautogui
import numpy as np
import pandas as pd
import pkg_resources

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

MODEL_PATH = pkg_resources.resource_filename('qais', 'models/')
def_bigrams = os.path.join(MODEL_PATH, 'bigrams.csv')


class Automator:
    '''
    Automation of Incremental Search.
    '''
    keys = ''
    timings = []

    def __init__(self, query, chinese=False, bigrams=None, factor=0):
        # Check current language
        self.__check_language(chinese)

        # Translate Chinese characters to Pinyin string
        if chinese == True:
            py = xpinyin.Pinyin()
            self.keys = py.get_pinyin(query, '')
        else:
            self.keys = query

        # Load keystroke timing model
        if bigrams is not None:
            bigrams = pd.read_csv(bigrams)
        else:
            bigrams = pd.read_csv(def_bigrams)

        # Create keystroke timing sequence
        self.timings = [0]
        for i in range(len(self.keys) - 1):
            bigram = bigrams[(bigrams['1st_key'] == self.keys[i]) & (bigrams['2nd_key'] == self.keys[i+1])]
            interval = np.random.normal(bigram['mean'].tolist()[0], bigram['std'].tolist()[0] * factor)
            self.timings.append(self.timings[-1] + interval)

        # Type Space to select the default candidate
        if chinese == True:
            self.keys += ' '
            self.timings.append(self.timings[-1] + 200)

    
    def __check_language(self, chinese):
        '''
        Check if the current language matches the query.
        '''
        if platform.system() == 'Windows':
            user32 = ctypes.WinDLL('user32', use_last_error=True)
            curr_window = user32.GetForegroundWindow()
            thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
            klid = user32.GetKeyboardLayout(thread_id)
            lid_hex = hex(klid & (2**16 - 1))

            if lid_hex != '0x0':
                if chinese == True:
                    if lid_hex != '0x804':
                        raise Exception('Please switch to Chinese keyboard')
                else:
                    if lid_hex != '0x409':
                        raise Exception('Please switch to English keyboard')


    def open_browser(self, browser):
        '''
        Open browser with no notifications.
        '''
        if browser.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-quic')
            options.add_argument('--no-sandbox')
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
            self.driver = webdriver.Chrome(chrome_options = options)
        elif browser.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
            options.set_preference("dom.push.enabled", False)
            self.driver = webdriver.Firefox(firefox_options = options)
        elif browser.lower() == 'edge':
            options = EdgeOptions()
            options.set_capability("dom.push.enabled", False)
            self.driver = webdriver.Edge(capabilities=options.to_capabilities())
        else:
            raise Exception('browser not supported')
        self.driver.maximize_window()


    def get_website(self, url):
        '''
        Get website in browser.
        '''
        self.driver.get(url)
        time.sleep(1)

        def __isElemExist(elem):
            try:
                self.driver.find_element_by_id(elem)
            except:
                return False
            else:
                return True

        while __isElemExist('reload-button'):
            self.driver.find_element_by_id('reload-button').click()
            time.sleep(1)


    def user_login(self, user, password):
        '''
        Log in with an account.
        '''
        pyautogui.typewrite(user)
        pyautogui.press('tab')
        pyautogui.typewrite(password)
        pyautogui.press('enter')
        time.sleep(1)

    
    def wait_element(self, xpath):
        '''
        Wait until the element is ready.
        '''
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            time.sleep(1)
        except:
            return False
        else:
            return True

    
    def click_once(self, xpath):
        '''
        Click once on the element.
        '''
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(1)


    def switch_ime(self):
        '''
        Switch Pinyin IME for Chinese queries.
        '''
        pyautogui.hotkey('ctrl', 'space')
        time.sleep(1)


    def type_query(self):
        '''
        Type query according to keys and timings.
        '''
        now = time.time()
        time_seq = [now + time / 1000 for time in self.timings]
        
        for i in range(len(self.keys)):
            while True:
                if time.time() > time_seq[i]:
                    break
            pyautogui.platformModule._keyDown(self.keys[i])
            pyautogui.platformModule._keyUp(self.keys[i])

        time.sleep(1)


    def close_browser(self):
        '''
        Close browser.
        '''
        self.driver.quit()
