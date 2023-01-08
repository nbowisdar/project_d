
from playwright.async_api import Page
from playwright_stealth import stealth_async

from loguru import logger


async def new_tab(browser, link) -> Page:
    page = await browser.new_page()
    await stealth_async(page)
    await page.goto(link)
    return page


async def support_steam(browser, link_support_steam):

    # create the page with steam's support
    page_steam_support = await new_tab(browser, link_support_steam)
    logger.info(link_support_steam)  ############################################
    await page_steam_support.goto(link_support_steam)
    # refrash steam's cookie
    await page_steam_support.pause()
    logger.info("get icon steam")
    await page_steam_support.get_by_role("link", name="Профиль").click()

    # TODO wait refrash page
    await page_steam_support.pause()
    # await expect(page_steam_support.locator())
    await page_steam_support.close()


async def auth_steam(browser, link_verification_steam):
    # get new tab for verification in the steam
    page_verif_steam = await new_tab(browser, link_verification_steam)

    # get link from the steam navigator panel
    # page.locator("#global_header").get_by_role("link", name="ПОДДЕРЖКА").click(button="middle")
    link_support_steam = await page_verif_steam.locator("#global_header"
                                              ).get_by_role("link", name="ПОДДЕРЖКА").get_attribute("href")

    await support_steam(browser, link_support_steam)

    # refrash page
    await page_verif_steam.reload()

    # click sign in
    await page_verif_steam.get_by_role("button", name="Sign In").click()

    # close page
    await page_verif_steam.close()

