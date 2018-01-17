# this is the steps file for behave project

from dicephrase import *
from behave import *


@given('get_word_list runs')
def step_impl(context):
    pass


@when('eff wordlist is fetched')
def step_impl(context):
    context.test_wordlist = get_word_list('eff')


@then('the first entry is "11111	abacus"')
def step_impl(context):
    assert '11111   abacus' in context.test_wordlist
