import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("zadatak_2.csv")
lg = data["LanguagesWorkedWith"]
godine = data["Responder_age"]
podaci_python = []
podaci_cpp = []
podaci_js = []
broj_programskih_jezika = []
r_go = []
html_css = []

for broj in range(len(data)):
    if "Python" in lg[broj]:
        podaci_python.append(godine[broj])

for broj in range(len(lg)):
    broj_programskih_jezika.append(len(lg[broj]))

for broj in range(len(lg)):
    if "R" in lg[broj] and godine[broj] < 30 or "Go" in lg[broj] and godine[broj] > 30:
        r_go.append(godine[broj])
    if "HTML/CSS" in lg[broj] and godine[broj] > 30:
        html_css.append(godine[broj])

# prikaz liste godina ljudi znaju R i mladji su od 30 ili stariji od 30 koji znaju Go
print(r_go)
# lista ljudi koji znaju HTML/CSS i stariji od 40
print(html_css)

print(f"Prosecna godina je {np.mean(podaci_python)}")

for broj in range(len(data)):
    if "C++" in lg[broj]:
        podaci_cpp.append(godine[broj])
    if "JavaScript" in lg[broj]:
        podaci_js.append(godine[broj])
# najcesca godina ljudi koji znaju cpp
print(np.bincount(podaci_cpp).argmax())
# najcesca godina ljudi koji znaju js
print(np.bincount(podaci_js).argmax())


bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(godine, bins=bins, edgecolor='black')

plt.xlabel('Broj programskih jezika koji znaju')
plt.ylabel('Broj ljudi')

plt.tight_layout()
plt.show()

bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.hist(broj_programskih_jezika, bins=bins, edgecolor='black')

plt.xlabel('Broj godina')
plt.ylabel('Broj programskih jezika koji znaju')

plt.tight_layout()
plt.show()
