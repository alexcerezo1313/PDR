# Basat en el document de referència PDR.pdf
# Fitxer: empresa.py

import streamlit as st

st.set_page_config(
    page_title="Guia Creació i Creixement d'Empresa",
    layout="wide"
)

# Llista de passos de l'aplicació
PAGES = [
    "Introducció",
    "Requeriments Legals",
    "Capital i Finançament",
    "Idea i Mercat",
    "Personal",
    "Escalabilitat",
    "Altres Aspectes Clau"
]

# Inicialitzar l'estat de la sessió
def init_state():
    defaults = {
        'page': 0,
        'forma': "",
        'capital': 0.0,
        'target_capital': 0.0,
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

# Navegació entre pàgines
def next_page():
    if st.session_state.page < len(PAGES) - 1:
        st.session_state.page += 1

st.sidebar.title("Navegació")
selection = st.sidebar.radio("Passos:", PAGES, index=st.session_state.page)
st.session_state.page = PAGES.index(selection)
st.sidebar.write(f"Pàgina {st.session_state.page+1} de {len(PAGES)}")

# -------- Pàgina 1: Introducció --------
def pagina_introduccio():
    st.title("Crea la teva empresa des d'aquí")
    st.markdown(
        "**Què és una empresa?** "
        "L'empresa és una organització amb personalitat jurídica que pretén generar riquesa i ocupació "
        "mitjançant la producció de béns o serveis per satisfer les necessitats de la societat."  
        "Una unitat econòmica i social amb responsabilitat legal pròpia."
    )
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 2: Requeriments Legals --------
def pagina_requeriments_legals():
    st.header("1. Requeriments Legals")
    st.markdown(
        "**Formes jurídiques:** defineixen la responsabilitat, capital mínim i estructura fiscal.\n"
        "- **Societat Limitada (SL):** capital mínim 3.000€, responsabilitat limitada.\n"
        "- **Societat Anònima (SA):** capital mínim 60.000€, accions transferibles.\n"
        "- **Autònom:** responsabilitat il·limitada, menys tràmits burocràtics."
    )
    st.markdown(
        "**Permisos i llicències:** requisits per operar segons activitat i ubicació.\n"
        "- **Llicència d'obertura:** autorització municipal per establiments.\n"
        "- **Permisos sanitaris:** obligatoris per manipulació d'aliments.\n"
        "- **Autorització mediambiental:** per activitats amb impacte al medi ambient."
    )
    st.markdown(
        "**Protecció de dades i propietat intel·lectual:** cal complir RGPD, LOPDGDD i registrar marques/patents al OEPM."
    )
    # Document detallat en PDF (substituir després pel PDF propi)
    detall_doc = """
REQUERIMENTS LEGALS - GUIA DETALLADA

1. FORMES JURÍDIQUES:
   • SL: capital mínim 3.000€, escriptura pública i registre mercantil.
   • SA: capital mínim 60.000€, accions lliurement transmissibles.
   • Autònom: alta a l'RETA, sense capital mínim.

2. PERMISOS I LLICÈNCIES:
   • Llicència d'obertura: tramitar a l'ajuntament.
   • Permisos sanitaris: Departament de Salut.
   • Autorització mediambiental: Departament de Medi Ambient.

3. PROTECCIÓ DE DADES I PROPIETAT INTEL·LECTUAL:
   • RGPD i LOPDGDD: polítiques internes i drets ARCO.
   • Registre de marca i patents: OEPM.
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
        index=["Societat Limitada (SL)", "Societat Anònima (SA)", "Autònom"].index(st.session_state.forma) if st.session_state.forma else 0
    )
    st.session_state.forma = forma
    st.write(f"Has seleccionat: **{st.session_state.forma}**")
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 3: Capital i Finançament --------
def pagina_capital():
    st.header("2. Capital i Finançament")
    st.markdown("Introdueix el capital obtingut i l'objectiu de capital:")
    capital = st.number_input(
        "Capital obtingut (de moment) (€):", min_value=0.0, value=st.session_state.capital, step=100.0
    )
    st.session_state.capital = capital
    target = st.number_input(
        "Capital objectiu (€):", min_value=0.0, value=st.session_state.target_capital, step=100.0
    )
    st.session_state.target_capital = target
    if capital > 0:
        st.write("### Recomanació d'assignació de fons")
        st.write(f"- Inversions fixes (50%): {capital * 0.5:.2f} €")
        st.write(f"- Fons de maniobra (30%): {capital * 0.3:.2f} €")
        st.write(f"- Reserves i imprevistos (20%): {capital * 0.2:.2f} €")
    st.markdown(
        "**Fonts de finançament:**\n"
        "- Capital propi: estalvis i reinversió de beneficis.\n"
        "- Capital aliè: préstecs bancaris, business angels, venture capital.\n"
        "- Subvencions i ajuts: programes públics i europeus.\n"
        "- Crowdfunding: finançament col·lectiu en línia."
    )
    guia_fin = """
GUIA PAS A PAS: OBTENCIÓ DE FINANÇAMENT
1. Preparar un pla de negoci sòlid.
2. Contactar entitats bancàries amb documentació completa.
3. Presentar el projecte a inversors privats.
4. Sol·licitar ajuts i subvencions.
5. Llançar campanya de crowdfunding.
"""
    st.download_button(
        "Descarrega Guia Finançament (PDF)",
        guia_fin,
        file_name="guia_financament.pdf",
        mime="application/pdf"
    )
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 4: Idea i Mercat --------
def pagina_idea_mercat():
    st.header("3. Idea i Mercat")
    st.markdown("Descriu la teva idea de negoci:")
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
    st.markdown(
        "**Guia per redactar la idea:**\n1. Defineix el problema.\n2. Presenta la solució.\n3. Destaca el valor diferencial."
    )
    market = st.selectbox(
        "Estat del mercat:", ["Saturat", "Normal", "En auge"], index=["Saturat","Normal","En auge"].index(st.session_state.market) if st.session_state.market else 1
    )
    st.session_state.market = market
    # Descripció dels estats de mercat
    if market == "Saturat":
        st.write("**Mercat Saturat:** alta competència i demanda estabilitzada.")
    elif market == "Normal":
        st.write("**Mercat Normal:** equilibri entre oferta i demanda.")
    else:
        st.write("**Mercat en Auge:** pocs competidors i demanda creixent.")
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 5: Personal --------
def pagina_personal():
    st.header("4. Personal")
    # Imatge de l'organigrama
    st.image("organigrama.png", caption="Organigrama típic d'una empresa", use_column_width=True)
    st.markdown(
        "En aquest organigrama, el CEO lidera l'estratègia general, sota el qual trobem els responsables de tecnologia (CTO), finances (CFO) i operacions (COO)."
    )
    perfils = st.multiselect(
        "Perfils necessaris:",
        ["Desenvolupador", "Comercial", "Administratiu", "Operacions"]
    )
    st.session_state.perfils = perfils
    st.markdown(
        "**Perfils detallats:**\n"
        "- **Desenvolupador:** disseny i manteniment tècnic del producte.\n"
        "- **Comercial:** estratègies de vendes i gestió de clients.\n"
        "- **Administratiu:** gestió financera, comptable i administrativa.\n"
        "- **Operacions:** logística, producció i control de qualitat."
    )
    # Document nòmines i cotitzacions
    nomina_doc = """
GESTIÓ DE NÒMINES I COTITZACIONS

1. SALARI BRUT I NET
   - Salari brut: suma de percepcions abans de retencions.\n   - Salari net: import a cobrar després de retencions d'IRPF.\n
2. RETENCIONS IRPF
   - Percentatge depèn del salari i situació personal.\n
3. COTITZACIONS SEGURETAT SOCIAL
   - Empresa: ~30% sobre salari brut.\n   - Treballador: ~6.35% sobre salari brut.\n
4. TRÀMITS
   - Comunicació mensual de nòmines a la TGSS.\n   - Declaracions trimestrals i anuals.\n"""
    st.download_button(
        "Descarrega Gestió de Nòmines (PDF)",
        nomina_doc,
        file_name="nomines.pdf",
        mime="application/pdf"
    )
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 6: Escalabilitat --------
def pagina_escalabilitat():
    st.header("5. Escalabilitat")
    st.markdown(
        "Com escalar una empresa mantenint l'eficiència:\n"
        "1. Estandarditza processos operatius.\n"
        "2. Automatitza tasques repetitives amb tecnologia (ERP, CRM).\n"
        "3. Descentralitza la presa de decisions amb equips responsables.\n"
        "4. Fomenta la cultura de formació contínua.\n"
        "5. Mantén una estructura organitzativa àgil i adaptable.\n"
        "6. Utilitza KPI per mesurar rendiment i ajustar estratègies.\n"
        "7. Diversifica canals de venda per ampliar mercat.\n"
        "8. Externalitza funcions no estratègiques.\n"
        "9. Busca aliances estratègiques i networking.\n"
        "10. Planifica escalades de recursos segons demanda."     
    )
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 7: Altres Aspectes Clau (Resum) --------
def pagina_altres_aspectes():
    st.header("6. Resum Final")
    if st.button("Mostrar Resum"):
        st.write(f"- **Forma jurídica:** {st.session_state.forma}")
        st.write(f"- **Capital obtingut:** {st.session_state.capital} € (objectiu: {st.session_state.target_capital} €)")
        st.write(f"- **Idea:** {st.session_state.idea}")
        st.write(f"- **Competidors:** {', '.join(st.session_state.competidors)}")
        st.write(f"- **Estat del mercat:** {st.session_state.market}")
        st.write(f"- **Perfils:** {', '.join(st.session_state.perfils)}")
        st.write(f"- **Delegacions previstes:** {st.session_state.delegations}")
        # Consells segons estat de mercat
        if st.session_state.market == "Saturat":
            st.write("**Consell:** mercat saturat → aposta per la innovació i diferenciació.")
        elif st.session_state.market == "Normal":
            st.write("**Consell:** mercat estable → consolida quotas i optimitza costos.")
        else:
            st.write("**Consell:** mercat en auge → aprofita el creixement i expandeix-te ràpidament.")
        # Resum detallat 10 línies
        st.markdown(
            "**Resum detallat i consells generals:**\n"
            "1. Defineix clarament la teva proposta de valor.\n"
            "2. Estableix objectius finances i d'impacte social.\n"
            "3. Selecciona l'estructura jurídica adequada per al teu volum.\n"
            "4. Gestiona el finançament amb diversitat de fonts.\n"
            "5. Valida la teva idea amb un estudi de mercat rigorós.\n"
            "6. Dissenya un equip amb perfils equilibrats i motivats.\n"
            "7. Automatitza i externalitza per escalar sense ineficiències.\n"
            "8. Mantén el focus en la qualitat del producte/servei.\n"
            "9. Mesura KPI i ajusta l'estratègia periòdicament.\n"
            "10. Fomenta una cultura d'innovació i adaptabilitat."
        )

# Mapeig de funcions i execució
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

