# wtforms-validators
This package does not replace the wtforms builtin validators, instead it provides few validators which are not provided in wtforms package that are frequently used in web applications. 

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

__Examples__ :

```
from wtforms_validators import ActiveUrl, Alpha
...

class SignupForm(Form):
    login_id = StringField('login Id', [DataRequired(), Alpha()])
    url = StringField('profile url', [DataRequired(), ActiveUrl()])
```

You can also use wild card to import all validators from this package.

```
from wtforms_validators import *
```

### Accepted:
Validates if the field is either yes, on, 1, true or `True`. Can be used for validating terms of service, opt ins etc.,

Parameters: 
* message - (optional) - Error message to raise in case of a validation error.

### ActiveUrl:
Validates if the url is active by checking A or AAAA dns records.

Parameters: 
* message - (optional) - Error message to raise in case of a validation error.

### Alpha:
The field under validation must be entirely of alphabetic characters.

Parameters: 
* message - (optional) - Error message to raise in case of a validation error.

### AlphaDash:
The field under validation must be entirely of alphabets and dash(`-`).

Parameters: 
* message - (optional) - Error message to raise in case of a validation error.

### AlphaSpace:
The field under validation must be entirely of alphabets and spaces. 

`Note:` The data in field is not stripped, so the field will be valid even if it only contains spaces. You will need to either add a filter to strip input data or add another validator to check if the field does not contain only spaces.

Parameters: 
* message - (optional) - Error message to raise in case of a validation error.

### AlphaNumeric:
The field under validation must be entirely of alphabets and numbers.

Parameters:
* message - (optional) - Error message to raise in case of a validation error.

### NotEqualTo:
validates if the value of the field under validation is not equal to other field in the form.

Parameters:
* fieldname – The name of the other field.
* message - (optional) - Error message to raise in case of a validation error.

### Integer
The field under validation must be entirely of numbers.

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