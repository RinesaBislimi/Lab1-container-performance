
<p align="left">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/University_of_Prishtina_logo.svg/1200px-University_of_Prishtina_logo.svg.png" alt="Logo e Universitetit të Prishtinës" width="120"/>
</p>

# Universiteti i Prishtinës “Hasan Prishtina”
## Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike

**Niveli:** Master  
**Lënda:** Menaxhimi i Burimeve në Cloud Computing  

---

### **Titulli i Projektit:**  
**Optimizimi i Performancës së Kontejnerëve nën Kufizime të Burimeve**

**Profesor:** Prof. Dr. Artan Mazrekaj  

---

### **Anëtarët e Grupit:**


# Universiteti i Prishtinës “Hasan Prishtina”
## Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike

**Niveli:** Master  
**Lënda:** Menaxhimi i Burimeve në Cloud Computing  

---

### **Titulli i Projektit:**  
**Optimizimi i Performancës së Kontejnerëve nën Kufizime të Burimeve**

**Profesor:** Prof. Dr. Artan Mazrekaj  

---

### **Anëtarët e Grupit:**
- **Alba Thaqi**  
- **Rinesa Bislimi**

# Lab1-container-performance

Ky projekt simulon performancën e kontejnerëve nën kufizime të ndryshme të CPU-së dhe memories duke përdorur Docker dhe Python.

## Përshkrimi
Skriptet testojnë ndikimin e kufizimeve të CPU-së dhe memories në kohën e ekzekutimit të detyrave, dhe ruajnë rezultatet si grafika `.png` dhe një raport `.txt` në folderin **output**.

## Përmbajtja
- **app.py** – Skripti kryesor që gjeneron grafikat dhe rezultatet.
- **Dockerfile** – Përshkruan imazhin që përdoret për të ekzekutuar testet.
- **output/** – Folderi ku ruhen rezultatet (krijohet automatikisht gjatë ekzekutimit).

## Ekzekutimi i projektit

### Ndërto imazhin Docker
```bash
docker build --no-cache -t perf-test .
```
### Ekzekuto testin dhe ruaj rezultatet në folderin lokal output
Në PowerShell (Windows) përdor këtë komandë:

```bash
docker build --no-cache -t perf-test .
```


## Rezultatet e krijuara automatikisht

Pas ekzekutimit, në folderin output/ do të gjenerohen skedarët:

` result_0.5.png → Grafiku për 0.5 CPU `

` result_1.0.png → Grafiku për 1.0 CPU `

` result_2.0.png → Grafiku për 2.0 CPU `

` results_all.png → Krahasim përfundimtar i performancës `

` load_balancer.png → Vizualizim i shpërndarjes së ngarkesës `

` results.txt → Përmbledhje numerike e rezultateve `