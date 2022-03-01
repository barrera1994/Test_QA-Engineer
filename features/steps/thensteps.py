from behave import then, use_step_matcher
from hamcrest import equal_to, assert_that, only_contains

use_step_matcher("re")


@then(u'I run the search')
def step_impl(context):
    return context.google.run_search()

@then(u'I Validate that the total of the results of the query is different from "(?P<quantity_results>.*)"')
def step_impl(context, quantity_results):
    return context.google.validate_query(quantity_results)