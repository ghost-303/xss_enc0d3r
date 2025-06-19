import xss
import xss_encode
import argparse
import c_xss


def main():
    parser = argparse.ArgumentParser(description=" Task 2 - Payload Generation")
    parser.add_argument("--xss",action="store_true", help="Generate Cross Site Payloads")
    parser.add_argument("--xssen", action="store_true", help="Generate XSS Encoded Payloads")
    parser.add_argument("--xssc", action="store_true", help="Encoding Custom Payload")
    args = parser.parse_args()
  

    if args.xss:
        print("[+] CROSS SITE SCRIPTING PAYLOADS [+]")
        xss.xss_file()

    if args.xssen:
        print("[+] ENCODED PAYLOADS OF XSS [+]")
        xss_encode.en_xss_file()

    if args.xssc:
        c_xss.get_custom_payload()


if __name__=="__main__":
    main()







