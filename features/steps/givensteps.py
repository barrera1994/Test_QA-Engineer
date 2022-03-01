from behave import given, use_step_matcher

use_step_matcher("re")

@given(u'I navigate to the "(?P<url>.*)" url')
def visit_login(context, url):
    return context.google.visit_sitie(url)
