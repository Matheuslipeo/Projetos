print('***Cálculo de Despesa e Receita de uma Lavoura***')
desp1 = float(input('Qual a sua despesa com semente/muda? '))
desp2 = float(input('Qual a sua despesa com fertilizante? '))
desp3 = float(input('Qual a sua despesa com esterco/adubo? '))
desp4 = float(input('Qual a sua despesa com mão de obra? '))
desp5 = float(input('Qual a sua despesa com luz? '))
desp6 = float(input('Gastos pontuais não previstos? Se sim, informe o valor: '))
quant_plant = int(input('Quantos pés/mudas você plantou? '))
total = desp1+desp2+desp3+desp4+desp5+desp6
custo_pe = total/quant_plant
print ('O total da sua despesa é de R$:{:.2f} reias, e o custo por pés/muda é de R$:{:.2f} reias'.format(total,custo_pe))

prod = float(input('Qual a sua produção média por pé/muda? '))
preco = float(input('Qual o preço médio unitário de venda? '))
total2 = prod*preco*quant_plant
print ('Se você plantou {:.2f} pés, e a sua produção estimada por pés for de {:.2f} UN e o preço de venda por UN for {:.2f}, você terá uma receita estimada em {:.2f} reais'.format(quant_plant,prod,preco,total2))
lucro = total2-total
print ('Com base nos dados nessa plantação você irá lucrar R$:{:.2f} reais'.format(lucro))