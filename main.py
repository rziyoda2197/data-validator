class DataValidator:
    def __init__(self, data):
        self.data = data

    def validate_email(self):
        import re
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(email_regex, self.data))

    def validate_phone_number(self):
        return self.data.isdigit() and len(self.data) == 10

    def validate_date(self):
        from datetime import datetime
        try:
            datetime.strptime(self.data, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def validate_password(self):
        return (self.data.isalnum() or self.data.isalpha() or self.data.isdigit()) and len(self.data) >= 8

    def validate_credit_card_number(self):
        import re
        credit_card_regex = r"^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9]{2})[0-9]{12}|3[47][0-9]{13})$"
        return bool(re.match(credit_card_regex, self.data))

    def validate(self):
        return {
            "email": self.validate_email(),
            "phone_number": self.validate_phone_number(),
            "date": self.validate_date(),
            "password": self.validate_password(),
            "credit_card_number": self.validate_credit_card_number()
        }
```

```python
# Test qilish
data = {
    "email": "example@example.com",
    "phone_number": "1234567890",
    "date": "2022-01-01",
    "password": "examplepassword",
    "credit_card_number": "4111111111111111"
}

validator = DataValidator(data)
print(validator.validate())
