# Created by mariamarques at 7/6/21
Feature: # Enter feature name here
  # Enter feature description here
  

  Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon Orders link
 Then Verify Sign In page is opened

Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify 'Your Shopping Cart is empty.' text present
