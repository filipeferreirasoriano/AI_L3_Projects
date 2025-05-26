import numpy as np
import skfuzzy as fuzz
from flask import Flask, render_template, request
from skfuzzy import control as ctrl

app = Flask(__name__)

# Entradas
experiencia = ctrl.Antecedent(np.arange(0, 11, 1), "experiencia")
turnover = ctrl.Antecedent(np.arange(0, 11, 1), "turnover")
clareza_requisitos = ctrl.Antecedent(np.arange(0, 11, 1), "clareza_requisitos")
complexidade = ctrl.Antecedent(np.arange(0, 11, 1), "complexidade")
mudanca_escopo = ctrl.Antecedent(np.arange(0, 11, 1), "mudanca_escopo")
disponibilidade_cliente = ctrl.Antecedent(
    np.arange(0, 11, 1), "disponibilidade_cliente"
)
maturidade_processo = ctrl.Antecedent(np.arange(0, 11, 1), "maturidade_processo")
orcamento = ctrl.Antecedent(np.arange(0, 11, 1), "orcamento")
ferramentas = ctrl.Antecedent(np.arange(0, 11, 1), "ferramentas")
estimativas = ctrl.Antecedent(np.arange(0, 11, 1), "estimativas")
comunicacao = ctrl.Antecedent(np.arange(0, 11, 1), "comunicacao")
integracao = ctrl.Antecedent(np.arange(0, 11, 1), "integracao")
tamanho_equipe = ctrl.Antecedent(np.arange(0, 11, 1), "tamanho_equipe")
tempo = ctrl.Antecedent(np.arange(0, 11, 1), "tempo")
dependencia = ctrl.Antecedent(np.arange(0, 11, 1), "dependencia")

risco = ctrl.Consequent(np.arange(0, 11, 1), "risco")

# Funções de pertinência
for var in [
    experiencia,
    turnover,
    clareza_requisitos,
    complexidade,
    mudanca_escopo,
    disponibilidade_cliente,
    maturidade_processo,
    orcamento,
    ferramentas,
    estimativas,
    comunicacao,
    integracao,
    tamanho_equipe,
    tempo,
    dependencia,
]:
    var["baixa"] = fuzz.trimf(var.universe, [0, 0, 5])
    var["media"] = fuzz.trimf(var.universe, [2, 5, 8])
    var["alta"] = fuzz.trimf(var.universe, [5, 10, 10])

risco["baixo"] = fuzz.trimf(risco.universe, [0, 0, 4])
risco["medio"] = fuzz.trimf(risco.universe, [3, 5, 7])
risco["alto"] = fuzz.trimf(risco.universe, [6, 10, 10])

# Regras fuzzy
rules = [
    ctrl.Rule(experiencia["baixa"] & turnover["alta"], risco["alto"]),
    ctrl.Rule(clareza_requisitos["baixa"] & complexidade["alta"], risco["alto"]),
    ctrl.Rule(mudanca_escopo["alta"] & disponibilidade_cliente["baixa"], risco["alto"]),
    ctrl.Rule(maturidade_processo["alta"] & ferramentas["alta"], risco["baixo"]),
    ctrl.Rule(estimativas["baixa"] & comunicacao["baixa"], risco["medio"]),
    ctrl.Rule(integracao["baixa"] & tamanho_equipe["alta"], risco["medio"]),
    ctrl.Rule(tempo["baixa"] & dependencia["alta"], risco["alto"]),
    ctrl.Rule(experiencia["alta"] & comunicacao["alta"], risco["baixo"]),
    ctrl.Rule(orcamento["baixa"] & tempo["baixa"], risco["alto"]),
    ctrl.Rule(orcamento["media"] & maturidade_processo["alta"], risco["baixo"]),
    ctrl.Rule(turnover["media"] & comunicacao["baixa"], risco["medio"]),
    ctrl.Rule(integracao["alta"] & tamanho_equipe["baixa"], risco["baixo"]),
    ctrl.Rule(
        disponibilidade_cliente["alta"] & clareza_requisitos["alta"], risco["baixo"]
    ),
    ctrl.Rule(dependencia["media"] & tempo["media"], risco["medio"]),
    ctrl.Rule(complexidade["baixa"] & experiencia["alta"], risco["baixo"]),
    ctrl.Rule(ferramentas["baixa"] & estimativas["baixa"], risco["alto"]),
    ctrl.Rule(estimativas["alta"] & tempo["alta"], risco["baixo"]),
    ctrl.Rule(mudanca_escopo["baixa"] & comunicacao["alta"], risco["baixo"]),
    ctrl.Rule(clareza_requisitos["media"] & experiencia["media"], risco["medio"]),
    ctrl.Rule(tamanho_equipe["media"] & dependencia["media"], risco["medio"]),
]

sistema_controle = ctrl.ControlSystem(rules)
avaliador = ctrl.ControlSystemSimulation(sistema_controle)


@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        entradas = [
            "experiencia",
            "turnover",
            "clareza_requisitos",
            "complexidade",
            "mudanca_escopo",
            "disponibilidade_cliente",
            "maturidade_processo",
            "orcamento",
            "ferramentas",
            "estimativas",
            "comunicacao",
            "integracao",
            "tamanho_equipe",
            "tempo",
            "dependencia",
        ]
        for var in entradas:
            avaliador.input[var] = float(request.form[var])
        avaliador.compute()
        resultado = round(avaliador.output["risco"], 2)
    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
