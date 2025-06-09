import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Guía Creación y Crecimiento de Empresa",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Carga de PDF de referencia (PDR.pdf) ---
@st.cache_data
def load_pdf(path):
    with open(path, "rb") as f:
        return f.read()

pdf_bytes = load_pdf("PDR.pdf")

# --- Textos centralizados extraídos de PDR.pdf y ampliados ---
TEXTS = {
    "intro": (
        "Crear una empresa es un proceso que abarca desde la idea hasta el crecimiento. "
        "Incluye aspectos legales, financieros, estratégicos, de mercado y de gestión de recursos humanos."
    ),
    "req_summary": (
        "- Formas jurídicas (SL: capital mín. 3.000€; SA: capital mín. 60.000€; Autónomo: sin capital mín.)\n"
        "- Permisos y licencias (apertura, sanitarios, ambientales)\n"
        "- Protección de datos (RGPD, LOPDGDD) y registro de marca/patentes (OEPM)\n"
        "- Obligaciones contables y fiscales"
    ),
    "req_detail": (
        "1. FORMAS JURÍDICAS:\n"
        "   • Sociedad Limitada (SL): responsabilidad limitada, capital mín. 3.000€.\n"
        "   • Sociedad Anónima (SA): acciones transferibles, capital mín. 60.000€.\n"
        "   • Autónomo: alta en RETA, responsabilidad personal.\n\n"
        "2. PERMISOS Y LICENCIAS:\n"
        "   • Licencia de apertura: trámite municipal.\n"
        "   • Permisos sanitarios: manipulación de alimentos.\n"
        "   • Autorización medioambiental: actividades con impacto.\n\n"
        "3. PROTECCIÓN DE DATOS Y PROPIEDAD INTELECTUAL:\n"
        "   • Políticas internas y derechos ARCO (RGPD, LOPDGDD).\n"
        "   • Registro de marca y patentes en OEPM."
    ),
    "fin_summary": (
        "- Fuentes propias: ahorro, reservas.\n"
        "- Fuentes ajenas: préstamos bancarios, business angels, venture capital.\n"
        "- Subvenciones públicas y crowdfunding."
    ),
    "idea_summary": (
        "1. Definir problema y solución.\n"
        "2. Realizar brainstorming y estudios de caso.\n"
        "3. Validar con feedback (clientes, expertos).\n"
        "4. Analizar competidores para diferenciarse."
    ),
    "personal_summary": (
        "- Reclutamiento: definir perfil y publicar ofertas.\n"
        "- Formación: cursos, mentoring y "sombra" de expertos.\n"
        "- Retención: salario competitivo, incentivos, ambiente.\n"
        "- Protocolos: manejo de conflictos y emergencias."
    ),
    "escal_summary": (
        "1. Estandarizar procesos y automatizar (ERP/CRM).\n"
        "2. Delegar con organigrama claro.\n"
        "3. KPI para medir y ajustar.\n"
        "4. Uso de tecnología y comunicación centralizada."
    ),
    "otros_summary": (
        "- Elaborar presupuestos (escenarios optimista, realista, pesimista).\n"
        "- Análisis de riesgos y planes de contingencia.\n"
        "- Seguros adecuados y networking empresarial."
    ),
    "practica": (
        "La parte práctica implica: \n"
        "• Crear tu plan de negocio en plantilla editable.\n"
        "• Calendarizar pasos y responsables.\n"
        "• Realizar checklists de trámites.\n"
        "• Herramientas recomendadas: Trello, Notion, Google Sheets."
    ),
    "conclusiones": (
        "1. Definir tu propuesta de valor y validar mercado.\n"
        "2. Elegir forma jurídica y asegurar permisos.\n"
        "3. Plan financiero sólido y diversificar financiación.\n"
        "4. Formar un equipo motivado y KPI claros.\n"
        "5. Emplear tecnología para escalar eficientemente."
    ),
    "referencias": (
        "- Álex Cerezo Porta, \"L'empresa: Creació i desenvolupament\" (PDR.pdf)\n"
        "- Agencia Tributaria (AEAT)\n"
        "- OEPM: Registro de Marcas y Patentes\n"
        "- RGPD y LOPDGDD (BOE)"
    )
}

# Lista de páginas
def init_state():
    defaults = { 'page': 0, 'forma': None, 'capital': 0.0, 'target': 0.0,
                 'idea': '', 'competidores': [], 'market': None, 'perfils': [] }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
init_state()

PAGES = [
    "Introducción",
    "Requerimientos Legales",
    "Capital y Financiación",
    "Idea y Mercado",
    "Personal",
    "Escalabilidad",
    "Otros Aspectos Clave",
    "Parte Práctica",
    "Conclusiones",
    "Referencias"
]

# Navegación lateral
def next_page():
    if st.session_state.page < len(PAGES) - 1:
        st.session_state.page += 1

# Sidebar
st.sidebar.title("Contenido")
# Barra de progreso
total = len(PAGES)
current = st.session_state.page + 1
st.sidebar.progress(current / total)
selection = st.sidebar.radio("Secciones:", PAGES, index=st.session_state.page)
st.session_state.page = PAGES.index(selection)
# Descarga PDR completo
st.sidebar.download_button("Descargar PDR completo", pdf_bytes,
                           file_name="PDR.pdf", mime="application/pdf")

# Botón de navegación común
def nav_button(label="Continuar"):
    if st.button(label):
        next_page()

# --- Definición de páginas ---

def page_introduccion():
    st.title("Crea tu empresa paso a paso")
    st.markdown(TEXTS["intro"])
    nav_button()


def page_requerimientos():
    st.header("1. Requerimientos Legales")
    with st.expander("Ver detalle completo"):
        st.code(TEXTS["req_detail"])
    st.markdown("**Resumen rápido:**")
    st.markdown(TEXTS["req_summary"])
    nav_button()


def page_capital():
    st.header("2. Capital y Financiación")
    col1, col2 = st.columns([2,1])
    with col1:
        st.write("Introduzca los datos de capital:")
        cap = st.number_input("Capital actual (€)", value=st.session_state.capital, step=100.0)
        tgt = st.number_input("Objetivo de capital (€)", value=st.session_state.target, step=100.0)
        st.session_state.capital, st.session_state.target = cap, tgt
    with col2:
        if cap > 0:
            st.metric("Inversiones fijas (50%)", f"{cap*0.5:.2f} €")
            st.metric("Fondo maniobra (30%)", f"{cap*0.3:.2f} €")
            st.metric("Reservas (20%)", f"{cap*0.2:.2f} €")
        else:
            st.info("Introduce capital > 0 para ver recomendaciones")
    st.markdown("**Fuentes de financiación:**")
    st.markdown(TEXTS["fin_summary"])
    nav_button()


def page_idea_mercado():
    st.header("3. Idea y Mercado")
    st.text_input("Describe tu idea de negocio:", value=st.session_state.idea, key="idea")
    compet = st.multiselect("Competidores clave:", ["Competidor A","B","C"], key="competidores")
    st.session_state.competidores = compet
    st.markdown(TEXTS["idea_summary"])
    market = st.selectbox("Estado del mercado:", ["Saturado","Normal","En auge"], key="market")
    colors = {"Saturado":"🔴","Normal":"🟠","En auge":"🟢"}
    st.write(f"{colors[market]} {market}")
    nav_button()


def page_personal():
    st.header("4. Personal")
    st.image("organigrama.png", caption="Organigrama típico", use_column_width=True)
    perfils = st.multiselect("Perfiles necesarios:", ["Desarrollador","Comercial","Administrativo","Operaciones"], key="perfils")
    st.session_state.perfils = perfils
    st.markdown(TEXTS["personal_summary"])
    nav_button()


def page_escalabilidad():
    st.header("5. Escalabilidad")
    with st.expander("Ver consejos clave"):
        st.markdown(TEXTS["escal_summary"])
    nav_button()


def page_otros():
    st.header("6. Otros Aspectos Clave")
    st.markdown(TEXTS["otros_summary"])
    nav_button()


def page_practica():
    st.header("7. Parte Práctica")
    st.markdown(TEXTS["practica"])
    nav_button()


def page_conclusiones():
    st.header("8. Conclusiones")
    st.markdown(TEXTS["conclusiones"])
    nav_button()


def page_referencias():
    st.header("9. Referencias")
    st.markdown(TEXTS["referencias"])
    # Enlace al PDF original
    st.download_button("Ver PDR original", pdf_bytes,
                       file_name="PDR.pdf", mime="application/pdf")

# Mapeo de funciones
func_map = {
    "Introducción": page_introduccion,
    "Requerimientos Legales": page_requerimientos,
    "Capital y Financiación": page_capital,
    "Idea y Mercado": page_idea_mercado,
    "Personal": page_personal,
    "Escalabilidad": page_escalabilidad,
    "Otros Aspectos Clave": page_otros,
    "Parte Práctica": page_practica,
    "Conclusiones": page_conclusiones,
    "Referencias": page_referencias
}

# Ejecución de la página seleccionada
func_map[selection]()
