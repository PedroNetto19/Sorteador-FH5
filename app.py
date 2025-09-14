# 1. Primeiro, importamos a classe 'Flask'.
# Essa classe é o coração do nosso aplicativo web.
from flask import Flask, render_template, request
import sorteador_logica

# 2. Em seguida, criamos uma instância (um objeto) do Flask.
# O '__name__' é uma variável que diz ao Flask onde encontrar arquivos
# (como templates HTML e arquivos estáticos).
app = Flask(__name__)

# 3. Agora, definimos a nossa primeira "rota". Uma rota é um endereço
# (URL) que o seu navegador vai visitar. A rota '/' é a página principal.
@app.route('/', methods=['GET', 'POST'])
def home():
    # 4. Esta função será executada quando alguém visitar a rota '/'.
    if request.method == 'POST':
        filtros_selecionados = request.form.getlist('grupo')
        resultado = sorteador_logica.sortear_carro(filtros_selecionados)
        return render_template('index.html', resultado=resultado)
    
    else:
        return render_template('index.html', resultado={'carro': None, 'tunagem': None})
# 5. Por fim, essa parte do código garante que o servidor seja
# executado apenas quando você rodar o arquivo diretamente.
# O 'debug=True' permite que o servidor reinicie automaticamente
# quando você fizer alterações no código, o que é ótimo para o desenvolvimento.
if __name__ == 'main':
    app.run(debug=True)


