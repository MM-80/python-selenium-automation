# Created by mariamarques at 6/24/21
Feature: Loops test cases


  Scenario: Bestsellers links can be opened
    Given Open Amazon Best Sellers
    When Verify the best sellers {expected_links} link
    Then User can click on top links and verify that new page opens
