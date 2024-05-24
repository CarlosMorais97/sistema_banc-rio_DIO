# Desafio de Python
## Desafio para a criação de um sistema bancário
### Criar um sistema bancário com funções: depositar, sacar, criar usuário e criar conta
- O primeiro passo foi criar o menu simples e de rápido entendimento
- A função depositar foi criada utilizando 3 (três) parâmetros(*saldo, valor, extrato*) posicionais, retornando saldo e extrato, onde o valor depositado seria incrementado ao saldo e salvo no extrato.
- A função sacar foi criado com 6 (seis) parâmetros(*saldo, valor, extrato, limite, numero_saques e limite_saques*) por chaves, retornando saldo, extrato e numero de saques, para isso a conta teria primeiro que ter algum valor maior que 0 (zero) para que possa efetuar o saque, o limite para o valor do saque teria que ser até R$500,00 e cada usuário só pode realizar 3 (três) operações de saque, tudo isso sendo incrementado na variável extrato.
- A função extrato foi criada com 2 (dois) parâmetros (*saldo, extrato*) sendo saldo posicional e extrato por chave, e tinha que apenas mostrar todas as operações de depósito e saque na tela quando solicitado.
- A função de criar usuário tinha apenas 1 (um) parâmetro(*usuarios*), que utilizei uma lista para armazenar os usuários que tem que digitar os números de um CPF, nome completo e endereço completo que quando salvo, não permite outro usuário com o mesmo CPF através da função *filtrar_usuários*.
- A função de criar conta tinha 3 (três) parâmetros(*AGENCIA, numero_conta, usuarios*) posicionais, para criar a conta teria que existir um CPF cadastrado, desse modo poderiam existir mais de uma conta para um único CPF, a agência era a mesma para todas as contas e o número da conta era salvo em uma lista onde se iniciaria com o número 1 (um).
- Por fim coloquei a função de listar contas, caso queiram saber quantas contas estão cadastradas no sistema como um todo.
