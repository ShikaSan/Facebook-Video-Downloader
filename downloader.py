from datetime import datetime
from tqdm import tqdm
import requests
import re
import os
import os.path #Added this import for absolute path

banner = (r'''

  ___ ___  __   ___    _           ___                  _              _         
 | __| _ ) \ \ / (_)__| |___ ___  |   \ _____ __ ___ _ | |___  __ _ __| |___ _ _ 
 | _|| _ \  \ V /| / _` / -_) _ \ | |) / _ \ V  V / ' \| / _ \/ _` / _` / -_) '_|
 |_| |___/   \_/ |_\__,_\___\___/ |___/\___/\_/\_/|_||_|_\___/\__,_\__,_\___|_|  
                                                            [Sameera Madushan]

''')

print(banner)

def main():
    try:
        if len(list) == 2:
            if 0 in list and 1 in list:
                _input_1 = str(input("\nPress 'A' to download the video in HD quality.\nPress 'B' to download the video in SD quality.\n: ")).upper()
                if _input_1 == 'A':
                    print("\nDownloading the video in HD quality... \n")
                    video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                    file_size_request = requests.get(video_url, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024
                    save_path = "./Downloads/" #Added download/save path
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    complete_filename = os.path.join(save_path, filename) #Added absolute path
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(complete_filename + '.mp4', 'wb') as f: #changed filename to the absolute path variable
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\nVideo downloaded successfully.")   

                if _input_1 == 'B':
                    print("\nDownloading the video in SD quality... \n")
                    video_url = re.search(r'sd_src:"(.+?)"', html).group(1)
                    file_size_request = requests.get(video_url, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024
                    save_path = "./Downloads/" #Added download/save path
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    complete_filename = os.path.join(save_path, filename) #Added absolute path
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(complete_filename + '.mp4', 'wb') as f: #changed filename to the absolute path variable
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\nVideo downloaded successfully.")   

        if len(list) == 2:
            if 1 in list and 2 in list:
                _input_2 = str(input("\nOops! The video is not available in HD quality. Would you like to download it? ('Y' or 'N'): ")).upper()
                if _input_2 == 'Y':
                    print("\nDownloading the video in SD quality... \n")
                    video_url = re.search(r'sd_src:"(.+?)"', html).group(1)
                    file_size_request = requests.get(video_url, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024
                    save_path = "./Downloads/" #Added download/save path
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    complete_filename = os.path.join(save_path, filename) #Added absolute path
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(complete_filename + '.mp4', 'wb') as f: #changed filename to the absolute path variable
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\nVideo downloaded successfully.")
                if _input_2 == 'N':
                    exit()

        if len(list) == 2:
            if 0 in list and 3 in list:
                _input_2 = str(input("\nOops! The video is not available in SD quality. Would you like to download it? ('Y' or 'N'): \n")).upper()
                if _input_2 == 'Y':
                    print("\nDownloading the video in HD quality... \n")
                    video_url = re.search(r'hd_src:"(.+?)"', html).group(1)
                    file_size_request = requests.get(video_url, stream=True)
                    file_size = int(file_size_request.headers['Content-Length'])
                    block_size = 1024
                    save_path = "./Downloads/" #Added download/save path
                    filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                    complete_filename = os.path.join(save_path, filename) #Added absolute path
                    t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                    with open(complete_filename + '.mp4', 'wb') as f: #changed filename to the absolute path variable
                        for data in file_size_request.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                    t.close()
                    print("\nVideo downloaded successfully.")
                if _input_2 == 'N':
                    exit()
    except(KeyboardInterrupt):
        print("\nProgramme Interrupted")

try:
    while True:
        url = input("\nEnter the URL of Facebook video: ")
        x = re.match(r'^(https:|)[/][/]www.([^/]+[.])*facebook.com', url)

        if x:
            html = requests.get(url).content.decode('utf-8')
        else:
            print("\nNot related with Facebook domain.")
            exit()

        _qualityhd = re.search('hd_src:"https', html)
        _qualitysd = re.search('sd_src:"https', html)
        _hd = re.search('hd_src:null', html)
        _sd = re.search('sd_src:null', html)

        list = []
        _thelist = [_qualityhd, _qualitysd, _hd, _sd]
        for id,val in enumerate(_thelist):
            if val != None:
                list.append(id)

        main()
        again = input("\nWanna download another video? (Y or N): ").upper()
        if again == str("Y"):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(banner)
            continue
        else:
            break

except KeyboardInterrupt:
    print("\nProgramme Interrupted")
    
