import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os 

driver = uc.Chrome()
driver.maximize_window()
driver.get("https://google.com")
time.sleep(1)

search_box = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
time.sleep(1)
import random
import time

for char in "song lyrics finder":
    search_box.send_keys(char)
    time.sleep(random.uniform(0.2, 0.1))  
search_box.send_keys(Keys.RETURN)
time.sleep(1)

first_data = driver.find_element(By.XPATH , '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a/h3')
first_data.click()
time.sleep(1)

search_item = driver.find_element(By.XPATH,'//*[@id="search-word"]')
search_item.send_keys("kabhi kabhi")
search_item.send_keys(Keys.RETURN)
time.sleep(5)

results = driver.find_elements(By.CSS_SELECTOR,'.gsc-webResult.gsc-result')

songs = []
for r in results:
    try:
        title = r.find_element(By.CSS_SELECTOR, ".song-title").text
        link = r.find_element(By.CSS_SELECTOR, "a.gs-title").get_attribute("href")
        if title and link:
            songs.append({"title": title, "link": link})
    except:
        pass
excel_file_path = "kabhi_kabhi_results.xlsx"
# Save results to Excel
if os.path.exists(excel_file_path):
    os.remove(excel_file_path)
    
if songs:
    df = pd.DataFrame(songs)
    df.to_excel(excel_file_path, index=False)
    print(" Saved results to kabhi_kabhi_results.xlsx")
else:
    print(" No results found — maybe the site’s structure is different.")



# breakpoint()
driver.quit()



# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pandas as pd
# from urllib.parse import quote # Used to format the search term for the URL

# # --- 1. SETUP ---
# driver = uc.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 15) # Wait for a maximum of 15 seconds

# # --- 2. DEFINE SEARCH TERM AND BUILD THE URL ---
# # This is much more reliable than trying to click on search bars.
# # We build the search results URL directly.
# search_term = "kabhi kabhi"
# # The quote() function handles spaces and special characters (e.g., "kabhi kabhi" -> "kabhi+kabhi")
# formatted_search = quote(search_term)
# url = f"https://www.chosic.com/song-finder/?q={formatted_search}"

# # --- 3. NAVIGATE TO THE PAGE ---
# print(f"Navigating to: {url}")
# driver.get(url)

# # --- 4. LOOP THROUGH RESULTS AND EXTRACT DETAILS ---
# song_data = []
# try:
#     # First, wait until the song containers are visible on the page.
#     # The selector finds all <article> tags that have the class 'song-item'. This is the container for each song.
#     song_containers_xpath = "//article[@class='song-item']"
#     wait.until(EC.presence_of_all_elements_located((By.XPATH, song_containers_xpath)))
    
#     # Now, find all of them
#     song_containers = driver.find_elements(By.XPATH, song_containers_xpath)
#     print(f"Found {len(song_containers)} songs on the page.")

#     # Loop through each song container we found
#     for song in song_containers:
#         try:
#             # Use relative XPaths (starting with '.') to find elements *inside* the container
#             title = song.find_element(By.XPATH, ".//h3[@class='song-title']").text
#             artist = song.find_element(By.XPATH, ".//p[@class='song-artist']").text
#             # The link is on the 'a' tag inside the 'h3' title element
#             link = song.find_element(By.XPATH, ".//h3[@class='song-title']/a").get_attribute('href')
            
#             # Append the extracted data as a dictionary to our list
#             song_data.append({
#                 'Title': title,
#                 'Artist': artist,
#                 'Link': link
#             })
#             print(f"Scraped: {title} by {artist}")

#         except Exception as e:
#             # If one song has a weird format and fails, we print an error and continue with the next one.
#             print(f"Could not extract details for one song. Skipping. Error: {e}")

# except Exception as e:
#     print(f"Could not find any song results. The page might have changed or there was a loading error. Error: {e}")

# # --- 5. SAVE TO EXCEL ---
# if song_data:
#     df = pd.DataFrame(song_data)
#     filename = f"{search_term.replace(' ', '_')}_chosic_results.xlsx"
#     df.to_excel(filename, index=False)
#     print(f"\n✅ Success! Saved {len(song_data)} songs to {filename}")
# else:
#     print("\n❌ No data was scraped.")

# driver.quit()