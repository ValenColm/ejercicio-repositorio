const productos = {
    producto1: { id: 1, nombre: "Laptop", precio: 3500, categoria: "tecnologia" },
    producto2: { id: 2, nombre: "Cafetera", precio: 900, categoria: "hogar" }
};
const categoriasMap = new Map();
categoriasMap.set("tecnologia", "Laptop");
console.log(categoriasMap);

categoriasMap.forEach((producto, categoria) => {
  console.log(`Categoría: ${categoria} - Producto: ${producto}`);
});

for (let key in productos){
    console.log(key, productos[key]);
}
for (let clave in productos) {
  console.log("Clave:", clave);
  console.log("Valor:", productos[clave]);
}




const listaNumeros = [1, 2, 2, 3, 1, 4, 5, 4, 6];
const miSet = new Set(listaNumeros);
console.log(miSet)
miSet.add(7);
console.log("Después de agregar 7:", miSet);
console.log("¿Existe el número 2?", miSet.has(2));
console.log("¿Existe el número 9?", miSet.has(9));
miSet.delete(7);
console.log("Después de eliminar 7:", miSet);
for (const numero of miSet) {
  console.log("Valor del Set:", numero);
}


console.log(" VALIDACIÓN DE PRODUCTOS");

for (let clave in productos) {
  const producto = productos[clave];

  if (
    producto.id &&
    producto.nombre &&
    typeof producto.precio === "number" &&
    producto.precio > 0
  ) {
    console.log("Producto válido:", producto);
  } else {
    console.log("Producto inválido:", producto);
  }
}

console.log(" PRUEBAS ");

console.log("Lista completa de productos:", productos);

console.log("Lista de números únicos:", miSet);

categoriasMap.forEach((producto, categoria) => {
  console.log(`Categoría: ${categoria} - Producto: ${producto}`);
});
