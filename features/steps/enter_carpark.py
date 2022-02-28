from behave import *
from Vehicle import Vehicle
from Carpark import Carpark


@given(u'an empty car park')
def step_impl(context):
    car_park = Carpark(15)
    car_park.add_car(Vehicle("abc123", "Car"))
    context.carpark = car_park


@when(u'a car with a reg number of "abc" enters the car park')
def step_impl(context):
    car1 = Vehicle("abc123", "Car")
    context.carpark.add_car(car1)


@then(u'a car with reg number of "abc" should occupy a space in the car park')
def step_impl(context):
    assert context.car_park.spaces[0].reg == "abc123"


@then(u'the car should not occupy the list and will return the string "CALL THE POLICE!"')
def step_impl(context):
    count = 0
    for car in context.carpark.spaces:
        if car.reg == "abc123":
            count += 1

    assert count == 1

