from behave import *
from dicephrase import *
import unittest
from unittest.mock import patch
from unittest import TestCase
import builtins

use_step_matcher("re")


@given("User does not provide valid input")
def step_impl(context):
    mock = unittest.mock.MagicMock()
    user_input = ['\n', '']

    with patch('builtins.input', side_effect=user_input):
        mock()
        context.options_results = get_options()


@when("user presses enter without input")
def step_impl(context):
    pass


@then("the program should inform user that default settings will be used")
def step_impl(context):
    pass


@then("the program should return the default options")
def step_impl(context):
    expected_result = ['--no-caps', '-n 5', '-d .']

    print('expected: ', expected_result)
    print('actual: ', context.options_results)
    assert(context.options_results[1] is expected_result[1])


@given("User provides valid input for both options")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mock = unittest.mock.MagicMock()
    # mock.return_value = 2
    # mock.side_effect = '-'
    user_input = ['2', '-']

    with patch('builtins.input', side_effect=user_input):
        mock()
        context.options_results = get_options()


@when("options are returned")
def step_impl(context):
    print(context.options_results)


@then("they should contain the input in a list of strings")
def step_impl(context):
    expected_result = ['--no-caps', '-n 2', '-d -']

    print('expected: ', expected_result)
    print('actual: ', context.options_results)
    assert(context.options_results[1] is expected_result[1])
