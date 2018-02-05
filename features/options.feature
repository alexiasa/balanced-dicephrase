Feature: User Options
  Users can specify options for passphrase output

  Scenario: Invalid or empty input
    Given User does not provide valid input
    When user presses enter without input
    Then the program should inform user that default settings will be used
    And the program should return the default options


  Scenario: Valid inputs
    Given User provides valid input for both options
    When options are returned
    Then they should contain the input in a list of strings



