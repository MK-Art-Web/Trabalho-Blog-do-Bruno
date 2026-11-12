# 🧪 Relatório de Testes de Usabilidade e Acessibilidade
**Projeto:** CyberSeguro — Blog de Segurança Digital para a Comunidade de Acopiara  
**Etapa:** Entrega da Semana 3 | **Data dos Testes:** 04 e 05 de Novembro de 2024  
**Equipe Responsável:** Daniel Costa (Designer/UX) e Bruno Santos (Pesquisador)

---

## 1. Metodologia do Teste
Para assegurar que o blog cumprisse sua missão social de educar públicos diversos em Acopiara, foram selecionadas **3 pessoas externas ao grupo e sem formação prévia em TI**, representando as diferentes parcelas da comunidade previstas no público-alvo:

1. **Dona Maria das Graças (68 anos):** Aposentada, utiliza smartphone básico (Android) para falar com a família e consultar saldo previdenciário. Baixa familiaridade técnica.
2. **Seu Francisco Souza (46 anos):** Pequeno comerciante (proprietário de uma mercearia no centro de Acopiara), atende clientes e recebe comprovantes pelo WhatsApp Comercial.
3. **Lucas Gabriel (16 anos):** Estudante do Ensino Médio de outra escola pública local, usuário frequente de redes sociais (Instagram, TikTok) e jogos online.

### Roteiro de Tarefas Propostas aos Testadores:
* **Tarefa 1:** Acessar a página inicial pelo celular e encontrar um artigo que ensine como se proteger de clonagem de WhatsApp.
* **Tarefa 2:** Abrir o artigo prático de Verificação em Duas Etapas e tentar identificar o passo a passo de ativação no aplicativo que mais utiliza.
* **Tarefa 3:** Encontrar o canal de dúvidas ou contato e enviar uma mensagem simples com uma dúvida simulada.
* **Tarefa 4:** Avaliar a legibilidade dos textos (tamanho da fonte, contraste de cores e clareza das palavras).

---

## 2. Resultados Coletados por Usuário

### Teste 1: Dona Maria das Graças (Perfil Idosa / Aposentada)
* **Tempo médio para encontrar os artigos:** 1min 15s.
* **Pontos Positivos Observados:** Adorou o uso de ícones e emojis grandes (📱, 🎣, 🔑); conseguiu navegar facilmente rolando a tela; achou a analogia da pescaria no phishing muito clara ("Agora entendi o que meu neto falava!").
* **Dificuldades e Feedbacks:** Achou o texto inicial em algumas caixas um pouco miúdo no celular com tela menor; perguntou se o botão azul do topo servia para voltar à página principal.
* **Ajuste Realizado:** Aumentamos o tamanho base da fonte para `16px`, elevamos o contraste da cor secundária e ampliamos a área de toque dos botões do menu mobile.

---

### Teste 2: Seu Francisco Souza (Perfil Comerciante Local)
* **Tempo médio para encontrar os artigos:** 45s.
* **Pontos Positivos Observados:** Navegação ágil; identificou de imediato a importância da matéria sobre senhas e a de LGPD sobre o uso do CPF; achou muito prático o formulário de contato para tirar dúvidas.
* **Dificuldades e Feedbacks:** Sugeriu que o checklist prático de 2FA ficasse visualmente destacado como uma lista de tarefas que ele pudesse ir conferindo enquanto lia.
* **Ajuste Realizado:** Implementamos na classe `.checklist` marcadores verdes de verificação (✅) e criamos a caixa de destaque `.tip-box` e `.warning-box` com bordas laterais coloridas para chamar a atenção para ações imediatas.

---

### Teste 3: Lucas Gabriel (Perfil Jovem / Estudante)
* **Tempo médio para encontrar os artigos:** 20s.
* **Pontos Positivos Observados:** Elogiou a identidade visual limpa e moderna ("Não parece site antigo de prefeitura, é bonito!"); testou a página de "Nova Postagem" e gostou do preview em tempo real.
* **Dificuldades e Feedbacks:** Notou que quando navegava apenas com o teclado no computador da escola, o cursor não destacava claramente onde estava o foco em alguns links.
* **Ajuste Realizado:** Adicionamos a regra CSS `:focus-visible` com borda contrastante de 3px em azul, garantindo conformidade com o critério de acessibilidade WCAG 2.4.7 (Foco Visível).

---

## 3. Síntese dos Ajustes Implementados no Blog

| Área Avaliada | Problema Relatado no Teste | Solução Implementada no Código |
| :--- | :--- | :--- |
| **Acessibilidade Visual** | Dificuldade de leitura para idosos em celulares compactos | Aumento do tamanho de fonte de parágrafos para `1.05rem` e linha para `1.8`, garantindo contraste mínimo de 4.5:1. |
| **Navegação por Teclado** | Ausência de destaque no elemento selecionado via tecla Tab | Implementação do seletor `:focus-visible` e do link oculto `.skip-link` para pular direto ao conteúdo principal. |
| **Escaneabilidade** | Textos longos cansativos em tutoriais de configuração | Substituição de parágrafos contínuos por `.step-list` (lista com números circulares destacados) e caixas `.tip-box`. |
| **Menu Mobile** | Dificuldade para fechar o menu no celular após toque | Adicionado script que recolhe automaticamente o menu retrátil ao clicar em qualquer link interno. |
| **Canal de Dúvidas** | Incerteza se a mensagem de contato foi gravada | Adição do componente visual `.notification` (toast verde) confirmando que a mensagem foi recebida com sucesso. |

---

## 4. Conclusão dos Testes
A rodada com pessoas reais da comunidade de Acopiara foi decisiva para lapidar a experiência do usuário. O projeto deixou de ser apenas um exercício acadêmico em sala de aula e tornou-se uma ferramenta verdadeiramente acolhedora, inclusiva e funcional para os moradores.
