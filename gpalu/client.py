import re
from asyncio import AbstractEventLoop
from typing import List, Optional

from aiohttp import ClientSession

from .constants import EMAILS_REGEX, GPALU_EMAIL_REGEX
from .http import HTTP
from .models import Email


class Gpalu:
    def __init__(
        self,
        loop: Optional[AbstractEventLoop] = None,
        session: Optional[ClientSession] = None,
    ) -> None:
        self.loop = loop
        self.session = session

        self.http: HTTP = HTTP(session=session, loop=loop)

    async def close(self) -> None:
        await self.http.close()

    async def __aenter__(self) -> 'Gpalu':
        return self

    async def __aexit__(self, *_) -> None:
        await self.close()

    async def get_emails(self, email_address: str) -> List[Email]:
        """Retrieves a list of emails.

        Args:
            email_address (str): The email address.

        Returns:
            List[Email]: A list of Email objects.
        """
        assert re.match(
            GPALU_EMAIL_REGEX, email_address
        ), 'The email address is either invalid or does not use a valid Gpa.lu domain.'

        content = await self.http.get_email_inbox(email_address)
        return [
            Email(self.http, email_address, id=x, subject=i, from_email=l)
            for x, i, l in re.findall(EMAILS_REGEX, content)
        ]
