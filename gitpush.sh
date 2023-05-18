#!/bin/bash

# Author: Joo Haeji(joohj7). 
# URL: https://github.com/joohj7/lisfo-global
# Contact: joohj7@gmail.com


# REPLACE THIS as your github.io structure
web_folder_path='web-data' # 여기서 /을 앞에 넣으면 안됨. 이미지 경로 할때는 앞에 / 넣어줘야 url상에서 image폴더 찾을 수 있지만 로컬에서 실행할때는 루트로 들어가기에...

    # Jekyll에서 사용되는 meta 정보 추가하기
    # echo -n "Enter a subtitle: "
    # read  meta_subtitle
    # echo -n "Enter categories: "
    # read  meta_categories
    # echo -n "Enter tags: "
    # read  meta_tags


    # Changing a file name and move
    # If directories not exist, make it. 

    # git add
    git add *
    git commit -m "$fixed_filename is uploaded(auto)"

    echo -e "Work for the $meta_title post is completed!\n"
done

git push origin origin/main