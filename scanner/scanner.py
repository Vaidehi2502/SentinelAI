import re
from scanner.rules_php import patterns as php_patterns
from scanner.rules_python import patterns as python_patterns
from scanner.rules_js import patterns as js_patterns
from scanner.rules_cpp import patterns as cpp_patterns
from scanner.rules_java import patterns as java_patterns
from ai_engine import analyze_code

descriptions = {

    "SQL Injection":
    "User input may reach a database query and allow SQL Injection.",

    "XSS":
    "User input may be executed in the browser.",

    "Command Injection":
    "User input may execute operating system commands.",

    "Path Traversal":
    "User input may access unauthorized files or directories.",

    "Hardcoded Secret":
    "Sensitive credentials found in source code."

}
fixes = {

    "SQL Injection":
    "Use prepared statements and parameterized queries.",

    "XSS":
    "Sanitize user input using htmlspecialchars().",

    "Command Injection":
    "Avoid system() with user input. Use allowlists.",

    "Path Traversal":
    "Validate filenames and restrict file access.",

    "Hardcoded Secret":
    "Store secrets in environment variables."
}
secure_examples = {

    "SQL Injection":
    '$stmt = $conn->prepare("SELECT * FROM users WHERE id=?");',

    "XSS":
    'echo htmlspecialchars($_GET["comment"]);',

    "Command Injection":
    '$allowed = ["start","stop"];',

    "Path Traversal":
    '$allowed = ["home.php"];',

    "Hardcoded Secret":
    'API_KEY = os.getenv("API_KEY")'
}


def scan_file(filepath):

    findings = []
    extension = filepath.split(".")[-1].lower()
    if extension == "php":

        patterns = php_patterns

    elif extension == "py":

        patterns = python_patterns

    elif extension == "js":

        patterns = js_patterns

    elif extension == "cpp":

        patterns = cpp_patterns

    elif extension == "java":

        patterns = java_patterns

    else:

        patterns = {}

    try:

        with open(filepath, "r", errors="ignore") as file:

                full_code = file.read()

        lines = full_code.splitlines()

        for line_no, line in enumerate(lines, start=1):

            lower_line = line.lower()

            for vuln, data in patterns.items():

                for pattern in data["patterns"]:
                    if re.search(
                        pattern,
                        line,
                        re.IGNORECASE
                ):
                        already_found = False

                        for finding in findings:

                            if (
                                finding["type"] == vuln
                                and
                                finding["line"] == line_no
                            ):

                                already_found = True

                        if already_found:

                            break

                        findings.append({

                            "type": vuln,

                            "severity": data["severity"],

                            "line": line_no,

                            "code": line.strip(),

                            "description":
                            descriptions.get(vuln),

                            "fix":
                            fixes.get(vuln),

                            "secure_code":
                            secure_examples.get(vuln)

                        })
                        ai_response = analyze_code(

                                    full_code,

                                    vuln

                                )

                        findings[-1]["ai_explanation"] = ai_response
                        break

        return findings

    except Exception as e:

        return [{
            "type": "Scanner Error",
            "severity": "ERROR",
            "line": "-",
            "code": str(e),
            "description":
            "An error occurred while scanning the file."
        }]