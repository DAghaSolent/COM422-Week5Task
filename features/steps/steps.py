from behave import *
from Car import Car
from Motorbike import Motorbike
from Carpark import Carpark


@given(u'an empty car park')
def step_impl(context):
    car_park = Carpark(15)
    context.carpark = car_park


@when(u'a car with a reg number of "abc" enters the car park')
def step_impl(context):
    car = Car("abc123", "Honda")
    context.carpark()

@then(u'a car with reg number of "abc" should occupy a space in the car park')
def step_impl(context):
