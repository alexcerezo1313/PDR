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
    index=st.session_state.page
)
# Actualitzar pàgina en funció de la selecció
st.session_state.page = PAGES.index(selection)
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
    st.markdown("- **Societat Limitada (SL):** responsabilitat limitada al capital aportat, capital mínim 3.000€. Ideal per pimes.")
    st.markdown("- **Societat Anònima (SA):** capital mínim 60.000€, accions transferibles. Recomanada per grans inversions.")
    st.markdown("- **Autònom:** responsabilitat il·limitada, gestió simplificada. Apte per professionals independents.")
    st.markdown("**Permisos i llicències**: autoritzacions administratives per operar segons activitat i ubicació. Alguns exemples:")
    st.markdown("- **Llicència d'obertura:** permís municipal per establiments.")
    st.markdown("- **Permisos sanitaris:** obligatoris per manipulació d'aliments o activitats sanitàries.")
    st.markdown("- **Autorització mediambiental:** per activitats amb impacte ambiental, regulada per la Generalitat.")
    st.markdown("**Protecció de dades i propietat intel·lectual**: cal complir el RGPD i registrar marques/patents al OEPM.")
    # Document detallat descarregable
    detall_doc = """
DOCUMENT DE REFERÈNCIA: REQUERIMENTS LEGALS

1. FORMES JURÍDIQUES

Societat Limitada (SL)
- Capital mínim: 3.000€.
- Responsabilitat: limitada al capital.
- Constitució: escriptura pública i registre mercantil.

Societat Anònima (SA)
- Capital mínim: 60.000€.
- Responsabilitat: limitada.
- Accions: lliurement transmissibles.

Autònom
- Responsabilitat: il·limitada.
- Simplificació: menor burocràcia.

2. PERMISOS I LLICÈNCIES

Llicència d'obertura
- Emesa per l’ajuntament.
- Tipus segons activitat.

Permisos sanitaris
- Obligatori per activitats alimentàries.
- Expedients al Departament de Salut.

Autorització mediambiental
- Per a activitats amb emissions o residus.
- Tràmits al Departament de Medi Ambient.

3. PROTECCIÓ DE DADES

- RGPD i LOPDGDD.
- Obligacions: registre de tractaments, polítiques de privacitat.
- Drets: accés, rectificació, supressió.

4. PROPIETAT INTEL·LECTUAL

- Registre de marques al OEPM.
- Patents d’invencions.
- Models d’utilitat i dissenys industrials.
"""
    st.download_button(
        "Descarrega Requeriments Legals detallats (PDF)",
        detall_doc,
        file_name="requeriments_legals.pdf",
        mime="application/pdf"
    )
    forma = st.selectbox(
        "Forma jurídica:",
        ["Societat Limitada (SL)", "Societat Anònima (SA)", "Autònom"],
        index=["Societat Limitada (SL)","Societat Anònima (SA)","Autònom"].index(st.session_state.forma) if st.session_state.forma else 0
    )
    st.session_state.forma = forma
    st.write(f"Has seleccionat: **{st.session_state.forma}**")
    if st.button("Continuar"):
        next_page()

# Pàgina 3: Capital i Finançament
def pagina_capital():
    st.header("2. Capital i Finançament")
    st.markdown("Introdueix el capital obtingut (es recordarà en tot el procés):")
    capital = st.number_input(
        "Capital obtingut (€):", min_value=0.0, value=st.session_state.capital, step=100.0
    )
    st.session_state.capital = capital
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
    idea = st.text_input("Quina és la teva idea?", value=st.session_state.idea)
    st.session_state.idea = idea
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
        "Estat del mercat:", ["Saturat", "Normal", "En auge"], index=["Saturat","Normal","En auge"].index(st.session_state.market) if st.session_state.market else 1
    )
    st.session_state.market = market
    if st.button("Continuar"):
        next_page()

# Pàgina 5: Personal
def pagina_personal():
    st.header("4. Personal")
    st.markdown("**Organigrama típic d'una empresa:**\nCEO\n├─ CTO\n├─ CFO\n└─ COO")
    perfils = st.multiselect(
        "Perfils necessaris:",
        ["Desenvolupador", "Comercial", "Administratiu", "Operacions"]
    )
    st.session_state.perfils = perfils
    st.markdown("**Perfils detallats:**\n- Desenvolupador: disseny i manteniment del producte.\n- Comercial: vendes i relacions amb clients.\n- Administratiu: gestió financera i documental.\n- Operacions: logística i producció.")
        st.markdown("""**Gestió de nòmines i cotitzacions:**
Les nòmines inclouen salari brut i retencions d'IRPF.
L'empresa cotitza a la Seguretat Social (~30% del salari brut).""")
