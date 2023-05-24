// script.js

import { createFolderElements } from './utils.js';

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