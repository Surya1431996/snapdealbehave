from behave import *

from features.pages.login import Login_Page


@given(u'i navigated to siginpage')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.valid_title()
    loginpage.enter_to_sigin_page()


@when(u'i navigate to register page')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_register_page()


@when(u'i eneter to frame field')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_frame_field()


@when(u'i enter mobile field')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_mob_field("ast98490@gmail.com")


@when(u'i enter to continue button')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_cont_field()


@then(u'i enter to validation1page')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    wrnmsg = "Please enter verification code (OTP) sent to:"
    assert loginpage.enter_to_v1.__eq__(wrnmsg)


@then(u'i enter to validation2page')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    wrnmsg = "Create an account on Snapdeal"
    assert loginpage.enter_to_v2.__eq__(wrnmsg)


@then(u'i enter to validation3page')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    wrnmsg = "Please enter a valid mobile number or email"
    assert loginpage.enter_to_v3.__eq__(wrnmsg)


@then(u'i enter to validation4page')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    wrnmsg = "Please enter your mobile number or email"
    assert loginpage.enter_to_v4.__eq__(wrnmsg)


@when(u'i enter to google field')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_google_field()


@when(u'i enter to email field')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_emailfield("ast9849044@gmail.com")


@when(u'i eneter to next')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_next()


@when(u'i enter to password field')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_passwordfield("surya@123")


@when(u'i enter to pass next')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_passnext()


@then(u'i enter to validation 5 page')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    wrnmsg = "Create an account on Snapdeal"
    assert loginpage.enter_to_v5.__eq__(wrnmsg)


@then(u'i enter to validation 6 page')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_v6()


@when(u'i enter mobile field1')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_mob_field("asshahi1991@gmail.com")


@when(u'i enter mobile field2')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_mob_field("assha")


@when(u'i enter mobile field3')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_mob_field("")


@when(u'i enter to email field1')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_emailfield("ast984904@gmail.com")


@when(u'i enter to password field1')
def step_impl(context):
    loginpage = Login_Page(context.driver)
    loginpage.enter_to_passwordfield("surya@123")