// script.js

import { createFolderElements, loadHTMLFile, openOverlay, closeOverlay } from './utils.js';

document.addEventListener('DOMContentLoaded', function() {
  fetch('folders.json')
    .then(response => response.json())
    .then(data => {
      const rootFolder = data.rootFolder;
      const foldersData = data.folders;

      const sidebarElement = document.querySelector('.sidebar');
      const overlayElement = document.querySelector('.overlay');
      overlayElement.addEventListener('click', closeOverlay); // 오버레이 클릭 시 숨김
      createFolderElements(foldersData, sidebarElement, rootFolder, mainElement);
    })
    .catch(error => {
      console.error('Error loading folders.json:', error);
    });
});
