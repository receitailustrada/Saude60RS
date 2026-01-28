import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA (TÍTULO E ÍCONE) ---
st.set_page_config(
    page_title="Saúde 60+ RS",
    page_icon="🏥",
    layout="centered"
)

# --- ESTILO VISUAL (SIMULANDO GOV.BR/CLEAN) ---
# O Streamlit já é "clean" por natureza. Vamos apenas organizar.

# Cabeçalho com as cores do RS/Gov
st.markdown("""
    <div style='background-color: #FFFFFF; padding: 10px; border-bottom: 4px solid #db2b30; border-radius: 5px; margin-bottom: 20px;'>
        <h1 style='color: #007934; margin:0;'>Saúde 60+ <span style='color:#db2b30'>RS</span></h1>
        <p style='color: #666; margin:0;'>Regulação e Estratificação de Risco (IVCF-20)</p>
    </div>
""", unsafe_allow_html=True)

# --- MENU LATERAL (A ESTRATÉGIA PARA OS 50 PROTOCOLOS) ---
protocolo = st.sidebar.selectbox(
    "Selecione o Protocolo:",
    ["Cardiologia", "Neurologia (Em breve)", "Geriatria (Em breve)"]
)

st.sidebar.markdown("---")
st.sidebar.info("Desenvolvido para suporte à decisão clínica na APS/RS.")

# --- LÓGICA DO PROTOCOLO: CARDIOLOGIA ---
if protocolo == "Cardiologia":
    st.subheader("💙 Protocolo de Valvopatias")
    st.write("Insira os dados do Ecocardiograma:")

    # Entradas de dados (Inputs Web)
    col1, col2 = st.columns(2)
    with col1:
        fe = st.number_input("Fração de Ejeção (FE %)", min_value=0, max_value=100, value=65)
    with col2:
        gradiente = st.number_input("Gradiente Médio (mmHg)", min_value=0, value=20)
    
    sintomatico = st.checkbox("Paciente apresenta sintomas? (Dispneia, Síncope, Angina)")

    # Botão de Ação
    if st.button("ANALISAR CASO", type="primary"):
        # --- O CÉREBRO MÉDICO (IGUAL AO ANTERIOR) ---
        # Protocolo Cruz Alta 2025 / Estado 2022
        
        decisao = "MANTER NA APS"
        tipo_alerta = "success" # Verde
        detalhe = "Paciente não atinge critérios de gravidade para regulação imediata."

        # Regra 1: Estenose Aórtica (Grave)
        if gradiente >= 40:
            decisao = "ENCAMINHAR: ESTENOSE AÓRTICA GRAVE"
            tipo_alerta = "error" # Vermelho
            detalhe = f"Gradiente Médio {gradiente} mmHg (Critério: ≥ 40 mmHg)."
        
        # Regra 2: Insuficiência Mitral (FE Baixa)
        elif fe <= 60:
            decisao = "ENCAMINHAR: INSUFICIÊNCIA MITRAL"
            tipo_alerta = "warning" # Laranja
            detalhe = f"Fração de Ejeção {fe}% (Critério: ≤ 60% indica disfunção)."

        # Regra 3: Baixo Fluxo / Baixo Gradiente
        elif gradiente < 40 and sintomatico:
            decisao = "DISCUTIR CASO / INVESTIGAR"
            tipo_alerta = "warning" # Laranja
            detalhe = "Suspeita de 'Low-flow Low-gradient'. Necessário Eco de Estresse ou Tomografia."

        # --- EXIBIÇÃO DO RESULTADO ---
        if tipo_alerta == "error":
            st.error(f"### {decisao}")
        elif tipo_alerta == "warning":
            st.warning(f"### {decisao}")
        else:
            st.success(f"### {decisao}")
            
        st.markdown(f"**Justificativa Técnica:** {detalhe}")
        
        # Área de Copiar e Colar
        texto_copiar = f"PACIENTE COM ESTRATIFICAÇÃO DE RISCO REALIZADA.\nPARECER: {decisao}\nJUSTIFICATIVA: {detalhe}\nFONTE: Protocolo Saúde 60+ RS."
        st.text_area("Copie para o GERCON:", texto_copiar, height=100)
