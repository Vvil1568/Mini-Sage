import sys
import subprocess
import streamlit as st

st.set_page_config(layout="wide", page_title="LMS Moodle", page_icon="sage.png")

st.caption("Личный кабинет / Мои курсы / Информатика 10 класс / Практикум / Задание 1")
st.divider()

col_moodle, col_assistant = st.columns([2.3, 1.0], gap="large")

with col_moodle:
    col_status, col_task = st.columns([1, 4])
    with col_status:
        with st.container(border=True):
            st.markdown("**Вопрос 1**")
            st.caption("Пока нет ответа")
            st.caption("Балл: 1,00")
            st.caption("Отметить")

    task_text = """
            Напишите программу, которая считывает с клавиатуры целое число N.  
            Программа должна вывести сумму всех четных чисел от 1 до N.
            
            Пример ввода: 6  
            Пример вывода: 12
            """

    with col_task:
        with st.container(border=True):
            st.subheader("Сумма четных чисел от 1 до N")
            st.markdown(task_text)

    default_code = (
        "n = int(input())\n"
        "total = 0\n"
        "for i in range(1, n):\n"
        "    if i % 2 == 0:\n"
        "        total = total + 'i'\n"
        "print(total)"
    )
    student_code = st.text_area("Код:", value=default_code, height=150, label_visibility="collapsed")

    btn1, btn2, _ = st.columns([1, 1, 3])
    with btn1:
        run_test = st.button("Проверить решение", type="primary")
    with btn2:
        st.button("Сохранить черновик")

    if run_test:
        try:
            proc = subprocess.run(
                [sys.executable, "-c", student_code],
                input="6",
                capture_output=True,
                text=True,
                timeout=3
            )
            if proc.returncode != 0:
                st.error("Тест 1 провален (Ошибка выполнения):")
                st.code(proc.stderr, language="python")
            elif proc.stdout.strip() == "12":
                st.success("Тест 1 пройден успешно!")
            else:
                st.error(f"Тест 1 провален: ожидалось '12', получено '{proc.stdout.strip()}'")
        except subprocess.TimeoutExpired:
            st.error("Тест 1 провален: Превышено время ожидания (возможно, бесконечный цикл)")


            
import sage

SAGE = "sage.jpg"

with col_assistant:
    with st.container(border=True):
        st.image(SAGE, width=45)
        st.header("Мудрец")

        chat_box = st.container(height=400)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        with chat_box:
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"], avatar=SAGE if msg["role"] == "assistant" else None):
                    st.markdown(msg["content"])

        user_query = st.chat_input("Задай вопрос Мудрецу...")

        if user_query:
            st.session_state.messages.append({"role": "user", "content": user_query})
            with chat_box:
                with st.chat_message("user"):
                    st.markdown(user_query)

            answer = sage.get_sage_response(task_text, user_query, st.session_state.messages, student_code)

            st.session_state.messages.append({"role": "assistant", "content": answer})
            with chat_box:
                with st.chat_message("assistant", avatar=SAGE):
                    st.markdown(answer)