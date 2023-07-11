import streamlit as st
from streamlit_autorefresh import st_autorefresh
import pandas as pd
import json

st.set_page_config(layout="wide")
count = st_autorefresh(interval=20000, limit=None, key="ar")
tabs = st.sidebar.radio('Real Time Stress', ('Apresentação', 'Medidações atuais', 'Dicas para Redução de Estresse'))

if tabs == 'Apresentação':
    # Título e apresentação
    st.markdown('<h1 style="text-align: center;">Real Time Stress</h1>', unsafe_allow_html=True)
    st.markdown('## Cuidando da sua saúde mental em tempo real')

    # intro
    st.markdown('A saúde mental é um aspecto fundamental para o bem-estar e qualidade de vida. O estresse é uma das principais causas de problemas de saúde mental, e é essencial identificar e gerenciar o estresse de forma adequada.')
    st.markdown('O Real Time Stress é um aplicativo desenvolvido para auxiliar no monitoramento do nível de estresse em tempo real, fornecendo uma ferramenta útil para acompanhar e tomar medidas para reduzir o estresse.')

    # benefícios
    st.markdown('### Benefícios do Real Time Stress')
    st.markdown('- Monitoramento contínuo do nível de estresse')
    st.markdown('- Identificação de momentos de alta tensão')
    st.markdown('- Orientações para redução do estresse')
    st.markdown('- Acompanhamento do progresso ao longo do tempo')

    # rodapé
    st.markdown('---')
    st.markdown('**Disclaimer:** Este aplicativo não substitui o acompanhamento médico ou profissional na área de saúde mental. Consulte sempre um profissional qualificado para obter orientações personalizadas.')
# aba do gráfico
elif tabs == 'Medidações atuais':
    st.write("""
            # Acompanhamento em tempo real
            """)

    with open('../Application/db.json') as f:
        data = json.loads(f.read())
    data = data['_default']
    df = pd.DataFrame(data).transpose()
    df.set_index('time', inplace=True)
    #print(df.head())
    st.line_chart(df)

    # rodapé
    st.markdown('---')
    st.markdown('**Disclaimer:** Este aplicativo não substitui o acompanhamento médico ou profissional na área de saúde mental. Consulte sempre um profissional qualificado para obter orientações personalizadas.')
# aba de dicas
else:
    st.markdown('<h1 style="text-align: center;">Dicas para Redução de Estresse</h1>', unsafe_allow_html=True)
    st.write('        ')
    st.write('        ')
    st.write('        ')
    st.write('        ')
    st.write('Aqui estão algumas dicas para ajudar a reduzir o estresse:')
    st.write('- Respire fundo e faça exercícios de relaxamento')
    st.write('- Pratique atividades físicas regulares')
    st.write('- Durma o suficiente e mantenha uma dieta saudável')
    st.write('- Faça pausas regulares durante o trabalho')
    st.write('- Encontre atividades prazerosas para relaxar, como ouvir música ou ler um livro')
    st.write('- Cultive relacionamentos saudáveis e compartilhe seus sentimentos com pessoas próximas')
    st.write('- Gerencie seu tempo e priorize suas tarefas')
    st.write('- Evite pensamentos negativos e pratique a positividade')
    st.write('- Busque ajuda profissional quando necessário')

    # adicional
    st.subheader('Dicas Avançadas')
    st.write('- Evite o consumo excessivo de cafeína e álcool')
    st.write('- Estabeleça limites saudáveis e aprenda a dizer "não" quando necessário')
    st.write('- Mantenha-se organizado e estabeleça metas realistas')
    st.write('- Aprenda técnicas de gerenciamento de estresse, como visualização e relaxamento muscular progressivo')
    st.write('- Desenvolva habilidades de comunicação e resolução de conflitos')
    st.write('- Reserve um tempo para hobbies e atividades criativas')
    st.write('- Mantenha-se conectado com a natureza e aproveite o ar livre')
    st.write('- Desconecte-se das telas e dedique tempo para desconectar e descansar')

    # rodapé
    st.markdown('---')
    st.markdown('**Disclaimer:** Este aplicativo não substitui o acompanhamento médico ou profissional na área de saúde mental. Consulte sempre um profissional qualificado para obter orientações personalizadas.')