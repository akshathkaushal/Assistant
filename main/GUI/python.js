function greet() {
    console.log("hello from js");
    let { PythonShell } = require("python-shell");
    var path = require('path');
    var options = {
        scriptPath: path.join(__dirname, '/../')
    }

    var start = new PythonShell('/Backend/hello.py', options)

    start.on('message', function(message) {
        swal(message)
    })
}