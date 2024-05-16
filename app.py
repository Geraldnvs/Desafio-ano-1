import streamlit as st

# Função para armazenar o histórico de chat em uma sessão de streamlit
def get_chat_history():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = "Bem-vindo ao Chatbot de Suporte Técnico!\n\n"
    return st.session_state.chat_history

def append_to_chat(user_input, response):
    st.session_state.chat_history += f"Você: {user_input}\nChatbot: {response}\n\n"

def main():
    st.title("Assistente de Suporte Técnico de TI")
    tab1, tab2, tab3, tab4 = st.tabs(["Chatbot", "Referências Técnicas", "Análise de Dados", "Chamados Abertos"])

    with tab1:
        show_chatbot_page()

    with tab2:
        show_references_page()

    with tab3:
        show_data_analysis_page()

    with tab4:
        show_open_tickets_page()

def show_chatbot_page():
    st.header("Chatbot de Suporte Técnico")
    
    # Carregar ou iniciar o histórico de chat
    chat_history = get_chat_history()
    
    # Exibir o histórico de chat
    chat_display = st.text_area("Chat:", value=chat_history, height=300, max_chars=None)

    # Área de entrada para o usuário digitar a pergunta
    user_input = st.text_input("Digite sua pergunta:", key="user_input")

    # Botão para enviar a pergunta
    if st.button("Enviar", key="send"):
        # Simulando a resposta do chatbot
        if user_input:
            response = "Lorem ipsum dolor sit amet, consectetur adipiscing elit..."
            append_to_chat(user_input, response)
            chat_display.text = get_chat_history()
        else:
            st.warning("Por favor, digite uma pergunta.")

def show_references_page():
    st.header("Referências Técnicas")
    st.write("Aqui você encontra documentos, vídeos e FAQs técnicos.")

def show_data_analysis_page():
    st.header("Análise de Dados dos Chamados")
    st.write("Visualização de dados sobre chamados resolvidos.")

def show_open_tickets_page():
    st.header("Chamados Abertos")
    st.write("Lista de todos os chamados técnicos ainda abertos.")

if __name__ == "__main__":
    main()
