import os
import shutil
import time
from automation import automate_browser
     
def read_file_to_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines() if line.strip() != '']

def delete_all_files_and_folders():
    time.sleep(1)
    folder_path = r'.\profile'
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path) 
                
def start():
    try:
        delete_all_files_and_folders()
        headless = input(f"Bạn có muốn mở cửa sổ không ? (y/n): ").strip().lower()
        automate_browser(headless)
        time.sleep(3)        
        delete_all_files_and_folders()
        time.sleep(1)
    except Exception as e:
        pass

if __name__ == '__main__':
    start()