# 📄 Prompt Mestre e Guia de Engenharia de Prompt
## Projeto: Blog de Segurança Digital para a Comunidade (Acopiara-CE)

Este documento reúne o **Prompt Mestre Completo (All-in-One)** e os **Prompts Modulares Semanais** prontos para serem utilizados em qualquer modelo avançado de Inteligência Artificial (ChatGPT, Claude, Gemini ou Antigravity) para recriar todo o projeto avaliativo prático com 100% de conformidade com a rubrica escolar.

---

## 🌟 Opção 1: O Mega-Prompt Mestre (Execução Completa em 1 Clique)

> **Instruções:** Copie todo o bloco de código abaixo e cole no seu assistente de IA.

```markdown
Você é um desenvolvedor web especialista, designer de UX/UI, educador em segurança da informação e líder técnico.

Sua missão é desenvolver integralmente o projeto escolar prático avaliativo intitulado:
"Projeto Avaliativo Prático 01: Blog de Segurança Digital para a Comunidade"
Curso: Ensino Médio Técnico em Informática | Série: 2º ano | Célula de 5 integrantes.

### 1. CONTEXTO E SITUAÇÃO-PROBLEMA
A cidade de Acopiara (CE) está passando por rápida digitalização. O comércio local vende por WhatsApp e Instagram, serviços públicos operam via smartphone e idosos recebem benefícios por aplicativos bancários. Porém, nos últimos meses, a Associação de Moradores registrou aumento expressivo de golpes: mensagens bancárias falsas, links promocionais fraudulentos, clonagem de WhatsApp, roubo de contas e senhas reutilizadas. A Associação enviou um ofício à escola técnica solicitando a criação de um canal confiável, atualizado e fácil de entender para proteger a comunidade.

### 2. ARQUITETURA E TECNOLOGIAS EXIGIDAS
- Tecnologias: HTML5 semântico, CSS3 moderno/acessível e JavaScript Vanilla (nativo, sem frameworks pesados).
- Responsividade: Design "mobile-first" que funcione perfeitamente em telas de celulares pequenos até monitores grandes.
- Acessibilidade: Conformidade com WCAG 2.1 AA (contraste de cor mínimo de 4.5:1, foco visível :focus-visible, links de salto <a href="#main" class="skip-link">, botões táteis e atributos aria).
- Privacidade: O blog NÃO pode coletar nem rastrear dados pessoais sem consentimento e justificativa expressa.
- Identidade Visual: Nome "CyberSeguro", logotipo com ícone de escudo (🛡️), paleta harmônica (azul primário #1a73e8, verde acento #34a853, alertas amarelo e vermelho) e tipografia Inter (Google Fonts).

### 3. PÁGINAS E ARQUIVOS QUE VOCÊ DEVE CRIAR

1. `css/style.css`: Estilo visual completo, responsivo, acessível, com sistema de cards, tipografia, formulários e regras @media print.
2. `js/main.js`: Lógica para menu mobile retrátil, persistência de postagens e contatos via localStorage, escape de caracteres contra XSS e pré-visualização ao vivo.
3. `index.html`: Página inicial com:
   - Apresentação do projeto e situação-problema de Acopiara;
   - Definição explícita do Público-Alvo (idosos, comerciantes locais e estudantes);
   - Apresentação da equipe de 5 alunos e suas funções;
   - Grid com os 6 cards de artigos originais;
   - Seção dinâmica reservada para publicações da comunidade (<div id="dynamic-posts">).
4. `sobre.html`: História do atendimento ao ofício da Associação de Moradores, missão do blog e perfil detalhado dos 5 integrantes:
   - Ana Silva (Coordenadora de Projeto)
   - Bruno Santos (Pesquisador de Conteúdo)
   - Carla Oliveira (Redatora e Revisora)
   - Daniel Costa (Designer / UX)
   - Elena Souza (Responsável Técnica)
5. `transparencia.html`: Página explicando como a IA foi empregada com responsabilidade, tabela de ferramentas (ChatGPT/Gemini), o que foi aproveitado, corrigido e descartado, compromissos éticos e relação de fontes oficiais consultadas.
6. `criar-postagem.html`: Página funcional dedicada a criar publicações, com campos de título, categoria, autor, barra de ferramentas (negrito, itálico, títulos H2/H3, citações, dicas, avisos) e pré-visualização em tempo real.
7. `contato.html`: Formulário de contato/dúvidas com validação visual, canais institucionais e aviso de privacidade.
8. `diario-de-bordo.html`: Versão documental pronta para leitura e impressão em PDF (Ctrl+P) do Diário de Bordo de IA, com tabela cronológica de prompts e espaço para assinaturas da célula.

### 4. AS SEIS POSTAGENS OBRIGATÓRIAS (300 A 600 PALAVRAS CADA, LINGUAGEM LEIGA E FONTES AO FINAL)
- `post-phishing.html`: Como identificar links e e-mails falsos, analogia da pescaria, exemplos brasileiros e dicas de prevenção.
- `post-whatsapp.html`: Clonagem de contas, diferença entre engenharia social (código de 6 dígitos) e SIM swap (troca de chip), e o que fazer se invadido.
- `post-senhas.html`: Senhas fracas mais usadas, técnica da frase secreta memorável e uso de gerenciadores de senhas gratuitos.
- `post-2fa.html` [FORMATO PRÁTICO]: Guia passo a passo com telas do WhatsApp, Google e Instagram, comparativo SMS vs. App Autenticador e Checklist final de checagem.
- `post-wifi.html`: Os riscos de conexões públicas gratuitas em praças, ataque do falso ponto de acesso, diferença HTTP vs. HTTPS e uso de rede móvel.
- `post-lgpd.html`: Lei Geral de Proteção de Dados (Lei 13.709/2018) explicada para pessoas comuns e comerciantes, cuidados com o CPF e o papel da ANPD.

### 5. DOCUMENTOS AVALIATIVOS COMPLEMENTARES (FORMATO MARKDOWN)
- `PLANO_DO_PROJETO.md`: Entrega da Semana 1 com justificativa, público, cronograma e funções do grupo.
- `RELATORIO_DE_TESTES.md`: Entrega da Semana 3 com relatório de testes de usabilidade com 3 pessoas externas sem intimidade com TI (uma idosa de 68 anos, um comerciante local de 46 anos e um jovem de 16 anos), registrando feedbacks e melhorias implementadas no código.
- `REFLEXOES_FINAIS.md`: Respostas individuais do Item 10 da rubrica para cada um dos 5 alunos (10 a 15 linhas para cada uma das 4 perguntas reflexivas).
- `ROTEIRO_APRESENTACAO.md`: Roteiro cronometrado de 10 a 15 minutos com estrutura de slides, falas distribuídas entre os alunos e guia de respostas para a banca.

Gere todo o código e os textos completos, sem abreviações, com alto padrão de acabamento e profissionalismo.
```

---

## 🧩 Opção 2: Prompts Modulares por Semana (Execução Passo a Passo)

Caso prefira desenvolver o projeto em etapas pedagógicas (ou em modelos com limite de contexto menor), use a sequência a seguir:

---

### 📅 Semana 1 — Compreender, Planejar e Estruturar o Projeto
**Objetivo:** Criar a identidade, o planejamento e os arquivos base de estilo e layout.

```markdown
Atue como líder de projeto de software e redator técnico. 
Com base na situação-problema da cidade de Acopiara-CE (onde a Associação de Moradores solicitou à escola técnica um canal educativo contra golpes digitais em idosos e comerciantes locais), elabore a documentação da Semana 1:

1. Gere o arquivo `PLANO_DO_PROJETO.md` contendo:
   - Nome oficial: "CyberSeguro: Seu Escudo Digital na Comunidade";
   - Diagnóstico da situação-problema e justificativa;
   - Descrição detalhada dos 3 públicos-alvo (idosos, comerciantes de WhatsApp e jovens);
   - Divisão das atribuições dos 5 membros (Ana Silva - Coordenação, Bruno Santos - Pesquisa, Carla Oliveira - Redação, Daniel Costa - UX/Design, Elena Souza - Técnica);
   - Matriz dos 6 temas selecionados e cronograma semanal de 4 semanas.

2. Crie os arquivos base:
   - `css/style.css`: Estilização completa, moderna, com variáveis CSS, tipografia Inter, classes para caixas de destaque (.tip-box, .warning-box, .danger-box), listas de passos (.step-list), checklist (.checklist) e design responsivo.
   - `js/main.js`: Código JavaScript para menu responsivo móvel, gerenciamento de postagens via localStorage e funções utilitárias.
```

---

### 📅 Semana 2 — Base no Ar e Primeiras 3 Postagens
**Objetivo:** Criar a página inicial, página sobre e os 3 primeiros artigos de conscientização.

```markdown
Atue como desenvolvedor front-end e redator especialista em segurança digital para leigos.
Crie as seguintes páginas HTML conectadas ao `css/style.css` e `js/main.js`:

1. `index.html`:
   - Hero banner com o propósito do blog;
   - Seções claras apresentando o Projeto, o Público-Alvo e a Equipe;
   - Grid de cards com títulos atrativos, tags coloridas e resumos;
   - Área <div id="dynamic-posts"></div> para postagens dinâmicas.

2. `sobre.html`:
   - Contexto da criação após o ofício da Associação de Moradores;
   - Missão institucional de democratização do conhecimento;
   - Cards com a foto/avatar e atribuições dos 5 integrantes da célula.

3. Redija na íntegra 3 artigos educativos (300 a 600 palavras cada, com subtítulos, caixas de alerta e fontes oficiais ao final):
   - `post-phishing.html`: O que é phishing, como identificar links maliciosos e o que fazer se cair no golpe. Fontes: CERT.br, Banco Central e SaferNet.
   - `post-whatsapp.html`: Como criminosos clonam contas de WhatsApp, o golpe do código SMS, o SIM swap e dicas de proteção. Fontes: CERT.br e WhatsApp FAQ.
   - `post-senhas.html`: Por que senhas fracas são perigosas, a técnica da frase-senha e recomendação de gerenciadores gratuitos. Fontes: CERT.br e Have I Been Pwned.
```

---

### 📅 Semana 3 — Desenvolver, Aprimorar e Testar com Usuários
**Objetivo:** Concluir as 3 postagens restantes (incluindo o formato prático), a página de criação de posts, o canal de contato e o relatório de testes.

```markdown
Atue como especialista em UX/UI, acessibilidade e desenvolvedor web.
Elabore os seguintes arquivos:

1. Os 3 artigos finais (300 a 600 palavras cada):
   - `post-2fa.html` (FORMATO PRÁTICO): Guia passo a passo ilustrado com números para ativar confirmação em duas etapas no WhatsApp, Google e Instagram, além de alerta sobre SMS vs App e checklist final com caixas de verificação.
   - `post-wifi.html`: Riscos de redes públicas abertas, diferença de HTTP vs HTTPS com analogia do cadeado e alternativas seguras.
   - `post-lgpd.html`: Explicação clara da LGPD para cidadãos e pequenos comerciantes, cuidados com o CPF e o papel da ANPD.

2. As páginas interativas:
   - `criar-postagem.html`: Formulário funcional para publicação de novos artigos pela comunidade, com barra de formatação (negrito, links, subtítulos, dicas) e pré-visualização ao vivo.
   - `contato.html`: Canal para envio de dúvidas e sugestões, contendo validação e aviso sobre privacidade e não coleta de dados.

3. `RELATORIO_DE_TESTES.md`:
   - Registro de testes de usabilidade realizados com 3 pessoas da comunidade de Acopiara: Dona Maria das Graças (68 anos - aposentada), Seu Francisco Souza (46 anos - comerciante) e Lucas Gabriel (16 anos - estudante).
   - Relação de feedbacks colhidos e melhorias implementadas no CSS/HTML (aumento de contraste, ajuste de fontes e foco por teclado).
```

---

### 📅 Semana 4 — Revisão Ética, Diário de Bordo, Reflexões e Apresentação
**Objetivo:** Finalizar a documentação avaliativa, a transparência no uso da IA e o roteiro de defesa oral perante a banca.

```markdown
Atue como coordenador pedagógico e redator de relatórios acadêmicos.
Produza os documentos finais de entrega do projeto:

1. `transparencia.html`: Página do blog explicando a postura ética no uso de IA, compromisso de dupla checagem em fontes oficiais e tabela transparente com ferramentas, prompts, aproveitamentos e descartes.

2. `diario-de-bordo.html`: Versão para impressão/PDF do Diário de Bordo Oficial de IA com registro cronológico das semanas 1 a 4, alertas de erros gerados por IA e corrigidos pelos alunos, e campos para assinatura da equipe.

3. `REFLEXOES_FINAIS.md`:
   - Respostas individuais obrigatórias (Item 10 da rubrica) para cada um dos 5 alunos (Ana Silva, Bruno Santos, Carla Oliveira, Daniel Costa e Elena Souza).
   - Cada aluno deve responder de 10 a 15 linhas para cada uma das 4 perguntas:
     1. Maior aprendizado técnico e pessoal;
     2. Momentos em que a IA ajudou e momentos em que errou ou precisou de correção;
     3. Como o conhecimento de informática pode proteger a comunidade;
     4. O que fariam diferente se tivessem mais tempo.

4. `ROTEIRO_APRESENTACAO.md`:
   - Estrutura de apresentação de 10 a 15 minutos slide a slide;
   - Divisão de falas entre os 5 alunos;
   - Guia de preparação para responder às principais perguntas da banca de professores.
```

---

## 💡 Dicas de Sucesso para a Execução

1. **Evite Alucinações de Links:** Ao solicitar geração de artigos por IA, exija que ela indique apenas domínios reais de órgãos consolidados (`cert.br`, `gov.br`, `antt.gov.br`, `safernet.org.br`, `bcb.gov.br`).
2. **Priorize a Linguagem Humana:** A IA tende a soar corporativa e formal demais. Instrua o modelo a utilizar o tom de *"estudante do interior cearense conversando de forma acolhedora com sua avó ou com o vizinho da mercearia"*.
3. **Auditoria de Acessibilidade:** Sempre peça para validar o contraste de cores das tags e botões para garantir leitura agradável a pessoas da terceira idade.
