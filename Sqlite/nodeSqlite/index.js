const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('./data/chinook.db', sqlite3.OPEN_READONLY, (err) => {
    if (err) {
        return console.error(err.message);
    }

    console.log("Connected to the sqlite data");
});

// Usando db.all:

// let sql = `
// SELECT DISTINCT name FROM playlists 
// ORDER BY name
// `

// db.all(sql, [], (err, rows) => {
//     if (err) {
//         throw err;
//     }
//     rows.forEach((row) => {
//         console.log(row);
//     })
// })

// Usando db.get()

let sql = `
SELECT PlaylistId id, Name name FROM playlists
WHERE PlaylistId = ?
`

let playlistId = 1;

db.get(sql, [playlistId], (err, row) => {
    if (err) {
        return console.error(err.message);
    }
    return row
    ? console.log(row.id, row.name)
    : console.log(`No playlist found with the id ${playlistId}`);
})


db.close((err) => {
    if (err) {
        return console.error(err.message);
    }
    console.log("Close database connection");
});