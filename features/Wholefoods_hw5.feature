# Created by mariamarques at 6/16/21
  # Adding line for testing git upload
Feature: Test wholefoods page


  Scenario: User can see the text ‘Regular’ and a product name
    Given Open Amazon wholefoods deals page
    Then Verify that every product has a text ‘Regular’ and a name

