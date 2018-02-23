import os.path
import string

class AnalisadorLexico():    
    def __init__(self):
        self.operadores = '> < = >= +'.split()
        self.delimitadores = '; , ( ) [ ] { } :'.split()
        self.digito = '0123456789'
        self.letra = string.ascii_letters
        self.arquivo_entrada = 'codigo.txt'
        self.arquivo_saida = 'resultado-lex.csv'
        self.reservadas = 'and def exec if not else return assert del finally import or try break elif for in pass while from is print yield continue except global lambda raise'.split()

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

    def tokens_reservados(self, token):
        if token in self.reservadas:
            return True
        return False

    def qual_token_reservado(self, entrada):
        i = 0        
        while i < len(self.reservadas):
            if self.reservadas[i] == entrada:
                return self.reservadas[i]
            i+=1

    def arquivo(self):
        arq_saida = open(self.arquivo_saida,'w')
        if not os.path.exists(self.arquivo_entrada):
            arq_saida.write("Arquivo de entrada inexistente")
            # print("Open")
            return        
        cabecalho = "IDENTIFICAÇAO;TOKEN;POSICAO LINHA; POSICAO COLUNA\n"
        arq_saida.write(cabecalho)
        return arq_saida

    def averiguar(self):        
        arq_saida = self.arquivo()
        if not arq_saida:
            pass
        else:
            arq_entrada = open(self.arquivo_entrada, 'r')
            linha_codigo = arq_entrada.readline()        
            numero_linha = 0
            
            while linha_codigo:
                i = 0
                tamanho_linha = len(linha_codigo)
                while i < tamanho_linha:
                    carac_atual = linha_codigo[i]
                    print(i)
                    print(carac_atual)
                    carac_seguinte = None
                    if (i+1) < tamanho_linha:
                        carac_seguinte = linha_codigo[i+1]
                    if carac_seguinte != None and self.averiguar_operadores(carac_atual+carac_seguinte):
                        arq_saida.write('Operador;'+carac_atual+carac_seguinte+';'+str(numero_linha)+';'+str(i)+'\n')
                        i+=1
                    elif self.averiguar_operadores(carac_atual):
                        arq_saida.write('Operador;'+carac_atual+';'+str(numero_linha)+';'+str(i)+'\n')
                        #print(i)
                    elif self.averiguar_digito(carac_atual):
                        string_temp = carac_atual
                        #print(carac_atual)
                        i += 1
                        carac_atual = linha_codigo[i]
                        while self.averiguar_digito(carac_atual) and (i+1 < tamanho_linha):
                            string_temp += carac_atual
                            #print(string_temp)
                            i+=1                        
                            carac_atual = linha_codigo[i]                    
                        arq_saida.write('Número inteiro;'+string_temp+';'+str(numero_linha)+';'+str(i)+'\n')
                        if not self.averiguar_digito(carac_atual):
                           i -= 1
                    elif self.averiguar_delimitador(carac_atual):
                        arq_saida.write('Delimitador;'+ carac_atual +';'+str(numero_linha)+';'+str(i)+'\n')
                    elif self.averiguar_letra(carac_atual):                    
                        string_temp = carac_atual
                        i+=1
                        algum_erro = False
                        while i < tamanho_linha:                        
                            carac_seguinte = None
                            carac_atual = linha_codigo[i]
                            if i+1 < tamanho_linha:
                                cara_seguinte = linha_codigo[i+1]
                            if self.averiguar_letra(carac_atual) or self.averiguar_digito(carac_atual) or carac_atual == '_':
                                string_temp += carac_atual
                                #print(string_temp)
                            elif self.averiguar_delimitador(carac_atual) or carac_atual == ' ' or carac_atual == '\t' or carac_atual == '\r':
                                i -= 1
                                break
                            elif carac_seguinte != None and self.averiguar_operadores(carac_atual+carac_seguinte) or self.averiguar_operadores(carac_atual):
                                i-=1
                                break
                            elif carac_atual != '\n':
                                algum_erro = True
                                break                            
                            i+=1
                        if algum_erro:
                            while i+1 < tamanho_linha:
                                i+=1
                                carac_atual = linha_codigo[i]
                                if self.averiguar_delimitador(carac_atual) or carac_atual == ' ' or carac_atual == '\t' or carac_atual == '\r':
                                    i-=1
                                    break
                        else:
                            if self.tokens_reservados(string_temp):
                                arq_saida.write('Token Reservado;'+self.qual_token_reservado(string_temp)+';'+str(numero_linha)+';'+str(i)+'\n')
                            else:
                                arq_saida.write('Constante;'+string_temp+';'+str(numero_linha)+';'+str(i)+'\n')
                    i+=1
                linha_codigo = arq_entrada.readline()
                numero_linha += 1
            arq_entrada.close()
            arq_saida.close()
