## story_pricing_02
* greet
 - utter_greet
* pricing
 - utter_ask_car
* car_model{"make": "BMW", "model": "i3"}
 - utter_ask_model_year
* year_model
 - action_get_model_year
 - utter_ask_dob
* user_dob{"time": "2017-01-01T00:00:00.000Z"}
 - action_verify_dob
 - utter_ask_license_expire
* expire_date{"time": "2017-01-01T00:00:00.000Z"}
 - action_verify_expire_date
 - action_pricing
* thanks
 - utter_goodbye
 
## pricing_with_chitchat
* greet
 - utter_greet
* chitchat
 - utter_chitchat
 - utter_name
* name{"name": "John"}
 - utter_greet
* pricing
 - utter_ask_car
* car_model{"make": "BMW", "model": "i3", "time": "2017-01-01T00:00:00.000Z"}
 - action_get_model_year
 - utter_ask_license_expire
* expire_date{"time": "2017-01-01T00:00:00.000Z"}
 - utter_ask_dob
* user_dob{"time": "2017-01-01T00:00:00.000Z"}
 - action_pricing
* thanks
 - utter_goodbye
 
## fallback
  - utter_fallback