// utils.js

export function createFolderElements(foldersData, parentElement, rootFolder, mainElement) {
    foldersData.forEach(folderData => {
      const folderElement = document.createElement('div');
      folderElement.classList.add('folder');
  
      const folderNameElement = document.createElement('div');
      folderNameElement.classList.add('folder-name');
      folderNameElement.textContent = folderData.id;
      folderNameElement.addEventListener('click', function() {
        folderElement.classList.toggle('expanded');
      });
      folderElement.appendChild(folderNameElement);
  
      const files = folderData.files;
      if (files && files.length > 0) {
        const fileListElement = document.createElement('ul');
        fileListElement.classList.add('file-list');
  
        files.forEach(function(file) {
            const fileElement = document.createElement('li');
            const fileLinkElement = document.createElement('a');
            fileLinkElement.textContent = file.split('.')[0];
            fileLinkElement.href = '#' + rootFolder + '/' + folderData.id + '/' + file; // '#' 추가
            fileLinkElement.addEventListener('click', function() {
              openOverlay(rootFolder + '/' + folderData.id + '/' + file); // 오버레이 열기
            });
            fileElement.appendChild(fileLinkElement);
            fileListElement.appendChild(fileElement);
          });
  
        folderElement.appendChild(fileListElement);
      }
      parentElement.appendChild(folderElement);
    });
  }
  

  export function loadHTMLFile(url, element) {
    fetch(url)
      .then(response => response.text())
      .then(html => {
        element.innerHTML = html;
      })
      .catch(error => {
        console.error('Error loading HTML file:', error);
      });
  }


  export function openOverlay(fileUrl) {
    const overlayElement = document.querySelector('.overlay');
    overlayElement.innerHTML = `<iframe src="${fileUrl}" frameborder="0" width="100%" height="100%"></iframe>`;
    overlayElement.style.display = 'block'; // 오버레이 표시
  }


  export function closeOverlay() {
    const overlayElement = document.querySelector('.overlay');
    overlayElement.style.display = 'none'; // 오버레이 숨김
  }
  