function validarCPF(cpf) {
  cpf = cpf.replace(/[^\d]+/g, ""); // Remove caracteres não numéricos

  if (cpf === "" || cpf.length !== 11) return false;

  // Elimina CPFs invalidos conhecidos
  if (/^(\d)\1{10}$/.test(cpf)) return false;

  for (let j = 0; j < 2; j++) {
    let soma = 0,
      r;
    for (let i = 0; i < 9 + j; i++) {
      soma += parseInt(cpf.charAt(i)) * (10 + j - i);
    }
    r = (soma * 10) % 11;
    if (r === 10 || r === 11) r = 0;
    if (r !== parseInt(cpf.charAt(9 + j))) return false;
  }

  return true;
}

// Exemplo de uso
console.log(validarCPF("000.000.000-00")); // Deve retornar false para CPF inválido
console.log(validarCPF("123.456.789-09")); // Substitua por um CPF válido para testar
