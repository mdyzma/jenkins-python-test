from behave import given, when, then

@given(u'we have irisvmpy installed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given we have irisvmpy installed')

@when(u'we run program')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we run program')

@then(u'<species> will be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Something will be displayed')
