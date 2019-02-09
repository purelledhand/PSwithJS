function titleCase(str) {
  return str.split(' ').map(w=>
    w[0].toUpperCase()+w.slice(1).toLowerCase()
  ).join(' ');
}


/**
 * Find all non-whitespace characters (\S)
 * At the beginning of string (^)
 * Or after any whitespace character (\s)
 */
function titleCase2(str) {
  return str.toLowerCase().replace(/(^|\s)\S/g, L => L.toUpperCase());
}

console.log(titleCase("I'm a liTTle tea pot"));
console.log(titleCase2("sHoRt AnD sToUt"));