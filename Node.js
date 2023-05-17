const express = require("express");
const fs = require("fs");
const path = require("path");

const app = express();

app.use(express.static("public"));

app.get("/files", (req, res) => {
  const folder = req.query.folder;
  const folderPath = path.join(__dirname, "public", folder);
  
  fs.readdir(folderPath, (err, files) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ error: "Failed to read folder contents." });
    }

    const fileList = files.filter(file => fs.statSync(path.join(folderPath, file)).isFile());
    res.json({ files: fileList });
  });
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});