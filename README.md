# Gpa.lu api wrapper

Asynchronous api wrapper for the disposable email service [gpa.lu](https://gpa.lu).

## Installation

```
pip install gpa.lu
```

## Usage example

```py
import asyncio

from gpalu import Gpalu


async def main() -> None:
    async with Gpalu() as gpa:
        # Les.codes, yarien.eu, gpa.lu, and saucent.online are all compatible.
        all_emails = await gpa.get_emails('hello@gpa.lu')
        recent_email = all_emails[0]

        # Retrieves the email content
        content = await recent_email.get_content()

        print(f'From: {recent_email.from_email}')
        print(f'Subject: {recent_email.subject}')
        print(f'Content: {content}')

        # If you want to delete the email
        await recent_email.delete()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

```

## Contribute

make pull request
