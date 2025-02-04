from bs4 import BeautifulSoup
import requests
import smtplib

# URL of the product
url = "https://www.amazon.in/dp/B07WDKKJ45/?_encoding=UTF8&ref_=cct_cg_Budget_2d1&pf_rd_p=375fdfe4-1f68-4b1c-af1e-66eb7600ee3e&pf_rd_r=P7D3K0HD5F64V9NNHQJ6&th=1"

# Set headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Send a request to the URL
response = requests.get(url, headers=headers)
response.raise_for_status()  # Raise an error if the request fails

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Debug: Print the HTML content
# with open("amazon_page.html", "w", encoding="utf-8") as file:
#     file.write(soup.prettify())

# Extract the product title
title = soup.find("span", id="productTitle")
if title:
    title = title.get_text().strip()
    print(f"Product Title: {title}")
else:
    print("Product title not found!")
    exit()

# Extract the price
price_whole = soup.find("span", class_="a-price-whole")
if price_whole:
    price = price_whole.get_text().replace(",", "").replace(".", "")  # Remove commas and decimals
    price_as_float = float(price)
    print(f"Product Price: {price_as_float}")
else:
    print("Price not found!")
    exit()

# Set the price below which you would like to get a notification
BUY_PRICE = 100

# Send an email if the price is below the threshold
if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for ₹{price_as_float}!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login('dvssjayaprakash@gmail.com', "xklt rbue kqru xpkf")  # Use your App Password
        connection.sendmail(
            from_addr="dvssjayaprakash@gmail.com",
            to_addrs="dhulipallajayaprakash@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
    print("Email sent successfully!")
else:
    print("Price is not below the threshold. No email sent.")