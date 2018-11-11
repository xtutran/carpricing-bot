## story_greet <!--- The name of the story. It is not mandatory, but useful for debugging. --> 
* greet <!--- User input expressed as intent. In this case it represents users message 'Hello'. --> 
 - utter_name <!--- The response of the chatbot expressed as an action. In this case it represents chatbot's response 'Hello, how can I help?' --> 
 
## story_goodbye
* goodbye
 - utter_goodbye

## story_thanks
* thanks
 - utter_thanks
 
## story_name
* name{"name":"Sam"}
 - utter_greet

 ## story_pricing_03
* greet
 - utter_greet
* pricing
 - utter_ask_car
* car_model{"make": "BMW", "model": "i3"}
 - action_get_model_year
* year_model{"time": "2017-01-01T00:00:00.000Z"}
 - action_get_model_year
 - utter_ask_dob
* user_dob{"time": "2017-01-01T00:00:00.000Z"}
 - action_verify_dob
 - utter_ask_license_expire
* expire_date{"time": "2017-01-01T00:00:00.000Z"}
 - action_verify_expire_date
 - action_pricing