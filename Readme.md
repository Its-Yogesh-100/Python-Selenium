# 🛒 Amazon Product Scraper with Python, Selenium & BeautifulSoup

This project demonstrates a complete, real-world **web scraping and browser automation solution** using **Python**. It automates product search on **Amazon India**, extracts essential details like product title, price, and link, and saves them in a structured **CSV file** that can be analyzed in Excel or Google Sheets.

Whether you're learning **web automation**, practicing **data extraction**, or building a portfolio project using **Selenium and BeautifulSoup**, this scraper is an excellent hands-on example.

---

## 📌 Project Overview

This Python script:

- Opens the Amazon.in website
- Searches for laptops across multiple pages
- Scrapes the HTML of each product listing
- Extracts key product information (title, price, link)
- Saves the data in a clean and readable CSV file

Ideal for:
- Data analysts and Python learners
- Anyone exploring **automated web scraping**
- Developers practicing **browser interaction and dynamic HTML parsing**

---

## 🔧 Tools & Technologies

- **Python 3.x** – Scripting and data handling
- **Selenium WebDriver** – Web automation and browser control
- **BeautifulSoup (bs4)** – HTML parsing and data extraction
- **Pandas** – Data manipulation and CSV export
- **ChromeDriver** – Required for Selenium to control the Chrome browser

---

## 🗂 Project Structure

```
📁 Python-Selenium
├── project.py                    # Automates Amazon product search & saves HTML
├── collect.py                    # Parses saved HTML and generates CSV file
├── main.py                       # Basic Selenium test with python.org
├── locating_single_elements.py   # Example of locating a single element
├── locating_multiple_elements.py # Example of scraping multiple elements
├── data/                         # Folder containing scraped HTML files
├── data.csv                      # Final output file with product information
```

---

## 🚀 How to Set Up & Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/Its-Yogesh-100/Python-Selenium.git
cd Python-Selenium
```

### Step 2: Install Dependencies
```bash
pip install selenium pandas beautifulsoup4
```

### Step 3: Set Up ChromeDriver
- Download the correct version from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- Place `chromedriver.exe` in your project folder or add it to your system PATH

### Step 4: Create a Folder to Store HTML Files
```bash
mkdir data
```

---

## ▶️ Running the Scripts

### 🔹 1. Scrape HTML from Amazon

Use `project.py` to:
- Open Amazon.in
- Search for "laptop"
- Visit multiple result pages
- Save product containers as HTML files

```bash
python project.py
```

### 🔹 2. Extract & Export Data

Use `collect.py` to:
- Read the saved HTML files
- Parse product details using BeautifulSoup
- Store data in a structured CSV using Pandas

```bash
python collect.py
```

---

## 📊 Analyze the Data

Once `data.csv` is generated:
- Open it in **Microsoft Excel**, **Google Sheets**, or any spreadsheet tool
- Easily sort, filter, and analyze products, prices, or links
- Ideal for performing **price comparison** or **market research**

---

## 🧠 What This Project Demonstrates

- Using **Selenium WebDriver** to automate browser interactions
- Parsing complex HTML with **BeautifulSoup**
- Navigating dynamic content and managing delays
- Cleaning and storing extracted data with **Pandas**
- Building a working **web data pipeline** from browsing to CSV export

---

## 🚧 Challenges Faced

- **Dynamic HTML structures**: Amazon’s layout often changes, requiring flexible element targeting
- **Delayed loading**: Introduced `time.sleep()` to allow elements to fully load before scraping
- **Missing or inconsistent elements**: Wrapped extraction logic in `try-except` to prevent crashes
- **File handling**: Built a clean folder structure and naming system for organized data storage

---

## 💼 Use Cases

- Real-world automation project for portfolios
- Learning resource for Python web scraping
- E-commerce data collection and research
- Educational example for browser control with Selenium

---

## 🙌 Acknowledgements

This project was created as part of my journey into web automation and Python development. It helped me build confidence working with live websites, managing real data, and automating complex browser tasks.

---

## 📬 Connect with Me

Created with passion by **[Yogesh](https://www.linkedin.com/in/your-link)**  
🔗 GitHub: [Its-Yogesh-100](https://github.com/Its-Yogesh-100)  
📩 Open to collaborations, feedback, or questions.

---

## ⚠️ Disclaimer

This scraper is intended strictly for **educational purposes**. Please respect the terms of service of Amazon and avoid sending excessive or repeated automated requests.
