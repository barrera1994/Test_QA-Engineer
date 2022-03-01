from behave import then, use_step_matcher
from hamcrest import equal_to, assert_that, only_contains

use_step_matcher("re")

@when(u'I perform a search with the word "(?P<keyword>.*)"')
def step_impl(context, keyword):
    return context.google.send_value_input(keyword)
