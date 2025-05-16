from behave import given, when, then
from pages.login_page import LoginPage

@given('que o usuário está na página de login')
def step_open_login_page(context):
    context.page = LoginPage()
    context.page.open()

@when('ele preenche o usuário "{username}" e senha "{password}"')
def step_fill_credentials(context, username, password):
    context.page.fill_login(username, password)

@when('clica no botão de login')
def step_click_login(context):
    context.page.submit()

@then('ele deve ver a página inicial')
def step_verify_home(context):
    assert context.page.is_logged_in()
    context.page.close()

