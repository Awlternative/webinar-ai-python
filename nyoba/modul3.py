# !pip install -q langchain langchain-google-genai google-generativeai



## Import dan set API KEY
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


from langchain_google_genai import ChatGoogleGenerativeAI
import os
from google.colab import userdata

os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")

#inisialisasi model gemini
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

#uji coba llm
hasil  = llm.invoke("Tuliskan satu kalimat motivasi untuk programer pemula.")
print(hasil)



from langchain.prompts import PromptTemplate

template_text = "Beri saya 5 ide konten media sosial tentang {topic}"
prompt = PromptTemplate.from_template(template_text)
hasil = prompt.invoke({"topic": "Indonesia"})
print(hasil)



hasil_mentah = llm.invoke("Tuliskan satu kalimat motivasi untuk programer pemula.")

print("======= Objek hasil (AI message full)  ========)")
print(hasil_mentah)

#ambil hanya teks kontennya
print("======= Output saja  ========)")
print(hasil_mentah.content)



#import pembersih output
from langchain.schema.output_parser import StrOutputParser

#inisialisasi
output_parser =StrOutputParser()

contoh_output = output_parser.invoke(llm.invoke("Tuliskan satu kalimat motivasi untuk programer pemula."))
print(contoh_output)



#import operator pipe (|)
from langchain.schema.runnable import RunnableSequence

#buat chain sederhana : prompt > llm > parser
chain = prompt | llm | output_parser

#jalankan chain
hasil_chain = chain.invoke({"topic" : "Indonesia"})
print(hasil_chain)



#TANPA LANGCHAIN

# buat template prompt manual
topic = "indonesia"
prompt_text = f"Beri saya 5 ide konten media sosial tentang {topic}"

#panggil model langsung
hasil_mentah = llm.invoke(prompt_text)

#ambil konten saja
output = hasil_mentah.content

#cetak hasil
print(output)



chain = prompt | llm | output_parser

hasil_chain = chain.invoke({"topic" : "Indonesia"})
print(hasil_chain)



#contoh: langchain digunakan untuk membuat pipeline mult langkah yang kompleks
#tujuan: buat ringkasan dan 3 ide konten dari topik tertentu, hanya dalam 1 pipeline

from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough

#buat dua prompt berbeda
prompt_rangkuman = PromptTemplate.from_template(" Buat ringkasan tentang topik berikut : {topic}")

prompt_ide = PromptTemplate.from_template("Berdasarkan ringkasan tersebut, buat 3 ide konten media sosial yang menarik : {summary}")

#buat parser
parser = StrOutputParser()

#buat 2 chain
chain_rangkuman = prompt_rangkuman | llm | parser
chain_ide = prompt_ide | llm | parser

#pipeline: masukan topic > hasil ringkasan > hasil ide

power_chain = (
    {"summary" : chain_rangkuman, "topic" : RunnablePassthrough()} #input paralel
    | chain_ide
)

#jalankan
hasil = power_chain.invoke({"topic" : "Dampak AI terhadap dunia kerja"})
print(hasil)