from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # open new page 

    page = context.new_page()

    page.goto("https://www.sephora.com/shop/skincare/")

    page.mouse.wheel(0, 4000)

    context.close()
    browser.close()


with sync_playwright as playwright:
    run(playwright)    
