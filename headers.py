def analyze_headers(headers):
    header_dict = {line.split(':')[0]: line.split(':')[1].strip() for line in headers.split('\n') if line.strip()}
    return header_dict
