#!/usr/bin/env python3

from ppadb.client import Client as AdbClient
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
import threading
import time
import io

class ArknightsRA2Farmer(threading.Thread):
    def __init__(self, run_event):
        super().__init__()
        self.run_event = run_event
        self.device = AdbClient(host="127.0.0.1", port=5037).device("emulator-5554")
        
    def wipe_data(self, before_4th=False):
        #tap on dots-menu
        self.device.shell("input tap 1030 662")
        time.sleep(1)
        #wipe data
        self.device.shell(f"input tap {1111 if before_4th else 1151} 574")
        time.sleep(1.5)
        #confirm wipe
        self.device.shell("input tap 984 466")
        time.sleep(1.5)
        #confirm again
        self.device.shell("input tap 966 474")
        
    def get_areas_from_screenshot_for_event(self):
        screencap = Image.open(io.BytesIO(self.device.screencap()))
        return (screencap.crop((77,198,227,335)),screencap.crop((1155,100,1195,130)))
        
    def solve_event_node(self):
        #tap on right side
        self.device.shell("input tap 1067 406")
        time.sleep(2)
        #get event icon and act count from screenshot
        event_icon, act_count = self.get_areas_from_screenshot_for_event()
        #try to solve event
        y = 337
        for i in range(5):
            #tap on choice area 2 times
            self.device.shell(f"input tap 1027 {y}")
            time.sleep(2)
            self.device.shell(f"input tap 1027 {y}")
            time.sleep(3)
            #tap on screen (in case of reward)
            self.device.shell("input tap 350 420")
            time.sleep(2)
            event_icon2, act_count2 = self.get_areas_from_screenshot_for_event()
            #check act count area (equal zero means match)
            if pixelmatch(act_count, act_count2) == 0:
                #check event icon area
                if pixelmatch(event_icon, event_icon2) != 0:
                    #if not matches then the choice was "Leave"
                    break
            else:
                #if not equal then choice was correct
                time.sleep(3)
                self.device.shell("input tap 1067 406")
                time.sleep(3)
                #tap on alright choice
                self.device.shell("input tap 907 400")
                time.sleep(3)
                #tap again
                self.device.shell("input tap 1155 399")
                time.sleep(2)
                self.device.shell("input tap 1155 399")
                time.sleep(3.5)
                return True
            y += 40
        return False
        
    def solve_battle_node(self):
        #tap on start battle button on map
        self.device.shell("input tap 1176 569")
        time.sleep(2)
        #tap on start button in prepare-for-battle menu (squad composition)
        self.device.shell("input tap 1194 668")
        time.sleep(1.5)
        #confirm no ops
        self.device.shell("input tap 1010 470")
        time.sleep(10)
        #exit battle
        self.device.shell("input tap 70 49")
        time.sleep(2)
        #confirm exit
        self.device.shell("input tap 1016 476")
        time.sleep(4.5)
        #tap on screen for reward
        self.device.shell("input tap 618 392")
        time.sleep(8)
        
    def prepare_two_meals(self):
        #tap on cooking menu
        self.device.shell("input tap 566 664")
        time.sleep(2)
        #tap on auto+1 2 times
        for i in range(2):
            self.device.shell("input tap 941 569")
            time.sleep(1)
        #tap on prepare button
        self.device.shell("input tap 1131 563")
        time.sleep(2)
        #tap on centre
        self.device.shell("input tap 667 458")
        time.sleep(2)
        #exit cooking menu
        self.device.shell("input tap 33 27")
        time.sleep(1.5)
        
    def do_one_run(self):
        #Start 
        #tap start button
        self.device.shell("input tap 1176 642")
        time.sleep(9)
        
        #Intro
        #tap intro node
        self.device.shell("input tap 675 317")
        time.sleep(2)
        #tap on start-battle-button
        self.device.shell("input tap 1192 563")
        time.sleep(9)
        #10 times tap on dialog
        for i in range(12):
            self.device.shell("input tap 705 591")
            time.sleep(1.5)
        time.sleep(2)
        #tap on your response
        self.device.shell("input tap 1100 440")
        time.sleep(2)
        for i in range(12):
            self.device.shell("input tap 705 591")
            time.sleep(1.5)
        time.sleep(2)
        self.device.shell("input tap 1100 440")
        time.sleep(2)
        for i in range(3):
            self.device.shell("input tap 705 591")
            time.sleep(1.5)
        #tap on response 3 times
        for i in range(3):
            self.device.shell("input tap 1100 442")
            time.sleep(1)
        time.sleep(3)
        #tap on exit button
        self.device.shell("input tap 69 49")
        time.sleep(1.5)
        #confirm exit
        self.device.shell("input tap 941 472")
        time.sleep(9)
        
        #First event node
        #swipe
        self.device.shell("input tap 1000 75")
        time.sleep(1)
        self.device.shell("input swipe 1000 424 1000 75")
        time.sleep(2)
        #tap event node
        self.device.shell("input tap 869 142")
        time.sleep(2)
        if not self.solve_event_node():
            self.wipe_data(before_4th=True)
            return
        
        #First battle node
        self.device.shell("input swipe 600 420 1200 420")
        time.sleep(2)
        #tap node
        self.device.shell("input tap 457 73")
        time.sleep(2)
        self.solve_battle_node()
        
        #go to next day
        self.device.shell("input tap 1180 81")
        time.sleep(5)
        self.device.shell("input tap 632 589")
        time.sleep(2)
        
        #2nd day
        #Second battle node
        self.device.shell("input tap 511 524")
        time.sleep(2)
        self.solve_battle_node()
        
        #Second event
        self.device.shell("input tap 368 535")
        time.sleep(2)
        if not self.solve_event_node():
            self.wipe_data(before_4th=True)
            return
        
        #to next day
        self.device.shell("input tap 1180 81")
        time.sleep(5)
        self.device.shell("input tap 632 589")
        time.sleep(2)
        
        #3rd day
        self.device.shell("input swipe 198 337 499 353")
        time.sleep(2)
        
        self.prepare_two_meals()
        
        #Third battle node
        self.device.shell("input tap 550 519")
        time.sleep(2)
        self.solve_battle_node()
        
        #Third event node
        self.device.shell("input tap 812 468")
        time.sleep(2)
        if self.solve_event_node():
            #to next day
            self.device.shell("input tap 1180 81")
        else:
            #skip current day and go to next one
            self.device.shell("input tap 1180 81")
            time.sleep(1.5)
            self.device.shell("input tap 1186 164")
            time.sleep(2)
            self.device.shell("input tap 1002 470")
            time.sleep(2)
            self.device.shell("input tap 1180 81")
            
        time.sleep(6.5)
        #tap on reward
        self.device.shell("input tap 659 604")
        time.sleep(5)
        self.device.shell("input tap 643 593")
        time.sleep(3)
        
        #4th day - end of run
        self.wipe_data()
        
    def run(self):
        while self.run_event.is_set():
            self.do_one_run()
            time.sleep(4.5)
    
if __name__ == '__main__':
    run_event = threading.Event()
    run_event.set()
    farmer = ArknightsRA2Farmer(run_event)
    print("Press Ctrl+C to stop.")
    farmer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        run_event.clear()
        print("\nStop-signal received. Waiting for farmer to finish current run...")
        farmer.join()
