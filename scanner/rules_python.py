patterns = {

    "Command Injection": {

        "severity": "HIGH",

        "patterns": [

            r"os\.system",

            r"subprocess\.call",

            r"subprocess\.run"

        ]
    },

    "Hardcoded Secret": {

        "severity": "HIGH",

        "patterns": [

            r"password\s*=",

            r"api_key\s*=",

            r"secret\s*="

        ]
    }

}