Feature: Expert claims question

  Background:
    Given I am at landing page

  @chrome.browser
  Scenario: Expert claims question and receive message
    Given I am an expert
    When  An asker log in
    And   I start working
    And   Asker posts a question
    And   I wait to claim question
    And   I win the question
    And   Asker sends a message
    Then  Then I should see asker's message