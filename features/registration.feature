Feature: Registration functionality

  Scenario: Registration_with_all_fields
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno field
    When i eneter to continue button
    When i enters email field
    When i enetrs name field
    When i enters dob field
    When i enters password field
    When i enters pass continue field
    Then i eneters to validation  page

  Scenario: Registration with invalid email
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno1 field
    Then it shows  validation1 page

  Scenario: Registration with registered email
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno2 field
    When i eneter to continue button
    Then it show  validation2 page

  Scenario: Registration with invalid mobile no
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno3 field
    When i eneter to continue button
    When i enters email field1
    When i enetrs name field
    When i enters dob field
    When i enters password field
    When i enters pass continue field
    Then i eneters to validation3  page

  Scenario: Registration with registered mobile no
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno3 field
    When i eneter to continue button
    When i enters email field2
    When i enetrs name field
    When i enters dob field
    When i enters password field
    When i enters pass continue field
    Then i eneters to validation4  page

  Scenario: Registration with invalid name no
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno3 field
    When i eneter to continue button
    When i enters email field
    When i enetrs name field1
    When i enters dob field
    When i enters password field
    When i enters pass continue field
    Then i eneters to validation5  page

  Scenario: Registration with invalid password
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno field
    When i eneter to continue button
    When i enters email field
    When i enetrs name field
    When i enters dob field
    When i enters password field1
    When i enters pass continue field
    Then i eneters to validation6  page


  Scenario: Registration with valid no invalid name and password
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno field
    When i eneter to continue button
    When i enters email field
    When i enetrs name field2
    When i enters dob field
    When i enters password field2
    When i enters pass continue field
    Then i eneters to validation7  page

  Scenario: Registration with valid name invalid no and password
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno field
    When i eneter to continue button
    When i enters email field3
    When i enetrs name field
    When i enters dob field
    When i enters password field2
    When i enters pass continue field
    Then i eneters to validation8  page

  Scenario: Registration with valid pass invalid no and name
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno3 field
    When i eneter to continue button
    When i enters email field3
    When i enetrs name field2
    When i enters dob field
    When i enters password field
    When i enters pass continue field
    Then i eneters to validation9  page

  Scenario: Registration with valid mob invalid pass and valid name
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno field
    When i eneter to continue button
    When i enters email field
    When i enetrs name field
    When i enters dob field
    When i enters password field2
    When i enters pass continue field
    Then i eneters to validation10  page

  Scenario: Registration with valid mob invalid name and valid pass
   Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno field
    When i eneter to continue button
    When i enters email field
    When i enetrs name field2
    When i enters dob field
    When i enters password field
    When i enters pass continue field
    Then i eneters to validation11  page

  Scenario: Registration with valid nam invalid no and valid pass
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno field
    When i eneter to continue button
    When i enters email field3
    When i enetrs name field
    When i enters dob field
    When i enters password field
    When i enters pass continue field
    Then i eneters to validation12  page

  Scenario: Registration with empty fields
    Given i navigate to siginpage
    When i navigated to register page
    When i eneter to frame1 field
    When i enter mobileno field
    When i eneter to continue button
    When i enters email field
    When i enetrs name field
    When i enters dob field
    When i enters password field
    When i enters pass continue field
    Then i enetesr to validation13  page












