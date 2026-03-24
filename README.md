# IFSP-PTB - PTBDAMS: APIs REST - Tutorial

Autora: Débora Laranjeira

Esta tutorial exemplifica a implementação de dois microsserviços demonstrando a comunicação direta (síncrona) entre eles. É parte da aula da disciplina "Desenvolvimento de APIs e Microsserviços" do curso TADS - Campus Pirituba.


**💻 Cenário proposto:**

Microsserviço 1 – Produtos
* Endpoint: /produtos/{id}
* Consulta dados de disponibilidade no estoque

Microsserviço 2 – Estoque
* Endpoint: /estoque/{id}
* Retorna dados de inventário mockados

---

**✔ Tecnologias sugeridas:**
* FastAPI (Python)
* REST API
* Docker e Docker Compose

---

#### Subindo os containers

```
docker-compose up --build
```

**O que acontece aqui?**

* O Docker vai buildar as imagens dos dois serviços
* Criar containers separados
* Criar uma rede interna
* Permitir comunicação entre serviços pelo nome (estoque)

---

#### Testando os serviços

**Serviço de estoque**
Acesse no navegador ou estoque API:
```
http://localhost:8001/estoque/1
```
Saída esperada no Navegador: 

<img width="376" height="133" alt="image" src="https://github.com/user-attachments/assets/e137adf0-3ad3-4e0d-930c-ba59670972e0" />


**Serviço de produtos**
Acesse no navegador ou produtos API:
```
http://localhost:8000/produtos/1
```
Saída esperada no Navegador: 

<img width="669" height="133" alt="image" src="https://github.com/user-attachments/assets/78a38e50-0e41-4744-9e0c-2e1a40587384" />

**Erros esperados:** 

Delay: 

<img width="728" height="139" alt="image" src="https://github.com/user-attachments/assets/b54b0508-6e6c-49ae-b0f6-d8061815866c" />

Serviço Offline:

<img width="906" height="617" alt="image" src="https://github.com/user-attachments/assets/8214ed5e-ffbc-48a9-8a8d-034d0cd8d86c" />

**Neste tipo de implementação, quais problemas podem ocorrer?** 

Nesse sistema que eu montei, o maior problema acaba sendo o acoplamento síncrono, que cria uma dependência bem direta entre os serviços. Como o meu serviço de produtos precisa esperar o estoque responder para completar a requisição, qualquer instabilidade no estoque acaba travando o fluxo inteiro. Se o estoque ficar lento, a minha vitrine de produtos também fica lenta, o que aumenta a latência para quem está acessando. Além disso, tem o risco do efeito cascata: se o estoque cair de vez, o serviço de produtos até continua de pé, mas vai entregar uma informação incompleta ou dar erro se eu não tratar a falha direito. Outro ponto complicado é que a rede vira um ponto único de falha; se rolar um soluço na comunicação entre os containers, a experiência do usuário é prejudicada mesmo com o código funcionando. Por isso que eu tive que colocar aquele timeout e o tratamento de exceção, para garantir que o sistema tenha um mínimo de resiliência e não quebre totalmente quando um pedaço dele para de responder.


```
