# Basat en el document de referència PDR.pdf
# Fitxer: empresa.py

import streamlit as st

st.set_page_config(
    page_title="Guia Creació i Creixement d'Empresa",
    layout="wide"
)

# Llista de títols de cada pàgina
PAGES = [
    "Introducció", 
    "Requeriments Legals", 
    "Capital i Finançament", 
    "Idea i Mercat", 
    "Personal",
    "Escalabilitat",
    "Altres Aspectes Clau"
]

# Inicialitzar pàgina en session_state
if 'page' not in st.session_state:
    st.session_state.page = 0

# Funció per navegar entre pàgines
def next_page():
    if st.session_state.page < len(PAGES) - 1:
        st.session_state.page += 1

# Sidebar de navegació
st.sidebar.title("Navegació")
selection = st.sidebar.radio(
    "Passos:",
    PAGES,
    index=st.session_state.page
)
st.sidebar.write(f"Pàgina {st.session_state.page+1} de {len(PAGES)}")

# Funcions de cada pas
def pagina_introduccio():
    st.title("Benvinguts a la Guia Interactiva")
    st.markdown(
        "Aquesta aplicació us acompanyarà pas a pas en el procés de crear i fer créixer la vostra empresa.")
    if st.button("Continuar"):
        next_page()


def pagina_requeriments_legals():
    st.header("1. Requeriments Legals")
    st.markdown(
        "Escolliu la forma jurídica i definiu la documentació requerida:")
    forma = st.selectbox(
        "Forma jurídica:",
        ["Societat Limitada (SL)", "Societat Anònima (SA)", "Autònom"]
    )
    if forma:
        st.write(f"Has seleccionat: **{forma}**")
    st.markdown(
        "**Permisos i llicències:** llicència d'obertura, permisos sanitaris, medi ambient, etc.")
    st.markdown(
        "**Protecció de dades i propietat intel·lectual:** polítiques de privacitat, registre de marques i patents.")
    if st.button("Continuar"):
        next_page()


def pagina_capital():
    st.header("2. Capital i Finançament")
    st.markdown(
        "Entreu els imports obtinguts i veureu recomanacions d'ús:")
    capital = st.number_input(
        "Capital obtingut (€):", min_value=0.0, value=0.0, step=100.0
    )
    if capital > 0:
        st.write("### Recomanació d'assignació de fons")
        st.write(f"- **Inversions fixes** (50%): {capital * 0.5:.2f} €")
        st.write(f"- **Fons de maniobra** (30%): {capital * 0.3:.2f} €")
        st.write(f"- **Reserves i imprevistos** (20%): {capital * 0.2:.2f} €")
    if st.button("Continuar"):
        next_page()


def pagina_idea_mercat():
    st.header("3. Idea i Mercat")
    st.markdown(
        "Desenvolupeu la vostra idea i valideu-la amb el mercat:")
    feedback = st.text_area(
        "Quin feedback heu rebut de clients o mentors?"
    )
    competidors = st.multiselect(
        "Identifiqueu competidors clau:",
        ["Competidor A", "Competidor B", "Competidor C"]
    )
    if st.button("Continuar"):
        next_page()


def pagina_personal():
    st.header("4. Personal")
    st.markdown(
        "Definiu perfils de treball i estratègies de retenció:")
    perfils = st.multiselect(
        "Perfils necessaris:",
        ["Desenvolupador", "Comercial", "Administratiu", "Operacions"]
    )
    st.markdown(
        "Prepareu un pla de formació i incentius per al vostre equip.")
    if st.button("Continuar"):
        next_page()


def pagina_escalabilitat():
    st.header("5. Escalabilitat")
    st.markdown(
        "Planifiqueu la delegació i l'ús de tecnologia per créixer:")
    delegacions = st.number_input(
        "Nombre de delegacions previstes:", min_value=1, value=1, step=1
    )
    if st.button("Continuar"):
        next_page()


def pagina_altres_aspectes():
    st.header("6. Altres Aspectes Clau")
    st.markdown(
        "Feu un pressupost amb escenaris pessimist, realista i optimista:")
    pessimist = st.number_input(
        "Escenari pessimist (€):", min_value=0.0, value=0.0, step=100.0
    )
    realista = st.number_input(
        "Escenari realista (€):", min_value=0.0, value=0.0, step=100.0
    )
    optimista = st.number_input(
        "Escenari optimista (€):", min_value=0.0, value=0.0, step=100.0
    )
    if pessimist or realista or optimista:
        st.write("### Resum pressupost")
        st.write(f"- Pessimista: {pessimist:.2f} €")
        st.write(f"- Realista: {realista:.2f} €")
        st.write(f"- Optimista: {optimista:.2f} €")
    st.markdown("**Networking**: contacte amb associacions i esdeveniments sectorials.")

# Mapejar nom a funció i mostrar
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
