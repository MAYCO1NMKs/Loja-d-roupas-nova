{ pkgs, ... }: {
  # Usa o canal estavel do Nix
  channel = "stable-24.05";

  # Instala o Python e o pip usando o Nix
  packages = [
    pkgs.python3
    pkgs.pip
  ];

  idx = {
    extensions = [
      # Extensao recomendada para desenvolvimento em Python
      "ms-python.python"
    ];
    workspace = {
      # Roda apenas uma vez quando o workspace e criado.
      onCreate = {
        # Cria um ambiente virtual
        create-venv = "python -m venv venv";
        # Instala as dependencias do requirements.txt no ambiente virtual
        install-deps = "venv/bin/pip install -r requirements.txt";
      };

      # Roda toda vez que o workspace e iniciado.
      onStart = {
        # Roda as migracoes do banco de dados
        migrate = "venv/bin/python manage.py migrate";
      };
    };

    # Configura o preview da aplicacao web
    previews = {
      enable = true;
      previews = {
        web = {
          # Comando para iniciar o servidor de desenvolvimento do Django usando o Python do ambiente virtual
          command = ["venv/bin/python", "manage.py", "runserver", "0.0.0.0:$PORT"];
          manager = "web";
        };
      };
    };
  };
}
