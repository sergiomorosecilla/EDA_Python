# 📊 Proyecto EDA — Campaña Marketing Banco

Este repositorio contiene el desarrollo de un **Análisis Exploratorio de Datos (EDA)** aplicado a campañas de marketing de una entidad bancaria portuguesa.  
El objetivo principal ha sido ver los factores que han influido en el resultado de la campaña de marketing realizada, cuyo objetivo era conseguir el mayor número de suscripciones de depósitos a plazo.  

---

## 📁 Estructura del repositorio
```
- Data_folder
   - Archivos datos iniciales en bruto:
      - `bank-additional.csv`  
      - `customer-details.xlsx`
   - Archivos unificados y limpieza:
      - `clean&merge_data.ipynb`
      - `charts.ipynb`
- PDF con enunciado: 
   - `DetaProyect_EDA con Python.pdf`
- README.md:
   - Explicación del proyecto y Analisis con los hallazgos y conclusiones

```
---

## 🎯 Objetivos del análisis
- Transformación y limpieza de datos.  
- Análisis descriptivo de variables numéricas y categóricas.  
- Visualización de distribuciones, correlaciones y tendencias.  
- Generación de un informe con hallazgos clave e insights.  

---

## 📑 Informe del análisis
Puedes consultar el **informe completo con hallazgos y conclusiones** en:  

📄 [`reports/Informe_EDA_Bank_Marketing.docx`](reports/Informe_EDA_Bank_Marketing.docx)  

---

## 🛠️ Herramientas utilizadas
- Python 3.10  
- Pandas  
- NumPy  
- Matplotlib  
- Jupyter Notebook  

---

## ✅ Principales hallazgos (resumen)
- El **perfil más propenso a suscribir depósitos** corresponde a clientes de edad media (30–50 años), con estudios universitarios, ingresos estables y sin préstamos previos.  
- La **duración de la llamada** es un factor crítico en la probabilidad de éxito.  
- El **exceso de contactos previos** puede reducir la efectividad de la campaña.  
- Variables macroeconómicas como `euribor3m` y `emp.var.rate` están relacionadas con los resultados.  

---
