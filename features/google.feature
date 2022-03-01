
  Feature: features to test the functionalities

    Scenario: test to validate the search in google
      Given I navigate to the "https://www.google.com/" url
       When I perform a search with the word "Simetrik"
       Then I run the search
        And I Validate that the total of the results of the query is different from "0"