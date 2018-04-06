import string

class AnalisadorLexico():
    def __init__(self):
        self.operadores = '+ - / *'.split()
        self.delimitadores = '( )'.split()
        self.digito = '0123456789'
        self.letra = string.ascii_letters
        self.analise_lexica_correta = False

    def averiguar_operadores(self, entrada):
        if entrada in self.operadores:
            return True
        return False

    def averiguar_digito(self, entrada):     
        if entrada in self.digito:
            return True
        return False
    
    def averiguar_delimitador(self, entrada):        
        if entrada in self.delimitadores:
            return True
        return False

    def averiguar_letra(self, caracter):
        if caracter in self.letra:
            return True
        return False

    def averiguar(self, entrada):
        tamanho_linha = len(entrada)
        i=0
        while i < tamanho_linha:
            carac_atual = entrada[i]
            carac_seguinte = None
            if self.averiguar_operadores(carac_atual):
               self.analise_lexica_correta = True
               print(carac_atual)
            elif self.averiguar_digito(carac_atual):
                string_temp = carac_atual
                # print(carac_atual)
                i += 1
                carac_atual = entrada[i]
                while self.averiguar_digito(carac_atual) and (i + 1 < tamanho_linha):
                    string_temp += carac_atual
                    # print(string_temp)
                    i += 1
                    carac_atual = entrada[i]
                    print(string_temp)
                self.analise_lexica_correta = True
                if not self.averiguar_digito(carac_atual):
                    i -= 1
                i+=1
        if self.analise_lexica_correta:
            return self.analise_lexica_correta
        return False
