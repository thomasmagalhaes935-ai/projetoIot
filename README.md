# Processo Seletivo – Intensivo Maker | IoT
## Etapa Prática – Sistemas Embarcados

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker | IoT**.

Esta atividade tem como objetivo avaliar suas competências em **Sistemas Embarcados**, com foco em **organização de projeto, lógica de firmware e simulação de hardware**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Objetivo principal**  
> Avaliar sua capacidade de **planejar, estruturar e desenvolver** uma solução funcional de sistemas embarcados, seguindo boas práticas de engenharia.

---

## 🏁 Passo 0 – Antes de Tudo

Se você **nunca utilizou Git ou GitHub**, não se preocupe.  
Siga atentamente os passos abaixo — eles fazem parte do processo de aprendizagem esperado.

---

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

> 📌 O GitHub será utilizado para:
> - Envio do seu projeto  
> - Versionamento do código  
> - Correção e validação automática via GitHub Actions  

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta responsável pelo controle de versões do seu código.

### Windows
Baixe e instale o **Git Bash**:  
https://git-scm.com/downloads

### Linux / macOS
Verifique se o Git já está instalado:

```bash
git --version
```
> Caso não esteja, instale pelo gerenciador de pacotes do seu sistema.

## ⚙ Passo 1 – Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório no seu GitHub.

### 1️⃣ Fork do Repositório
No canto superior direito desta página, clique em Fork

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />


Uma cópia do repositório será criada no seu perfil do GitHub

> 🔎 O Fork permite que você trabalhe de forma independente, sem alterar o repositório original do processo seletivo.

### 2️⃣ Clone do Repositório

No repositório do seu Fork, clique em **<> Code**

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Copie a URL e execute no terminal:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

> O comando git clone cria uma cópia local do repositório para desenvolvimento.

### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de duas formas. Escolha apenas uma.

#### 🔹 Opção A – Ambiente Python Local

**Requisitos:**

- Python 3.10 ou 3.11
- pip

**Instale as dependências:**

```bash
pip install -r requirements.txt
```

#### 🔹 Opção B – Dev Container (Recomendado)

Este repositório inclui um Dev Container, garantindo um ambiente padronizado.

**Requisitos:**

- VS Code
- Docker instalado
- Extensão Dev Containers

**Passos:**

1. Abra o repositório no VS Code
2. Clique em “Reopen in Container”
3. Aguarde a criação automática do ambiente

> ➡️ Todas as dependências serão instaladas automaticamente.

## 🔐 Passo 2 – Criando sua API Key do Wokwi

A simulação do projeto será executada automaticamente via GitHub Actions, utilizando o Wokwi CLI.

Para isso, você precisa gerar uma API Key.

1. Acesse: https://wokwi.com/dashboard/ci
2. Faça login (Google ou GitHub)
3. Clique em Generate API Token
4. Copie a chave gerada (exemplo: wokwi-xxxxxxxx)

>⚠️ Importante
- Nunca faça commit dessa chave
- Ela deve ser armazenada apenas como secret no GitHub

## 🔒 Passo 3 – Configurando a API Key no GitHub (Secrets)

**No repositório do seu Fork:**

1. Vá em Settings
2. Acesse Secrets and variables → Actions
3. Clique em New repository secret
4. Nome: WOKWI_API_KEY
5. Valor: sua chave gerada
6. Salve

> ✔️ As GitHub Actions do template já estão preparadas para usar essa variável automaticamente.

## 🧠 Passo 4 – Desafio Técnico

Você deverá desenvolver um projeto de sistemas embarcados simulados, utilizando Python e Wokwi.

### 📁 Estrutura mínima esperada

```text
/project
 ├── src/
 │   └── main.py        # Código principal do projeto
 ├── wokwi.toml         # Configuração da simulação
 ├── diagram.json       # Circuito no Wokwi
 └── README.md          # Explicação do seu projeto
```

> Você pode expandir essa estrutura se desejar, desde que mantenha os arquivos essenciais.

### 🛠 Como Desenvolver seu Projeto

O desenvolvimento acontece principalmente nos arquivos abaixo:

#### 1️⃣ src/main.py

- Código Python executado na simulação
- Implementa a lógica do sistema embarcado
- Exemplos: controle de LEDs, leitura de sensores, estados, temporizações, etc.

#### 2️⃣ diagram.json

- Define o hardware virtual do projeto
- Componentes como:
  - LEDs
  - Botões
  - Sensores
  - Placa microcontroladora

#### 3️⃣ wokwi.toml

- Configura a simulação:
  - Tipo de placa
  - Framework
  - Dependências adicionais

#### 4️⃣ Commit e Push

Após suas alterações:

```bash
git add .
git commit -m "Descrição clara do que foi feito"
git push
```
### ⚙ Execução Automática (GitHub Actions)

A cada push, o GitHub Actions irá automaticamente:

- Executar o pipeline de build
- Rodar a simulação via Wokwi CLI
- Validar que o projeto executa sem erros

### 📌 Caso algo falhe:

- Vá até a aba Actions
- Analise os logs da execução
- Corrija e envie novamente

## 📊 Critérios de Avaliação

Esta etapa será avaliada considerando:

- Funcionamento correto da simulação
- Código organizado e legível
- Estrutura de arquivos correta
- Uso adequado do Wokwi
- Commits claros e bem descritos
- Projeto executando sem falhas nas Actions

---

## 📎 Submissão Final

Após concluir o desenvolvimento:

1. Verifique se o projeto **executa sem erros** nas GitHub Actions  
2. Confirme que todos os arquivos obrigatórios estão presentes  
3. Copie o link do **seu repositório no GitHub**

📤 Envie o link conforme as orientações do processo seletivo na plataforma **Moodle**.

---

## 📝 Relatório do Candidato

O arquivo **`README.md` do seu repositório** deve ser utilizado como o  
**relatório final do desafio técnico**.

Preencha todas as seções abaixo de forma **clara, objetiva e técnica**.

> 💡 **Dica importante**  
> Não é necessário um relatório extenso.  
> O principal critério é demonstrar **clareza nas decisões técnicas**, organização e entendimento do sistema embarcado desenvolvido.

---
Sistema Inteligente de Monitoramento e Rega Simulada de Plantas

### 👤 Identificação do Candidato

- **Nome completo: Thomas de Sousa Magalhães 
- **GitHub:* thomasmagalhaes935-ai

---

## 1️⃣ Visão Geral da Solução

O projeto desenvolvido consiste em um **sistema embarcado inteligente para monitoramento de umidade e controle de rega de múltiplas plantas**, utilizando simulação no Wokwi com microcontrolador ESP32.

A solução representa quatro tipos de plantas com necessidades hídricas diferentes:

- Cacto  
- Suculenta  
- Samambaia  
- Horta  

Cada planta possui comportamento próprio de secagem e volume de rega.

O sistema permite ao usuário:

- Selecionar a planta monitorada por botão  
- Regar manualmente a planta selecionada  
- Alterar as condições climáticas usando o potenciômetro  
- Visualizar o estado da planta através de LED RGB  
- Identificar plantas em estados críticos através de LEDs individuais piscantes  
- Acompanhar dados detalhados via terminal  

O objetivo foi simular um sistema de automação para cuidar de plantas em casa, utilizando conceitos básicos de sistemas embarcados, como leitura de entradas, controle de saídas, uso de estados, temporização e interação com o usuário.

O projeto foi desenvolvido e testado no Wokwi via navegador e depois sua estrutura foi organizada no VS Code para poder ser subida para o github. 

---

## 2️⃣ Arquitetura do Sistema Embarcado

O flux do programa opera em **loop infinito**, realizando continuamente:

1. Leitura dos botões  
2. Controle de debounce 
3. Atualização do pisca-alerta dos LEDs em estado críticos  
4. Leitura do potenciômetro (clima externo)  
5. Simulação de perda de umidade das plantas  
6. Atualização dos LEDs indicadores  
7. Atualização do LED RGB da planta focada  
8. Impressão de informações no terminal serial  


### Entradas:

- **Botão 1 (Azul) :** Regar planta selecionada  
- **Botão 2 (Preto) :** Alternar planta selecionada   
- **Potenciômetro:** Simula clima ambiente (Muito Seco/ Seco / Ideal / Umido/ Muito umido)


Cada planta possui atributos independentes:

- Nome  
- Umidade atual  
- Taxa base de secagem  
- Quantidade de água quando regada  
- Última vez regada  

A taxa de secagem é influenciada pelo potenciômetro

O sistema classifica a planta em cinco estados, o estado atual é representado pela cor no LED RGB:

 - Seco_Critico (Vermelho)
 - Seco (Laranja)
 - Ideal (Verde)
 - Umido (Azul)
 - Excesso (Roxo)

Características dos Leds individuais:

- LED aceso fixo = planta selecionada
- LED piscando = planta em estado crítico
- LED apagado = planta não selecionada




## 3️⃣ Componentes Utilizados na Simulação

| Componente | Quantidade | Função no Sistema |  Ligação |
|-----------|-----------|------------------|---------------|
| ESP32  | 1 | Microcontrolador principal responsável pelo processamento do sistema | — |
| Push Button | 2 | Um botão para rega manual e outro para seleção de planta |  33 /  26 |
| Potenciômetro | 1 | Simula condições climáticas que afetam a secagem das plantas |  34 |
| LED RGB (Cátodo Comum) | 1 | Indica o estado da planta selecionada por cores |  4, 5 e 18 |
| LED Laranja | 1 | Indicador da planta 1 | 12 |
| LED Branco | 1 | Indicador da planta 2 | 13 |
| LED Roxo | 1 | Indicador da planta 3 | 14 |
| LED Ciano | 1 | Indicador da planta 4 |  27 |

## 4️⃣ Decisões Técnicas Relevantes

Funções com responsabilidades especificas:

 - interpretar_clima()
 - determinar_estado()
 - set_color()
 - atualizar_led_rgb()
 - verificar_botoes()

Uso de dicionário para o armazenamento dos dados das plantas

Uso de time.ticks_ms() para evitar variaveis bloqueantes como o sleep()



## 5️⃣ Resultados Obtidos

O sistema executa de forma perfeita na simulação Wokwi do navegador

Funcionalidades Implementadas:

 - Seleção entre 4 plantas
 - Rega individual por botão
 - Controle climático por meio do potenciômetro
 - Simulação dinâmica de secagem
 - Indicação visual por LED RGB
 - Alertas críticos com leds piscantes
 - Terminal informativo com dados técnicos

Durante a simulação:

 - Plantas perdem umidade ao longo do tempo
 - Clima seco acelera perda de água
 - Regar recupera a umidade
 - LEDs respondem em tempo real
 - Mudança de planta ocorre instantaneamente

## 6️⃣ Comentários Adicionais (Opcional)

A maior dificuldade foi em ajustar corretamente a lógica botões e temporizações.
O projeto foi refeito 3 vezes para poder compilar perfeitamente no gitActions.

Possiveis melhorias futuras:

 - Display OLED com os dados mais relevantes
 - Rega automática por limite mínimo
 - Histórico de umidade
 - Sensores reais de solo e temperatura

> ✅ Este relatório faz parte da avaliação técnica.  
> Clareza, objetividade e organização são tão importantes quanto o funcionamento do código.

---

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
Mostre sua capacidade de pensar como um engenheiro de sistemas embarcados.
****
