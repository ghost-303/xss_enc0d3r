def xss_file():
    try:
        file=open("xss_payload.txt",'r')
        line=file.readline()
        while line:
            print(line.strip())       #encoded_line_based_code = encoder.l1(line_based_code, 3)
            line=file.readline()
        file.close()
    except Exception as e:
        print(f"Error in reading file: {e}")

