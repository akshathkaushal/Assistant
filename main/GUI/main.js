const electron = require('electron');
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require('path');
const url = require('url');

let win;

function launch() {
    win = new BrowserWindow({
        webPreferences: {
            nodeIntegration: true
        }
    });

    win.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file',
        slashes: true
    }));

    win.on('close', () => {
        win = null;
    });

    //win.webContents.openDevTools()
}

app.on("ready", launch);

app.on('window-all-closed', () => {
    if(process.platform != 'darwin') {
        app.quit()
    }
});

app.on('activate', () => {
    if(win==null){
        launch()
    }
});