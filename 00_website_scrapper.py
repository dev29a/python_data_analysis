import asyncio
from playwright.async_api import async_playwright

class Website_Scrapper:

    def __init__(self, url):
        self.site_title: str = ''
        self.site_body_text: str = ''


