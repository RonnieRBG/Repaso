class Medicamento():
    DESCUENTO = 0.05
    IVA = 0.19 

if __name__ == "__main__":
    remedio = Medicamento()
    print(Medicamento().DESCUENTO)
    print(f"Los medicamentos tienen un IVA del {int(remedio.IVA * 100)} %")