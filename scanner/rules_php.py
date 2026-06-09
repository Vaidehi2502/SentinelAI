patterns = {

    "SQL Injection": {

        "severity": "HIGH",

        "patterns": [

            r"SELECT.*\$_GET",

            r"SELECT.*\$_POST",

            r"INSERT.*\$_GET",

            r"UPDATE.*\$_GET",

            r"DELETE.*\$_GET"

        ]
    },

    "XSS": {

        "severity": "MEDIUM",

        "patterns": [

            r"echo\s+\$_GET",

            r"echo\s+\$_POST"

        ]
    }

}