async function getData (callback) {
    const sqlite3 = require('sqlite3').verbose();

    let db = new sqlite3.Database('./data/chinook.db', sqlite3.OPEN_READONLY, (err) => {
        if (err) {
            return console.error(err.message);
        }
        console.log("Connected to the sqlite data");
    });

    let sql = `
    SELECT 
        title
    FROM
        albums
    `;

    db.all(sql, [], (err, rows) => {
        if (err) {
            throw err;
        }
        callback(rows);
    });

    db.close((err) => {
    if (err) {
        return console.error(err.message);
    }
    console.log("Close database connection");
});
}

export default function showData () {
    getData(log);
}

function log () {
    console.log(data)
}