from playwright.sync_api import sync_playwright
import sys

APPS = [
    "https://nyc311-ai-etl.streamlit.app/",
    "https://triage-desk-te0v.onrender.com/",
    "https://grounded-rag-nr9dmpzrh79njaamznujzv.streamlit.app/",
]

failed = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    for url in APPS:
        print("\n======================================")
        print(f"Opening: {url}")
        print("======================================")

        page = browser.new_page()

        try:
            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=120000
            )

            page.wait_for_timeout(5000)

            # STREAMLIT SLEEP PAGE
            wake_button = page.get_by_text(
                "Yes, get this app back up!",
                exact=False
            )

            if wake_button.count() > 0:
                print("Streamlit app is sleeping.")
                print("Clicking wake-up button...")

                wake_button.first.click()

                for attempt in range(18):
                    print(f"Waiting for Streamlit: {attempt + 1}/18")

                    page.wait_for_timeout(10000)

                    try:
                        page.reload(
                            wait_until="domcontentloaded",
                            timeout=90000
                        )
                    except Exception:
                        pass

                    if page.get_by_text(
                        "Yes, get this app back up!",
                        exact=False
                    ).count() == 0:
                        print("Streamlit sleep page disappeared.")
                        break
                else:
                    raise Exception("Streamlit app failed to wake.")

            # RENDER COLD START
            elif "onrender.com" in url:
                print("Render app detected.")
                print("Waiting for possible cold start...")

                for attempt in range(12):
                    page.wait_for_timeout(10000)

                    try:
                        page.reload(
                            wait_until="domcontentloaded",
                            timeout=90000
                        )
                    except Exception:
                        pass

                    content = page.content().lower()

                    if (
                        "render" not in page.title().lower()
                        or "loading" not in content
                    ):
                        print("Render app appears awake.")
                        break

            else:
                print("App already appears awake.")

            page.wait_for_timeout(5000)

            print(f"Title: {page.title()}")
            print(f"Final URL: {page.url}")

            content = page.content()

            if "This app has gone to sleep" in content:
                raise Exception("Streamlit app is still sleeping.")

            print("SUCCESS")

        except Exception as e:
            print(f"FAILED: {e}")
            failed.append(url)

        finally:
            page.close()

    browser.close()


if failed:
    print("\nFAILED APPS:")
    for app in failed:
        print(app)
    sys.exit(1)

print("\nALL APPS CHECKED SUCCESSFULLY")
