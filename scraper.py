from playwright.async_api import async_playwright

async def fetch_job_titles():
    async with async_playwright() as p:
        browser = await p.chromium.connect("ws://playwright:3000")
        page = await browser.new_page()
        await page.goto("https://jobs.ua/vacancy", timeout=60000)

        # Wait for the job elements to load
        await page.wait_for_selector("li.b-vacancy__item")

        # Query all job elements
        job_items = await page.query_selector_all("li.b-vacancy__item")
        job_titles = []

        # Extract job title from each job element
        for item in job_items:
            title_element = await item.query_selector("a.b-vacancy__top__title")
            if title_element:
                title = (await title_element.inner_text()).strip()
                job_titles.append(title)

        await browser.close()
        return job_titles

