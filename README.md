# Marketing Dashboard API

Uma API de dashboard de marketing.

## Como executar a API

Siga os passos abaixo para executar a aplicação em seu ambiente local.

### Pré-requisitos

- Python 3.x instalado
- `pip` (gerenciador de pacotes do Python)

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone <https://github.com/VitorMozer9/marketing-dashboard-api.git>
    cd <https://github.com/VitorMozer9/marketing-dashboard-api.git>
    ```

2.  **Crie o arquivo de ambiente (`.env`):**
    É fundamental criar um arquivo `.env` na raiz do projeto. Você pode copiar o arquivo de exemplo `.env.example` para começar:
    ```bash
    # No Linux/macOS
    cp .env.example .env

    # No Windows (Command Prompt)
    # copy .env.example .env
    ```
    Após copiar, abra o arquivo `.env` e preencha as variáveis com os valores corretos para o seu ambiente.

3.  **Crie e ative um ambiente virtual (Recomendado):**
    ```bash
    # Cria o ambiente virtual
    python -m venv venv

    # Ativa no Linux/macOS
    source venv/bin/activate

    # Ativa no Windows (PowerShell)
    # .\venv\Scripts\Activate.ps1
    ```

4.  **Instale as dependências:**
    Com o ambiente virtual ativado, instale os pacotes necessários do arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a aplicação:**
    ```bash
    python -m src.app
    ```

### Acesso

Após iniciar, a API estará disponível no seguinte endereço: http://localhost:5000
*(**Nota:** Se a porta for diferente, por favor, ajuste o link e o arquivo `.env` se necessário.)*
