# Q3) Date Format Conversion: Develop a Python function that takes a string representing a 
# date in one format (e.g., "MM/DD/YYYY") and converts it to another format (e.g., "YYYY-MM-DD")
# using regular expressions to parse and rearrange the components

import re

def convert_date(date_string, from_format="MM/DD/YYYY", to_format="YYYY-MM-DD"):
    """
    Convert date from one format to another using regex
    Supported formats: MM/DD/YYYY, DD/MM/YYYY, YYYY-MM-DD, etc.
    """
    
    # Regex patterns for different date formats
    patterns = {
        "MM/DD/YYYY": r'(\d{1,2})/(\d{1,2})/(\d{4})',
        "DD/MM/YYYY": r'(\d{1,2})/(\d{1,2})/(\d{4})',
        "YYYY-MM-DD": r'(\d{4})-(\d{1,2})-(\d{1,2})',
        "MM-DD-YYYY": r'(\d{1,2})-(\d{1,2})-(\d{4})',
        "DD-MM-YYYY": r'(\d{1,2})-(\d{1,2})-(\d{4})'
    }
    
    # Extract components based on input format
    match = re.match(patterns[from_format], date_string)
    if not match:
        return f"Error: Date '{date_string}' doesn't match format '{from_format}'"
    
    # Get components (order depends on input format)
    if from_format == "MM/DD/YYYY" or from_format == "MM-DD-YYYY":
        month, day, year = match.groups()
    elif from_format == "DD/MM/YYYY" or from_format == "DD-MM-YYYY":
        day, month, year = match.groups()
    elif from_format == "YYYY-MM-DD":
        year, month, day = match.groups()
    
    # Pad single-digit months/days with leading zero
    month = month.zfill(2)
    day = day.zfill(2)
    
    # Convert to target format
    if to_format == "YYYY-MM-DD":
        return f"{year}-{month}-{day}"
    elif to_format == "MM/DD/YYYY":
        return f"{month}/{day}/{year}"
    elif to_format == "DD/MM/YYYY":
        return f"{day}/{month}/{year}"
    elif to_format == "MM-DD-YYYY":
        return f"{month}-{day}-{year}"
    elif to_format == "DD-MM-YYYY":
        return f"{day}-{month}-{year}"
    else:
        return f"Error: Unsupported target format '{to_format}'"

def main():
    print("📅 DATE FORMAT CONVERTER")
    print("=" * 50)
    
    test_dates = [
        "12/25/2023",
        "05/01/2024", 
        "25/12/2023",  # European format
        "2023-12-31",
        "7/4/2023",
        "01-15-2024"
    ]
    
    print("Testing Date Conversions:")
    print("-" * 50)
    
    for date in test_dates:
        # Auto-detect format and convert to YYYY-MM-DD
        if re.match(r'\d{1,2}/\d{1,2}/\d{4}', date):
            if int(date.split('/')[0]) > 12:  # Likely DD/MM/YYYY
                converted = convert_date(date, "DD/MM/YYYY", "YYYY-MM-DD")
            else:
                converted = convert_date(date, "MM/DD/YYYY", "YYYY-MM-DD")
        elif re.match(r'\d{4}-\d{1,2}-\d{1,2}', date):
            converted = convert_date(date, "YYYY-MM-DD", "MM/DD/YYYY")
        elif re.match(r'\d{1,2}-\d{1,2}-\d{4}', date):
            converted = convert_date(date, "MM-DD-YYYY", "YYYY-MM-DD")
        else:
            converted = "Unknown format"
        
        print(f"📅 {date:15} → {converted}")

if __name__ == "__main__":
    main()

