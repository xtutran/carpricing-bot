# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import requests
import json
from rasa_core_sdk import Action
import pandas as pd
from duckling import DucklingWrapper
# from rasa_core.events import SlotSet
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.events import Restarted

logger = logging.getLogger(__name__)
d = DucklingWrapper()


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = requests.get('http://api.icndb.com/jokes/random').json() #make an apie call
        joke = request['value']['joke'] #extract a joke from returned json response
        dispatcher.utter_message(joke) #send the message back to the user
        return []

# class ActionAskModelYear(Action):
#     def name(self):
#         # define the name of the action which can then be included in training stories
#         return "action_ask_model_year"

#     def run(self, dispatcher, tracker, domain):
#         # what your action should do
#         user_message = tracker.latest_message['text']

#         dt = d.parse_time(user_message)


#         model_year = dt[0][:4] if dt is not None else None
#         return [SlotSet("model_year", model_year)]

class ActionGetModelYear(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_get_model_year"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        user_message = tracker.latest_message['text']
        dt = d.parse_time(user_message)
        print(user_message)
        print(dt)
        years = [v['text'] for v in dt if v['value']['grain'] == u'year']
        model_year = None
        if len(years) == 1:
            # dispatcher.utter_template("utter_ask_dob", tracker, silent_fail=True)
            model_year = years[0]
        # else:
        #     dispatcher.utter_template("utter_ask_model_year", tracker, silent_fail=True)

        return [SlotSet("model_year", model_year)]


class ActionVerifyDob(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_verify_dob"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        # user_message = tracker.latest_message['text']
        # print(tracker.latest_message)

        dt = tracker.get_slot('time')
        age = None
        print(dt)
        if dt is not None:
            age = int((pd.datetime.now() - pd.to_datetime(dt[0][:10])).days / 365)
            #if age >= 20:
                #dispatcher.utter_template("utter_ask_license_expire", tracker, silent_fail=True)
            if age < 20:
                dispatcher.utter_message("You are under 20 years old and not eligible to drive a car. "
                                         "Could you come back again later?")
                # dispatcher.utter_template("utter_ask_dob", tracker, silent_fail=True)
        else:
            dispatcher.utter_message("I cannot recognise your date of birth. Could you enter again?")
            # dispatcher.utter_template("action_verify_dob", tracker, silent_fail=True)
        return [SlotSet("user_age", age), SlotSet("user_dob", dt[0])]


class ActionVerifyExpireDate(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_verify_expire_date"

    def run(self, dispatcher, tracker, domain):
        # user_message = tracker.latest_message['text']
        # print(tracker.latest_message)

        # res = d.parse_time(user_message)
        dt = tracker.get_slot('time')
        exp_period = None
        if dt is not None:
            # dt = res[0]['value']['value'][:10]
            exp_period = round(((pd.to_datetime(dt[0][:10]) - pd.datetime.now()).days / 365), 2)
            if exp_period > 0:
                dispatcher.utter_message("Thank you for your info. Please hold on & we are proccessing your inquery!")
                # dispatcher.utter_message("Your car pricing should be: 100$")
            else:
                dispatcher.utter_message("Your driver license already expired. Please renew it first!")
        else:
            dispatcher.utter_message("I cannot recognise your license expire date. Could you enter again?")

        return [SlotSet("license_exp", exp_period)]


class ActionPricing(Action):
    def name(self):
        return "action_pricing"

    def run(self, dispatcher, tracker, domain):
        make = tracker.get_slot('make')
        model = tracker.get_slot('model')
        model_year = tracker.get_slot('model_year')
        user_age = tracker.get_slot("user_age")
        license_exp = tracker.get_slot("license_exp")

        print(make)
        print(model)
        print(model_year)
        print(user_age)
        print(license_exp)
        dispatcher.utter_message('Your car insurance pricing should be: 100$') 
        return [Restarted(), AllSlotsReset()]
