# Created by mariamarques at 6/9/21
Feature: Amazon Best Sellers tests
  # Enter feature description here

  Scenario: Amazon Best Sellers displays 5 links
    Given Open Amazon Best Sellers page
    Then Verify 5 links are displayed
