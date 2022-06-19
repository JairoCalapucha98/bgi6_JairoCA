#!/usr/bin/env python
# coding: utf-8

# ## <center><h2>BIOINFORMÁTICA GO2</h2></center>
# # <center><h2>Tarea de PYTHON N°.1</h2></center>
# 
# ### Nombre: Jairo Calapucha
# ### Fecha de entrega: Sábado 17 de junio de 2022
# 
# <center><h2>Actividad</h2></center>
# 
# ## Conceptos generales 
# 
# <center><h2>Código Genético</h2></center>
# 
# ### ¿Qué es el dogma central de la Biología?
# 
# El dogma central de la biología molecular destaca que al sintetizar proteínas , el ADN se transcribe en ARNm, que se traduce en proteína. Una diferencia entre los genes eucarióticos y procarióticos es que los genes eucarióticos pueden contener intrones (secuencias intermedias), que no son secuencias codificantes, y deben separarse del transcrito primario de ARN antes de que se convierta en ARNm y pueda traducirse en proteína. Los genes procarióticos no tienen intrones, por lo que su ARN no está sujeto a corte y empalme (Karp, 2014).
# 
# ### ¿Qué es el codon de inicio?
# 
# Es el primer aminoácido utilizado en el proceso de traducción(Karp, 2014).
# 
# ### ¿Qué es el codon final?
# 
# Hay 3 codones STOP en el código genético: UAG, UAA y UGA. Estos codones señalan el final de la cadena polipeptídica durante la traducción. Estos codones también se conocen como codones sin sentido o codones de terminación, ya que no codifican un aminoácido (Karp, 2014).
# 
# ### ¿Qué es el ARNm?
# 
# El ARN mensajero (ARNm abreviado) es un tipo de ARN monocatenario implicado en la síntesis de proteínas. El ARNm está hecho de una plantilla de ADN durante el proceso de transcripción. El papel del ARNm es transportar información de proteínas desde el ADN en el núcleo de una célula hasta el citoplasma de la célula (interior acuoso), donde la maquinaria de producción de proteínas lee la secuencia de ARNm y traduce cada codón de tres bases en su aminoácido correspondiente en un creciente cadena de proteínas(Karp, 2014).
# 
# ### ¿Qué es el ADN?
# 
# El ADN, o ácido desoxirribonucleico, es el material hereditario en los humanos y en casi todos los demás organismos. Casi todas las células del cuerpo de una persona tienen el mismo ADN. La mayor parte del ADN se encuentra en el núcleo de la célula (donde se denomina ADN nuclear), pero también se puede encontrar una pequeña cantidad de ADN en las mitocondrias (donde se denomina ADN mitocondrial o ADNmt)(Karp, 2014).
# 
# ### ¿Qué es el ADNc?
# 
# En genética , el ADN complementario ( ADNc ) es ADN sintetizado a partir de un molde de ARNm maduro en una reacción catalizada por la enzima transcriptasa inversa . El ADNc se utiliza a menudo para clonar genes eucariotas en procariotas(Karp, 2014).
# 
# ### ¿Qué es la secuencia reversa complementaria?
# 
# El complemento inverso de una secuencia de ADN se forma invirtiendo las letras, intercambiando A y T e intercambiando C y G. Por lo tanto, el complemento inverso de ACCTGAG es CTCAGGT.
# 
# ### ¿Qué es Forward?
# 
# 
# 
# ### ¿Qué es el Backward?
# 
# 
# 
# ### Referencia
# 
# Karp, G. (2014). Biología celular y molecular: Conceptos y experimentos (7a ed.). México D.F.: McGraw-Hill.
# 

# In[ ]:





# In[4]:


seq1 = "AAGGACCNGACATCCATCGCTGATGTCAATCCCCCGTGGATCGTAAGTCCGGGAGTAGGAGGAGGAAGGGTCGTCCCACAGTGCGAAGAGGCTTCTGACCTACTGACGGTACCTCCTCAGTGTCAGCCTATAGTCGGAGCTCGAGGGAGACTCGGTCCTCTGTAAAAGTCCGAATACCTTTGATGAAGGAGGTCTTCTATAGGACGGTAG"
seq1


# In[6]:


nuc_g = seq1.count('G') #Primero se crea el nombre de un nucleótido llamdo nuc_c que contiene el número de elementos G, El comando count, sirve para contar un núemro de elementos dentro del registro
nuc_c = seq1.count('C')  #número de elementos C

len_seq1 = len(seq1) #Lend comando sirve para sacar la longuitud o la totalidad de elemntos de la secuencia

porcent_GC = 100*(nuc_c + nuc_g)/ len_seq1 #Se está realizando una suma del número total de elementos G Y C dividpo entre el númer total de elementos de la secuencia.
porcent_GC # mostrar el resultado

round(porcent_GC, 2) #Este comando hace que se redondee a dos decimales


# ACTIVIDAD #2. Encontrar la secuencia complementaria y el reverso complementario(RComp)

# In[14]:


# Codigo para hallar la cadena complemendaria del la secuencia, mRNAA, reverso de la cadena complementaria

gene_funcional = seq1.replace("A", "t") #Esamos creando un gen temporal donde se cambia todas las A por t
gene_funcional = gene_funcional.replace("T", "a")#Esamos creando un gen temporal donde se cambia todas las T por a
gene_funcional = gene_funcional.replace("C", "g")#Esamos creando un gen temporal donde se cambia todas las C por g
gene_funcional = gene_funcional.replace("G", "c")#Esamos creando un gen temporal donde se cambia todas las G por c
cseq1 = gene_funcional.upper() #Upper cambia todas las minusculas por mayúsculas
rcseq1 = cseq1[::-1] # reverso de la cadena complementaria


print(seq1) #Imprime el gen principal
print(cseq1) #Imprime la secuencia complementaria
print(rcseq1) # reverso del  ADN complementario


# ACTIVIDAD #3. Encontrar el(los) sitio(s) de inicio y sitios de pare, es decir los marcos de lectura de transcripción forward.

# In[12]:


gen_show = cseq1.replace('ATG', "111") # indentifica el condon de inicio y remplaza por el caracter "111"
#Se indentifica el condon stop y remplaza "TAG" por "222" , "TGA" por "333" , "TAA" por "444"
gen_show = gen_show.replace('TAG', "222") 
gen_show = gen_show.replace('TGA', "333")
gen_show = gen_show.replace('TAA', "444")
print(gen_show) #imprime los cambios ejecutados


# ACTIVIDAD #4. Indentifiación de codones de inicio y final en sentido forwarl del la secuencia complementaria

# In[15]:



gen_rc = rcseq1.replace('ATG', "ooo") # indentifica el condon de inicio y remplaza por el caracter "ooo"
#Se indentifica el condon stop y remplaza "TAG" por "***" , "TGA" por "***" , "TAA" por "***"
gen_rc = gen_rc.replace('TAG', "***") 
gen_rc = gen_rc.replace('TGA', "***")
gen_rc = gen_rc.replace('TAA', "***")
print(gen_rc)#imprime los cambios ejecutados
print(rcseq1) # reverso del  secuencia complementaria


# Resultados
# ARNm = "TTCCTGGNCTG222G222CGACTACAGT222GGGGCACC222CATTCAGGCCCTCATCCTCCTCCTTCCCAGCAGGGTGTCACGCTTCTCCGAAGACTGG111ACTGCC111GAGGAGTCACAGTCGGATATCAGCCTCGAGCTCCCTC333GCCAGGAGACATTTTCAGGCTT111GAAACTACTTCCTCCAGAAGATATCCTGCCATC"
# 
# Segun el amrco del ARNm solo se va a codificar 2 proteinas ( en teoría). 

# In[ ]:





# In[ ]:





# In[ ]:




