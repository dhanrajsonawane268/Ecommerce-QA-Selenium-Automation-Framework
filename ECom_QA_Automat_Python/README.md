 🛒 E-Commerce Selenium QA Automation Framework  
### 📌 Automation Testing Project for Flipkart & Swag Labs  
#### 🚀 Built Using Python | Selenium | PyTest | Page Object Model

---

## 👨‍💻 About the Developer (Author)
🎯 **Dhanraj Rajendra Sonawane**  
📍 MCA Student | QA Automation Engineer (Selenium) | Python Developer  

📬 **Contact Information**
| Platform | Link |
|----------|------|
| 📧 Email | dhanrajsonawane268@gmail.com |
| 📱 Mobile | 808090xxxx |
| 🌐 GitHub | https://github.com/dhanrajsonawane268 |
| 💼 LinkedIn | https://www.linkedin.com/in/dhanraj-sonawane-985a52283 |
| 🏆 HackerRank | https://www.hackerrank.com/profile/dhanrajsonawane2 |

---

# 📚 Project Overview

🔍 **This Automation Framework tests real E-Commerce flows on:**

| Website | Functionality Covered |
|----------|----------------------|
| 🛍 **Flipkart** | Product Search → Open Product → Extract Title & Price → Screenshot |
| 🧪 **Swag Labs** | Login Test → Add Product → Cart Validation |

🎯 **Goal:** Build a complete, clean, industry-level automation framework for Freshers & QA Engineers.

---

## 🏗 Tech Stack Used

| Category | Tools/Libraries |
|----------|----------------|
| Programming | Python |
| Automation | Selenium WebDriver |
| Test Runner | PyTest |
| Design Pattern | POM (Page Object Model) |
| Reporting | PyTest-HTML |
| Utility | WebDriver Manager, Config Parser |

---

## 📂 Project Folder Structure

ECommerce-QA-Selenium-Automation-Framework/
│── pages/
│ │── login_page.py
│ │── inventory_page.py
│ │── flipkart_page.py
│
│── tests/
│ │── test_login.py
│ │── test_products.py
│ │── test_flipkart.py
│
│── utils/
│ │── config_reader.py
│ │── driver_factory.py
│
│── reports/ (Auto Generated)
│── conftest.py
│── config.ini
│── README.md
│── requirements.txt

yaml
Copy code

---

## ⚙️ Features Supported

✔ **POM (Page Object Model) Architecture**  
✔ 🔒 Authentication Testing (Swag Labs Login)  
✔ 📦 Add-to-Cart Validation  
✔ 🔎 Product Search on Flipkart  
✔ 💰 Fetch Product Price & Title  
✔ 📸 Screenshot on Failure & Success  
✔ 🔄 Browser Management using WebDriver Factory  
✔ 🧾 .ini Config Based Credentials  
✔ 🌐 Chrome Headless Supported  
✔ 🧪 PyTest Markers (Smoke & Regression)  

---

## 🔧 Installation & Setup Guide

### 📌 Step 1: Clone Repository

```bash
git clone https://github.com/dhanrajsonawane268/Ecommerce-QA-Selenium-Automation-Framework.git
cd Ecommerce-QA-Selenium-Automation-Framework
📌 Step 2: Create Virtual Environment
bash
Copy code
python -m venv venv
📌 Step 3: Activate Environment
OS	Command
Windows	venv\Scripts\activate
Mac/Linux	source venv/bin/activate

📌 Step 4: Install Dependencies
bash
Copy code
pip install -r requirements.txt
🧪 Running Test Cases
▶ Run All Tests
bash
Copy code
pytest
▶ Run with Verbose Output
bash
Copy code
pytest -v
🧪 Run Only Smoke Tests
bash
Copy code
pytest -m smoke
🔁 Run Only Regression Tests
bash
Copy code
pytest -m regression