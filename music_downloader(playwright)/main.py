import time
import asyncio
from playwright.async_api import async_playwright
import sys
import re

async def download_song(song_name: str):
    """
    This function downloads a song from the specified website.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set headless=True to run in background
        page = await browser.new_page()
        try:
            await page.goto("https://tidal.squid.wtf/")

            # Type the song name into the search box and press Enter
            await page.locator('input[type="text"]').fill(song_name)
            await page.locator('input[type="text"]').press("Enter")

            # Wait for search results to appear

            # Now that results are loaded, find and click the first download button
            async with page.expect_download() as download_info:
                time.sleep(3)
                print("sleep ended searching for it now")
                await page.click('button[title="Download track"]')
            
            import os
            download = await download_info.value
            
            download_dir = "~/Downloads/"
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
            
            file_path = os.path.join(download_dir, download.suggested_filename)
            await download.save_as(file_path)
            print(f"Downloaded '{song_name}' successfully!")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

async def main():
    if len(sys.argv) != 2:
        print("Usage: python download_song.py <path_to_text_file>")
        song_name = input("Enter the song name")
        await download_song(song_name.strip())
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as f:
            song_name = f.readline().strip()
            file_empty = True
            for line in f:
                song_name = line.strip()
                if song_name:
                    file_empty = False
                    await download_song(song_name)
            if file_empty:
                print("The file is empty")
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")

if __name__ == "__main__":
    asyncio.run(main())

