Feature: Expert claims question which is sent by API

  Background:
    Given I am at expert landing page

  @chrome.browser
    @expert.in.session
  Scenario Outline: Expert claims question and receive message
    Given I log in with Facebook
    When  An asker log in
    And   I click on START WORKING button
    And   Asker posts a question
    And   I wait to claim question the question that asker've posted
    And   I win the question
    And   Asker sends <message>
    Then  I should see asker's <message>

    Examples: Message types
      | message    |
      | text       |
      | image      |
      | excel file |