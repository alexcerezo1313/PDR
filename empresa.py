# Basat en el document de referència PDR.pdf
# Fitxer: empresa.py

import streamlit as st

st.set_page_config(
    page_title="Guia Creació i Creixement d'Empresa",
    layout="wide"
)

# Ordre dels passos
PAGES = [
    "Introducció",
    "Requeriments Legals",
    "Idea i Mercat",
    "Capital i Finançament",
    "Estructura i Organització de l’Empresa",
    "Escalabilitat",
    "Altres Aspectes Clau"
]

# Inicialitzar estat

def init_state():
    defaults = {
        'page': 0,
        'forma': "",
        'detailed_idea': "",
        'num_competidors': 0,
        'competidors': [],
        'forca': [],
        'feblesa': [],
        'market': "",
        'punt_mort': 0.0,
        'have_punt_mort': None,
        'all_self': None,
        'part_percent': 0,
        'perfils': [],
        # Personal roles
        'dir_admin': "",
        'dir_fin': "",
        'dir_qual': "",
        'gest_personal': "",
        'dir_prod': "",
        'resp_magatzem': "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
init_state()

def next_page():
    if st.session_state.page < len(PAGES) - 1:
        st.session_state.page += 1

# Sidebar
st.sidebar.title("Navegació")
selection = st.sidebar.radio("Passos:", PAGES, index=st.session_state.page)
st.session_state.page = PAGES.index(selection)
st.sidebar.write(f"Pàgina {st.session_state.page+1} de {len(PAGES)}")

# Pàgina 1: Introducció
def pagina_introduccio():
    st.title("Dona-li forma a la teva emprenedoria")
    st.markdown("""
Un emprenedor és una persona que té la il·lusió de crear quelcom que tingui valor mitjançant un projecte propi. Normalment, les emprenedories surten de la detecció d’una necessitat a la nostra societat i l’intenció de satisfer aquesta necessitat.

Aquesta emprenedoria la pots formalitzar com a professional autònom o creant una empresa. Aquesta empresa també pot comptar amb més socis. És molt important l’elecció dels socis per coincidir en la visió comuna del projecte i garantir la continuïtat de l’empresa.

Una empresa és una organització o entitat econòmica que, dotada de personalitat jurídica, realitza activitats productives o comercials amb l'objectiu de generar valor, riquesa i ocupació. Opera en un entorn de mercat per satisfer necessitats dels consumidors, assumint riscos i responsabilitats legals.

Les empreses poden ser de propietat individual o col·lectiva, públiques o privades, i s'organitzen segons diferents formes jurídiques que defineixen la seva estructura, fiscalitat i responsabilitat.
""")
    if st.button("Continuar"):
        next_page()

# Pàgina 2: Requeriments Legals
def pagina_requeriments_legals():
    st.header("1. Requeriments Legals")
    st.markdown("""
**Formes jurídiques:**
- **Autònom:** responsabilitat il·limitada; alta al RETA; adequat per professionals independents.
- **Societat Limitada (SL):** capital mínim 3.000€; responsabilitat limitada; ideal per pimes.
- **Societat Anònima (SA):** capital mínim 60.000€; accions transmissibles.
- **Societat Cooperativa:** empresa col·lectiva amb gestió democràtica i enfocament social.

**Permisos i llicències:**
- **Registre Mercantil:** inscripció obligatòria per a societats.
- **Administracions (SS, Agència Tributària):** alta i cotitzacions.
- **IAE:** declaració de l'activitat econòmica mitjançant epígrafs.
- **CNAE:** codi estadístic de classificació de l'activitat.
- **IVA i Impost de Societats (IS):** obligacions tributàries segons forma i facturació.
""")
    st.info("S’aconsella contractar una gestoría per portar aquests tràmits, amb assessoria fiscal, laboral i legal.")
    # PDF placeholder
    detall = """[Contingut complet PDF Requeriments Legals]"""
    st.download_button("Descarrega Requeriments Legals (PDF)", detall, file_name="requeriments_legals.pdf", mime="application/pdf")
    forma = st.selectbox("Forma jurídica:", ["Autònom","SL","SA","Societat Cooperativa"], index=["Autònom","SL","SA","Societat Cooperativa"].index(st.session_state.forma) if st.session_state.forma in ["Autònom","SL","SA","Societat Cooperativa"] else 0)
    st.session_state.forma = forma
    if st.button("Continuar"):
        next_page()

# Pàgina 3: Idea i Mercat
def pagina_idea_mercat():
    st.header("2. Idea i Mercat")
    st.session_state.detailed_idea = st.text_area(
        "Explica detalladament la teva idea de negoci i com et diferencies de la competència:",
        value=st.session_state.detailed_idea,
        height=200
    )
    n = st.number_input("Nombre de competidors (0-5):", min_value=0, max_value=5, value=st.session_state.num_competidors)
    st.session_state.num_competidors = n
    noms, forca, feblesa = [], [], []
    for i in range(n):
        noms.append(st.text_input(f"Nom competidor {i+1}", key=f"nom_c{i}"))
        forca.append(st.text_area(f"Punts forts competidor {i+1}", key=f"forca_c{i}"))
        feblesa.append(st.text_area(f"Punts febles competidor {i+1}", key=f"feblesa_c{i}"))
    st.session_state.competidors = noms
    st.session_state.forca = forca
    st.session_state.feblesa = feblesa
    options = ["Saturat","Normal","En auge","No creat"]
    st.session_state.market = st.selectbox("Estat del mercat:", options, index=options.index(st.session_state.market) if st.session_state.market in options else 0)
    desc = {
        "Saturat": "Mercat saturat: alta competència, demanda estabilitzada.",
        "Normal": "Mercat normal: equilibri oferta-demanda.",
        "En auge": "Mercat en auge: poca competència i demanda creixent.",
        "No creat": "Mercat no creat: idea innovadora sense competidors directes."
    }
    st.write(desc[st.session_state.market])
    if st.button("Continuar"):
        next_page()

# Pàgina 4: Capital i Finançament
def pagina_capital():
    st.header("3. Capital i Finançament")
    st.markdown(
        "**Punt mort**: volum de vendes necessari perquè el benefici sigui zero. Correspon a les despeses fixes anuals (lloguer, sou, quotes...)."
    )
    st.session_state.punt_mort = st.number_input("Introdueix el teu punt mort (euros):", min_value=0.0, value=st.session_state.punt_mort, step=100.0)
    st.markdown("Tens aquest import disponible?")
    have = st.radio("", ["Sí","No"])
    st.session_state.have_punt_mort = have
    if have == "No":
        st.markdown("**Fonts de finançament:** préstecs, subvencions, business angels, crowdfunding...")
        guia = """[PDF Guia Finançament detallat]"""
        st.download_button("Descarrega Guia Finançament (PDF)", guia, file_name="guia_financament.pdf", mime="application/pdf")
    else:
        choice = st.radio("Tots els fons són teus o només aportaràs una part?", ["Tot propi","Només part"])
        st.session_state.all_self = choice
        if choice == "Tot propi":
            st.markdown("**Recomanació 50/30/20** per assignar fons: 50% inversions, 30% fons maniobra, 20% reserves.")
        else:
            pct = st.slider("Percentatge que aportaràs (%)", 0, 100, 50)
            st.session_state.part_percent = pct
            st.markdown(f"Has d'obtenir {100-pct}% adicional de finançament extern.")
            st.markdown("**Fonts de finançament:** préstecs, subvencions, business angels, crowdfunding...")
            guia = """[PDF Guia Finançament detallat]"""
            st.download_button("Descarrega Guia Finançament (PDF)", guia, file_name="guia_financament.pdf", mime="application/pdf")
    if st.button("Continuar"):
        next_page()

# Pàgina 5: Estructura i Organització de l’Empresa
def pagina_personal():
    st.header("4. Estructura i Organització de l’Empresa")
    st.image("organigrama.jpg", width=350)
    st.markdown("Una mateixa persona pot exercir més d'un rol.")
    st.session_state.dir_admin = st.text_input("Director administratiu:")
    st.session_state.dir_fin = st.text_input("Director financer:")
    st.session_state.dir_qual = st.text_input("Director de qualitat:")
    st.session_state.gest_personal = st.text_input("Gestió de personal:")
    st.session_state.dir_prod = st.text_input("Director de producció:")
    st.session_state.resp_magatzem = st.text_input("Responsable de magatzem:")
    if st.button("Continuar"):
        next_page()

# Pàgina 6: Escalabilitat

def pagina_escalabilitat():
    st.header("5. Escalabilitat")
    # Disclaimers
    st.warning("Primer de tot s'ha de crear l'empresa; però una vegada fet, es pot escalar tot i que no és obligatori.")
    st.warning("No totes les empreses són escalables.")
    # Consells per escalar
    st.markdown("""
**Consells per escalar mantenint eficiència:**
1. Utilitzar un software informàtic per controlar i optimitzar processos operatius.
2. Estandarditzar i documentar els processos crítics.
3. Delegar responsabilitats amb equips especialitzats.
4. Invertir en formació contínua del personal.
5. Mantenir estructures planes (evitar massa gerents de cada departament).
6. Establir índexs de mesura (per exemple, temps mitjà de resolució d'avaries o servici, i ajustar KPI segons resultats).
7. Vendre a través de canals digitals i físics per diversificar ingressos.
8. Externalitzar activitats no estratègiques (per exemple, subcontractar la producció de pa d’un restaurant).
9. Establir aliances amb empreses no competidores però amb clients comuns.
10. Planificar recursos segons pics de demanda anticipats per mantenir un servei òptim.
""")
    if st.button("Continuar"):
        next_page()

# Pàgina 7: Altres Aspectes Clau

def pagina_altres_aspectes():
    st.header("6. Altres Aspectes Clau")
    st.markdown(
        "Genera un informe complet de la teva emprenedoria amb tota la informació introduïda."
    )
    # Generació de PDF mitjançant ReportLab
    import io
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Informe Emprenedoria Personalitzat")
    y -= 30
    c.setFont("Helvetica", 12)
    # Resum de forma jurídica
    c.drawString(50, y, f"Forma jurídica: {st.session_state.forma}")
    y -= 20
    # Idea detallada
    c.drawString(50, y, "Idea de negoci:")
    y -= 15
    text = st.session_state.detailed_idea or "-"
    for line in text.split("
"):
        if y < 50:
            c.showPage(); y = height - 50
        c.drawString(60, y, line)
        y -= 15
    # Competidors
    if st.session_state.competidors:
        c.drawString(50, y, "Competidors:")
        y -= 15
        for i, nom in enumerate(st.session_state.competidors):
            if y < 50:
                c.showPage(); y = height - 50
            c.drawString(60, y, f"{i+1}. {nom}")
            y -= 15
            c.drawString(70, y, f"Fortaleses: {st.session_state.forca[i]}")
            y -= 15
            c.drawString(70, y, f"Febleses: {st.session_state.feblesa[i]}")
            y -= 20
    # Estat del mercat
    if y < 50:
        c.showPage(); y = height - 50
    c.drawString(50, y, f"Estat del mercat: {st.session_state.market}")
    y -= 20
    # Punt mort i finançament
    c.drawString(50, y, f"Punt mort: {st.session_state.punt_mort} €")
    y -= 20
    if st.session_state.have_punt_mort == "Sí":
        if st.session_state.all_self == "Tot propi":
            c.drawString(50, y, "Assignació 50/30/20: inversions/fons maniobra/reserves.")
        else:
            c.drawString(50, y, f"Percentatge propi: {st.session_state.part_percent}% propis. Resta de finançament extern.")
    else:
        c.drawString(50, y, "Fonts externes: préstecs, subvencions, business angels, crowdfunding.")
    y -= 30
    # Organització de l'empresa
    if y < 50:
        c.showPage(); y = height - 50
    c.drawString(50, y, "Organització i rols assignats:")
    y -= 15
    roles = [
        ("Director administratiu", st.session_state.dir_admin),
        ("Director financer", st.session_state.dir_fin),
        ("Director qualitat", st.session_state.dir_qual),
        ("Gestió de personal", st.session_state.gest_personal),
        ("Director producció", st.session_state.dir_prod),
        ("Responsable magatzem", st.session_state.resp_magatzem)
    ]
    for title, person in roles:
        if y < 50:
            c.showPage(); y = height - 50
        c.drawString(60, y, f"{title}: {person}")
        y -= 15
    # Consells finals
    c.showPage()
    y = height - 50
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Resum i Consells Generals:")
    y -= 25
    consells = [
        "1. Clarifica valor diferencial.",
        "2. Estableix objectius clars.",
        "3. Escull estructura jurídica adient.",
        "4. Diversifica fonts de finançament.",
        "5. Realitza un estudi de mercat.",
        "6. Forma un equip equilibrat.",
        "7. Automatitza processos.",
        "8. Mantén focus en qualitat.",
        "9. Mesura i ajusta KPIs.",
        "10. Fomenta innovació contínua."
    ]
    c.setFont("Helvetica", 12)
    for line in consells:
        if y < 50:
            c.showPage(); y = height - 50
        c.drawString(60, y, line)
        y -= 15
    c.save()
    buffer.seek(0)
    st.download_button(
        "Descarrega Informe Empresarial (PDF)",
        buffer,
        file_name="informe_emprenedoria.pdf",
        mime="application/pdf"
    )
# Execució final
func_map = {
    "Introducció": pagina_introduccio,
    "Requeriments Legals": pagina_requeriments_legals,
    "Idea i Mercat": pagina_idea_mercat,
    "Capital i Finançament": pagina_capital,
    "Estructura i Organització de l’Empresa": pagina_personal,
    "Escalabilitat": pagina_escalabilitat,
    "Altres Aspectes Clau": pagina_altres_aspectes
}
func_map[selection]()
