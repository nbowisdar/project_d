import asyncio

from playwright.async_api import async_playwright, Page, expect
from loguru import logger

from playwright_contrl import new_tab, auth_steam
import works_fs


@logger.catch
async def main():
    async with async_playwright() as p:
        user_data_dir = works_fs.path_near_exefile('Profile') / "User Data"
        browser = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            viewport={'width': 1920, 'height': 1080},
            headless=False
        )

        page_csgofloat = await new_tab(browser, 'https://csgofloat.com/db')

        # if this locator exists == auth in steam
        # get link and go to new tab
        if await page_csgofloat.locator("mat-toolbar").get_by_role("img").nth(1).is_visible(timeout=3):
            # click the img "auth steam" on the db page csgofloat
            link_verification_steam = await page_csgofloat.locator("mat-toolbar"
                                                                   ).get_by_role("img").nth(1).get_attribute("href")

            logger.info(link_verification_steam) ##############################

            await auth_steam(browser, link_verification_steam)

            await page_csgofloat.reload()

        await page_csgofloat.pause()
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
