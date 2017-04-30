# TaskSys

Uma **Django REST API** simples para manter controle das suas tarefas diárias.

Desenvolvido utilizando os packages incluidos em : `./requirements.txt` (veja instalação para mais detalhes)


## Instruções

Estas instruções irão permitir que você obtenha uma cópia do projeto e execute-a na sua máquina local para desenvolvimento e testes.

### Pré-requisitos

1.  Conhecimento básico em:
    * Terminal/console/bash/prompt de comando;
    * git;
    * Python;
    * virtualenv;


1. Certifique-se de possuir o Python 3 instalado em sua máquina


1. Certifique-se de possuir o Python instalado em sua máquina (versão 2.7.X);

1. Instalação do PostgreSQL9.5;


Para manter as configurações apenas neste projeto, utilize o [*virtualenv*](https://virtualenv.pypa.io/en/stable/)  (veja instalação para mais detalhes)



### Instalação



Navegue até a pasta onde você clonou este repositório. Se ainda não o fez, digite o seguinte código no terminal:

```
$ git clone https://github.com/AndreLuisGO/tasksys.git
```
Após feito, navegue até a pasta com
```
$ cd tasksys
```

* Modifique as configurações de conexão com o banco de dados no arquivo  `tasksys/settings.py`, nas linhas 88-91 com seu usuário, senha, host e portas conforme suas configurações.




1 - Instale o pip utilizando:
```
$ sudo easy_install pip
```

2 - Ative o seu ambiente virtual (virtualenv)
Caso o ambiente tenha sido ativado, você irá notar o nome do mesmo (ex: `env`) no terminal:
```
(env) $
```

Pronto, agora estamos prontos para instalar as dependências para que o projeto seja executado.


3 - Para instalação das dependências, navegue até a pasta raiz do projeto tasksys :
```
cd /tasksys
```

4 - Agora, instale os requisitos:

```
(env) $ pip install -r requirements.txt
```

5 - Agora, basta iniciar o servidor

```
python3 manage.py runserver
```

6 - Se tudo der certo, você irá ver a seguinte mensagem:

```
Performing system checks...                                                                                                                                                                                                                     System check identified no issues (0 silenced).                                                                         April 27, 2017 - 15:01:37                                                                                               Django version 1.11, using settings 'tasksys.settings'                                                                  Starting development server at http://127.0.0.1:8000/                                                                   Quit the server with CTRL-BREAK.
```


7 - Feito isso, abra seu navegador e acesse:

`http://127.0.0.1:8000/tarefas`

O resultado é uma janela com a informação da API REST. Isso significa que o servidor da API está funcional e em execução.

 Caso queira ver o resultado em JSON, use:

`http://127.0.0.1:8000/tarefas/?format=json`

Isso retornara o json com todas as tarefas do banco.

Para ver o resultado de uma tarefa específica, use

`127.0.0.1:8000/tarefas/1`
ou
`127.0.0.1:8000/tarefas/5/?format=json`

onde o /1/ deve ser a chave primária (PK) da tarefa que se deseja obter os dados. ( no caso, da tarefa de PK = 1)

## Deploy

Add additional notes about how to deploy this on a live system

## Construído com

* [Dango](https://www.djangoproject.com/)
* [Django Rest Framework](www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [Psycopg2](http://initd.org/psycopg/)


## Autor

* [**André Luis Oliveira**] - (https://github.com/AndreLuisGO)


## Reconhecimentos

* Toda a vasta comunidade de desenvolvedores do StackOverflow
* [Derek Banas](https://www.youtube.com/derekbanas) e seus incríveis tutoriais.
* Todos que, de alguma maneira, contribuíram para o sucesso do projeto, mesmo que moralmente.
