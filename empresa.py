# Basat en el document de referència PDR.pdf
# Fitxer: empresa.py

import streamlit as st

st.set_page_config(
    page_title="Guia Creació i Creixement d'Empresa",
    layout="wide"
)

# Definició de pàgines
PAGES = [
    "Introducció", 
    "Requeriments Legals", 
    "Capital i Finançament", 
    "Idea i Mercat", 
    "Personal", 
    "Escalabilitat", 
    "Altres Aspectes Clau"
]

# Estat inicial
def init_state():
    defaults = {
        'page': 0,
        'forma': "",
        'capital': 0.0,
        'idea': "",
        'competidors': [],
        'market': "",
        'perfils': [],
        'delegations': 1
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

init_state()

# Funció de navegació
def next_page():
    if st.session_state.page < len(PAGES) - 1:
        st.session_state.page += 1

# Sidebar interactiu
st.sidebar.title("Navegació")
selection = st.sidebar.radio(
    "Passos:",
    PAGES,
    index=st.session_state.page,
    key='page'
)
st.sidebar.write(f"Pàgina {st.session_state.page+1} de {len(PAGES)}")

# Pàgina 1: Introducció
def pagina_introduccio():
    st.title("Benvinguts a la Guia Interactiva")
    st.markdown(
        "Aquest assistent et guiarà, pas a pas, en la creació i creixement de la teva empresa.")
    if st.button("Continuar"):
        next_page()

# Pàgina 2: Requeriments Legals
def pagina_requeriments_legals():
    st.header("1. Requeriments Legals")
    st.markdown("**Què és la forma jurídica?** La forma jurídica determina la responsabilitat legal i la manera fiscal de l'empresa.")
    st.markdown("- **Societat Limitada (SL):** responsabilitat limitada al capital aportat.")
    st.markdown("- **Societat Anònima (SA):** capital social més elevat, accions transferibles.")
    st.markdown("- **Autònom:** responsabilitat il·limitada, ideal per activitats individuals.")
    st.markdown("**Permisos i llicències**: autoritzacions administratives per operar. Alguns exemples:")
    st.markdown("- **Llicència d'obertura** per establiments.")
    st.markdown("- **Permisos sanitaris** per activitats alimentàries.")
    st.markdown("- **Autorització mediambiental** per activitats amb impacte.")
    st.markdown("**Protecció de dades i propietat intel·lectual**: cal complir la normativa de privacitat i registrar marques/patents.")
    # Documents descarregables
    privacy_doc = """[NOM EMPRESA]\nPolítica de privacitat i protecció de dades.\nResponsable del tractament: [Nom].\nFinalitats: gestió administrativa, comunicacions.\nDrets: accés, rectificació, supressió.\n..."""
    ip_doc = """[NOM EMPRESA]\nAcord de cessió de drets de propietat intel·lectual.\nParties: [Nom Empresa] i [Col·laborador].\nObjecte: creacions originals, software, dissenys.\n..."""
    st.download_button("Descarrega Acord Protecció de Dades", privacy_doc, file_name="proteccio_dades.txt")
    st.download_button("Descarrega Acord Propietat Intel·lectual", ip_doc, file_name="propietat_intellectual.txt")
    forma = st.selectbox(
        "Forma jurídica:",
        ["Societat Limitada (SL)", "Societat Anònima (SA)", "Autònom"],
        key='forma'
    )
    st.write(f"Has seleccionat: **{st.session_state.forma or forma}**")
    if st.button("Continuar"):
        next_page()

# Pàgina 3: Capital i Finançament
def pagina_capital():
    st.header("2. Capital i Finançament")
    st.markdown("Introdueix el capital obtingut (es recordarà en tot el procés):")
    capital = st.number_input(
        "Capital obtingut (€):", min_value=0.0, value=st.session_state.capital, step=100.0, key='capital'
    )
    if capital > 0:
        st.write("### Recomanació d'assignació de fons")
        st.write(f"- **Inversions fixes** (50%): {capital * 0.5:.2f} €")
        st.write(f"- **Fons de maniobra** (30%): {capital * 0.3:.2f} €")
        st.write(f"- **Reserves i imprevistos** (20%): {capital * 0.2:.2f} €")
    st.markdown("**Fonts de finançament:**")
    st.markdown("- **Capital propi:** estalvis, reinversió dels beneficis.")
    st.markdown("- **Capital aliè:** préstecs bancaris, business angels, venture capital.")
    st.markdown("- **Subvencions i ajuts:** programes públics i europeus.")
    st.markdown("- **Crowdfunding:** finançament col·lectiu en línia.")
    guia_fin = """Guia pas a pas per obtenir finançament:\n1. Preparar pla de negoci.\n2. Contactar entitats bancàries.\n3. Buscar inversors privats.\n4. Sol·licitar ajuts públics.\n5. Llençar campanya de crowdfunding.\n..."""
    st.download_button("Descarrega Guia Finançament", guia_fin, file_name="guia_financament.txt")
    if st.button("Continuar"):
        next_page()

# Pàgina 4: Idea i Mercat
def pagina_idea_mercat():
    st.header("3. Idea i Mercat")
    st.markdown("Descriu la teva idea:")
    idea = st.text_input("Quina és la teva idea?", value=st.session_state.idea, key='idea')
    st.markdown("Selecciona competidors clau:")
    opcions = ["Competidor A", "Competidor B", "Competidor C"]
    competidors_raw = st.multiselect("Competidors predefinits:", opcions)
    competidors = []
    for i, comp in enumerate(competidors_raw):
        nom = st.text_input(f"Nom competidor {i+1}", value=comp, key=f"comp_{i}")
        competidors.append(nom)
    st.session_state.competidors = competidors
    st.markdown("**Guia per redactar la teva idea:**\n1. Defineix el problema.\n2. Explica la solució.\n3. Valor diferencial.")
    market = st.selectbox(
        "Estat del mercat:", ["Saturat", "Normal", "En auge"], index=["Saturat","Normal","En auge"].index(st.session_state.market) if st.session_state.market else 1, key='market'
    )
    if st.button("Continuar"):
        next_page()

# Pàgina 5: Personal
def pagina_personal():
    st.header("4. Personal")
    st.markdown("**Organigrama típic d'una empresa:**\nCEO\n├─ CTO\n├─ CFO\n└─ COO")
    perfils = st.multiselect(
        "Perfils necessaris:",
        ["Desenvolupador", "Comercial", "Administratiu", "Operacions"],
        default=st.session_state.perfils,
        key='perfils'
    )
    st.markdown("**Perfils detallats:**\n- Desenvolupador: disseny i manteniment del producte.\n- Comercial: vendes i relacions amb clients.\n- Administratiu: gestió financera i documental.\n- Operacions: logística i producció.")
    st.markdown("**Gestió de nòmines i cotitzacions:**\nLes nòmines inclouen salari brut i retencions d'IRPF.\nL'empresa cotitza a la Seguretat Social (~30% del salari brut).")
    if st.button("Continuar"):
        next_page()

# Pàgina 6: Escalabilitat
def pagina_escalabilitat():
    st.header("5. Escalabilitat")
    st.markdown("Planificar la delegació consisteix a assignar tasques a responsables o nous departaments.")
    deleg = st.number_input(
        "Nombre de punts de delegació previstos:",
        min_value=1,
        value=st.session_state.delegations,
        step=1,
        key='delegations'
    )
    st.write(f"Has planificat {deleg} punts de delegació.")
    st.markdown("L'ús de tecnologia (ERP, CRM, automatització) facilita l'expansió sense augmentar costos lineals.")
    if st.button("Continuar"):
        next_page()

# Pàgina 7: Altres Aspectes Clau (Resum)
def pagina_altres_aspectes():
    st.header("6. Resum Final")
    st.markdown("Revisa totes les dades introduïdes:")
    if st.button("Mostrar Resum"):
        st.write(f"- **Forma jurídica:** {st.session_state.forma}")
        st.write(f"- **Capital obtingut:** {st.session_state.capital} €")
        st.write(f"- **Idea:** {st.session_state.idea}")
        st.write(f"- **Competidors:** {', '.join(st.session_state.competidors)}")
        st.write(f"- **Estat del mercat:** {st.session_state.market}")
        st.write(f"- **Perfils:** {', '.join(st.session_state.perfils)}")
        st.write(f"- **Delegacions previstes:** {st.session_state.delegations}")

# Mapejar i mostrar
func_map = {
    "Introducció": pagina_introduccio,
    "Requeriments Legals": pagina_requeriments_legals,
    "Capital i Finançament": pagina_capital,
    "Idea i Mercat": pagina_idea_mercat,
    "Personal": pagina_personal,
    "Escalabilitat": pagina_escalabilitat,
    "Altres Aspectes Clau": pagina_altres_aspectes
}

func_map[selection]()

