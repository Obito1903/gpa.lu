from asyncio import AbstractEventLoop, get_event_loop
from typing import Any, Dict, Optional

from aiohttp import ClientSession

from .constants import BASE_URL


class HTTP:
    def __init__(
        self,
        session: Optional[ClientSession] = None,
        loop: Optional[AbstractEventLoop] = None,
    ) -> None:
        self.loop = loop or get_event_loop()
        self.session = session or ClientSession(loop=loop, connector=aiohttp.TCPConnector(verify_ssl=False))

    async def close(self) -> None:
        await self.session.close()

    async def request(self, method: str, path: str, data: Optional[Dict[str, Any]] = {}) -> str:
        """Initiates an http request.

        Args:
            method (str): Request method.
            path (str): URL path.
            data (Optional[Dict[str, Any]], optional): Request data. Defaults to {}.

        Returns:
            str: The content of the response.
        """
        async with self.session.request(method, BASE_URL + path, data=data) as response:
            return await response.text()

    async def delete_email(self, email: str, id: str) -> str:
        """Deletes the email message.

        Args:
            email (str): The email address.
            id (str): The id of the email message.

        Returns:
            str: The content of the response
        """
        return await self.request('POST', email, {'delete': id})

    async def get_email_content(self, email: str, id: str) -> str:
        """Retrieves the email message content.

        Args:
            email (str): The email address.
            id (str): The email message's id.

        Returns:
            str: The content of the email.
        """
        return await self.request('GET', f'{email}/{id}?noheader')

    async def get_email_inbox(self, email: str) -> str:
        """Retrieves the inbox of the email.

        Args:
            email (str): The email address.

        Returns:
            str: The content of the response
        """
        return await self.request('GET', email)
