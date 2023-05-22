import asyncio
from playwright.async_api import async_playwright




async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('https://www.sephora.com/shop/skincare')
        print(await page.title())

    
    # # Wait for the product list to load
    # page.wait_for_selector('.css-ix8km1')

    # # Get all product links on the page
    # product_links = page.query_selector_all('.css-ix8km1 a')
    # product_links = [link.get_attribute('href') for link in product_links]

    # Loop through each product link and extract the product name and price
    # for link in product_links:
    #     page.goto(link)
    #     page.wait_for_selector('.css-1gkpw3d')

    #     product_name = page.query_selector('.css-1pgnl76').inner_text()
    #     product_price = page.query_selector('.css-0').inner_text()

    #     print(product_name, product_price)

    await browser.close()


asyncio.run(main())