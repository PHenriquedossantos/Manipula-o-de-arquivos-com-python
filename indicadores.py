arquivo = open('Alunos.txt', 'r')
linhas = arquivo.readlines()
del linhas[:4]
hashtag_site_org = 0
hashtag_yt_org = 0
hashtag_ig_org = 0
hashtag_igfb_org = 0
total_org = 0
anuncio = 0
for linha in linhas:
  email, origem = linha.split(',')

  if '_org' in origem:
    total_org += 1 
    if 'hashtag_site_org' in origem:
      hashtag_site_org += 1
    elif 'hashtag_yt_org' in origem:
      hashtag_yt_org += 1
    elif 'hashtag_ig_org' in origem:
      hashtag_ig_org += 1
    elif 'hashtag_igfb_org' in origem or 'hashtag_ig_org' in origem:
      hashtag_igfb_org += 1
  else:
    anuncio += 1

arquivo.close()

print('total organicos {}'.format(total_org))
print('total anuncios {}'.format(anuncio))

with open('Indicadores.txt', 'w') as arquivo_indicadores:
  arquivo_indicadores.write('total organicos {}\n'.format(total_org))
  arquivo_indicadores.write('total anuncios {}\n'.format(anuncio))
print('FIM DO CÓDIGO')