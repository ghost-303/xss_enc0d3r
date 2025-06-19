import urllib.parse
def en_xss_file():
    try:
        with open("xss_payload.txt", 'r') as file:
            for line in file:
                line = line.strip()  # remove whitespace
                encoded_line = urllib.parse.quote(line)
                print(encoded_line)
    except Exception as e:
        print(f"Error in reading file: {e}")
