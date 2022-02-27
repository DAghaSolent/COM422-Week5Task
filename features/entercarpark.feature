Feature: Vehicles entering the carpark

    Scenario: A car enters a car park with spaces
        Given an empty car park
        When a car with a reg number of "abc" enters the car park
        Then a car with reg number of "abc" should occupy a space in the car park



