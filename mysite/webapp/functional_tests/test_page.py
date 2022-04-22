# @Author: Seyed Mohammad Reza Shahrestani
# @date: 22/04/2022


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from django.test import Client
from selenium.webdriver.support.ui import Select


class TestPage(StaticLiveServerTestCase):

    def setUp(self):
        self.options = Options()
        self.options.headless = False
        self.browser = webdriver.Chrome(chrome_options=self.options)
        self.client = Client()
        self.count = 0


    def tearDown(self):
        self.browser.close()


    def test_home_page_is_stats_page(self):
        self.browser.get('http://localhost:8000/')
        self.browser.implicitly_wait(1)
        browser_title = self.browser.title

        self.assertEqual(browser_title, "Statistics")
    

    def test_stats_page_is_stats_page(self):
        self.browser.get('http://localhost:8000/stats')
        self.browser.implicitly_wait(1)
        browser_title = self.browser.title

        self.assertEqual(browser_title, "Statistics")


    def test_playground_page_is_playground_page(self):
        self.browser.get('http://localhost:8000/playground')
        self.browser.implicitly_wait(1)
        browser_title = self.browser.title

        self.assertEqual(browser_title, "Playground")


    def test_nav_logo_links_to_home_page(self):
        self.browser.get('http://localhost:8000/')
        self.browser.implicitly_wait(1)
        self.browser.find_element(By.ID,"logoButton").click()
        newBrowser = webdriver.Chrome(chrome_options=self.options)
        newBrowser.get('http://localhost:8000/')
        newBrowser.implicitly_wait(1)
        homePage = newBrowser.current_url

        self.assertEqual(self.browser.current_url, homePage)


    def test_nav_statistic_links_to_stats_page(self):
        self.browser.get('http://localhost:8000/')
        self.browser.implicitly_wait(1)
        self.browser.find_element(By.ID,"statsPageButton").click()

        self.assertEqual(self.browser.current_url, "http://localhost:8000/stats")


    def test_nav_playground_links_to_playground_page(self):
        self.browser.get('http://localhost:8000/')
        self.browser.implicitly_wait(1)
        self.browser.find_element(By.ID,"playgroundPageButton").click()

        self.assertEqual(self.browser.current_url, "http://localhost:8000/playground")


    def test_nav_github_button_links_to_github_page(self):
        self.browser.get('http://localhost:8000/')
        self.browser.implicitly_wait(1)
        self.browser.find_element(By.ID,"githubPageButton").click()

        self.assertEqual(self.browser.current_url, "https://github.com/smrshahrestani")


    def test_playground_query_results_returns_10_items(self):
        self.browser.get('http://localhost:8000/playground')
        query = """PREFIX bd: <http://www.bigdata.com/rdf#> 
                PREFIX wd: <http://www.wikidata.org/entity/> 
                PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
                PREFIX wikibase: <http://wikiba.se/ontology#> 
                #added before 2016-10
                SELECT DISTINCT ?country ?countryLabel
                WHERE
                {
                ?country wdt:P31 wd:Q3624078 .
                #not a former country
                FILTER NOT EXISTS {?country wdt:P31 wd:Q3024240}
                #and no an ancient civilisation (needed to exclude ancient Egypt)
                FILTER NOT EXISTS {?country wdt:P31 wd:Q28171280}
                OPTIONAL { ?country wdt:P36 ?capital } .

                SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
                }
                ORDER BY ?country
                LIMIT 10
        """
        predicate = " "
        self.browser.find_element(By.ID,"/query").send_keys(query)
        self.browser.find_element(By.ID,"predicate").send_keys(predicate)
        self.browser.find_element(By.ID,"submit").send_keys(Keys.RETURN)
        self.browser.implicitly_wait(60)
        
        # if it gets a 500 response, it waits 10 seconds and then runs the test again
        if(self.browser.title == "Server Error (500)" and self.count <= 3):
            print("error 500")
            time.sleep(10)
            self.test_playground_query_results_returns_10_items()
            self.count += 1
        
        html_list = self.browser.find_element(By.ID, "tbody")
        items = html_list.find_elements_by_tag_name("th")

        # Resets the counter
        self.count = 0

        self.assertEqual(len(items), 10)


    def test_playground_query_results_contains_the_predicate_and_label(self):
        self.browser.get('http://localhost:8000/playground')
        query = """PREFIX bd: <http://www.bigdata.com/rdf#> 
                PREFIX wd: <http://www.wikidata.org/entity/> 
                PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
                PREFIX wikibase: <http://wikiba.se/ontology#> 
                #added before 2016-10
                SELECT DISTINCT ?country ?countryLabel
                WHERE
                {
                ?country wdt:P31 wd:Q3624078 .
                #not a former country
                FILTER NOT EXISTS {?country wdt:P31 wd:Q3024240}
                #and no an ancient civilisation (needed to exclude ancient Egypt)
                FILTER NOT EXISTS {?country wdt:P31 wd:Q28171280}
                OPTIONAL { ?country wdt:P36 ?capital } .

                SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
                }
                ORDER BY ?country
                LIMIT 10
        """
        predicate = " is known as "
        self.browser.find_element(By.ID,"/query").send_keys(query)
        self.browser.find_element(By.ID,"predicate").send_keys(predicate)
        self.browser.find_element(By.ID,"submit").send_keys(Keys.RETURN)
        self.browser.implicitly_wait(60)

        # if it gets a 500 response, it waits 10 seconds and then runs the test again
        if(self.browser.title == "Server Error (500)" and self.count <= 3):
            print("error 500")
            self.test_playground_query_results_contains_the_predicate_and_label()

        label = self.browser.find_element(By.ID, "label_result")
        openai = self.browser.find_element(By.ID, "openai_result")
        hFace = self.browser.find_element(By.ID, "huggingface_result")

        # Resets the counter
        self.count = 0

        self.assertTrue(label.text.lower() in openai.text.lower())
        self.assertTrue(label.text.lower() in hFace.text.lower())
    

    def test_playground_predicate_has_more_than_one_dollar_simbol_fails(self):
        self.browser.get('http://localhost:8000/playground')

        query = "A query"
        predicate = " $ A predicate with more than one $ $ "
        self.browser.find_element(By.ID,"/query").send_keys(query)
        self.browser.find_element(By.ID,"predicate").send_keys(predicate)
        self.browser.find_element(By.ID,"submit").send_keys(Keys.RETURN)
        self.browser.implicitly_wait(5)

        self.assertEqual(self.browser.title, "")
    

    def test_stats_page_apply_results_are_not_empty(self):
        self.browser.get('http://localhost:8000/stats')
        select = Select(self.browser.find_element_by_id('queryDropDown'))
        select.select_by_value('1')
        self.browser.find_element(By.ID,"apply").send_keys(Keys.RETURN)
        self.browser.implicitly_wait(10)
        query = self.browser.find_element(By.ID, "query").text
        answerQuery = self.browser.find_element(By.ID, "answerQuery").text 

        self.assertTrue(query != '')
        self.assertTrue(answerQuery != '')


    def test_stats_page_results_contains_the_predicate_and_label(self):
        self.browser.get('http://localhost:8000/stats')
        select = Select(self.browser.find_element_by_id('queryDropDown'))
        select.select_by_value('3')
        self.browser.find_element(By.ID,"apply").send_keys(Keys.RETURN)
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.ID, "dropdownButton").send_keys(Keys.RETURN)
        predicate = self.browser.find_elements_by_class_name("dropdown-item")[0].text
        self.browser.find_element(By.ID, "predicateText").send_keys(predicate)
        self.browser.find_element(By.ID, 'submit').send_keys(Keys.RETURN)
        self.browser.implicitly_wait(100)

        # if it gets a 500 response, it waits 10 seconds and then runs the test again
        if(self.browser.title == "Server Error (500)" and self.count <= 3):
            print("error 500")
            self.test_stats_page_results()

        label = self.browser.find_element(By.ID, "label_result")
        openai = self.browser.find_element(By.ID, "openai_result")
        hFace = self.browser.find_element(By.ID, "huggingface_result")
        html_list = self.browser.find_element(By.ID, "tbody")
        items = html_list.find_elements_by_tag_name("th")
        
        # Resets the counter
        self.count = 0

        self.assertEqual(len(items), 19)
        self.assertTrue(label.text.lower() in openai.text.lower())
        self.assertTrue(label.text.lower() in hFace.text.lower())