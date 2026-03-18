# uv add playwright
# uv sync
# playwright install
# above will only work after activating the .venv 

from turtle import title
from playwright.sync_api import Browser, sync_playwright

def main():
    with sync_playwright() as p:
        browser  = p.chromium.launch(headless=False)
        page = browser.new_page()
        # page.goto("https://www.nobelprize.org/prizes/physics/1956/shockley/biographical/")
        page.goto("https://www.nab.com.au/")
    
        title = page.title()

        print(f"Page title: {title}")
        print(page.inner_text('body'))

        links = page.locator("a[href]").all()

        links = page.eval_on_selector_all(
        "a[href]",
        "elements => elements.map(el => el.href)")

        for link in links:
            print(link)


        browser.close()

if __name__ == "__main__":
    main()
