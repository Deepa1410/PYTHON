import qrcode
def read_text_from_file(file_path):
    with open(file_path,"r") as file:
        text = file.read()
    return text    
