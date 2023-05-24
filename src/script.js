// script.js

import { createFolderElements, loadHTMLFile } from './utils.js';

document.addEventListener('DOMContentLoaded', function() {
  fetch('../folders.json')
    .then(response => response.json())
    .then(data => {
      const rootFolder = data.rootFolder;
      const foldersData = data.folders;

      const sidebarElement = document.querySelector('.sidebar');
      const mainElement = document.querySelector('.main');
      createFolderElements(foldersData, sidebarElement, rootFolder, mainElement);
    })
    .catch(error => {
      console.error('Error loading folders.json:', error);
    });
});