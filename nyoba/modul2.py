## install Library
##!pip install langchain langchain-google-genai



## Import dan set API KEY
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from google.colab import userdata

os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")




#definsikan template teks
template_text = "Buat cerita pendek nguawor, peak, dan ABSOLUTE CINEMA tentang {topik} dalam 80 kata."

#buat objek PromptTemplate
prompt = PromptTemplate.from_template(template_text)



llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")



# buat chain sederhana
chain = LLMChain(llm=llm, prompt=prompt)

# jalankan chain
hasil_chain = chain.run({"topik": "kucing pemalas"})
print(hasil_chain)