###
minuman = "Kopi Kenangan", "Kopi Jawa"
print(minuman)


###
topik = "Kopi Kenangan"
full_prompt = f"Beri saya 5 ide konten media sosial tentang {topik}"
print(full_prompt)


###
input_data = {
    "topic" : "Kopi Kenangan",
    "tone" : "professional",
    "audience" : "pemula"
}

print(f"topik yang diminta: {input_data['topic']}")
print(f"nada: {input_data['tone']}")


###
def create_prompt(topic, tone):
  """
  Function ini bikin prompt lengkap dari topik dan nada
  """
  prompt = f"buatlah 3 ide konten tentang {topic} dengan nada {tone}"
  return prompt

prompt_1=create_prompt("Kopi Kenangan", "Profesional")
prompt_2=create_prompt("Ketupat kandangan", "Santai")

print(prompt_1)
print(prompt_2)