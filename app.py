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
            Caso seja necessário, peça mais informações para o usuário.
            Utilize exemplos práticos e reais para ilustrar a solução.
            Utilize links de referência para que o usuário possa se aprofundar no assunto.
            Caso escreva um código, utilize uma função main() para que o usuário possa testar o código.
            Se o usuário solicitar por outra solução, forneça uma resposta alternativa mais simples.
            Seja sempre educado e respeitoso.
            Não forneça respostas que envolvam práticas ilegais, antiéticas ou que violem direitos autorais.
            Não forneça respostas que envolvam hacking, cracking ou qualquer forma de invasão de sistemas.
            Não forneça respostas que envolvam manipulação de dados pessoais ou sensíveis.
            Não forneça respostas que envolvam atividades maliciosas ou prejudiciais."""
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