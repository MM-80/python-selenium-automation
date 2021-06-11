# Created by mariamarques at 6/9/21
Feature: Test Amazon Cart
  # Enter feature description here

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Input pencils on search field
    And Click on the first product
    And Click on add to cart button
    Then Verify cart has one item

