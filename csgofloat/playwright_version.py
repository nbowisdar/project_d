import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async


async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch()  # in () write our parameters
            page = await browser.new_page()
            # await stealth_async(page)
            # await page.goto('https://hmaker.github.io/selenium-detector/')
            # await page.screenshot(path=f'example-{browser_type.name}.png')
            await page.goto('https://abrahamjuliot.github.io/creepjs/')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            # await page.goto('http://f.vision/')
            # await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

asyncio.run(main())

