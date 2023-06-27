Feature: Login functionality

  Scenario: Login_with_all_ registered fields
    Given i navigated to siginpage
    When i navigate to register page
    When i eneter to frame field
    When i enter mobile field
    When i enter to continue button
    Then i enter to validation1page

  Scenario: Login_with_all_ not registered mail fields
    Given i navigated to siginpage
    When i navigate to register page
    When i eneter to frame field
    When i enter mobile field1
    When i enter to continue button
    Then i enter to validation2page

  Scenario: Login_with_all_ not valid mail fields
    Given i navigated to siginpage
    When i navigate to register page
    When i eneter to frame field
    When i enter mobile field2
    When i enter to continue button
    Then i enter to validation3page

  Scenario: Login_with_all_ empty fields
    Given i navigated to siginpage
    When i navigate to register page
    When i eneter to frame field
    When i enter mobile field3
    When i enter to continue button
    Then i enter to validation4page

  Scenario: Login_with_un registered gmail fields
    Given i navigated to siginpage
    When i navigate to register page
    When i eneter to frame field
    When i enter to google field
    When i enter to email field
    When i eneter to next
    When i enter to password field
    When i enter to pass next
    Then i enter to validation 5 page

  Scenario: Login_with_registered gmail fields
    Given i navigated to siginpage
    When i navigate to register page
    When i eneter to frame field
    When i enter to google field
    When i enter to email field1
    When i eneter to next
    When i enter to password field1
    When i enter to pass next
    Then i enter to validation 6 page





