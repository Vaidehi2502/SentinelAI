# SentinelAI
AI-Powered Vulnerability Detection and Secure Code Analysis

A Flask web application that scans source files for security vulnerabilities using regex-based pattern detection and explains each finding with a locally-running **DeepSeek-Coder** AI model via **Ollama**.

---

## Features

- Upload any source file and receive an instant security report
- Regex-based detection across five languages: PHP, Python, JavaScript, Java, C/C++
- AI-generated explanation, severity assessment, and fix for each vulnerability (powered by DeepSeek-Coder)
- Security score (0–100) and risk level badge (LOW / MEDIUM / HIGH RISK)
- Detected language badge per vulnerability card (PHP, Python, JavaScript, SQL, etc.)
- Side-by-side vulnerable code vs. secure example view
- OWASP category tag on every card
- One-click **Download PDF** export of the full report
- Dark-mode cybersecurity dashboard UI

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| AI Engine | Ollama + DeepSeek-Coder |
| Vulnerability Detection | Regex (per-language rule files) |
| Frontend | Jinja2, HTML5, CSS3 |
| PDF Export | html2pdf.js (CDN) |

---

## Project Structure

```
practice/
├── app.py                  # Flask routes
├── ai_engine.py            # Ollama / DeepSeek-Coder integration
├── scanner/
│   ├── scanner.py          # Core scanning logic
│   ├── rules_php.py        # PHP vulnerability patterns
│   ├── rules_python.py     # Python vulnerability patterns
│   ├── rules_js.py         # JavaScript vulnerability patterns
│   ├── rules_java.py       # Java vulnerability patterns
│   └── rules_cpp.py        # C/C++ vulnerability patterns
├── templates/
│   ├── index.html          # Upload page
│   └── result.html         # Security report page
├── statics/
│   └── style.css           # Dark-mode dashboard styles
└── uploads/                # Temporary file storage
```

---

## Detected Vulnerabilities

| Vulnerability | Severity | Languages | OWASP |
|---|---|---|---|
| SQL Injection | HIGH | PHP, Java | A03:2021 – Injection |
| XSS | MEDIUM / HIGH | PHP, JavaScript | A03:2021 – Cross-Site Scripting |
| Command Injection | HIGH | PHP, Python | A03:2021 – Injection |
| Path Traversal | HIGH | PHP | A01:2021 – Broken Access Control |
| Hardcoded Secret | HIGH | Python | A02:2021 – Cryptographic Failures |
| Buffer Overflow | HIGH | C/C++ | A06:2021 – Vulnerable Components |

---

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- DeepSeek-Coder model pulled

---

## Setup & Run

### 1. Clone the repository

```bash
git clone <repo-url>
cd practice
```

### 2. Install Python dependencies

```bash
pip install flask ollama
```

### 3. Install and start Ollama

```bash
# Install Ollama (Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Pull the DeepSeek-Coder model
ollama pull deepseek-coder
```

### 4. Create the uploads directory

```bash
mkdir -p uploads
```

### 5. Run the app

```bash
python app.py
```

The app will be available at `http://127.0.0.1:5000`.

---

## Usage

1. Open `http://127.0.0.1:5000` in your browser
2. Click **Choose File** and select any source file (`.php`, `.py`, `.js`, `.java`, `.c`, `.cpp`)
3. Click **Scan**
4. Review the security report:
   - **Security Summary** — score, risk level, and severity breakdown
   - **Vulnerability Cards** — one card per finding with description, recommended fix, code comparison, and AI analysis
5. Click **Download PDF** to export the full report as a PDF

---

## Security Score

The score starts at 100 and is reduced per finding:

| Severity | Score Deduction |
|---|---|
| HIGH | −20 per finding |
| MEDIUM | −10 per finding |
| LOW | No deduction |

Score ≥ 80 → **LOW RISK** &nbsp;|&nbsp; 50–79 → **MEDIUM RISK** &nbsp;|&nbsp; < 50 → **HIGH RISK**

---

## Screenshots

### Upload Page
Dark-mode upload card with dashed file input and green Scan button.

### Security Report
- Sticky header with brand icon and Download PDF / Scan New File buttons
- 4-column stat grid with severity counts
- Animated progress bar for security score
- Solid-color risk badge
- Per-vulnerability cards with language badge, OWASP tag, line number, code blocks, and scrollable AI analysis box

---

## Adding New Rules

Create or edit a file in `scanner/rules_<language>.py` following this structure:

```python
patterns = {
    "Vulnerability Name": {
        "severity": "HIGH",   # HIGH | MEDIUM | LOW
        "patterns": [
            r"regex_pattern_1",
            r"regex_pattern_2",
        ]
    }
}
```

Then import and merge it inside `scanner/scanner.py`.

---

## License

MIT
