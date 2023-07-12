from selenium import webdriver

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Maximize the Chrome window

# Path to your Chrome webdriver executable
chromedriver_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # Replace with the path to your chromedriver.exe

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)

# Open YouTube and perform the search
search_query = "sleeping music"
youtube_url = f"https://www.youtube.com"
driver.get(youtube_url)
search_input = driver.find_element_by_name("search_query")
search_input.send_keys(search_query)
search_input.submit()

# Wait for the search results to load
driver.implicitly_wait(5)

# Click on the first search result
first_result = driver.find_element_by_css_selector("#video-title")
first_result.click()

# Close the browser
driver.quit()
