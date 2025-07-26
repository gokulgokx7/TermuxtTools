---

# TermuxtTools 🔧

A growing collection of simple, beginner-friendly tools built in Python for Termux.  
Useful for ethical hacking, networking awareness, and automation tasks on Android.

---

## 🚀 Tools Included

### ✅ IP Lookup Tool (`iplookup.py`)
Fetches geolocation and network information of any public IP address using a public API.

**🔍 Example Output:**
- IP: `8.8.8.8`
- City: Mountain View
- Country: United States
- ISP: Google LLC

---

### 🔎 Port Scanner (`portscanner.py`)
Scans a target host for open TCP ports to identify running services.

**🧪 Example Use:**
- Target: `scanme.nmap.org`
- Open Ports: 22 (SSH), 80 (HTTP), ...

---

### 🧾 HTTP Header Grabber (`headergrab.py`)
Grabs and displays HTTP headers of any website to inspect server info, content type, etc.

**🔍 Example Use:**
- Target: `example.com`
- Server: ECS (nyb/1D10)
- Content-Type: text/html

---

## 📦 Installation (Termux)

```bash
pkg update && pkg upgrade -y
pkg install git python -y
git clone https://github.com/gokulgokx7/TermuxtTools.git
cd TermuxtTools
pip install requests


---

▶️ Usage

Run each tool using Python:

python iplookup.py
python portscanner.py
python headergrab.py


---

📌 Requirements

Python 3

requests module (install with pip install requests)



---

👨‍💻 Author

Gokul Gokx7
Made with 💻 and 🔋 using only Android + Termux!


---

🌟 Support or Ideas?

Open an issue

Drop a ⭐ if you found it useful!



---

🛡️ Disclaimer

This project is intended for educational and ethical use only.
Do NOT use it for any unauthorized activities or real-world attacks.

---
