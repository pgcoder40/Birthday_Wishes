🎂 Birthday Wishes Automation

This project automatically sends personalized **birthday emails** to friends and family using Python and GitHub Actions.  
It reads birthdays from a CSV file, selects a random letter template, and sends the message via Gmail.


## 📂 Project Structure

Birthdaywishes

├── main.py  
├── birthdays.csv           
├── letter_templates/     
└── .github/workflows/   


## ⚙️ How It Works
1. **Check today’s date** (in IST timezone using `pytz`).
2. **Match birthdays** from `birthdays.csv`.
3. **Pick a random letter** from `letter_templates/`.
4. **Send email** using Gmail SMTP with credentials stored in GitHub Secrets.
5. **Run daily** via GitHub Actions (cron schedule).


## 📑 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Birthdaywishes.git
cd Birthdaywishes

**2. Add Dependencies**
Create a requirements.txt file:

pandas
pytz

**3. Configure GitHub Secrets**
Go to Settings → Secrets → Actions in your repository and add:

MY_EMAIL → your Gmail address

MY_PASSWORD → Gmail App Password (not your real password)

**4. Prepare Files**
birthdays.csv → contains name,email,year,month,day

letter_templates/ → add letter_1.txt, letter_2.txt, letter_3.txt with [NAME] placeholder

**Example birthdays.csv:**

csv
name,email,year,month,day
PG,gamer@example.com,2004,05,12
Jacksparrow,jack@example.com,2005,04,05


**🚀 GitHub Actions Workflow**
Example .github/workflows/birthday.yml:

yaml
name: Birthday Wishes

on:
  schedule:
    - cron: "0 19 * * *"   # Runs daily at 00:30 IST
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run birthday script
        env:
          MY_EMAIL: ${{ secrets.MY_EMAIL }}
          MY_PASSWORD: ${{ secrets.MY_PASSWORD }}
        run: python main.py

**Example Output:**
  When a birthday matches:
    ✅ Email sent successfully to Gokul (gokul@example.com)

 When no birthdays today:
    ℹ️ No birthdays today.
