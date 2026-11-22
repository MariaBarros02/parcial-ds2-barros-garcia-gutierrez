// Crear base de datos:

use huilasoft_bd 

//Crear colecciones: 

db.createCollection("tickets", {}) 

db.createCollection("agentes", {}) 

db.createCollection("defectos", {}) 


// llenar colecciones

db.tickets.insertMany([{num_ticket: "T1", llegada: 0, atencion: 5, prioridad "alta"}, {num_ticket: "T2", llegada: 3, atencion:7, prioridad "alta"}, {num_ticket: "T3", llegada: 6, atencion: 4, prioridad "media"}, {num_ticket: "T4", llegada: 14, atencion: 8 prioridad "baja"}, {num_ticket: "T5", llegada: 25, atencion: 6 prioridad "alta"}, {num_ticket: "T6", llegada: 28, atencion: 5, prioridad "alta"}, {num_ticket: "T7", llegada: 40, atencion: 9, prioridad "baja"}, {num_ticket: "T8", llegada: 52, atencion: 4, prioridad "alta"}]) 

db.agentes.insertMany([{nombre: "Laura Cerquera", nivel: "senior", tickets_hora: 10}, {nombre: "Andres Perdomo, nivel: "junior, tickets_hora: 6}]) 

db.defectos.insertMany([{semana: 1, def_encontrados: 28}, {semana: 2, def_encontrados: 23}, {semana: 3, def_encontrados: 22}, {semana: 4, def_encontrados: 17}, {semana: 5, def_encontrados: 16}, {semana: 6, def_encontrados: 12}, {semana: 7, def_encontrados: 12}, {semana: 8, def_encontrados: 9}])


//selects
//Consulta tickets de prioridad alta: 

db.tickets.find({prioridad: {$eq: "alta"}}) 

//Consulta tickets con atención mayor a 6 minutos: 

db.tickets.find({atencion: {$gt: 6}}) 

//Consulta semanas con menos de 15 defectos 


db.defectos.find({def_encontrados: {$lt: 15}}) 

//update


db.tickets.updateOne({num_ticket: "T7"}, {$set: {prioridad: "media"}}) 


//delete 


db.tickets.insertOne({num_ticket: 'T8', llegada: 58,  atencion: 1, prioridad: "alta"}) 

db.tickets.deleteOne({num_ticket: "T8"}) 


