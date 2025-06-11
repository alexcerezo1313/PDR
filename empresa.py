# Basat en el document de referència PDR.pdf
# Fitxer: empresa.py

import streamlit as st
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

st.set_page_config(
    page_title="Guia Creació i Creixement d'Empresa",
    layout="wide"
)

# Ordre dels passos
def init_pages():
    return [
        "Introducció",
        "Requeriments Legals",
        "Idea i Mercat",
        "Capital i Finançament",
        "Estructura i Organització de l’Empresa",
        "Escalabilitat",
        "Altres Aspectes Clau"
    ]
PAGES = init_pages()

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
        'dir_admin': "",
        'dir_fin': "",
        'dir_qual': "",
        'gest_personal': "",
        'dir_prod': "",
        'resp_magatzem': ""
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
init_state()

def next_page():
    if st.session_state.page < len(PAGES) - 1:
        st.session_state.page += 1

# Sidebar de navegació
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
- Autònom: responsabilitat il·limitada; alta al RETA.
- Societat Limitada (SL): capital mínim 3.000€; responsabilitat limitada.
- Societat Anònima (SA): capital mínim 60.000€; accions transmissibles.
- Societat Cooperativa: gestió democràtica; enfocament social.

**Permisos i llicències:**
- Registre Mercantil: inscripció obligatòria.
- SS i Agència Tributària: alta i cotitzacions.
- IAE: declaració d'activitat.
- CNAE: codi d'activitat econòmica.
- IVA i IS: obligacions tributàries.
""")
    st.info("S’aconsella contractar una gestoría amb assessoria fiscal, laboral i legal.")
    detall = "[Contingut PDF Requeriments Legals]"
    st.download_button("Descarrega Requeriments Legals (PDF)", detall, file_name="requeriments_legals.pdf", mime="application/pdf")
    forma = st.selectbox("Forma jurídica:", ["Autònom","SL","SA","Societat Cooperativa"], index=["Autònom","SL","SA","Societat Cooperativa"].index(st.session_state.forma) if st.session_state.forma in ["Autònom","SL","SA","Societat Cooperativa"] else 0)
    st.session_state.forma = forma
    if st.button("Continuar"):
        next_page()

# Pàgina 3: Idea i Mercat
def pagina_idea_mercat():
    st.header("2. Idea i Mercat")
    st.session_state.detailed_idea = st.text_area(
        "Explica detalladament la teva idea de negoci i diferenciació:",
        value=st.session_state.detailed_idea, height=200
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
    desc = {"Saturat":"Mercat saturat: alta competència.","Normal":"Mercat normal: equilibri.","En auge":"Mercat en auge: demanda creixent.","No creat":"Mercat no creat: sense competidors."}
    st.write(desc[st.session_state.market])
    if st.button("Continuar"):
        next_page()

# Pàgina 4: Capital i Finançament
def pagina_capital():
    st.header("3. Capital i Finançament")
    st.markdown("**Punt mort**: volum de vendes per tenir benefici zero.")
    st.session_state.punt_mort = st.number_input("Punt mort (euros):", min_value=0.0, value=st.session_state.punt_mort, step=100.0)
    have = st.radio("Tens aquest import disponible?", ["Sí","No"])
    st.session_state.have_punt_mort = have
    if have == "No":
        st.markdown("**Fonts de finançament:** préstecs, subvencions, business angels, crowdfunding.")
        guia = "[PDF Guia Finançament detallat]"
        st.download_button("Descarrega Guia Finançament (PDF)", guia, file_name="guia_financament.pdf", mime="application/pdf")
    else:
        choice = st.radio("Tots els fons són teus o només part?", ["Tot propi","Només part"])
        st.session_state.all_self = choice
        if choice == "Tot propi":
            st.markdown("**Recomanació 50/30/20**: 50% inversions,30% fons maniobra,20% reserves.")
        else:
            pct = st.slider("Percentatge propi (%)", 0, 100, 50)
            st.session_state.part_percent = pct
            st.markdown(f"Cal obtenir {100-pct}% de finançament extern.")
            st.markdown("**Fonts de finançament:** préstecs, subvencions, business angels, crowdfunding.")
            guia = "[PDF Guia Finançament detallat]"
            st.download_button("Descarrega Guia Finançament (PDF)", guia, file_name="guia_financament.pdf", mime="application/pdf")
    if st.button("Continuar"):
        next_page()

# Pàgina 5: Estructura i Organització de l’Empresa
def pagina_personal():
    st.header("4. Estructura i Organització de l’Empresa")
    st.image("organigrama.jpg", use_container_width=True)
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
    st.warning("Primer de tot s'ha de crear l'empresa; però es pot escalar tot i que no és obligatori.")
    st.warning("No totes les empreses són escalables.")
    st.markdown("""
1. Utilitzar software per controlar processos.
2. Estandarditzar processos crítics.
3. Delegar responsabilitats.
4. Formació contínua.
5. Estructures planes (evitar massa gerents).
6. Establir KPI (temps mitjà resposta, etc.).
7. Vendre per canals digitals i físics.
8. Externalitzar funcions no centrals.
9. Aliances amb empreses complementàries.
10. Planificar segons pics de demanda.
""")
    if st.button("Continuar"):
        next_page()

# Pàgina 7: Altres Aspectes Clau
def pagina_altres_aspectes():
    st.header("6. Altres Aspectes Clau")
    st.markdown("Genera un informe PDF amb tota la informació.")
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    w, h = letter
    y = h - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Informe Emprenedoria")
    y -= 30
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Forma jurídica: {st.session_state.forma}")
    y -= 20
    c.drawString(50, y, "Idea de negoci:")
    y -= 15
    for line in (st.session_state.detailed_idea or "-").split("\n"):
        if y < 50:
            c.showPage(); y = h - 50
        c.drawString(60, y, line)
        y -= 15
    if st.session_state.competidors:
        c.drawString(50, y, "Competidors:")
        y -= 15
        for i, nom in enumerate(st.session_state.competidors):
            if y < 50:
                c.showPage(); y = h - 50
            c.drawString(60, y, f"{i+1}. {nom}")
            y -= 15
            c.drawString(70, y, f"Fortaleses: {st.session_state.forca[i]}")
            y -= 15
            c.drawString(70, y, f"Febleses: {st.session_state.feblesa[i]}")
            y -= 20
    if y < 50:
        c.showPage(); y = h - 50
    c.drawString(50, y, f"Estat mercat: {st.session_state.market}")
    y -= 20
    c.drawString(50, y, f"Punt mort: {st.session_state.punt_mort} €")
    y -= 20
    have = st.session_state.have_punt_mort
    if have == "Sí":
        if st.session_state.all_self == "Tot propi":
            c.drawString(50, y, "Assignació 50/30/20 aplicable.")
        else:
            c.drawString(50, y, f"Part propi: {st.session_state.part_percent}%.")
    else:
        c.drawString(50, y, "Fonts externes necessàries.")
    y -= 30
    c.showPage()
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, h-50, "Resum i Consells Generals:")
    c.setFont("Helvetica", 12)
    y = h - 80
    for i, line in enumerate([
        "1. Clarifica valor diferencial.",
        "2. Estableix objectius clars.",
        "3. Escull estructura jurídica.",
        "4. Diversifica finançament.",
        "5. Realitza estudi de mercat.",
        "6. Forma equip equilibrat.",
        "7. Automatitza processos.",
        "8. Mantén focus en qualitat.",
        "9. Mesura KPIs.",
        "10. Fomenta innovació contínua."
    ]):
        if y < 50:
            c.showPage(); y = h - 50
        c.drawString(60, y, line)
        y -= 15
    c.save(); buffer.seek(0)
    st.download_button("Descarrega Informe (PDF)", buffer, file_name="informe_emprenedoria.pdf", mime="application/pdf")

# Execució final
func_map = {
    PAGES[0]: pagina_introduccio,
    PAGES[1]: pagina_requeriments_legals,
    PAGES[2]: pagina_idea_mercat,
    PAGES[3]: pagina_capital,
    PAGES[4]: pagina_personal,
    PAGES[5]: pagina_escalabilitat,
    PAGES[6]: pagina_altres_aspectes
}
func_map[selection]()
