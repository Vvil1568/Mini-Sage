from openai import OpenAI

API_KEY = "sk-7072ea6b35fb43cfbbfb44add70ab39"

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.deepseek.com"
)

SYSTEM_PROMPT = """
Ты — «Мудрец», дружелюбный наставник по программированию в школьной LMS.
Твоя цель — помочь ученику самостоятельно найти и исправить ошибку.

ПРАВИЛА:
1. КАТЕГОРИЧЕСКИ ЗАПРЕЩЕНО давать готовый код решения.
2. Не давай прямой ответ, задавай наводящие вопросы (метод Сократа).
3. Объясняй ошибки простыми словами.
4. Обсуждай задачу только если тебя попросили.
5. Хвали за старания и мотивируй не сдаваться!
"""

def get_sage_response(task_text, user_question, chat_history, student_code):
    context = f"""{SYSTEM_PROMPT}

    Условие задачи:
    {task_text}
    """
    
    messages = [{"role": "system", "content": context}]
    
    for msg in chat_history:
        messages.append({"role": msg["role"], "content": msg["content"]})
        
    messages.append({"role": "user", "content": f"[Текущий код ученика] ```python{student_code}``` [Сообщение ученика] {user_question}"})

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=messages,
        reasoning_effort="low"
    )
    
    return response.choices[0].message.content