# 🖼️ Screenshot Generator

A simple **Flask web app** to capture website screenshots instantly — built just for **weekend refreshment and practice**!  
Supports **multiple URLs (batch mode)**, **downloadable images**, and flexible options like format, viewport size, and full-page capture.  

---

## 🚀 Features

- Capture screenshots of any website 📸  
- Supports **PNG** and **JPEG** formats  
- **Full-page** capture option  
- **Custom viewport** size input (width & height)  
- Upload **multiple URLs** at once (batch mode)  
- Download your captured screenshots directly  
- Clean and responsive UI  

---

## 🧩 Project Structure
```
screenshot-generator/
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
└── static/
├── script.js
└── (screenshots saved here)

```
---

## ⚙️ Installation & Setup

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/screenshot-generator.git
   cd screenshot-generator
   ```
Create a virtual environment

```bash

python -m venv venv
venv\Scripts\activate      # for Windows
source venv/bin/activate   # for macOS/Linux
```
Install dependencies

```bash

pip install -r requirements.txt

```
Set your ScreenshotBase API key

Open app.py and replace the placeholder API key with your own from ScreenshotBase.

Run the app locally

```bash

python app.py
```
Open your browser

```

http://127.0.0.1:5000/
```
🌐 Deployment (Render)
Once everything works locally:

Push your code to GitHub

Go to Render Dashboard

Click New Web Service → Connect your repo

Set:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

Add environment variable:
```

SCREENSHOTBASE_API_KEY = your_api_key
```

Render will auto-deploy your Flask app.

💡 Example Use
You can enter:

```arduino

https://www.google.com
https://openai.com
https://kaggle.com

```
✅ The app will capture all screenshots and let you download them easily.

🧠 Inspiration
Just a weekend project built for fun, practice, and creativity!
Thanks to Kaggle and Google for the continuous learning opportunities. 🙌

### 🪄 Tech Stack
- Flask (Backend)

- HTML ,JavaScript (Frontend)

- ScreenshotBase API for capturing screenshots

- - -

### 🧑‍💻 Author

Soumyadeep Sarkar

AI/ML Engineer & Tech Enthusiast
