# 📋 Plano de Projeto — Blog de Segurança Digital CyberSeguro
**Curso:** Ensino Médio Técnico em Informática | **Série:** 2º Ano | **Duração:** 4 semanas  
**Localidade:** Acopiara - CE | **Modalidade:** Trabalho Avaliativo em Células

---

## 1. Identificação do Projeto
* **Nome do Blog:** **CyberSeguro — Seu Escudo Digital na Comunidade**
* **Instituição de Ensino:** Escola Estadual de Educação Profissional de Acopiara
* **Entidade Parceira:** Associação de Moradores de Acopiara (atendimento ao ofício recebido)
* **Plataforma Tecnológica Escolhida:** **HTML5, CSS3 Semântico e Moderno, JavaScript Vanilla** (arquitetura estática leve, responsiva, sem dependências externas pesadas e com persistência local via LocalStorage).

---

## 2. Situação-Problema e Justificativa
Com o avanço veloz da digitalização na cidade de Acopiara, os pequenos comerciantes passaram a receber pedidos e pagamentos por WhatsApp e Instagram, os órgãos públicos e prefeitura ofertaram serviços pelo celular, e famílias e idosos passaram a movimentar benefícios sociais por aplicativos bancários.

Paralelamente a essa transformação, a Associação de Moradores registrou uma onda crescente de golpes:
* Mensagens de phishing simulando bancos oficiais e órgãos do governo;
* Links fraudulentos prometendo benefícios, sorteios ou falsas promoções locais;
* Clonagem e roubo de contas de WhatsApp de moradores e estabelecimentos comerciais;
* Vazamento de dados cadastrais e reutilização contínua de senhas fracas.

**O Desafio:** Criar um canal digital confiável, atrativo, acessível e permanente em linguagem simples, capaz de educar pessoas de todas as idades (com pouca ou muita intimidade tecnológica) sobre segurança da informação.

---

## 3. Definição do Público-Alvo
1. **Idosos e Aposentados:** Usuários de aplicativos como Caixa Tem, Meu INSS e bancos digitais. Necessitam de instruções claras sobre não clicar em links de SMS/WhatsApp e não compartilhar códigos SMS.
2. **Micro e Pequenos Comerciantes:** Donos de mercadinhos, farmácias, padarias e lojas de roupas locais que realizam vendas por WhatsApp/Instagram e utilizam maquininhas de cartão ou Pix.
3. **Famílias, Jovens e Estudantes:** Cidadãos que compartilham dispositivos domésticos, usam Wi-Fi em praças públicas e precisam conscientizar familiares sobre senhas e privacidade.

---

## 4. Divisão de Funções na Célula de Trabalho
| Integrante | Papel Principal | Atribuições Centrais |
| :--- | :--- | :--- |
| **Ana Silva** | Coordenadora de Projeto | Acompanhar o cumprimento dos prazos, gerenciar reuniões de planejamento, fazer interlocução com os professores e orientar as entregas semanais. |
| **Bruno Santos** | Pesquisador de Conteúdo | Mapear fontes oficiais (CERT.br, ANPD, Bacen, SaferNet), validar dados técnicos e impedir a disseminação de fake news ou informações desatualizadas. |
| **Carla Oliveira** | Redatora e Revisora | Redigir os artigos com linguagem inclusiva e acessível (evitando jargões desnecessários), padronizar a gramática e revisar a extensão (300 a 600 palavras). |
| **Daniel Costa** | Designer / UX | Criar a identidade visual do CyberSeguro (paleta de cores, tipografia Inter, ícones e emojis), zelar pela acessibilidade (WCAG 2.1 AA) e usabilidade responsiva no celular. |
| **Elena Souza** | Responsável Técnica | Estruturar os arquivos HTML5 semânticos, implementar o CSS responsivo, desenvolver os recursos dinâmicos em JS (armazenamento de posts e contato) e gerenciar a publicação. |

---

## 5. Matriz de Conteúdo: Os 6 Temas Selecionados
1. **Tema 1 — Golpes de Phishing e Links Falsos:** `post-phishing.html` (Conceito, como funciona a "pescaria" digital, casos reais de bancos e correios, e como identificar links perigosos).
2. **Tema 2 — Clonagem e Roubo de Contas no WhatsApp:** `post-whatsapp.html` (Engenharia social do código de 6 dígitos, SIM swap da operadora e como agir imediatamente caso a conta seja invadida).
3. **Tema 3 — Senhas Seguras e Gerenciadores:** `post-senhas.html` (Mitos sobre senhas fáceis, técnica da "frase secreta" longa e como utilizar gerenciadores gratuitos).
4. **Tema 4 (Formato Prático) — Guia Passo a Passo: Verificação em Duas Etapas:** `post-2fa.html` (Passo a passo com telas do WhatsApp, Google e Instagram, comparativo SMS vs Aplicativo e Checklist final).
5. **Tema 5 — Perigos do Wi-Fi Público:** `post-wifi.html` (Riscos em praças e restaurantes, ataque do "gêmeo malvado", diferença visual entre HTTP e HTTPS, e uso seguro de redes móveis).
6. **Tema 6 — LGPD e Direitos na Era Digital:** `post-lgpd.html` (O que a Lei Geral de Proteção de Dados garante ao cidadão comum, cuidados com o CPF no comércio e o papel da ANPD).

---

## 6. Cronograma Detalhado das 4 Semanas
```
[Semana 1: Compreender e Planejar]
├── Leitura atenta da situação-problema de Acopiara
├── Definição da identidade do blog: CyberSeguro
├── Distribuição de funções entre os 5 integrantes
└── Entrega: Plano de Projeto consolidado

[Semana 2: Pesquisar e Produzir]
├── Pesquisa aprofundada nos repositórios CERT.br e Cartilha de Segurança
├── Desenvolvimento do esqueleto HTML/CSS e guia de estilos
├── Redação e validação dos 3 primeiros artigos (Phishing, WhatsApp e Senhas)
└── Entrega: Blog no ar com estrutura básica e 3 postagens funcionais

[Semana 3: Desenvolver e Aprimorar]
├── Redação dos temas 4 (Guia 2FA prático), 5 (Wi-Fi) e 6 (LGPD)
├── Implementação da página de publicação comunitária (criar-postagem.html)
├── Aplicação dos testes de usabilidade com 3 pessoas externas da comunidade
└── Entrega: Blog completo funcional e Relatório de Testes de Usabilidade

[Semana 4: Revisar e Apresentar]
├── Revisão editorial cruzada e conferência das referências
├── Conclusão e diagramação do Diário de Bordo de IA
├── Produção dos slides e ensaio da apresentação oral (10 a 15 min)
└── Entrega: Apresentação final para banca e entrega do Diário em PDF
```
