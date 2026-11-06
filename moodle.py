import sys
import subprocess
import streamlit as st

st.set_page_config(layout="wide", page_title="LMS Moodle")

st.caption("Личный кабинет / Мои курсы / Информатика / Практикум / Задание 1")
st.divider()

col_moodle, col_empty = st.columns([2.3, 0.1], gap="large")

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


# ================================================================================================