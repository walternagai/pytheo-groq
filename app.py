import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

def generate_response_groq(api_key, model, prompt):
    model = ChatGroq(model=model,
                     temperature=0.7, 
                     api_key=api_key)
    messages = [
        ("system", 
            """
            Você é o Pytheo, um assistente virtual que ajuda a aprender a linguagem Python.
            Seu nível de conhecimento é intermediário e você só deve responder perguntas sobre Python. 
            A sua resposta deve ser objetiva e clara.
            Evite escrever respostas longas e complexas. 
            Evite grandes sequências de código, mas caso isso seja necessário, divida em partes menores.
            Ajude o usuário a entender o problema e a solução de forma simples e direta.
            Seja sempre educado e respeitoso."""
        ),
        ("human", prompt)
    ]
    response = model.invoke(messages)
    return response.content

def main():    
    api_key = st.secrets.pytheo_groq.GROQ_API_KEY
    model = st.secrets.pytheo_groq.GROQ_MODEL

    st.title("🦜 Pytheo-groq")

    st.write("Pytheo é um assistente virtual que te ajuda a aprender Python de forma simples e objetiva.")

    st.markdown("""
                ### Aviso de Privacidade\n
                * Este aplicativo não armazena suas perguntas e respostas.\n
                * Evite perguntas ofensivas ou que possam violar a privacidade de outras pessoas.
    """)
    with st.form(key="my_form"):
        text = st.text_area("Escreva sua dúvida da linguagem Python:")
        submitted = st.form_submit_button("Enviar")
        if submitted:
            st.write("🦜 Pytheo diz:")
            response = generate_response_groq(api_key, model, text)
            st.write(response)

if __name__ == "__main__":
    main()