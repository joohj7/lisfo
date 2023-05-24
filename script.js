// script.js
document.addEventListener('DOMContentLoaded', function() {
      fetch('folders.json')
        .then(response => response.json())
        .then(data => {
          const rootFolder = data.rootFolder;
          const foldersData = data.folders;

          const sidebarElement = document.querySelector('.sidebar');
          createFolderElements(foldersData, sidebarElement, rootFolder);
        })
        .catch(error => {
          console.error('Error loading folders.json:', error);
        });
});

function createFolderElements(foldersData, parentElement, rootFolder) {
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
        fileLinkElement.href = `${rootFolder}/${folderData.id}/${encodeURIComponent(file)}`;
        fileElement.appendChild(fileLinkElement);
        fileListElement.appendChild(fileElement);
      });

      folderElement.appendChild(fileListElement);
    }

    parentElement.appendChild(folderElement);
  });
}