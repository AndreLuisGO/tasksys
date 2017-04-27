# TaskSys

Uma **Django REST API** simples para manter controle das suas tarefas diárias.

Desenvolvido utilizando os packages incluidos em : `./requirements.txt` (veja instalação para mais detalhes)


## Instruções

Estas instruções irão permitir que você obtenha uma cópia do projeto e execute-a na sua máquina local para desenvolvimento e testes.

### Prerequisites

 Conhecimento básico em:
    - Terminal/console/bash/prompt de comando
    - git
    - Python


Certifique-se de possuir o Python instalado em sua máquina (versão 2.7.X)


Para manter as configurações apenas neste projeto, utilize o *virtualenv*  (veja instalação para mais detalhes)



### Instalação



Navegue até a pasta onde você clonou este repositório. Se ainda não o fez, digite o seguinte código no terminal:

```
$ git clone https://github.com/AndreLuisGO/tasksys.git
```
Após feito, navegue até a pasta com
```
$ cd tasksys
```


1 - Instale o pip utilizando:
```
$ sudo easy_install pip
```

2 - Navegue até a pasta env e ative o ambiente virtual env
```
$ cd env/Scripts
```
```
$ activate
```
Caso o ambiente tenha sido ativado, você irá notar o nome `env` no terminal:
```
(env) $
```

Pronto, agora estamos prontos para instalar as dependências para que o projeto seja executado.


3 - Para instalação das dependências, navegue até a pasta /env/tasksys :
```
cd ../tasksys
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


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
