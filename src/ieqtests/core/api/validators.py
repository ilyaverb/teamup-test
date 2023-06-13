from django.core.exceptions import ValidationError


class LetterValidator:
    def __call__(self, value):
        allowed_letters = {'а', 'б', 'в', 'г', 'д'}
        if value not in allowed_letters:
            raise ValidationError(f"Invalid letter `{value}`. Allowed letters are: `а`, `б`, `в`, `г`, `д`")
