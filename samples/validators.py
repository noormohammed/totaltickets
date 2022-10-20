from dataclasses import dataclass
from django.core.exceptions import ValidationError
from django.conf import settings
from datetime import datetime
from django.utils.translation import gettext_lazy as _
# from samples.conf import settings



def validate_is_int(value) -> int|ValidationError:
    """Validates if the given input value is an integer

    :param value: input that needs to be validated
    :type value: any
    :returns: validated value on success, raises ValidationError otherwise.
    :rtype: int
    :raises: :class:`ValidationError`: a:{value} is invalid
    """

    """
    Strictly validating integer values
    Although isinstance(value, int) is faster, it validates booleans
    (True/False) as integers. Hence using type for validation.
    Alternatively, integers can also be validated with regex as:

    `re.match("[-+]?\d+$", str(value))`
    """

    if type(value) == int:
        return value
    else:
        # using gettext_lazy only for demo purpose, f-strings preferred
        raise ValidationError(
            _('a:%(value)s is invalid'),
            params={'value': value},
        )


def validate_is_string(value) -> str|ValidationError:
    """
    Validates if the given input value is a string

    :param value: input that needs to be validated
    :type value: any
    :returns: validated value on success, raises ValidationError otherwise.
    :rtype: str
    :raises: :class:`ValidationError`: b:{value} is invalid
    """

    if value and isinstance(value, str) and not value.isspace():
        return value

    else:
        raise ValidationError(f'b:{value} is invalid')


def validate_is_datetime(value) -> datetime|ValidationError:
    """
    Validates if the given input is either a valid datetime string / object

    :param value: input that needs to be validated
    :type value: any
    :returns: validated value on success, raises ValidationError otherwise.
    :rtype: datetime
    :raises: :class:`ValidationError`: c is invalid
    """

    try:
        if isinstance(value, datetime):
            return value

        return datetime.strptime(value, settings.DATETIME_FORMAT)
    except:
        raise ValidationError(f'c is invalid')


def add_years(start_date, years) -> datetime:
    """
    Adds the given number of years to the given datetime

    :param start_date: datetime to which years must be added
    :type start_date: datetime
    :param years: number of years to be added
    :type years: int
    :returns: new datetime with the added number of years.
    :rtype: datetime
    """

    return start_date.replace(year=start_date.year + years)


def validate_is_next_year(value) -> bool|ValidationError:
    """
    Validates if the given value is a next year datetime value.

    We check if the datetime.year equals next year.

    :param value: input that needs to be validated
    :type value: any
    :returns: True for success, raises ValidationError otherwise.
    :rtype: bool
    :raises: :class:`ValidationError`: c is not next year
    """

    next_year_date = add_years(datetime.today(), 1)

    if validate_is_datetime(value).year == next_year_date.year:
        return True
    else:
        raise ValidationError(f'c is not next year')