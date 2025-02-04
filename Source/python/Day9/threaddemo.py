import threading
import requests
import time

def fetch_url(url, results):
    response = requests.get(url)
    html_content = response.text  
    # Get the HTML content as a string
    with open("output.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    # Simulate a delay to ensure the URL is accessed within 1 second
    time.sleep(1)
    
    results.append(f"Fetched {url}:\n{html_content}\n")

urls = [
    "https://www.cmrcetexaminations.com/beeserp/login.aspx",
]

threads = []
results = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url, results))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# Display results in the console after all threads are done
for result in results:
    print(result)

print("All URLs fetched")
