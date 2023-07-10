from CpfCnpj import Documento

#cpf_um = Cpf("02389462154")
#print(cpf_um)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "02389462154"

documento = Documento.cria_documento(exemplo_cpf)

print(documento)


