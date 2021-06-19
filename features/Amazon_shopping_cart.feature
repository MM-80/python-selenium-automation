# Created by mariamarques at 6/3/21
Feature: Verify the shopping cart

  Scenario: User can verify that the shopping cart is empty
    Given Open Amazon page
    When click on cart icon
   Then verify that is empty