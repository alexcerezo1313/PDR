import streamlit as st

st.set_page_config(page_title="Guia Creació i Creixement d'Empresa", layout="wide")

PAGES = [
    "Introducció",
    "Requeriments Legals",
    "Idea i Mercat",
    "Capital i Finançament",
    "Estructura i Organització",
    "Escalabilitat",
    "Resum"
]

# Inicialitzar estat
def init_state():
    defaults = {
        'page': 0,
        'forma': "",
        'idea_summary': "",
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

# Navegació
def next_page():
    if st.session_state.page < len(PAGES) - 1:
        st.session_state.page += 1

selection = st.sidebar.radio("Passos:", PAGES, index=st.session_state.page)
st.session_state.page = PAGES.index(selection)

# Introducció
if selection == "Introducció":
    st.title("Dona-li forma a la teva emprenedoria")
    st.markdown(
        """
Un emprenedor és una persona amb la il·lusió de crear valor amb un projecte propi. Les emprenedories neixen sovint de la detecció d’una necessitat social.

Es pot formalitzar com a autònom o societat, amb un o diversos socis, i és clau compartir la visió per garantir la continuïtat.
"""
    )
    if st.button("Continuar"):
        next_page()

# Requeriments Legals
elif selection == "Requeriments Legals":
    st.header("Requeriments Legals")
    st.markdown(
        """
**Formes jurídiques:**
- Autònom: responsabilitat il·limitada; alta al RETA.
- SL: capital mínim 3.000€; responsabilitat limitada.
- SA: capital mínim 60.000€; accions transmissibles.
- Cooperativa: gestió democràtica; enfocament social.

**Permisos i llicències:**
- Registre Mercantil: inscripció oficial.
- SS i AEAT: alta i cotitzacions.
- IAE: activitat econòmica.
- CNAE: codi estadístic.
- IVA/IS: obligacions fiscals.
"""
    )
    st.info("S’aconsella contractar una gestoría amb assessoria fiscal, laboral i legal.")
    content = "[Contingut PDF Requeriments Legals]"
    st.download_button("Descarrega Requeriments Legals (PDF)", content, file_name="requeriments_legals.pdf", mime="application/pdf")
    oferta = ["Autònom","SL","SA","Cooperativa"]
    st.session_state.forma = st.selectbox("Forma jurídica:", oferta, index=oferta.index(st.session_state.forma) if st.session_state.forma in oferta else 0)
    if st.button("Continuar"):
        next_page()

# Idea i Mercat
elif selection == "Idea i Mercat":
    st.header("Idea i Mercat")
    st.session_state.idea_summary = st.text_input("Resum de la teva idea (ex: floristeria):", value=st.session_state.idea_summary)
    st.session_state.detailed_idea = st.text_area("Descripció detallada de la teva idea i diferenciació:", value=st.session_state.detailed_idea, height=200)
    st.session_state.num_competidors = st.number_input("Competidors (0-5):", min_value=0, max_value=5, value=st.session_state.num_competidors)
    comps, f, b = [], [], []
    for i in range(st.session_state.num_competidors):
        comps.append(st.text_input(f"Nom competidor {i+1}", key=f"nom{i}"))
        f.append(st.text_area(f"Punts forts competidor {i+1}", key=f"forca{i}"))
        b.append(st.text_area(f"Punts febles competidor {i+1}", key=f"feblesa{i}"))
    st.session_state.competidors = comps
    st.session_state.forca = f
    st.session_state.feblesa = b
    opts = ["Saturat","Normal","En auge","No creat"]
    st.session_state.market = st.selectbox("Estat del mercat:", opts, index=opts.index(st.session_state.market) if st.session_state.market in opts else 0)
    desc = {
        "Saturat":"Alta competència, demanda estabilitzada.",
        "Normal":"Equilibri oferta-demanda.",
        "En auge":"Pocs competidors, demanda creixent.",
        "No creat":"Idea innovadora sense competidors directes."
    }
    st.write(desc[st.session_state.market])
    if st.button("Continuar"):
        next_page()

# Capital i Finançament
elif selection == "Capital i Finançament":
    st.header("Capital i Finançament")
    st.markdown("**Punt mort:** vendes que fan benefici=0.")
    st.session_state.punt_mort = st.number_input("Punt mort (€):", value=st.session_state.punt_mort)
    have = st.radio("Tens aquest import disponible?", ["Sí","No"])
    if have == "No":
        st.markdown("**Fonts finançament:** préstecs, subvencions, angels, crowdfunding.")
        st.download_button("Descarrega Guia Finançament (PDF)", "[PDF]", file_name="guia_financament.pdf", mime="application/pdf")
    else:
        choice = st.radio("Fons propis o parcials?", ["Tot propi","Només part"])
        if choice == "Tot propi":
            st.markdown("**50/30/20**: inversions/fons maniobra/reserves.")
        else:
            pct = st.slider("% propis:",0,100,50)
            st.markdown(f"Cal obtenir {100-pct}% extern.")
            st.markdown("**Fonts finançament:** préstecs, subvencions, crowdfunding.")
            st.download_button("Descarrega Guia Finançament (PDF)", "[PDF]", file_name="guia_financament.pdf", mime="application/pdf")
    if st.button("Continuar"):
        next_page()

# Estructura i Organització
elif selection == "Estructura i Organització":
    st.header("Estructura i Organització de l’Empresa")
    st.image("organigrama.jpg", use_container_width=True)
    st.markdown("Una mateixa persona pot exercir diversos rols.")
    st.session_state.dir_admin = st.text_input("Director administratiu:")
    st.session_state.dir_fin = st.text_input("Director financer:")
    st.session_state.dir_qual = st.text_input("Director qualitat:")
    st.session_state.gest_personal = st.text_input("Gestió de personal:")
    st.session_state.dir_prod = st.text_input("Director producció:")
    st.session_state.resp_magatzem = st.text_input("Responsable magatzem:")
    # Plantilla nòmina PDF
    st.download_button("Descarrega Plantilla Nòmina (PDF)", "[PDF plantilla nòmina]", file_name="plantilla_nomina.pdf", mime="application/pdf")
    if st.button("Continuar"):
        next_page()

# Escalabilitat
elif selection == "Escalabilitat":
    st.header("Escalabilitat")
    st.warning("Cal crear primer; no totes les empreses són escalables.")
    st.markdown(
        """
1. Software per processos.
2. Estandarditzar tasques.
3. Delegar responsabilitats.
4. Formació contínua.
5. Structures planes.
6. KPI (temps resposta).
7. Vendre canal digital i físic.
8. Externalitzar funcions.
9. Aliances estratègiques.
10. Planificar segons demanda.
"""
    )
    st.download_button("Descarrega Consells Escalabilitat (PDF)", "[PDF consells]", file_name="consells_escalabilitat.pdf", mime="application/pdf")
    if st.button("Continuar"):
        next_page()

# Resum
elif selection == "Resum":
    st.header("Resum")
    lines = []
    lines.append(f"Forma jurídica: {st.session_state.forma}")
    lines.append("Idea resumida:"); lines.append(st.session_state.idea_summary)
    lines.append("Idea detallada:"); lines.extend(st.session_state.detailed_idea.split("\n"))
    if st.session_state.competidors:
        lines.append("Competidors:")
        for i,c in enumerate(st.session_state.competidors): lines.append(f"  {i+1}. {c}")
    lines.append(f"Estat mercat: {st.session_state.market}")
    lines.append(f"Punt mort: {st.session_state.punt_mort} €")
    have = st.session_state.have_punt_mort
    if have == "Sí":
        lines.append("Assignació 50/30/20" if st.session_state.all_self == "Tot propi" else f"% propis: {st.session_state.part_percent}%.")
    else:
        lines.append("Fonts externes necessàries.")
    lines.append("Rols assignats:")
    for title,person in [
        ("Director administratiu", st.session_state.dir_admin),
        ("Director financer", st.session_state.dir_fin),
        ("Director qualitat", st.session_state.dir_qual),
        ("Gestió personal", st.session_state.gest_personal),
        ("Director producció", st.session_state.dir_prod),
        ("Responsable magatzem", st.session_state.resp_magatzem)
    ]:
        lines.append(f"  {title}: {person}")
    resumo = "\n".join(lines)
    st.download_button("Descarrega Informe Final (PDF)", resumo, file_name="informe_emprenedoria.pdf", mime="application/pdf")
