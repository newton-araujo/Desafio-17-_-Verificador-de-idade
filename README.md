<h1>Desafio 17 - Verificador de idade</h1>

<h2>Objetivo:</h2>
<p>Este código tem como finalidade determinar a faixa etária do usuário com base na idade fornecida.</p>


<h3>Passos:</h3>

<ol>
<h2><li>Entrada de Dados:</li></h2>
<ul>
<li>Utiliza a função input para solicitar ao usuário que insira sua idade.</li>
<li>A entrada é convertida para um número inteiro usando int().</li>

    idade = int(input("Qual a sua idade: "))
</ul>

<h2><li>Condições de Verificação:</li></h2>
<ul>
<li>Utiliza uma estrutura condicional (if, elif, else) para avaliar a idade do usuário.</li>
<li>Classifica o usuário em uma das seguintes categorias: criança, adolescente ou adulto.</li>

    if idade < 13:
        print("Você é uma criança!")
    elif idade in range(13, 20):
        print("Você é um adolescente!")
    else:
        print("Você é um adulto!")
</ul>
</ol>

<h3>Mensagens Personalizadas:</h3>
<ul>
<li><b>Criança:</b> Se a idade for menor que 13.</li>
<li><b>Adolescente:</b> Se a idade estiver entre 13 e 19 (inclusive).</li>
<li><b>Adulto:</b> Para idades a partir de 20 anos.</li>
</ul>

<h3>Interatividade:</h3>
<p>O programa fornece uma experiência interativa ao adaptar a mensagem de saída com base na faixa etária do usuário, promovendo uma resposta personalizada.</p>

<h3>Conclusão:</h3>
<p>Ao executar este código, o usuário receberá uma mensagem indicando a qual categoria etária pertence, tornando o processo de verificação de idade simples e informativo.</p>