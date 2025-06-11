import streamlit as st

st.set_page_config(
    page_title="Guia Creació i Creixement d'Empresa",
    layout="wide"
)

PAGES = [
    "Introducció",
    "Requeriments Legals",
    "Idea i Mercat",
    "Capital i Finançament",
    "Estructura i Organització",
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
        'dir_admin': "",
        'dir_fin': "",
        'dir_qual': "",
        'gest_personal': "",
        'dir_prod': "",
        'resp_magatzem': ""
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val
init_state()

# Navegació

def next_page():
    if st.session_state.page < len(PAGES) - 1:
        st.session_state.page += 1

selection = st.sidebar.radio(
    "Passos:", PAGES, index=st.session_state.page
)
st.session_state.page = PAGES.index(selection)

# -------- Pàgina 1: Introducció --------
if selection == "Introducció":
    st.title("Dona-li forma a la teva emprenedoria")
    st.markdown(
        "Un emprenedor és una persona que té la il·lusió de crear quelcom que tingui valor mitjançant un projecte propi. "
        "Normalment, les emprenedories surten de la detecció d’una necessitat a la nostra societat i l’intenció de satisfer aquesta necessitat."
    )
    st.markdown(
        "Aquesta emprenedoria la pots formalitzar com a professional autònom o creant una empresa. Aquesta empresa també pot comptar amb més socis. "
        "És molt important l’elecció dels socis per coincidir en la visió comuna del projecte i garantir la continuïtat de l’empresa."
    )
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 2: Requeriments Legals --------
elif selection == "Requeriments Legals":
    st.header("Requeriments Legals")
    st.markdown(
        "**Formes jurídiques:**\n"
        "- Autònom: responsabilitat il·limitada; alta al RETA.\n"
        "- Societat Limitada (SL): capital mínim 3.000€; responsabilitat limitada.\n"
        "- Societat Anònima (SA): capital mínim 60.000€; accions transmissibles.\n"
        "- Societat Cooperativa: gestió democràtica; enfocament social."
    )
    st.markdown(
        "**Permisos i llicències:**\n"
        "- Registre Mercantil: inscripció obligatòria per a societats.\n"
        "- Administracions (Seguretat Social, Agència Tributària): alta i cotitzacions.\n"
        "- IAE (Impost sobre Activitats Econòmiques): declaració d'activitat.\n"
        "- CNAE (Classificació Nacional d’Activitats Econòmiques): codi d'activitat.\n"
        "- IVA i Impost de Societats: obligacions tributàries segons facturació."
    )
    st.info("S’aconsella contractar una gestoría per portar aquests tràmits amb assessoria fiscal, laboral i legal.")
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 3: Idea i Mercat --------
elif selection == "Idea i Mercat":
    st.header("Idea i Mercat")
    st.session_state.detailed_idea = st.text_area(
        "Explica detalladament la teva idea de negoci i diferenciació:",
        value=st.session_state.detailed_idea,
        height=200
    )
    st.session_state.num_competidors = st.number_input(
        "Nombre de competidors (0-5):", min_value=0, max_value=5,
        value=st.session_state.num_competidors
    )
    comps, f, b = [], [], []
    for i in range(st.session_state.num_competidors):
        comps.append(st.text_input(f"Nom competidor {i+1}", key=f"nom{i}"))
        f.append(st.text_area(f"Punts forts competidor {i+1}", key=f"forca{i}"))
        b.append(st.text_area(f"Punts febles competidor {i+1}", key=f"feblesa{i}"))
    st.session_state.competidors = comps
    st.session_state.forca = f
    st.session_state.feblesa = b
    options = ["Saturat", "Normal", "En auge", "No creat"]
    st.session_state.market = st.selectbox(
        "Estat del mercat:", options,
        index=options.index(st.session_state.market) if st.session_state.market in options else 0
    )
    descriptions = {
        "Saturat": "Mercat saturat: alta competència i demanda estabilitzada.",
        "Normal": "Mercat normal: equilibri entre oferta i demanda.",
        "En auge": "Mercat en auge: pocs competidors i demanda creixent.",
        "No creat": "Mercat no creat: idea innovadora sense competidors directes."
    }
    st.write(descriptions[st.session_state.market])
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 4: Capital i Finançament --------
elif selection == "Capital i Finançament":
    st.header("Capital i Finançament")
    st.markdown(
        "**Punt mort:** volum de vendes necessari perquè el benefici sigui zero. Correspon a les despeses fixes anuals (lloguer, sou, quotes...)."
    )
    st.session_state.punt_mort = st.number_input(
        "Punt mort (euros):", min_value=0.0,
        value=st.session_state.punt_mort, step=100.0
    )
    have = st.radio("Tens aquest import disponible?", ["Sí", "No"])
    st.session_state.have_punt_mort = have
    if have == "No":
        st.markdown("**Fonts de finançament:** préstecs, subvencions, business angels, crowdfunding.")
        st.download_button(
            "Descarrega Guia Finançament (PDF)",
            "[Contingut PDF guia financament]",
            file_name="guia_financament.pdf",
            mime="application/pdf"
        )
    else:
        choice = st.radio("Els fons són teus o només part?", ["Tot propi", "Només part"])
        st.session_state.all_self = choice
        if choice == "Tot propi":
            st.markdown("**Recomanació 50/30/20:** 50% inversions, 30% fons maniobra, 20% reserves.")
        else:
            st.session_state.part_percent = st.slider(
                "Percentatge propi (%)", 0, 100, 50
            )
            st.markdown(f"Cal obtenir {100 - st.session_state.part_percent}% de finançament extern.")
            st.markdown("**Fonts de finançament:** préstecs, subvencions, business angels, crowdfunding.")
            st.download_button(
                "Descarrega Guia Finançament (PDF)",
                "[Contingut PDF guia financament]",
                file_name="guia_financament.pdf",
                mime="application/pdf"
            )
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 5: Estructura i Organització --------
elif selection == "Estructura i Organització":
    st.header("Estructura i Organització de l’Empresa")
    st.image("organigrama.jpg", use_container_width=True)
    st.markdown("Una mateixa persona pot tenir més d'un rol.")
    st.session_state.dir_admin = st.text_input("Director administratiu:")
    st.session_state.dir_fin = st.text_input("Director financer:")
    st.session_state.dir_qual = st.text_input("Director de qualitat:")
    st.session_state.gest_personal = st.text_input("Gestió de personal:")
    st.session_state.dir_prod = st.text_input("Director de producció:")
    st.session_state.resp_magatzem = st.text_input("Responsable de magatzem:")
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 6: Escalabilitat --------
elif selection == "Escalabilitat":
    st.header("Escalabilitat")
    st.warning("Cal crear primer; no totes les empreses són escalables.")
    st.markdown(
        "1. Utilitzar software per controlar processos.\n"
        "2. Estandarditzar processos crítics.\n"
        "3. Delegar responsabilitats.\n"
        "4. Formació contínua.\n"
        "5. Estructures planes (evitar massa gerents).\n"
        "6. Establir KPI per mesurar eficiència (temps mitjà gestió avaries, servei).\n"
        "7. Vendre a través de canals digitals i físics.\n"
        "8. Externalitzar funcions no centrals (ex. producció de pa).\n"
        "9. Aliances amb empreses complementàries amb clients comuns.\n"
        "10. Planificar recursos segons pics de demanda."
    )
    if st.button("Continuar"):
        next_page()

# -------- Pàgina 7: Altres Aspectes Clau --------
elif selection == "Altres Aspectes Clau":
    st.header("Altres Aspectes Clau")
    # Generació de resum i descàrrega
    lines = []
    lines.append(f"Forma jurídica: {st.session_state.forma}")
    lines.append("Idea detallada:")
    lines.extend(st.session_state.detailed_idea.split("\n"))
    if st.session_state.competidors:
        lines.append("Competidors:")
        for i, c in enumerate(st.session_state.competidors):
            lines.append(f"  {i+1}. {c}")
    lines.append(f"Estat mercat: {st.session_state.market}")
    lines.append(f"Punt mort: {st.session_state.punt_mort} €")
    have = st.session_state.have_punt_mort
    if have == "Sí":
        if st.session_state.all_self == "Tot propi":
            lines.append("Assignació 50/30/20 aplicada.")
        else:
            lines.append(f"% propis: {st.session_state.part_percent}%. Resta extern.")
    else:
        lines.append("Fonts externes necessàries.")
    lines.append("Rols assignats:")
    roles = [
        ("Director administratiu", st.session_state.dir_admin),
        ("Director financer", st.session_state.dir_fin),
        ("Director de qualitat", st.session_state.dir_qual),
        ("Gestió personal", st.session_state.gest_personal),
        ("Director producció", st.session_state.dir_prod),
        ("Responsable magatzem", st.session_state.resp_magatzem)
    ]
    for title, person in roles:
        lines.append(f"  {title}: {person}")
    resumo = "\n".join(lines)
    st.download_button(
        "Descarrega Informe (TXT)", resumo,
        file_name="informe_emprenedoria.txt",
        mime="text/plain"
    )
