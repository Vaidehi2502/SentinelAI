patterns = {

    "Buffer Overflow": {

        "severity": "HIGH",

        "patterns": [

            r"gets\s*\(",

            r"strcpy\s*\(",

            r"sprintf\s*\("

        ]
    }

}