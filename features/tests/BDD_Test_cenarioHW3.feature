# Created by mariamarques at 5/31/21
Feature: Cancelling an order on Amazon

  Scenario: User can search for cancelling an order on Amazon
    Given Open Amazon page
    When Click on help icon
    And  Input Cancel Order in search the Help Library field
    Then Tap enter