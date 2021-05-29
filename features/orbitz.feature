
Feature: Orbitz flight booking system


  Scenario: Verify orbitz flight booking user journey
    Given I am on orbitz homepage
    When I click on flight selection option
    And I select roundtrip option
    And Enter source location
    And Enter destination location
    And  I Pick a date range and search for flights
    Then I validate the search results