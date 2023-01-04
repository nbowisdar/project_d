import asyncio

from loguru import logger
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async

import works_fs


@logger.catch
async def main():
    async with async_playwright() as p:
        user_data_dir = works_fs.path_near_exefile('Profile') / "User Data"
        browser = await p.chromium.launch_persistent_context(user_data_dir=user_data_dir)
        page = await browser.new_page()
        await stealth_async(page)

        await page.goto('https://csgofloat.com/db')
        
        await page.screenshot(path=f'chrome.png')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
