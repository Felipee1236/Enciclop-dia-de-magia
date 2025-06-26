# Enciclopédia de Magias 

Projeto de Banco de Dados- C07-L1
Felipe Campos de Souza
Sofia Nogueira Groke


## Estrutura do Banco de Dados

O sistema gerencia as seguintes entidades:

- **Escritor**: Autores das magias
- **Classe**: Classes de personagens (Mago, Bruxo, Druida, etc.)
- **Magia**: Magias com suas propriedades (nome, nível, escola, etc.)
- **Magia_has_Classe**: Relacionamento entre magias e classes

## Funcionalidades

### CRUD Completo para todas as entidades:
- **Escritores**: Criar, ler, atualizar e deletar escritores
- **Classes**: Gerenciar classes de personagens
- **Magias**: Gerenciar magias com todos os atributos
- **Relacionamentos**: Associar magias a classes

### Consultas Especiais:
- Buscar magias por escola
- Buscar magias por nível
- Ver todas as classes que podem usar uma magia
- Ver todas as magias disponíveis para uma classe
- Listar todas as associações magia-classe

## Pré-requisitos

- Python 3.7+
- MySQL Server
- Banco de dados `enciclopediaMagias` criado e populado

## Instalação

1. Clone ou baixe o projeto
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure a conexão com o banco de dados no arquivo `database/connection.py`:
   ```python
   HOST = 'localhost'
   USER = 'seu_usuario'
   PASSWORD = 'sua_senha'
   ```

4. Execute o sistema:
   ```bash
   python main.py
   ```

## Uso

O sistema apresenta um menu interativo com as seguintes opções:

1. **Gerenciar Escritores**: CRUD completo para escritores
2. **Gerenciar Classes**: CRUD completo para classes
3. **Gerenciar Magias**: CRUD completo para magias com consultas especiais
4. **Gerenciar Relacionamentos**: Associar/desassociar magias e classes

## Estrutura do Projeto

```
enciclopedia_magias/
├── database/
│   ├── __init__.py
│   └── connection.py
├── models/
│   ├── __init__.py
│   ├── escritor.py
│   ├── classe.py
│   ├── magia.py
│   └── magia_classe.py
├── main.py
├── requirements.txt
└── README.md
```

