import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#5f6368"))
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "CyberSeguro — Diário de Bordo de IA | Acopiara-CE")
            self.setStrokeColor(colors.HexColor("#dadce0"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
        # Footer
        footer_text = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(558, 36, footer_text)
        self.drawString(54, 36, "Projeto Avaliativo Prático 01 — Ensino Médio Técnico em Informática")
        self.setStrokeColor(colors.HexColor("#dadce0"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)
        self.restoreState()

def build_pdf():
    pdf_path = r"C:\Users\mayko\.gemini\antigravity\scratch\blog-seguranca-digital\Diario_de_Bordo_IA.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    primary = colors.HexColor("#1a73e8")
    dark = colors.HexColor("#202124")
    gray = colors.HexColor("#5f6368")
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=primary,
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=gray,
        spaceAfter=18
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=primary,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=dark,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=dark,
        spaceAfter=6
    )

    body_bold = ParagraphStyle(
        'Body_Bold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    prompt_style = ParagraphStyle(
        'Prompt_Style',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=4
    )

    story = []

    # Title & Header
    story.append(Paragraph("Diário de Bordo de Inteligência Artificial", title_style))
    story.append(Paragraph("<b>Projeto:</b> Blog CyberSeguro — Segurança Digital para a Comunidade de Acopiara<br/><b>Curso:</b> Ensino Médio Técnico em Informática | 2º Ano | Duração: 4 semanas<br/><b>Equipe:</b> Ana Silva (Coord.), Bruno Santos (Pesquisa), Carla Oliveira (Redação), Daniel Costa (UX/Design), Elena Souza (Técnica)", subtitle_style))
    
    # 1. Introdução e Diretrizes Éticas
    story.append(Paragraph("1. Introdução e Compromisso Ético com a IA", h1_style))
    story.append(Paragraph(
        "Este documento registra formalmente a utilização de ferramentas de Inteligência Artificial (ChatGPT e Google Gemini) ao longo das 4 semanas de execução do projeto. Cumprindo as diretrizes pedagógicas, a IA foi adotada estritamente como <i>ferramenta de apoio</i> (brainstorming, síntese preliminar, revisão linguística e depuração de código), mantendo a autoria, a checagem crítica e a responsabilidade editorial integralmente sob a equipe de estudantes.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Regra de Ouro da Equipe:</b> Nenhuma informação técnica foi publicada sem validação em pelo menos duas fontes oficiais (CERT.br, ANPD, Cartilha de Segurança para Internet, Banco Central ou SaferNet Brasil). Todo texto sugerido pela IA foi integralmente reescrito para adequação ao vocabulário acessível da comunidade de Acopiara.",
        body_style
    ))

    # 2. Tabela Resumo de Registro de Prompts e Ciclos de Validação
    story.append(Paragraph("2. Registro Cronológico de Ciclos de Prompts, Validação e Ajustes", h1_style))
    
    records = [
        ("Semana 1 - Planejamento", "ChatGPT-4o",
         "Sugira 10 nomes de projetos e blogs voltados a segurança da informação para comunidades do interior do Ceará, com tom acolhedor e protetor.",
         "O nome 'CyberSeguro' e o conceito de 'Escudo Digital da Comunidade'.",
         "Foram descartados nomes excessivamente corporativos ou em inglês sofisticado (ex: 'CyberDefense Hub', 'SecOps Acopiara') que afastariam o público leigo."),
         
        ("Semana 1 - Público-Alvo", "Google Gemini",
         "Quais são os principais desafios de segurança digital enfrentados por pequenos comerciantes que vendem no WhatsApp e por idosos que utilizam apps de benefícios?",
         "Mapeamento de dores: golpe do Pix falso, clonagem de número comercial e medo de clicar em notificações bancárias.",
         "Gemini sugeriu medidas de segurança muito corporativas (como firewall de borda e autenticação biométrica em hardware); descartamos e focamos em PIN de 2 fatores e comprovante bancário real."),

        ("Semana 2 - Post Phishing", "ChatGPT-4o",
         "Explique o que é phishing em linguagem leiga para pessoas de 60 anos, usando uma metáfora do cotidiano que não envolva jargão de TI.",
         "A analogia da pescaria (anzol com isca apetitosa) e a comparação com cartas falsas deixadas na porta de casa.",
         "A IA inventou uma estatística sem fonte ('85% dos brasileiros já caíram'). O dado foi descartado e substituído pelas estatísticas oficiais do CERT.br e Cetic.br."),

        ("Semana 2 - Post WhatsApp", "Google Gemini",
         "Monte um rascunho de artigo explicando a clonagem de WhatsApp e a diferença entre clonagem de chip (SIM swap) e roubo de código de 6 dígitos.",
         "A estrutura lógica do artigo dividindo o golpe em engenharia social versus fraude de chip telefônico.",
         "O Gemini citou passos de configuração desatualizados das telas do WhatsApp Android. Corrigimos testando diretamente no aplicativo atualizado."),

        ("Semana 3 - Guia 2FA", "ChatGPT-4o",
         "Crie um checklist de 8 passos simples para uma pessoa comum conferir se suas redes e aplicativos estão protegidos com 2FA.",
         "A estrutura de checklist prático com itens claros para WhatsApp, Gmail e Instagram.",
         "A IA recomendou SMS como 'muito seguro'; corrigimos inserindo alerta sobre o golpe de troca de chip (SIM swap) e indicando Google Authenticator."),

        ("Semana 3 - Código e Acessibilidade", "Google Gemini",
         "Revise este código CSS para garantir conformidade com WCAG 2.1 AA em taxa de contraste de cores e navegação por teclado.",
         "Ajuste da cor de contraste nos botões primários e implementação do skip-link (#main) e focus-visible.",
         "A IA sugeriu usar bibliotecas pesadas de acessibilidade via CDN; descartamos em prol de HTML semântico nativo e CSS leve sem dependências."),

        ("Semana 4 - Revisão e LGPD", "ChatGPT-4o",
         "Explique a LGPD em tópicos para que um dono de mercadinho de bairro em Acopiara saiba o que pode e não pode fazer com o CPF dos clientes.",
         "Exemplos práticos: não exigir CPF para compras comuns em dinheiro e guardar cadernos de fiado longe do balcão.",
         "O texto inicial afirmava que a LGPD aplica multas milionárias a mercadinhos imediatamente; corrigimos esclarecendo a atuação educativa e as regras para microempresas segundo a ANPD.")
    ]

    table_data = [[
        Paragraph("<b>Etapa / IA</b>", body_bold),
        Paragraph("<b>Comando (Prompt) Principal</b>", body_bold),
        Paragraph("<b>Aproveitado</b>", body_bold),
        Paragraph("<b>Corrigido / Descartado</b>", body_bold)
    ]]

    for etapa, ia, prompt, aprov, descart in records:
        table_data.append([
            Paragraph(f"<b>{etapa}</b><br/><font color='#1a73e8'>{ia}</font>", body_style),
            Paragraph(f"<i>\"{prompt}\"</i>", prompt_style),
            Paragraph(aprov, body_style),
            Paragraph(descart, body_style)
        ])

    col_widths = [90, 150, 130, 134]
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f3f4")),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#dadce0")),
    ]))
    story.append(t)
    story.append(Spacer(1, 14))

    # 3. Fontes de Validação Cruzada
    story.append(Paragraph("3. Metodologia de Checagem e Fontes Confiáveis", h1_style))
    story.append(Paragraph(
        "Para combater 'alucinações' ou imprecisões das IAs generativas, cada fato, dica técnica ou número foi submetido ao critério de dupla verificação utilizando fontes institucionais de alta credibilidade:",
        body_style
    ))
    
    sources = [
        ("CERT.br (Centro de Estudos, Resposta e Tratamento de Incidentes de Segurança no Brasil)", "Validação de tipologia de golpes, estatísticas de incidentes e recomendações da Cartilha de Segurança para Internet."),
        ("ANPD (Autoridade Nacional de Proteção de Dados)", "Checagem de termos da Lei Geral de Proteção de Dados (Lei 13.709/2018), direitos dos titulares e guias orientativos para microempresas."),
        ("Banco Central do Brasil (Bacen)", "Regulamentação do Mecanismo Especial de Devolução (MED) do Pix e orientações oficiais sobre fraudes financeiras bancárias."),
        ("SaferNet Brasil", "Canais de acolhimento e estatísticas de crimes cibernéticos no país."),
        ("Documentações Oficiais de Desenvolvedores", "Central de Ajuda oficial do WhatsApp (Meta) e Central de Segurança do Google para os tutoriais de 2FA.")
    ]

    for title, desc in sources:
        story.append(Paragraph(f"• <b>{title}:</b> {desc}", body_style))

    story.append(Spacer(1, 10))

    # 4. Conclusão da Equipe sobre o Uso de IA
    story.append(Paragraph("4. Conclusão da Equipe sobre o Uso de IA", h1_style))
    story.append(Paragraph(
        "O projeto demonstrou que a inteligência artificial acelera o desenvolvimento de layouts e a estruturação de conteúdo, mas exige vigilância crítica constante. Sem a intervenção humana dos estudantes para adaptar a linguagem e checar fontes, o material conteria dados desatualizados e terminologias inadequadas para a realidade de Acopiara. A tecnologia serviu ao aprendizado, e não como substituta da capacidade analítica da célula.",
        body_style
    ))
    
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Assinaturas da Célula de Trabalho:</b>", body_bold))
    story.append(Spacer(1, 10))
    story.append(Paragraph("________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ________________________<br/>Ana Silva (Coordenadora) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Bruno Santos (Pesquisador) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Carla Oliveira (Redatora)", body_style))
    story.append(Spacer(1, 14))
    story.append(Paragraph("________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ________________________<br/>Daniel Costa (Designer/UX) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Elena Souza (Responsável Técnica)", body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("Diario_de_Bordo_IA.pdf successfully built!")

if __name__ == '__main__':
    build_pdf()
