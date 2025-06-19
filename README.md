# xss_enc0d3r
This tool provides the user with the ability to encode their XSS payloads. With the help of "--xssc" flag, the user can enter q custom payload and the tool will encode it with URL based encoding scheme. The tool also gives a list of payloads in generic form and also in encoded form. The user can add their own list of XSS payloads to encode.
# Python Version
Version: 3.10
# Tool Required 
Tool: Pycharm
# Python Library
1. argparse
2. urllib.parse
# Usage
1. Generating Payload List: python3 main.py --xss
2. Generating Encoded List: python3 main.py --xssen
3. Generating Custom Encoded Payload: python3 main.py --xssc
