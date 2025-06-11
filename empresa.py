# Basat en el document de referència PDR.pdf
# Fitxer: empresa.py

import streamlit as st

st.set_page_config(
    page_title="Guia Creació i Creixement d'Empresa",
    layout="wide"
)

PAGES = [
    "Introducció",
    "Requeriments Legals",
    "Capital i Finançament",
    "Idea i Mercat",
    "Personal",
    "Escalabilitat",
    "Altres Aspectes Clau"
]

# Inicialitzar estat
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
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
init_state()

def next_page():
    if st.session_state.page < len(PAGES) - 1:
        st.session_state.page += 1

st.sidebar.title("Navegació")
selection = st.sidebar.radio("Passos:", PAGES, index=st.session_state.page)
st.session_state.page = PAGES.index(selection)
st.sidebar.write(f"Pàgina {st.session_state.page+1} de {len(PAGES)}")

# -------- Pàgina 1 --------
def pagina_introduccio():
    st.title("Crea la teva empresa des d'aquí")
    st.markdown(
        "Una empresa és una organització o entitat econòmica que, dotada de personalitat jurídica, "
        "realitza activitats productives o comercials amb l'objectiu de generar valor, riquesa i ocupació. "
        "Opera en un entorn de mercat per satisfer necessitats dels consumidors, assumint riscos i responsabilitats legals."
    )
    st.markdown(
        "Les empreses poden ser de propietat individual o col·lectiva, públiques o privades, "
        "i s'organitzen segons diferents formes jurídiques que defineixen la seva estructura, fiscalitat i responsabilitat."
    )
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 2 --------
def pagina_requeriments_legals():
    st.header("1. Requeriments Legals")
    st.markdown(
        "**Formes jurídiques:**\n"
        "- **Societat Limitada (SL):** capital mínim 3.000€, responsabilitat limitada als aportacions. Ideal per pimes.\n"
        "- **Societat Anònima (SA):** capital mínim 60.000€, accions transferibles. Recomanada per grans projectes.\n"
        "- **Autònom:** alta fàcil a la Seguretat Social, responsabilitat il·limitada, menys formalitats."
    )
    st.markdown(
        "**Permisos i llicències:**\n"
        "- **Llicència d'obertura:** autorització municipal per establiments.\n"
        "- **Permisos sanitaris:** obligatori per activitats alimentàries i sanitàries.\n"
        "- **Autorització mediambiental:** per activitats amb emissions o gestió de residus."
    )
    st.markdown(
        "**Protecció de dades i propietat intel·lectual:** RGPD, LOPDGDD, registre de marques i patents al OEPM."
    )
    detall_doc = """
REQUERIMENTS LEGALS - GUIA COMPLETA

1. FORMES JURÍDIQUES:
   • SL: capital mínim 3.000€, escriptura, registre mercantil.
   • SA: capital mínim 60.000€, accions transmissibles.
   • Autònom: alta RETA, sense capital.

2. PERMISOS I LLICÈNCIES:
   • Obertura: ajuntament.
   • Sanitaris: Depart. Salut.
   • Medi ambient: Depart. Medi Ambient.

3. RGPD I PROPIETAT INTEL·LECTUAL:
   • RGPD i LOPDGDD: polítiques, drets ARCO.
   • Marques i patents: OEPM.
"""
    st.download_button(
        "Descarrega Requeriments Legals (PDF)", detall_doc,
        file_name="requeriments_legals.pdf", mime="application/pdf"
    )
    forma = st.selectbox("Forma jurídica:", ["SL","SA","Autònom"],
                         index=["SL","SA","Autònom"].index(st.session_state.forma) if st.session_state.forma else 0)
    st.session_state.forma = forma
    st.write(f"Has seleccionat: **{forma}**")
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 3 --------
def pagina_capital():
    st.header("2. Capital i Finançament")
    st.markdown("Introdueix el capital obtingut (de moment) i l'objectiu de capital:")
    # Entrades de capital
    st.session_state.capital = st.number_input(
        "Capital obtingut (de moment) (€):", min_value=0.0,
        value=st.session_state.capital, step=100.0
    )
    st.session_state.target_capital = st.number_input(
        "Capital objectiu (€):", min_value=0.0,
        value=st.session_state.target_capital, step=100.0
    )
    # Recomanacions d'ús dels fons
    if st.session_state.capital > 0:
        st.write("### Recomanacions d’assignació de fons:")
        capital = st.session_state.capital
        st.write(f"- Inversions fixes (50%): {capital * 0.5:.2f} €")
        st.write(f"- Fons de maniobra (30%): {capital * 0.3:.2f} €")
        st.write(f"- Reserves i imprevistos (20%): {capital * 0.2:.2f} €")
    # Fonts de finançament
    st.markdown(
        "**Fonts de finançament:**
"
        "• Capital propi: estalvis i reinversió.
"
        "• Capital aliè: préstecs bancaris, business angels, venture capital.
"
        "• Subvencions i ajuts: programes públics i europeus.
"
        "• Crowdfunding: campanyes col·lectives."
    )
    # Guia de finançament per descarregar
    guia_fin = """
GUIA FINANÇAMENT - PAS A PAS
1. Preparar un pla de negoci sòlid.
2. Recopilar documentació financera.  
3. Contactar amb entitats bancàries i inversors.  
4. Sol·licitar subvencions i ajuts públics.  
5. Llançar campanya de crowdfunding.  
"""
    st.download_button(
        "Descarrega Guia Finançament (PDF)", guia_fin,
        file_name="guia_financament.pdf", mime="application/pdf"
    )
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 4 --------
def pagina_idea_mercat():
    st.header("3. Idea i Mercat")
    st.markdown("Descriu la teva idea de negoci:")
    st.session_state.idea = st.text_input("Quina és la teva idea?", value=st.session_state.idea)
    st.markdown("Selecciona competidors clau:")
    comps = st.multiselect("Competidors:", ["A","B","C"], default=st.session_state.competidors)
    noms = []
    for i, c in enumerate(comps): noms.append(st.text_input(f"Competidor {i+1}", value=c, key=f"c{i}"))
    st.session_state.competidors = noms
    st.markdown(
        "Guia idea: 1) Problema, 2) Solució, 3) Valor diferencial."
    )
    st.session_state.market = st.selectbox("Estat del mercat:", ["Saturat","Normal","En auge"], index=["Saturat","Normal","En auge"].index(st.session_state.market) if st.session_state.market else 1)
    if st.session_state.market == "Saturat": st.write("Mercat saturat: molta competència i demanda estabilitzada.")
    if st.session_state.market == "Normal": st.write("Mercat normal: equilibri oferta-demanda.")
    if st.session_state.market == "En auge": st.write("Mercat en auge: pocs competidors i demanda creixent.")
    if st.button("Continuar"): next_page()

# -------- Pàgina 5 --------
def pagina_personal():
    st.header("4. Personal")
    # Imatge de l'organigrama
    st.image("organigrama.jpg", caption="Organigrama d'empresa", use_column_width=True)
    # Funcions del directori
    st.markdown("""
**Funcions principals de l'organigrama:**

- **CEO:** Defineix la visió i estratègia global; representació legal.
- **CTO:** Coordina l'equip tècnic i la innovació tecnològica.
- **CFO:** Gestiona finances, pressupostos i informes econòmics.
- **COO:** Supervisa operacions, logística i qualitat.
""")
    # Perfils necessaris
    perfs = st.multiselect(
        "Perfils necessaris:",
        ["Desenvolupador", "Comercial", "Administratiu", "Operacions"],
        default=st.session_state.perfils
    )
    st.session_state.perfils = perfs
    # Descripció detalla dels perfils
    st.markdown("""
**Perfils detallats i responsabilitats:**

- **Desenvolupador:** Disseny arquitectònic, codificació, manteniment de software.
- **Comercial:** Estratègia de vendes, captació i fidelització de clients.
- **Administratiu:** Gestió administrativa, control de facturació i tràmits legals.
- **Operacions:** Coordinació de producció, magatzem i enviaments.
""")
    # Document PDF de nòmines
    nomina = """
GESTIÓ DE NÒMINES I COTITZACIONS

1. SALARI BRUT VS NET:
   - Salari brut: total remuneració abans de retencions.
   - Salari net: import després de retencions d'IRPF.

2. RETENCIONS IRPF:
   - Percentatge segons salari i situació personal.

3. COTITZACIONS SEGURETAT SOCIAL:
   - Empresa: aproximadament 30% del salari brut.
   - Treballador: aproximadament 6.35% del salari brut.

4. TIPUS DE CONTRACTES:
   - Indefinit, temporal, formació.

5. TRÀMITS A LA TGSS:
   - Enviament mensual de la declaració nominal (TC2).
   - Declaracions trimestrals i anuals.
"""
    st.download_button(
        "Descarrega Gestió de Nòmines (PDF)",
        nomina,
        file_name="nomines.pdf",
        mime="application/pdf"
    )
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 6 --------
def pagina_escalabilitat():
    st.header("5. Escalabilitat")
    st.markdown(
        "**Consells per escalar mantenint eficiència:**\n"
        "1. Documenta i estandarditza processos.\n"
        "2. Implanta ERP i CRM per automatitzar.\n"
        "3. Assigna responsabilitats clares a equips.\n"
        "4. Forma contínuament al personal.\n"
        "5. Mantén estructures planes i flexibles.\n"
        "6. Utilitza KPI per a presa de decisions.\n"
        "7. Diversifica canals de venda.\n"
        "8. Externalitza tasques no estratègiques.\n"
        "9. Cerques aliances i col·laboracions.\n"
        "10. Planifica recursos segons pics de demanda."
    )
    if st.button("Continuar"): next_page()

# -------- Pàgina 7 --------
def pagina_altres_aspectes():
    st.header("6. Resum Final")
    if st.button("Mostrar Resum"):
        st.write(f"**Forma jurídica:** {st.session_state.forma}")
        st.write(f"**Capital obtingut:** {st.session_state.capital} € (objectiu {st.session_state.target_capital} €)")
        st.write(f"**Idea:** {st.session_state.idea}")
        st.write(f"**Competidors:** {', '.join(st.session_state.competidors)}")
        st.write(f"**Estat mercat:** {st.session_state.market}")
        st.write(f"**Perfils:** {', '.join(st.session_state.perfils)}")
        # Consells mercat
        if st.session_state.market == "Saturat": st.write("Consell: innovació i diferenciació.")
        if st.session_state.market == "Normal": st.write("Consell: consolida quotes i optimitza.")
        if st.session_state.market == "En auge": st.write("Consell: aprofita creixement i expedició ràpida.")
        st.markdown(
            "**Resum i consells generals:**\n"
            "1. Clarifica valor diferencial.\n"
            "2. Estableix objectius clars.\n"
            "3. Escull estructura jurídica òptima.\n"
            "4. Diversifica finançament.\n"
            "5. Valida amb estudi de mercat.\n"
            "6. Forma equip equilibrat.\n"
            "7. Automatitza i externalitza.\n"
            "8. Mantén focus en qualitat.\n"
            "9. Mesura i ajusta KPI.\n"
            "10. Fomenta innovació contínua."
        )

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
