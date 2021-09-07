import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from secret_info import wildrift
from comment_list import comments_list_noemo
import random
import time



class instaBot:

    username_1 = wildrift[0]
    password_1 = wildrift[1]
    hashtags =  ['wildrifttürkiye', 'loltr', 'loltürkiye']
    comments = comments_list_noemo
    links = []
    postnum = 0

    def __init__(self):
        self.browser = webdriver.Chrome('./chromedriver.exe')
        self.login()
        self.hustle()

    def login(self):    
        self.browser.get('https://www.instagram.com/')
        print('Opened browser')
        print('Waiting')
        time.sleep(3)

        #input username
        username_field = self.browser.find_element_by_xpath("//input[@name='username']")
        username_field.clear()
        username_field.send_keys(self.username_1)
        print('Entered username')
        time.sleep(1)

        #input password
        password_field = self.browser.find_element_by_xpath("//input[@name='password']")
        password_field.clear()
        password_field.send_keys(self.password_1)
        print('Entered password')
        time.sleep(1)
        
        #submit button
        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        print('Clicked submit')
        time.sleep(3)

    def hustle(self):
        self.getTopPosts()
        
        self.execute()
        
        self.finalize()
        
        
    #Browses the hashtags in the hashtag list and tores them in list
    def getTopPosts(self):
        for hashtag in self.hashtags:
            self.browser.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
            print('Accessing hashtag: ' + hashtag)
            time.sleep(4)
            
            links = self.browser.find_elements_by_tag_name('a')
            condition = lambda link: '.com/p/' in link.get_attribute('href')
            valid_links = list(filter(condition, links))

            for i in range (0,9):
                link = links[i].get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

    
    # Execute the like and comment operatin 
    def execute(self):
        postnum = 1
        for link in self.links:
            self.browser.get(link)
            print('Accessing post ' + str(postnum) + ' out of ' + str(len(self.links)))
            time.sleep(4)

            # added the try excet
            try:
                self.browser.find_element_by_partial_link_text('wildriftmobatr')
                print('Account activity found')
                
            except NoSuchElementException:
                self.like()
                after_like_time = random.randint(3,6)
                time.sleep(after_like_time)

                self.comment()
                after_comment_time = random.randint(4,7)
                time.sleep(after_comment_time)

                self.postnum += 1
                post_wait_time = random.randint(60,90)
                time.sleep(post_wait_time)


    
    def comment(self):

        
        try:            
            comment_input = lambda: self.browser.find_element_by_tag_name('textarea')
            comment_input().click()
            comment_input().clear()
            print('Commenting...')
            comment = random.choice(self.comments)
            for letter in comment:
                comment_input().send_keys(letter)
                delay = random.randint(1,7) / 30
                time.sleep(delay)

            comment_input().send_keys(Keys.RETURN)
        
        except NoSuchElementException:
            print('Can not comment')

        
        

    def like(self):
        like_button = lambda: self.browser.find_element_by_class_name('fr66n')
        print('Liked the post')
        like_button().click()

    def finalize(self):
        print('Total posts liked:' + str(self.postnum))
        self.browser.close()
        sys.exit()



garyvee = instaBot()