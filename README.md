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


Prints com os resultados: 
```
No terminal de comando: 
<img width="709" height="43" alt="image" src="https://github.com/user-attachments/assets/0e58dd00-3949-40d5-aa99-4742da0dd0ab" />

No Docker:
<img width="889" height="428" alt="image" src="https://github.com/user-attachments/assets/66b1f8ca-2835-4c14-aa3a-7d8c5193f21a" />



```
