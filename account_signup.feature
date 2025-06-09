Feature: User Registration and Login

  Scenario: Create new account and login successfully
    Given the user is on the home page
    When the user navigates to the create account page
    And the user fills the registration form with valid data
    Then the user should be registered successfully

    When the user logs out
    And the user logs in with the registered credentials
    Then the user should be logged in successfully
