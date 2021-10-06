// Paquete necesario para conectar a bases de datos MySQL.
var mysql = require('mariadb');
// Consulta SQL.
var sql = 'SELECT * FROM luisjordan_category LIMIT 10';

// Parámetros de conexión a la base de datos.
var con = mysql.createConnection({
  host: "tu-host",
  user: "tu-user-de-db",
  password: "tu-pass-de-db",
  database : 'tu-nombre-de-db'
});

// Funcion que nos permite comprobar la conexión a la base de datos.
// con.connect(function(err) {
//   if (err) throw err;
//   console.log("Connected!");
// });

// Funcion que nos devolverá resultados de la base de datos.
con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
  con.query(sql, function (err, result) {
    if (err) throw err;

    // Bucle que recore los resultados y pinta en consola.
    for(i=0; i<result.length; i++){
    	console.log("Result: " + result[i].name);
    }

  });
});