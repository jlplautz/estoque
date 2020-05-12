# Estoque

Controle de estoque


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/rg3915/estoque.git
cd estoque
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


- Codigo NCM -> Nomenclatura Comum do Mercosul

```
Chegou o momento para você entender de uma vez por todas qual é o funcionamento da NCM. 
Cada número ou par representa uma característica:

    2 primeiros dígitos – Capítulo;
    4 primeiros dígitos – Posição;
    6 primeiros dígitos – Subposição;
    7º dígito da NCM – Item;
    8º dígito da NCM – Subitem.

O NCM 3003.10.12, por exemplo, deve ser entendido da seguinte forma:

    Capítulo 30: Produtos farmacêuticos;
    Posição 3003: Medicamentos (exceto os produtos das posições 30.02,030.05 ou 30.06) constituídos por produtos 
                  misturados entre si, preparados para fins terapêuticos ou profiláticos, mas não apresentados em doses 
                  nem acondicionados para venda a retalho;
    Subposição 3003.10: Que contenham penicilinas ou seus derivados, com estrutura do ácido penicilânico, 
                        ou estreptomicinas ou seus derivados;
    Item 3003.10.1: Que contenham penicilinas ou seus derivados, com estrutura do ácido penicilânico;
    Subitem 3003.10.12: Amoxicilina ou seus sais.
```


## Links

[python-decouple](https://github.com/henriquebastos/python-decouple)

[package-of-the-week-python-decouple](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)

[github.com/rg3915/tutoriais django-basic](https://github.com/rg3915/tutoriais/tree/master/django-basic)

[bootstrap starter-template](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)

[emmet](https://emmet.io/)

[start.html](https://github.com/JTruax/bootstrap-starter-template/blob/master/template/start.html)

[django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks)

[Class Based View - ccbv.co.uk](https://ccbv.co.uk/)

[form-inline](http://felipefrizzo.github.io/post/form-inline/)

[form-inline-cbv](http://felipefrizzo.github.io/post/form-inline-cbv/)

[django-bootstrap-form](https://django-bootstrap-form.readthedocs.io/en/latest/)

[Paginação - gist](https://gist.github.com/rg3915/01ca76f099f431c24bc0536bef83076b)

[Paginação - Bootstrap](https://getbootstrap.com/docs/4.3/components/pagination/)

