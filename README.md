# wtforms-validators
Additional validators for wtforms used in web applications frequently.

## Installation
```
pip install wtforms-validators
```

## Validators

- [Accepted](#Accepted)
- [ActiveUrl](#ActiveUrl)
- [Alpha](#Alpha)
- [AlphaDash](#AlphaDash)
- [AlphaSpace](#AlphaSpace)
- [AlphaNumeric](#AlphaNumeric)
- [NotEqualTo](#NotEqualTo)
- [Integer](#Integer)
- [IsJson](#IsJson)
- [DisposableEmail](#DisposableEmail)

__Examples__ :

```
from wtforms_validators import ActiveUrl, Alpha
...

class SignupForm(Form):
    login_id = StringField('login Id', [DataRequired(), Alpha()])
    url = StringField('profile url', [DataRequired(), ActiveUrl()])
```

### Accepted:
Validates if the field is yes, on, 1, true or `True`. Can be used for validating terms of service, opt-ins etc.,

Parameters:
* message - (optional) - Error message to raise in case of a validation error.

### ActiveUrl:
Validates if the URL is active by checking A or AAAA DNS records.

Parameters:
* message - (optional) - Error message to raise in case of a validation error.

### Alpha:
Validates the field to include alphabetic characters only.

Parameters:
* message - (optional) - Error message to raise in case of a validation error.

### AlphaDash:
Validates the field to only include alphabets and dash(`-`).

Parameters:
* message - (optional) - Error message to raise in case of a validation error.

### AlphaSpace:
Validates the field to only include alphabets and spaces.

`Note:` This validator does not strip the field's value, so input containing only spaces will still be valid. You will either have to register a filter to strip input data or add another validator to check if the field cannot contain only spaces.

Parameters:
* message - (optional) - Error message to raise in case of a validation error.

### AlphaNumeric:
Validates the field to only include alphabets and numbers.

Parameters:
* message - (optional) - Error message to raise in case of a validation error.

### NotEqualTo:
Checks the field under validation is not equal to another field.

Parameters:
* fieldname – The name of the other field.
* message - (optional) - Error message to raise in case of a validation error.

### Integer
Validates the field to only include numbers.

Parameters:
* message - (optional) - Error message to raise in case of a validation error.

### IsJson
The field under validation must be a valid JSON string.

Parameters:
* message - (optional) - Error message to raise in case of a validation error.

### DisposableEmail
The email address should not belong to a disposable email service provider.

Parameters:
* message - (optional) - Error message to raise in case of a validation error.