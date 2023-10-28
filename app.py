import PySimpleGUI as sg
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

sg.theme('DarkGreen5')
layout = [
    [sg.Text("Motivo de sua economia:")],
    [sg.InputText(key="motivo", size=(35, 1))],
    [sg.Text("Valor de sua economia mensal:")],
    [sg.InputText(key="mensal_R$", size=(35, 1))],
    [sg.Text("Valor total de sua meta:")],
    [sg.InputText(key="total_R$", size=(35, 1))],
    [sg.Button("Calcular")]
]

window = sg.Window("Meta Financeira", layout)

causas_masculinos = ["curso", "carro", "imóvel", "imovel", "filho", "negócio", "negocio", "sonho", "casamento", "desenvolvimento pessoal", "conforto", "projeto", "natal", "ano novo", "final do ano", "final de ano", "futuro", "investimento", "seguro", "cruzeiro"]  # Lista de causas consideradas masculinas
causas_femininos = ["educação", "educacao", "educaçao", "educaçao", "aposentadoria", "casa", "filha", "viagem", "segurança", "saúde", "saude", "independência", "independencia", "poupança", "riqueza", "dívida", "divida", "reserva"]  # Lista de causas consideradas femininas

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
   
    if event == "Calcular":
        motivo_RS = values["motivo"]
        mensal_RS = values["mensal_R$"]
        total_RS = values["total_R$"]

        try:
            mensal_RS = locale.atof(mensal_RS)
            total_RS = locale.atof(total_RS)

            resultado_tempo = total_RS / mensal_RS
            tempo_em_meses = int(resultado_tempo)
            
            genero_motivo = ""
            if motivo_RS.lower() in causas_masculinos:
                genero_motivo = "masculino"
            elif motivo_RS.lower() in causas_femininos:
                genero_motivo = "feminino"
            else:
                genero_motivo = "indefinido"

            if genero_motivo == "masculino":
                mensagem = f"Para você conseguir alcançar a sua meta, você irá precisar guardar {locale.currency(mensal_RS, grouping=True)} durante {tempo_em_meses} meses, no final deste tempo você irá ter o dinheiro para o seu {motivo_RS}!"
            if genero_motivo == "indefinido":
                mensagem = f"Para você conseguir alcançar a sua meta, você irá precisar guardar {locale.currency(mensal_RS, grouping=True)} durante {tempo_em_meses} meses!"
            elif genero_motivo == "feminino":
                mensagem = f"Para você conseguir alcançar a sua meta, você irá precisar guardar {locale.currency(mensal_RS, grouping=True)} durante {tempo_em_meses} meses, no final deste tempo você irá ter o dinheiro para a sua {motivo_RS}!"

            sg.popup(mensagem)

        except ValueError:
            sg.popup_error("Por favor, insira um valor válido para os campos de valores")
