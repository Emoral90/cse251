from datetime import datetime, timedelta
import threading
import requests
import json

class Request_thread(threading.Thread):

    def __init__(self, url):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}

    def run(self):
        response = requests.get(self.url)
        # Check the status code to see if the request succeeded.
        if response.status_code == 200:
            self.response = response.json()
        else:
            print('RESPONSE = ', response.status_code)

class Deck:

    def __init__(self, deck_id):
        self.id = deck_id
        self.reshuffle()

    def reshuffle(self):
        # TODO - add call to reshuffle using a thread
        t_rs = threading.Thread(target=)

    def draw_card(self):
        # TODO add call to get a card using a thread
        pass

    def draw_endless(self):
        return self.draw_card()

if __name__ == '__main__':

    # TODO - run the program team_get_deck_id.py and insert
    #        the deck ID here. You only need to run the 
    #        team_get_deck_id.py program once.

    deck_id = 'lqj6wdy7d5ui'

    # TODO Loop 55 times and call draw_endless, then print out the name of each card
    print(Deck.draw_endless(deck_id))