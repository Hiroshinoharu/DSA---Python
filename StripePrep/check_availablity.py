from collections.abc import Set
from sys import prefix


def check_availability(data : str) -> str:
    lines = data.strip().splitlines()
    print(lines)
    # process each line, normalise names, store duplicates

    suffix_list = ["Inc.", "Corp.", "LLC", "L.L.C.", "LLC."]

    prefixes = ["The", "An", "A"]

    # Keep a result list
    result = []

    # Declare a used set
    used = set()

    # Split the string by the pipe (|)
    for line in lines:
        acct_id, company_name = line.split("|")
        print(acct_id,company_name)
        # Apply the normalisation rules
        normalised_company_name = company_name.lower()
        print("Converted to lowercase: ", normalised_company_name)
        
        # Check for & or ,
        normalised_company_name = normalised_company_name.replace("&", " ").replace(",", " ")
        normalised_company_name = " ".join(normalised_company_name.split())
        print("Replaced symbols:", normalised_company_name)

        # Remove any Suffixes contained on the lsit
        for suffix in suffix_list:
            if normalised_company_name.endswith(suffix.lower()):
                normalised_company_name = normalised_company_name.removesuffix(suffix.lower()).strip()
        
        print("Removed Suffix: ", normalised_company_name)

        # Any leading "The", "An" and "A" are ignored
        for prefix in prefixes:
            if normalised_company_name.startswith(prefix.lower()):
                normalised_company_name = normalised_company_name.removeprefix(prefix.lower()).strip()
        print("After the prefixes removed: ", normalised_company_name)

        # Ignore And during the letter unless if it placed different like the start
        if "and" in normalised_company_name and not normalised_company_name.startswith("and "):
            normalised_company_name = normalised_company_name.replace("and","")
            normalised_company_name = " ".join(normalised_company_name.split())
        
        # After the transformation if the name is empty or just characters
        if normalised_company_name.strip() == "" or normalised_company_name in used:
            result.append(f"{acct_id}|Name Not Available")
        else:
            used.add(normalised_company_name)
            result.append(f"{acct_id}|Name Available")
    
    return "\n".join(result)

data = """acct_1|Llama, Inc.
acct_2|the llama inc.
acct_3|Llama and friend, LLC
acct_4|Llama & friend LLC
"""

print(check_availability(data))