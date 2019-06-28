import pytest
from wtforms import Label
from wtforms_validators import (
    ValidationError,
    Accepted,
    ActiveUrl,
    Alpha,
    AlphaDash,
    AlphaSpace,
    AlphaNumeric,
    Integer,
    NotEqualTo,
    IsJson,
    DisposableEmail
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


@pytest.mark.parametrize('test_v', ['123131', '23167', '1', '0'])
def test_integer(test_v, dummy_form, dummy_field):
    validator = Integer()
    dummy_field.data = test_v
    validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', ['123.231', 'lorem', None, False])
def test_integer_raises(test_v, dummy_form, dummy_field):
    validator = Integer()
    dummy_field.data = test_v
    with pytest.raises(ValidationError):
        validator(dummy_form, dummy_field)


@pytest.mark.parametrize(
    "field_val,equal_val", [
        ("test", "invalid_field_name"),
        ("bad_value", "foo")
    ]
)
def test_not_equal(
    field_val, equal_val, dummy_form, dummy_field, dummy_field_class
):
    """
    It should raise ValidationError if the values are equal
    """
    dummy_field.data = field_val
    other_field = dummy_field_class("test", label=Label("foo", "foo"))
    other_field.data = equal_val
    dummy_form["foo"] = other_field
    validator = NotEqualTo('foo')
    validator(dummy_form, dummy_field)


@pytest.mark.parametrize(
    "field_val,equal_val", [
        ("test", "test"),
        ("foo", "foo")
    ]
)
def test_not_equal_raises(
    field_val, equal_val, dummy_form, dummy_field, dummy_field_class
):
    """
    It should raise ValidationError if the values are equal
    """
    dummy_field.data = field_val
    other_field = dummy_field_class("test", label=Label("foo", "foo"))
    other_field.data = equal_val
    dummy_form["foo"] = other_field
    validator = NotEqualTo('foo')
    with pytest.raises(ValidationError):
        validator(dummy_form, dummy_field)


@pytest.mark.parametrize(
    'test_j', [
        '{}',
        "{\"213\":\"231\",\"test\":\"test1\", \
            \"twt\":{\"213\":\"231\",\"test\":\"test1\"}}"
    ]
)
def test_isjson(test_j, dummy_form, dummy_field):
    validator = IsJson()
    dummy_field.data = test_j
    validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_j', ['lorem', False, None])
def test_isjson_raises(test_j, dummy_form, dummy_field):
    validator = IsJson()
    dummy_field.data = test_j
    with pytest.raises(ValidationError):
        validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', [
    'example@example.com',
    'dsfjksdf@gmail.com'
    ])
def test_disposable_email(test_v, dummy_form, dummy_field):
    validator = DisposableEmail()
    dummy_field.data = test_v
    validator(dummy_form, dummy_field)


@pytest.mark.parametrize('test_v', ['lorem', 'dfskj@getnada.com'])
def test_disposable_email_raises(test_v, dummy_form, dummy_field):
    validator = DisposableEmail()
    dummy_field.data = test_v
    with pytest.raises(ValidationError):
        validator(dummy_form, dummy_field)
