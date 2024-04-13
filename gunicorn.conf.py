import os
from gunicorn.app.wsgiapp import WSGIApplication

# Define o caminho para o arquivo wsgi.py do seu projeto Django
wsgi_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wsgi.py')

# Crie a aplicação Gunicorn com as opções de configuração desejadas
app = WSGIApplication(wsgi_path,
                       workers=3,  # Número de trabalhadores
                       worker_class='sync',  # Classe do trabalhador
                       worker_connections=1000,  # Número de conexões por trabalhador
                       max_requests=1000,  # Número máximo de solicitações por trabalhador
                       max_requests_jitter=1000,  # Desvio padrão do número máximo de solicitações por trabalhador
                       )