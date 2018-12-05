""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy.util import smart_run

import schedule

import threading

import sys
import time

# login credentials
insta_username = ''
insta_password = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,bypass_suspicious_attempt=True, bypass_with_mobile=True)


def liking_thread(self,session):
    while 1:
        print ("starting the thread to like users")
        try:
            session.like_by_tags(['designer'], amount=10) #weight=5 words most prioritized #1
            time.sleep(300)
            session.like_by_tags(['freelancers'], amount=9) #weight=4 words                   #2
            time.sleep(300)        
            session.like_by_tags(['artist'], amount=8) #weight=3 words                   #3
            time.sleep(300)
            session.like_by_tags(['gamedesign'], amount=7) #weight=2 words                   #4
            time.sleep(300)
            session.like_by_tags(['blizzard'], amount=6) #weight=1 words                   #5
            time.sleep(300)
            
        except KeyboardInterrupt:
            sys.exit()        



def following_thread(self,session):
    while 1:
        print ("starting the thread to follow users")
        try:
            session.follow_by_tags(['designer'], amount=10)
            time.sleep(300)
            session.follow_user_following(['behance', 'artstationhq', 'upworkinc'], amount=5, randomize=False, sleep_delay=200)
            
        except KeyboardInterrupt:
            sys.exit()   




with smart_run(session):
    """Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                      delimit_by_numbers=True,
                                       max_followers=10000,
                                        min_followers=100,
                                        min_following=100)
    
    session.set_dont_include(["fashion", "clothing", "handbags", "software engineer"])
    session.set_dont_like(["fashion", "clothing","handbags"])
    session.like_by_tags(["freelancedesigner"], amount=10)
    session.follow_by_tags(["freelancedesigner"], amount=10)
    session.follow_user_following(['behance', 'artstationhq', 'upworkinc'], amount=5, randomize=False, sleep_delay=200)
    session.follow_user_following(['behance', 'artstationhq', 'upworkinc'], amount=5, randomize=False, sleep_delay=200)
    session.follow_user_following(['behance', 'artstationhq', 'upworkinc'], amount=5, randomize=False, sleep_delay=200)
    session.follow_user_following(['behance', 'artstationhq', 'upworkinc'], amount=5, randomize=False, sleep_delay=200)
    session.follow_user_following(['behance', 'artstationhq', 'upworkinc'], amount=5, randomize=False, sleep_delay=200)
    session.like_by_tags(['freelancers','designers'], amount=10) #weight=4 words                   #2
    time.sleep(300)        
    try:
        t1=threading.Thread(following_thread, session)
        t1.daemon = True
        t1.start()
        t2=threading.Thread(liking_thread, session)
        t2.daemon = True
        t2.join()
    except:
        print ("Error: unable to start threads")    



