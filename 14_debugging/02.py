## 02 - Weather Forecast
import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")

predict_weather()
# On line 5 we are passing random_choice a list containing
# the strings 'True' and 'False', which both evaluate as truthy.
# Replacing these with the values True and False will fix this bug.
