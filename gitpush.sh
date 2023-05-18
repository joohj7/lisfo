#!/bin/bash

# Author: Joo Haeji(joohj7). 
# URL: https://github.com/joohj7/lisfo-global.git 
# Contact: joohj7@gmail.com


# REPLACE THIS as your github.io structure 
web_folder_path='web-data' # 여기서 /을 앞에 넣으면 안됨. 이미지 경로 할때는 앞에 / 넣어줘야 url상에서 image폴더 찾을 수 있지만 로컬에서 실행할때는 루트로 들어가기에...

# Changing a file name and move
# If directories not exist, make it. 

# git add
git add *
git commit -m "[$date] $fixed_filename is uploaded(auto)" 
git push 