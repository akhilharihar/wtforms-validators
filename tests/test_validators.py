import pytest
from wtforms_validators import (
    ValidationError,
    Accepted,
    ActiveUrl,
    Alpha,
    AlphaDash,
    AlphaSpace,
    AlphaNumeric
)


@pytest.mark.parametrize('test_v', ['yes', 'on', '1', 'true', True])
def test_accepted(test_v, dummy_form, dummy_field):
    validator = Accepted()
    dummy_field.data = test_v
    validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', [False, 'off', '0', 'false', 'no'])
def test_accepted_raises(test_v, dummy_form, dummy_field):
    validator = Accepted()
    dummy_field.data = test_v
    with pytest.raises(ValidationError):
        validator(dummy_form, dummy_field)


@pytest.mark.parametrize('url_val', [
    u'http://google.com:80',
    u'https://www.hotmail.com/login?testsdsfa',
    u'https://github.com/akhilharihar/wtforms-validators',
    u'https://www.facebook.com/login/device-based?login_attempt=1',
])
def test_active_url(url_val, dummy_form, dummy_field):
    validator = ActiveUrl()
    dummy_field.data = url_val
    validator(dummy_form, dummy_field)


@pytest.mark.parametrize('url_val', [
    u"http://www.foobar-.dk/",
    u"http://foobar.test",
    u"http://localhost.com:abc",
])
def test_active_url_raises(url_val, dummy_form, dummy_field):
    validator = ActiveUrl()
    dummy_field.data = url_val
    with pytest.raises(ValidationError):
        validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', ['lorem', 'python', 'this'])
def test_alpha(test_v, dummy_form, dummy_field):
    validator = Alpha()
    dummy_field.data = test_v
    validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', ['lorem1', '12321'])
def test_alpha_raises(test_v, dummy_form, dummy_field):
    validator = Alpha()
    dummy_field.data = test_v
    with pytest.raises(ValidationError):
        validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', ['lorem-', 'py-thon', '-this'])
def test_alpha_dash(test_v, dummy_form, dummy_field):
    validator = AlphaDash()
    dummy_field.data = test_v
    validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', ['lor-em1', '12@321'])
def test_alpha_dash_raises(test_v, dummy_form, dummy_field):
    validator = AlphaDash()
    dummy_field.data = test_v
    with pytest.raises(ValidationError):
        validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', ['lorem dfadsfs', 'python language'])
def test_alpha_space(test_v, dummy_form, dummy_field):
    validator = AlphaSpace()
    dummy_field.data = test_v
    validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', ['lorem1 jdlf', '12321 dfdsqer'])
def test_alpha_space_raises(test_v, dummy_form, dummy_field):
    validator = AlphaSpace()
    dummy_field.data = test_v
    with pytest.raises(ValidationError):
        validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', ['lorem12123', '232', '342pyon', 'th4532'])
def test_alpha_numeric(test_v, dummy_form, dummy_field):
    validator = AlphaNumeric()
    dummy_field.data = test_v
    validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', ['lorem1#234fdsa', '123ds@df21'])
def test_alpha_numeric_raises(test_v, dummy_form, dummy_field):
    validator = AlphaNumeric()
    dummy_field.data = test_v
    with pytest.raises(ValidationError):
        validator(dummy_form, dummy_field)
