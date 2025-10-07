{ pkgs, ... }: {
  # Usa o canal estável do Nix
  channel = "stable-24.05";

  # Instala o Python e o pip. As dependências do Python serão geridas pelo pip.
  packages = [
    pkgs.python3
    pkgs.python3Packages.pip
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
      # Roda apenas uma vez quando o workspace é criado para instalar as dependências.
      onCreate = {
        install-deps = "pip install -r requirements.txt";
      };
      onStart = {
        # Roda as migrações quando o workspace inicia
        run-migrations = "python manage.py migrate";
      };
    };

    # Configura o preview da aplicação web
    previews = {
      enable = true;
      previews = {
        web = {
          command = ["python" "manage.py" "runserver" "0.0.0.0:$PORT"];
          manager = "web";
        };
      };
    };
  };
}
