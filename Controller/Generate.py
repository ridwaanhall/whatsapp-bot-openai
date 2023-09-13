import openai
import os

app = Flask(__name__)

openai.api_key = os.environ['API_KEY']

def generate_answer(question):
  model_engine = "text-davinci-002"
  prompt = (f"Q: {question}\n"
            "A:")

  response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
  )

  answer = response.choices[0].text.strip()
  return answer