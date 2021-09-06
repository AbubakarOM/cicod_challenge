# Created by Abubakar Omolaja Muhammed at 2021-09-05

Feature: SignUp Page

  As a new CICOD customer
  I should be able to SignUp
  So that I can perform transactions.

  Background: That a user with valid creds will be granted access
    Given I am on the CICOD SignUp Page

  Scenario: SignUp
    User with valid credentials can SignUp successfully.

    When I enter the web "URL" on the browser
    And I click on "SignUp
    And I insert the "Email"
    And I select the "country code"
    And I insert the "phone number"
    And I inser the "business name"
    And I click "Next"
    Then I select the "Plan"
    When I click the "Terms of use"
    And I click "Start free trial"
    Then I should see a message display telling to go and varify my account from my "Email"
    And I copy "password" from my Email
    And I insert my current password
    And I insert my new password
    And I insert my new password to confirm
    And I click Done
    Then I close the browser
  


