from typing import Any

from ..http import HTTP


class Email:
    def __init__(self, http: HTTP, email: str, **data: Any) -> None:
        self._http = http
        self._email = email

        self.subject = data.pop('subject')
        self.from_email = data.pop('from_email')
        self.id = data.pop('id')

    async def get_content(self) -> str:
        """Retrieves the content of the email.

        Returns:
            str: The email content.
        """
        return await self._http.get_email_content(self._email, self.id)

    async def delete(self) -> bool:
        """Deletes the email.

        Returns:
            bool: True if successful.
        """
        await self._http.delete_email(self._email, self.id)
        return True

    def __repr__(self) -> str:
        x = [f'{attr}=\'{val}\'' for attr, val in self.__dict__.items() if not attr.startswith('_')]
        return f'Email({", ".join(x)})'
