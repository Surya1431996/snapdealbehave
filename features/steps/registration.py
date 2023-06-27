from behave import *
from selenium import webdriver
from features.pages.registration import Registration_Page


@given(u'i navigate to siginpage')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_sigin_page()


@when(u'i navigated to register page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_register_page()


@when(u'i eneter to frame1 field')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_frame_field()


@when(u'i enter mobileno field')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_mob_field("teja05863@gmail.com")


@when(u'i enter mobileno1 field')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_mob_field("teja05863@gmail")


@when(u'i enter mobileno2 field')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_mob_field("ast98490@gmail.com")


@when(u'i enter mobileno3 field')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_mob_field("teju89011@gmail.com")


@when(u'i eneter to continue button')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_cont_field()


@when(u'i enters email field')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_email_field("8985209434")


@when(u'i enters email field1')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_email_field("898520943")


@when(u'i enters email field2')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_email_field("9560432706")


@when(u'i enters email field3')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_email_field("")


@when(u'i enetrs name field')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_name_field("surya")


@when(u'i enetrs name field1')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_name_field("s")


@when(u'i enetrs name field2')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_name_field("")


@when(u'i enters dob field')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_dob_field()


@when(u'i enters password field')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_password_field("Surya@143")


@when(u'i enters password field1')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_password_field("Surya")


@when(u'i enters password field2')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_password_field("")


@when(u'i enters pass continue field')
def step_impl(context):
    registration = Registration_Page(context.driver)
    registration.enter_to_pass_conti_field()


@then(u'i eneters to validation  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    expemsg = "Please enter verification code (OTP) sent to:"
    assert registration.enter_to_verify_valid_text.__eq__(expemsg)


@then(u'it shows  validation1 page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid mobile number or email"
    assert registration.enter_to_verify_valid_text1.__eq__(wrnmsg)


@then(u'it show  validation2 page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid mobile number or email"
    assert registration.enter_to_verify_valid_text2.__eq__(wrnmsg)


@then(u'i eneters to validation3  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid mobile number"
    assert registration.enter_to_verify_valid_text3.__eq__(wrnmsg)


@then(u'i eneters to validation4  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "An account already exists with +91 9560432706"
    assert registration.enter_to_verify_valid_text4.__eq__(wrnmsg)


@then(u'i eneters to validation5  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid name"
    assert registration.enter_to_verify_valid_text5.__eq__(wrnmsg)


@then(u'i eneters to validation6  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid password"
    assert registration.enter_to_verify_valid_text6.__eq__(wrnmsg)


@then(u'i eneters to validation7  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid name"
    assert registration.enter_to_verify_valid_text5.__eq__(wrnmsg)
    wrnmsg1 = "Please enter a valid password"
    assert registration.enter_to_verify_valid_text6.__eq__(wrnmsg1)


@then(u'i eneters to validation8  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid mobile number"
    assert registration.enter_to_verify_valid_text3.__eq__(wrnmsg)
    wrnmsg1 = "Please enter a valid password"
    assert registration.enter_to_verify_valid_text6.__eq__(wrnmsg1)


@then(u'i eneters to validation9  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid mobile number"
    assert registration.enter_to_verify_valid_text3.__eq__(wrnmsg)
    wrnmsg1 = "Please enter a valid name"
    assert registration.enter_to_verify_valid_text5.__eq__(wrnmsg1)


@then(u'i eneters to validation10  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid password"
    assert registration.enter_to_verify_valid_text6.__eq__(wrnmsg)


@then(u'i eneters to validation11  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid name"
    assert registration.enter_to_verify_valid_text5.__eq__(wrnmsg)


@then(u'i eneters to validation12  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg = "Please enter a valid mobile number"
    assert registration.enter_to_verify_valid_text3.__eq__(wrnmsg)


@then(u'i enetesr to validation13  page')
def step_impl(context):
    registration = Registration_Page(context.driver)
    wrnmsg1 = "Please enter a valid mobile number"
    assert registration.enter_to_verify_valid_text3.__eq__(wrnmsg1)
    wrnmsg = "Please enter a valid name"
    assert registration.enter_to_verify_valid_text5.__eq__(wrnmsg)
    wrnmsg2 = "Please enter a valid password"
    assert registration.enter_to_verify_valid_text6.__eq__(wrnmsg2)






