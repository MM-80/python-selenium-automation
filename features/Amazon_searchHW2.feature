# Created by mariamarques at 5/27/21
Feature: Test Amazon searchHW2
  # Enter feature description here

  Scenario: user can search for solutions of cancelling an order on Amazon
    Given Open Amazon Help page
    When Input Cancel Order in search Help Library field
    And tap enter
    Then Verify cancel items or order is present

