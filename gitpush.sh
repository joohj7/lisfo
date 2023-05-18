#!/bin/bash

# Author: Joo Haeji(joohj7). 
# URL: https://github.com/joohj7/lisfo-global.git 
# Contact: joohj7@gmail.com

# REPLACE THIS as your github.io structure 
web_folder_path='web-data' 

# git add, commit, push
# git add $web_folder_path/* # 만약 특정 폴더로 제한하고 싶으면 주석 풀기
git add * 
git commit -m "file is uploaded(auto)" 
git push 