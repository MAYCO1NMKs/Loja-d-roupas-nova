{ pkgs, ... }: {
  # Usa o canal estável do Nix
  channel = "stable-24.05";

  # Instala o Python e o pip usando o Nix
  packages = [
    pkgs.python3
    pkgs.pip
  ];

  # Variáveis de ambiente para o Django
  env = {
    SECRET_KEY = "django-insecure-@e^z-v71g@+6_j85_d=12#m#9v2_#g81%j7$3k2d(2@k7#t_l";
    DEBUG = "True";
    ALLOWED_HOSTS = "*";
    CSRF_TRUSTED_ORIGINS = "https://*.cloudworkstations.dev";
  };

  idx = {
    extensions = [
      # Extensão recomendada para desenvolvimento em Python
      "ms-python.python"
    ];
    workspace = {
      # Roda apenas uma vez quando o workspace é criado.
      onCreate = {
        # Cria um ambiente virtual
        create-venv = "python -m venv venv";
        # Instala as dependências do requirements.txt no ambiente virtual
        install-deps = "venv/bin/pip install -r requirements.txt";
      };

      # Roda toda vez que o workspace é iniciado.
      onStart = {
        # Roda as migrações do banco de dados
        migrate = "venv/bin/python manage.py migrate";
        # Cria um superusuário se não existir
        create-superuser = "venv/bin/python manage.py create_superuser";
      };
    };

    # Configura o preview da aplicação web
    previews = {
      enable = true;
      previews = {
        web = {
        
          command = ["venv/bin/python" "manage.py" "runserver" "0.0.0.0:$PORT"];
          manager = "web";
        };
      };
    };
  };
}
