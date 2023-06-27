from behave import *
from selenium import webdriver
from features.pages.Itemcheckout_page import Itemcheckout_page


@given(u'i navigated to home page')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.valid_title()


@when(u'i navigated to siginpage')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_sigin_page1()


@when(u'i enter to valid product')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.valid_product("Laptops")


@when(u'i enter to valid product1')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.valid_product1("Laptops")


@when(u'i enter search button')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.search_butto()


@when(u'i enter to title3')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.title3()


@when(u'i enter to search item')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.search_item()


@when(u'i enter to title4')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.title4()


@when(u'i enter to item')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.item()


@when(u'i enter buynow')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.buynow()


@when(u'i entet title 5')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.title5()


@when(u'i enter to google login')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_google_field()


@when(u'i enter to google login1')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.glogin()


@when(u'i eneter mail field')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_emailfield("ast984904@gmail.com")


@when(u'i enter to next')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_next()


@when(u'i enter to password')
def step_impl(context):
    context.itemcheckout = Itemcheckout_page(context.driver)
    context.itemcheckout.enter_to_passwordfield("surya@123")


@when(u'i enter to pass next button')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_passnext()


@when(u'i enter pin')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.dapin("201307")


@when(u'i enter name')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.daname("surya")


@when(u'i enter address')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.daaddress("203, 401, sr plaza , noida")


@when(u'i enetr locality')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.dalocality("hospital")


@when(u'i enter mob')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.daaltmob("9560432706")


@when(u'i enter radiobtn')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.daradiobtn()


@when(u'i enter savecont')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.dasavecont()


@when(u'i enter paymbtn')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.dapymbtn()


@when(u'i enter dacod')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.dacod()


@when(u'i enter plc order')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.daplc()


@then(u'it to enter cod title')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.codtitle()


@when(u'i enter paybtn')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.paybtn()


@when(u'i enetr debit card')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.dadd()


@when(u'i enter dc no')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.dacno("5260990218592810")


@when(u'i enter mon')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.mon()


@when(u'i enter year')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.yy()


@when(u'i enter cvv')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.dacvv("861")


@then(u'it will enter to payment page')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.dapay()


@when(u'i enetr net baanking')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.danb()


@when(u'i enter otb')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.otb()


@when(u'i enter dascpa')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.dascpa()


@when(u'i enter bank')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.bank()


@then(u'it will enter to bank page')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.banktitle()


@when(u'i eneter mail field1')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_emailfield11("ast98490@gmail.com")


@when(u'i eneter mail field2')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_emailfield11("shtl9196@gmail.com")


@when(u'i navigated to register page1')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_register_page1()


@when(u'i eneter to frame2 field')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_frame_field()


@when(u'i eneter mail field3')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_emailfield11("ast984904@gmail.com")


@when(u'i enter to next3')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_next12()


@when(u'i enter to password3')
def step_impl(context):
    context.itemcheckout = Itemcheckout_page(context.driver)
    context.itemcheckout.enter_to_passwordfield12("surya@123")


@when(u'i enter to pass next button3')
def step_impl(context):
    itemcheckout = Itemcheckout_page(context.driver)
    itemcheckout.enter_to_passnext12()
