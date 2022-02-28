Feature: Vehicles entering the carpark

    Scenario: A car enters a car park with spaces
        Given an empty car park
        When a car with a reg number of "abc123" enters the car park
        Then a car with reg number of "abc123" should occupy a space in the car park

    Scenario: A duplicate reg plate attempts to enter car park
        Given a car park with a car parked in it
        When a car with a reg number of "abc123" enters the car park
        Then the car should not occupy the list and will return the string "CALL THE POLICE!"
