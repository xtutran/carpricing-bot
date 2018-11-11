<!--- Make sure to update this training data file with more training examples from https://forum.rasa.com/t/grab-the-nlu-training-dataset-and-starter-packs/903 --> 
## intent:greet
- hey
- hello
- hello there
- good morning
- good evening
- hey there
- hey dude


## intent:goodbye
- goodbye
- have a nice day
- see you around
- see you later


## intent:thank
- Thanks
- Thank you
- Thank you so much
- Perfect


## intent:affirm
- yes yes yes
- yeah
- absolutely
- for sure
- definitely


## intent:name
- My name is [Juste](name)  <!--- Square brackets contain the value of entity while the text in parentheses is a a label of the entity --> 
- I am [Josh](name)
- I'm [Lucy](name)
- People call me [Greg](name)
- Usually people call me [Amy](name)
- My name is [John](name)
- You can call me [Sam](name)
- Please call me [Linda](name)
- I am [Richard](name)
- I'm [Tracy](name)
- Call me [Sally](name)
- I am [Philipp](name)
- I am [Charlie](name)


<!-- ## intent:joke
- Can you tell me a joke?
- I would like to hear a joke
- Tell me a joke
- A joke please
- Tell me a joke please
- I would like to hear a joke
- I would loke to hear a joke, please
- Can you tell jokes?
- Please tell me a joke
- I need to hear a joke -->


## intent:pricing
- I would like to have some car insurance
- Automobile insurance
- any offer for my car
- need an insurance policy
- insure my car

<!-- - make
- model
- year
- age
- date -->

<!-- ## intent:make
- I have a [BMW](make) 
- I have a [Toyota](make)
- I own a [Honda](make)
- I just buy a [Kia](make) -->
<!-- - [Chevrolet](make) -->


## intent:car_model
- I have [Toyota](make) [T100](model)
- I own [Honda](make) [Civic CRX](model)
- I buy [Kia](make) [Morning](model)
- I have [BMW](make) [i3](model) model
- I drive [Chevrolet](make) [200SX](model) model
<!-- - I have a [Chevrolet](make) [200SX](model) [2010](year) -->
<!-- - I have a [Honda](make) [Civic](model) [2000](year) -->
<!-- - [200SX](model) -->


## intent:year_model
- model 2018
- model 2017
- year 2015
- year 1999

## intent:user_dob
- date of birth 
- birth date
- birth

<!-- ## intent:issue_date
- The issue date
- Issue date
- issued date
- issue
- My license has been issued -->

## intent:expire_date
- license will expire
- The expiration date
- expired date
- expiration date
- Expired
- Expiration

## intent:chitchat
- can you share your boss with me?
- i want to get to know your owner
- i want to know the company which designed you
- i want to know the company which generated you
- i want to know the company which invented you
- i want to know who invented you
- May I ask who invented you?
- please tell me the company who created you
- please tell me who created you
- tell me more about your creators
- tell me more about your founders
- Ahoy matey how are you?
- are you alright
- are you having a good day
- Are you ok?
- are you okay
- Do you feel good?
- how are things going
- how are things with you?
- How are things?
- how are you
- how are you doing
- how are you doing this morning
- how are you feeling
- how are you today
- How are you?
- How is the weather today?
- What's the weather like?
- How is the weather?
- What is the weather at your place?
- Do you have good weather?
- Is it raining?
- What's it like out there?
- Is it hot or cold?
- Beautiful day, isn't it?
- What's the weather forecast?
- Is it quite breezy outside?

## intent:stop
- ok then you cant help me
- that was shit, you're not helping
- you can't help me
- you can't help me with what i need
- i guess you can't help me then
- ok i guess you can't help me
- that's not what i want
- ok, but that doesnt help me
- this is leading to nothing
- this conversation is not really helpful
- you cannot help me with what I want
- I think you cant help me
- hm i don't think you can do what i want
- stop
- stop go back
- do you get anything?
- and you call yourself bot company? pff
- and that's it?
- nothing else?


## lookup:make  <!-- no list to specify lookup table file -->
data/make_list.txt

## lookup:model  <!-- no list to specify lookup table file -->
data/model_list.txt



<!-- ## intent:age
- I am [48](age)
- [20](age)

## intent:year
- It is model [2017](year)
- Model [1990](year)
- [2000](year)

## intent:date
- [13-11-2017](date)
- [20-11-1989](date) -->